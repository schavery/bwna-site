# BWNA WordPress Deployment Guide

Complete guide for deploying the BWNA WordPress site to WordPress.com

## Prerequisites

- [ ] WordPress.com account (Business plan or higher for custom themes)
- [ ] Scraped content from Wix site
- [ ] Theme fully developed and tested locally
- [ ] All media files optimized
- [ ] Mailchimp form URLs

---

## Phase 1: Prepare for Deployment

### 1.1 Run the Scraper

```bash
cd scrapers
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
python scrape_site.py
```

Review the output in `scraped-content/`:
- Check `scrape_report.json` for summary
- Verify all pages were captured
- Confirm Mailchimp forms were detected
- Review screenshots for design accuracy

### 1.2 Update Theme Design

Based on scraped content:

1. **Extract Colors**: Review screenshots and update CSS variables in `style.css`
2. **Typography**: Identify fonts and add to theme
3. **Layout**: Adjust spacing, widths, and structure
4. **Components**: Build matching header, footer, buttons, etc.

### 1.3 Optimize Media

```bash
# Compress images (use ImageOptim, TinyPNG, or similar)
# Recommended: images should be < 500KB each
# Convert to WebP if possible for better performance
```

---

## Phase 2: Local Testing

### 2.1 Set Up Local WordPress

**Using Local by Flywheel** (Recommended):
1. Download Local: https://localwp.com/
2. Create new site: "bwna-test"
3. Copy theme to: `app/public/wp-content/themes/bwna-theme/`
4. Activate theme in WordPress admin

**Using Docker**:
```bash
docker run -d \
  -p 8080:80 \
  -e WORDPRESS_DB_HOST=db \
  -e WORDPRESS_DB_USER=wordpress \
  -e WORDPRESS_DB_PASSWORD=wordpress \
  --name bwna-wp \
  wordpress:latest
```

### 2.2 Import Content

1. **Create Pages**:
   - Use scraped JSON files as reference
   - Create pages matching Wix structure
   - Copy content from `pages/*.json`
   - Upload featured images

2. **Create Blog Posts** (if applicable):
   - Import blog content
   - Set publish dates
   - Assign categories/tags

3. **Upload Media**:
   - Go to Media > Add New
   - Bulk upload images from `scraped-content/media/images/`
   - Update media library metadata (alt text, descriptions)

### 2.3 Configure Mailchimp Forms

1. Get embed URLs from scraped data (`scrape_report.json`)
2. Add forms to pages using shortcode:
   ```
   [mailchimp src="https://YOUR_MAILCHIMP_URL" width="100%" height="600"]
   ```
3. Test form submissions

### 2.4 Set Up Menus

1. **Appearance > Menus**
2. Create "Primary Menu":
   - Add pages matching Wix navigation
   - Set menu hierarchy
   - Assign to "Primary Menu" location
3. Create "Footer Menu" (if needed)

### 2.5 Configure Widgets

1. **Appearance > Widgets**
2. Add widgets to Footer 1, 2, 3
3. Consider adding:
   - Text/HTML widgets
   - Social media links
   - Contact information

### 2.6 Test Locally

- [ ] All pages display correctly
- [ ] Navigation works
- [ ] Mailchimp forms work
- [ ] Images load properly
- [ ] Responsive design works on all devices
- [ ] Links are not broken
- [ ] Search functionality works

---

## Phase 3: WordPress.com Deployment

### 3.1 Sign Up for WordPress.com

1. Go to https://wordpress.com/
2. Create account or log in
3. Choose "Business" plan or higher (required for custom themes)
4. Select domain name or use temporary subdomain

### 3.2 Upload Theme

1. **Zip the theme**:
   ```bash
   cd wordpress/wp-content/themes
   zip -r bwna-theme.zip bwna-theme/
   ```

2. **Upload to WordPress.com**:
   - Log in to WordPress.com dashboard
   - Go to Appearance > Themes
   - Click "Add New" > "Upload Theme"
   - Select `bwna-theme.zip`
   - Click "Install Now"
   - Activate the theme

### 3.3 Import Content

**Option 1: Manual Entry** (Recommended for small sites)
- Create each page manually
- Copy content from local site
- Upload images

**Option 2: WordPress Exporter/Importer**
1. On local site: Tools > Export > All content
2. Download XML file
3. On WordPress.com: Tools > Import > WordPress
4. Upload XML file
5. Import media files

**Option 3: WP All Import Plugin** (if available on WordPress.com)
- More flexible for complex imports
- Can map scraped JSON to WordPress content

### 3.4 Configure Site Settings

1. **Settings > General**:
   - Site Title
   - Tagline
   - Time Zone

2. **Settings > Reading**:
   - Set homepage (static front page)
   - Set blog page (if applicable)

3. **Settings > Permalinks**:
   - Choose permalink structure
   - Try to match Wix URLs where possible

4. **Appearance > Customize**:
   - Upload logo
   - Set colors (if using customizer)
   - Configure header/footer

### 3.5 Set Up Menus & Widgets

Repeat the same configuration from local testing:
- Create and assign menus
- Configure widget areas
- Test navigation

### 3.6 Add Mailchimp Forms

Add Mailchimp shortcodes to appropriate pages:
```
[mailchimp src="YOUR_MAILCHIMP_URL" width="100%" height="600"]
```

---

## Phase 4: Testing & Launch

### 4.1 Pre-Launch Checklist

