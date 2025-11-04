# BWNA Website Scraper

Automated scraping tools to extract content, media, and structure from the Wix site at https://www.bwnapdx.org/

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### 2. Run the Scraper

```bash
python scrape_site.py
```

## What Gets Scraped

The scraper will extract:

- **All pages** on the site with full content
- **Navigation structure** (menus and links)
- **All images and media** files
- **Mailchimp form iframes** (both signup forms)
- **Meta data** (titles, descriptions, Open Graph tags)
- **Page screenshots** (desktop and mobile views)
- **Content structure** (headings, paragraphs, lists)
- **Internal links** for site structure

## Output Structure

```
scraped-content/
├── pages/                  # Individual page data
│   ├── home.html          # Full HTML
│   ├── home.json          # Structured data
│   ├── about.html
│   ├── about.json
│   └── ...
├── media/                  # Downloaded assets
│   ├── images/            # All images
│   └── documents/         # PDFs and other files
├── screenshots/            # Visual reference
│   ├── home_desktop.png
│   ├── home_mobile.png
│   └── ...
└── scrape_report.json     # Complete summary
```

## Configuration

Edit `config.json` to customize:

```json
{
  "site_url": "https://www.bwnapdx.org",
  "wait_time": 3000,           // Wait for page load (ms)
  "headless": true,            // Run browser in background
  "viewport": {
    "width": 1920,
    "height": 1080
  }
}
```

## Features

### Mailchimp Form Detection

The scraper specifically looks for Mailchimp iframe embeds and captures:
- iframe source URL
- Dimensions
- Placement location on each page

This ensures we can recreate the signup forms in WordPress.

### Blog Post Detection

The scraper will identify and extract blog/news posts, preserving:
- Post title and content
- Publication dates (if available)
- Images and media
- Categories/tags

### Smart Content Extraction

Uses multiple strategies to find content:
- Looks for `<main>`, `<article>` tags
- Removes navigation, footers, scripts
- Preserves content hierarchy
- Extracts structured data (headings, lists, etc.)

## Troubleshooting

### Scraper hangs or times out
- Increase `wait_time` in config.json
- Run with `headless: false` to see what's happening

### Missing content
- Some content may be lazy-loaded
- Check the screenshots to verify what was captured

### Permission errors
- Ensure output directories are writable
- Run with appropriate permissions

## Next Steps

After scraping:

1. Review `scrape_report.json` for overview
2. Check screenshots for visual accuracy
3. Review JSON files for content structure
4. Verify Mailchimp forms were detected
5. Begin theme development to match design
