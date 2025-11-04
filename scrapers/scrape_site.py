#!/usr/bin/env python3
"""
Wix to WordPress Migration Scraper
Scrapes the BWNA Wix site and extracts all content, pages, and media
"""

import asyncio
import json
import os
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
from datetime import datetime

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from tqdm import tqdm


class WixScraper:
    def __init__(self, config_path='config.json'):
        """Initialize the scraper with configuration"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        self.site_url = self.config['site_url']
        self.output_dir = Path(self.config['output_dir'])
        self.screenshots_dir = Path(self.config['screenshots_dir'])
        self.media_dir = Path(self.config['media_dir'])
        self.pages_dir = Path(self.config['pages_dir'])

        # Create directories
        for dir_path in [self.output_dir, self.screenshots_dir,
                         self.media_dir, self.pages_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

        self.pages_data = []
        self.visited_urls = set()
        self.media_urls = set()

    async def scrape_page(self, browser, url, page_name=None):
        """Scrape a single page with Playwright"""
        print(f"\nScraping: {url}")

        page = await browser.new_page(
            viewport=self.config['viewport'],
            user_agent=self.config['user_agent']
        )

        try:
            # Navigate and wait for content
            await page.goto(url, wait_until='networkidle', timeout=30000)
            await page.wait_for_timeout(self.config['wait_time'])

            # Get rendered HTML
            html_content = await page.content()

            # Parse with BeautifulSoup
            soup = BeautifulSoup(html_content, 'lxml')

            # Extract page title
            title = soup.find('title')
            title_text = title.get_text() if title else page_name or 'Untitled'

            # Clean filename
            filename = self._clean_filename(title_text)

            # Extract main content
            content_data = {
                'url': url,
                'title': title_text,
                'filename': filename,
                'scraped_at': datetime.now().isoformat(),
                'meta': self._extract_meta(soup),
                'navigation': await self._extract_navigation(page),
                'content': self._extract_content(soup),
                'images': self._extract_images(soup, url),
                'forms': await self._extract_forms(page),
                'links': await self._extract_links(page, url),
            }

            # Take screenshots
            desktop_screenshot = self.screenshots_dir / f"{filename}_desktop.png"
            await page.screenshot(path=str(desktop_screenshot), full_page=True)

            # Mobile screenshot
            await page.set_viewport_size(self.config['mobile_viewport'])
            await page.wait_for_timeout(1000)
            mobile_screenshot = self.screenshots_dir / f"{filename}_mobile.png"
            await page.screenshot(path=str(mobile_screenshot), full_page=True)

            # Save HTML
            html_file = self.pages_dir / f"{filename}.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            # Save JSON data
            json_file = self.pages_dir / f"{filename}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(content_data, f, indent=2, ensure_ascii=False)

            self.pages_data.append(content_data)

            print(f"✓ Saved: {filename}")
            return content_data

        except Exception as e:
            print(f"✗ Error scraping {url}: {e}")
            return None
        finally:
            await page.close()

    async def _extract_navigation(self, page):
        """Extract navigation menu structure"""
        try:
            nav_items = await page.evaluate('''() => {
                const navLinks = [];
                const selectors = [
                    'nav a',
                    '[role="navigation"] a',
                    'header a',
                    '.menu a',
                    '[data-testid="linkElement"]'
                ];

                for (const selector of selectors) {
                    const links = document.querySelectorAll(selector);
                    links.forEach(link => {
                        if (link.href && link.textContent.trim()) {
                            navLinks.push({
                                text: link.textContent.trim(),
                                href: link.href,
                                parent: link.closest('nav, header, [role="navigation"]')?.className || ''
                            });
                        }
                    });
                }

                return [...new Set(navLinks.map(JSON.stringify))].map(JSON.parse);
            }''')
            return nav_items
        except Exception as e:
            print(f"Warning: Could not extract navigation: {e}")
            return []

    def _extract_meta(self, soup):
        """Extract meta tags"""
        meta_data = {
            'description': '',
            'keywords': '',
            'og_tags': {},
        }

        # Meta description
        desc = soup.find('meta', attrs={'name': 'description'})
        if desc and desc.get('content'):
            meta_data['description'] = desc['content']

        # Meta keywords
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords and keywords.get('content'):
            meta_data['keywords'] = keywords['content']

        # Open Graph tags
        og_tags = soup.find_all('meta', property=re.compile(r'^og:'))
        for tag in og_tags:
            prop = tag.get('property', '').replace('og:', '')
            meta_data['og_tags'][prop] = tag.get('content', '')

        return meta_data

    def _extract_content(self, soup):
        """Extract main text content"""
        # Remove script, style, nav, footer
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()

        # Try to find main content area
        main_content = soup.find('main') or soup.find('article') or soup.find('body')

        if main_content:
            # Extract headings
            headings = []
            for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                for heading in main_content.find_all(tag):
                    headings.append({
                        'level': tag,
                        'text': heading.get_text(strip=True)
                    })

            # Extract paragraphs
            paragraphs = [p.get_text(strip=True) for p in main_content.find_all('p') if p.get_text(strip=True)]

            # Extract lists
            lists = []
            for ul in main_content.find_all(['ul', 'ol']):
                items = [li.get_text(strip=True) for li in ul.find_all('li')]
                lists.append({
                    'type': ul.name,
                    'items': items
                })

            return {
                'headings': headings,
                'paragraphs': paragraphs,
                'lists': lists,
                'text': main_content.get_text(separator='\n', strip=True)
            }

        return {'text': ''}

    def _extract_images(self, soup, base_url):
        """Extract all images"""
        images = []
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src')
            if src:
                full_url = urljoin(base_url, src)
                images.append({
                    'src': full_url,
                    'alt': img.get('alt', ''),
                    'title': img.get('title', ''),
                })
                self.media_urls.add(full_url)
        return images

    async def _extract_forms(self, page):
        """Extract form information, including iframes (Mailchimp)"""
        try:
            forms_data = await page.evaluate('''() => {
                const forms = [];

                // Regular forms
                document.querySelectorAll('form').forEach(form => {
                    const fields = [];
                    form.querySelectorAll('input, textarea, select').forEach(field => {
                        fields.push({
                            type: field.type || field.tagName.toLowerCase(),
                            name: field.name,
                            id: field.id,
                            placeholder: field.placeholder || '',
                            required: field.required
                        });
                    });

                    forms.push({
                        type: 'form',
                        action: form.action,
                        method: form.method,
                        fields: fields
                    });
                });

                // iFrames (for Mailchimp embeds)
                document.querySelectorAll('iframe').forEach(iframe => {
                    const src = iframe.src;
                    if (src && (src.includes('mailchimp') || src.includes('list-manage'))) {
                        forms.push({
                            type: 'iframe_mailchimp',
                            src: src,
                            width: iframe.width,
                            height: iframe.height
                        });
                    }
                });

                return forms;
            }''')
            return forms_data
        except Exception as e:
            print(f"Warning: Could not extract forms: {e}")
            return []

    async def _extract_links(self, page, base_url):
        """Extract all internal links from rendered page"""
        try:
            site_hostname = urlparse(self.site_url).netloc

            links_data = await page.evaluate('''(siteHostname) => {
                const links = [];
                const seenUrls = new Set();

                document.querySelectorAll('a[href]').forEach(link => {
                    try {
                        const url = new URL(link.href);
                        // Only include links from the same domain
                        if (url.hostname === siteHostname) {
                            // Remove fragments and create clean URL
                            const cleanUrl = url.origin + url.pathname + url.search;
                            if (!seenUrls.has(cleanUrl)) {
                                seenUrls.add(cleanUrl);
                                links.push({
                                    text: link.textContent.trim(),
                                    href: cleanUrl
                                });
                            }
                        }
                    } catch (e) {
                        // Skip invalid URLs
                    }
                });

                return links;
            }''', site_hostname)

            return links_data
        except Exception as e:
            print(f"Warning: Could not extract links: {e}")
            return []

    def _clean_filename(self, text):
        """Clean text to create valid filename"""
        # Remove special characters
        text = re.sub(r'[^\w\s-]', '', text)
        # Replace spaces with hyphens
        text = re.sub(r'[-\s]+', '-', text)
        return text.lower()[:50]

    async def discover_pages(self, browser, start_url):
        """Discover all pages on the site"""
        print(f"\n🔍 Discovering pages from {start_url}...")

        # Scrape homepage first
        homepage_data = await self.scrape_page(browser, start_url, 'home')
        self.visited_urls.add(start_url)

        if not homepage_data:
            print("Failed to scrape homepage")
            return

        # Collect all internal links
        to_visit = set()
        for link in homepage_data.get('links', []):
            url = link['href']
            # Remove fragments and query strings to avoid duplicates
            clean_url = url.split('#')[0].split('?')[0]
            if clean_url and clean_url not in self.visited_urls and urlparse(clean_url).netloc == urlparse(self.site_url).netloc:
                to_visit.add(clean_url)

        # Visit discovered pages - use while loop to process newly discovered URLs
        print(f"\n📄 Found {len(to_visit)} pages to scrape")

        with tqdm(desc="Scraping pages", unit="page") as pbar:
            while to_visit:
                url = to_visit.pop()

                if url in self.visited_urls:
                    continue

                self.visited_urls.add(url)
                page_data = await self.scrape_page(browser, url)
                pbar.update(1)

                # Discover more links from this page
                if page_data:
                    for link in page_data.get('links', []):
                        new_url = link['href']
                        # Remove fragments and query strings
                        clean_url = new_url.split('#')[0].split('?')[0]
                        if clean_url and clean_url not in self.visited_urls and urlparse(clean_url).netloc == urlparse(self.site_url).netloc:
                            to_visit.add(clean_url)
                            pbar.total = len(self.visited_urls) + len(to_visit)
                            pbar.refresh()

                await asyncio.sleep(1)  # Be polite

    async def download_media(self, browser):
        """Download all media files"""
        print(f"\n📥 Downloading {len(self.media_urls)} media files...")

        page = await browser.new_page()

        for i, url in enumerate(tqdm(list(self.media_urls), desc="Downloading media")):
            try:
                # Get filename from URL
                filename = Path(urlparse(url).path).name
                if not filename:
                    filename = f"media_{i}.jpg"

                # Create subdirectory based on file type
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')):
                    subdir = self.media_dir / 'images'
                else:
                    subdir = self.media_dir / 'documents'

                subdir.mkdir(exist_ok=True)
                filepath = subdir / filename

                # Download
                response = await page.goto(url, timeout=15000)
                if response and response.ok:
                    content = await response.body()
                    with open(filepath, 'wb') as f:
                        f.write(content)
            except Exception as e:
                print(f"Failed to download {url}: {e}")

        await page.close()

    def generate_report(self):
        """Generate summary report"""
        report_path = self.output_dir / 'scrape_report.json'

        report = {
            'scraped_at': datetime.now().isoformat(),
            'site_url': self.site_url,
            'total_pages': len(self.pages_data),
            'total_media': len(self.media_urls),
            'pages': [
                {
                    'title': page['title'],
                    'url': page['url'],
                    'filename': page['filename'],
                    'image_count': len(page.get('images', [])),
                    'form_count': len(page.get('forms', []))
                }
                for page in self.pages_data
            ],
            'navigation_structure': self.pages_data[0].get('navigation', []) if self.pages_data else [],
            'mailchimp_forms': []
        }

        # Find Mailchimp forms
        for page in self.pages_data:
            for form in page.get('forms', []):
                if form.get('type') == 'iframe_mailchimp':
                    report['mailchimp_forms'].append({
                        'page': page['title'],
                        'url': page['url'],
                        'iframe_src': form.get('src')
                    })

        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Report saved to {report_path}")
        return report

    async def run(self):
        """Main scraping workflow"""
        print("🚀 Starting Wix site scraper...")
        print(f"Target: {self.site_url}")

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.config['headless'])

            try:
                # Discover and scrape all pages
                await self.discover_pages(browser, self.site_url)

                # Download media
                if self.media_urls:
                    await self.download_media(browser)

                # Generate report
                report = self.generate_report()

                print("\n" + "="*60)
                print("✅ SCRAPING COMPLETE")
                print("="*60)
                print(f"Pages scraped: {report['total_pages']}")
                print(f"Media downloaded: {report['total_media']}")
                print(f"Mailchimp forms found: {len(report['mailchimp_forms'])}")
                print(f"\nOutput directory: {self.output_dir}")
                print("="*60)

            finally:
                await browser.close()


async def main():
    scraper = WixScraper('config.json')
    await scraper.run()


if __name__ == '__main__':
    asyncio.run(main())