- [ ] All pages created and content accurate
- [ ] All images uploaded and displaying
- [ ] Navigation menus working
- [ ] Mailchimp forms functional
- [ ] Footer content complete
- [ ] Logo uploaded
- [ ] Favicon set
- [ ] Blog posts migrated (if applicable)
- [ ] Mobile responsive on all pages
- [ ] Cross-browser testing complete

### 4.2 SEO Configuration

Install SEO plugin (if available on WordPress.com):
- Yoast SEO or Rank Math

For each page:
- [ ] Set SEO title (use scraped meta data)
- [ ] Set meta description
- [ ] Set focus keyword
- [ ] Add alt text to all images
- [ ] Check readability

### 4.3 Performance Testing

1. **Test page speed**:
   - Google PageSpeed Insights
   - GTmetrix
   - Target: < 3 second load time

2. **Optimize if needed**:
   - Further compress images
   - Enable caching (if available)
   - Minimize redirects

### 4.4 Set Up Analytics

1. **Google Analytics**:
   - Create GA4 property
   - Add tracking code to theme or via plugin
   - Verify tracking is working

2. **Google Search Console**:
   - Add property
   - Verify ownership
   - Submit sitemap

### 4.5 Final Testing

Test on multiple devices and browsers:

**Devices**:
- [ ] iPhone (Safari)
- [ ] Android phone (Chrome)
- [ ] iPad (Safari)
- [ ] Desktop (Chrome, Firefox, Safari, Edge)

**Test Cases**:
- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Mailchimp forms submit successfully
- [ ] Images display properly
- [ ] Contact information is correct
- [ ] Footer links work
- [ ] Search functionality works
- [ ] 404 page displays correctly

---

## Phase 5: Domain & Go-Live

### 5.1 Domain Setup

**Option 1: Use existing domain (bwnapdx.org)**
1. Update DNS settings at current registrar
2. Point to WordPress.com nameservers:
   - ns1.wordpress.com
   - ns2.wordpress.com
   - ns3.wordpress.com
3. Wait for propagation (up to 48 hours)

**Option 2: Transfer domain to WordPress.com**
1. Follow WordPress.com domain transfer process
2. Unlock domain at current registrar
3. Get authorization code
4. Initiate transfer in WordPress.com

### 5.2 SSL Certificate

WordPress.com provides free SSL certificates:
- Automatically provisioned after domain connection
- Verify HTTPS is working

### 5.3 Set Up Redirects

If Wix URLs differ from WordPress URLs:

1. Create redirect map:
   ```
   Old Wix URL → New WordPress URL
   ```

2. Implement redirects:
   - Use Redirection plugin (if available)
   - Or add to .htaccess (if accessible)
   - Or contact WordPress.com support

### 5.4 Go-Live

1. **Remove "Coming Soon" page** (if set)
2. **Verify domain is working**
3. **Test all functionality one more time**
4. **Announce launch** (email, social media, etc.)

---

## Phase 6: Post-Launch

### 6.1 Monitor

First week after launch:
- [ ] Check Google Analytics daily
- [ ] Monitor Google Search Console for errors
- [ ] Watch for broken links
- [ ] Check Mailchimp form submissions
- [ ] Monitor site speed
- [ ] Check error logs (if accessible)

### 6.2 Keep Wix Site Active

**Important**: Keep the Wix site live for 30-60 days:
- Set up redirects from Wix to WordPress
- Monitor traffic patterns
- Ensure search engines have indexed new site
- Catch any missed content

### 6.3 Update External Links

Update links to site wherever they appear:
- Social media profiles
- Email signatures
- Business listings (Google My Business, Yelp, etc.)
- Partner websites
- Newsletter archives

### 6.4 Backups

Set up automatic backups:
- WordPress.com includes backups
- Verify backup schedule
- Test restoration process

### 6.5 Maintenance Plan

Regular maintenance tasks:
- Update WordPress core (WordPress.com handles this)
- Update theme when needed
- Monitor and optimize performance
- Review analytics monthly
- Update content regularly

---

## Troubleshooting

### Theme Upload Issues
- **Error: Missing style.css**: Ensure style.css is in theme root with proper header
- **Error: Broken theme**: Check all PHP files for syntax errors
- **Theme won't activate**: Verify all required template files exist

### Content Issues
- **Images not displaying**: Check file paths and re-upload if needed
- **Formatting looks wrong**: Review HTML structure and CSS
- **Menu not showing**: Verify menu is assigned to correct location

### Mailchimp Forms
- **Form not displaying**: Check iframe embed code and shortcode syntax
- **Form not submitting**: Verify Mailchimp URL is correct and list is active
- **Styling issues**: Add custom CSS to adjust form appearance

### WordPress.com Limitations
- Some plugins may not be available
- .htaccess access may be limited
- Custom code may be restricted

**Solution**: Use WordPress.com's built-in features or contact support

---

## Rollback Plan

If issues arise after launch:

1. **Keep Wix site active** for quick rollback
2. **Update DNS** back to Wix if needed
3. **Communicate** with stakeholders about issues
4. **Fix issues** on WordPress.com staging site
5. **Relaunch** when ready

---

## Success Metrics

Track these metrics to measure successful migration:

- [ ] Page load speed: < 3 seconds
- [ ] Mobile usability: 100% in Google tools
- [ ] All pages indexed in Google within 2 weeks
- [ ] Traffic maintained or increased vs. Wix
- [ ] Mailchimp form submissions working
- [ ] Zero critical errors in Search Console
- [ ] Positive user feedback

---

## Need Help?

- WordPress.com Support: https://wordpress.com/support/
- WordPress Forums: https://wordpress.org/support/
- Theme Documentation: See theme README.md

---

**Last Updated**: 2025-11-04
