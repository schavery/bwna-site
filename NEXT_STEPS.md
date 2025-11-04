# Next Steps for BWNA WordPress Migration

## 🎯 Current Status

✅ **Completed**:
- Migration plan created
- Project structure set up
- Web scraper built (Python + Playwright)
- WordPress theme foundation created
- Documentation completed

## 📋 What to Do Next

### Step 1: Run the Scraper (Required)

This will extract all content, design elements, and media from the Wix site.

```bash
cd scrapers

# Set up Python environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install browser for Playwright
playwright install chromium

# Run the scraper
python scrape_site.py
```

**Expected Output**:
- All pages scraped to `scraped-content/pages/`
- All images downloaded to `scraped-content/media/images/`
- Screenshots in `scraped-content/screenshots/`
- Summary report: `scraped-content/scrape_report.json`

**What to Check**:
- Review `scrape_report.json` for overview
- Look at screenshots to verify design was captured
- Check that Mailchimp forms were detected
- Verify all pages are present

---

### Step 2: Analyze Scraped Content

Once scraping is complete:

1. **Review the scrape report**:
   ```bash
   cat scraped-content/scrape_report.json
   ```

2. **Create a style guide** based on screenshots:
   - Document colors (using eyedropper tool)
   - Identify fonts
   - Note spacing and layout patterns
   - Save to `docs/style-guide.md`

3. **List all pages** to be migrated:
   - Create `docs/page-inventory.md`
   - Include page hierarchy
   - Note special layouts

---

### Step 3: Update Theme Design

Based on the scraped content and style guide:

1. **Update CSS variables** in `wordpress/wp-content/themes/bwna-theme/style.css`:
   ```css
   :root {
     --color-primary: #YOUR_COLOR;
     --color-secondary: #YOUR_COLOR;
     --font-primary: 'Your Font', sans-serif;
     /* etc */
   }
   ```

2. **Add fonts** (if custom fonts are used):
   - Download font files to `assets/fonts/`
   - Add @font-face rules in style.css

3. **Build components** matching the Wix design:
   - Header navigation
   - Footer layout
   - Buttons
   - Content sections

4. **Create page templates** for different layouts:
   - Full width template
   - Sidebar template
   - Custom homepage sections

---

### Step 4: Set Up Local WordPress

To test the theme:

**Option A: Using Local by Flywheel** (Easiest)
1. Download: https://localwp.com/
2. Create new site: "bwna-test"
3. Copy theme folder to: `app/public/wp-content/themes/bwna-theme/`
4. Activate theme

**Option B: Using Docker**
```bash
# Create docker-compose.yml with WordPress + MySQL
docker-compose up -d
```

**Option C: Manual XAMPP/MAMP installation**
- Install XAMPP or MAMP
- Download WordPress
- Set up database
- Copy theme to wp-content/themes/

---

### Step 5: Import Content

With WordPress running locally:

1. **Create pages**:
   - Use scraped JSON files as reference
   - Copy content from `scraped-content/pages/*.json`
   - Maintain hierarchy from Wix

2. **Upload media**:
   - Bulk upload from `scraped-content/media/images/`
   - Add alt text (use scraped data)

3. **Set up menus**:
   - Create primary menu matching Wix navigation
   - Create footer menu

4. **Add Mailchimp forms**:
   - Get iframe URLs from `scrape_report.json`
   - Add using shortcode: `[mailchimp src="URL"]`

---

### Step 6: Test Locally

Before deploying:

- [ ] All pages display correctly
- [ ] Navigation works
- [ ] Mailchimp forms function
- [ ] Mobile responsive
- [ ] Images load properly
- [ ] Blog posts display (if applicable)

---

### Step 7: Deploy to WordPress.com

See detailed instructions in `docs/deployment-guide.md`

**Quick steps**:
1. Sign up for WordPress.com Business plan
2. Zip theme: `zip -r bwna-theme.zip bwna-theme/`
3. Upload theme via Appearance > Themes
4. Import content
5. Configure settings
6. Test thoroughly
7. Point domain to WordPress.com

---

## 📁 Project Structure Reference

```
bwna-wp/
├── MIGRATION_PLAN.md          # Complete migration strategy
├── NEXT_STEPS.md              # This file - your roadmap
├── README.md                  # Project overview
│
├── docs/                      # Documentation
│   ├── site-requirements.md   # Project requirements
│   ├── deployment-guide.md    # Step-by-step deployment
│   └── [CREATE THESE:]
│       ├── style-guide.md     # After scraping
│       └── page-inventory.md  # After scraping
│
├── scrapers/                  # Web scraping tools
│   ├── scrape_site.py        # Main scraper script
│   ├── requirements.txt       # Python dependencies
│   ├── config.json           # Scraper configuration
│   └── README.md             # Scraper documentation
│
├── scraped-content/          # Output from scraper
│   ├── pages/                # Page HTML and JSON
│   ├── media/                # Downloaded images
│   ├── screenshots/          # Design reference
│   └── scrape_report.json    # Summary report
│
└── wordpress/wp-content/themes/bwna-theme/
    ├── style.css             # Main stylesheet
    ├── functions.php         # Theme functions
    ├── [template files]      # All theme templates
    └── assets/               # CSS, JS, images
```

---

## 🆘 Common Issues & Solutions

### Scraper Issues

**Problem**: Scraper times out
- **Solution**: Increase `wait_time` in `config.json`

**Problem**: Content not captured
- **Solution**: Run with `headless: false` to see browser

**Problem**: Images not downloading
- **Solution**: Check network connection and try again

### Theme Issues

**Problem**: Theme won't activate
- **Solution**: Check PHP syntax errors in all files

**Problem**: Styling doesn't match
- **Solution**: Review scraped screenshots and adjust CSS

**Problem**: Mailchimp forms don't work
- **Solution**: Verify iframe URLs in scrape report

---

## 📞 Need Help?

1. **Review documentation**:
   - MIGRATION_PLAN.md (comprehensive guide)
   - deployment-guide.md (deployment steps)
   - Theme README.md (theme features)
   - Scraper README.md (scraping help)

2. **Check scrape report**:
   - `scraped-content/scrape_report.json`

3. **Verify prerequisites**:
   - Python 3.8+ installed
   - WordPress.com account ready
   - Local development environment

---

## 🎉 Success Checklist

Track your progress:

- [ ] Scraper ran successfully
- [ ] All content extracted
- [ ] Style guide created
- [ ] Theme design updated
- [ ] Local WordPress set up
- [ ] Content imported locally
- [ ] Local testing complete
- [ ] WordPress.com account created
- [ ] Theme uploaded to WordPress.com
- [ ] Content migrated to production
- [ ] Mailchimp forms working
- [ ] Domain pointed to WordPress.com
- [ ] Site launched successfully

---

**Ready to start?** Begin with **Step 1: Run the Scraper** above!
