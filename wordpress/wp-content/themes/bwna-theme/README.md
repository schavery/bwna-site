# BWNA WordPress Theme

Custom WordPress theme for Beaumont-Wilshire Neighborhood Association, migrated from Wix.

## Description

This theme replicates the design and functionality of the original Wix site at https://www.bwnapdx.org/

## Features

- Responsive design (mobile, tablet, desktop)
- Custom page templates
- Navigation menus (primary and footer)
- Widget-ready sidebar and footer
- Mailchimp embed support via shortcode
- Blog/post functionality
- SEO-friendly markup
- Custom logo support
- Featured images

## Installation

### For Local Development

1. Copy this theme folder to `wp-content/themes/`
2. Activate the theme in WordPress admin
3. Configure menus under Appearance > Menus
4. Set up widgets under Appearance > Widgets
5. Upload logo under Appearance > Customize

### For WordPress.com

1. Zip the entire theme folder
2. Upload via Appearance > Themes > Add New > Upload Theme
3. Activate and configure

## Theme Configuration

### Menus

Set up these menu locations:
- **Primary Menu**: Main navigation in header
- **Footer Menu**: Links in footer

### Widget Areas

- **Sidebar**: Right sidebar for blog posts
- **Footer 1-3**: Three footer columns

### Customization

Customize the following under Appearance > Customize:
- Site Identity (logo, site title)
- Colors (after design analysis)
- Typography (after design analysis)
- Header & Footer settings

## Mailchimp Integration

Use the shortcode to embed Mailchimp forms:

```
[mailchimp src="YOUR_MAILCHIMP_URL" width="100%" height="500"]
```

Example:
```
[mailchimp src="https://list-manage.com/subscribe/post?u=xxx&id=xxx" width="100%" height="600"]
```

## Page Templates

- **Default Template**: Standard page layout
- **Front Page**: Homepage with custom sections
- **Blog**: Post archive
- **Single Post**: Individual blog posts

## Development

### File Structure

```
bwna-theme/
├── style.css              # Main stylesheet with theme header
├── functions.php          # Theme functions
├── index.php             # Blog archive
├── front-page.php        # Homepage
├── page.php              # Static pages
├── single.php            # Single posts
├── header.php            # Site header
├── footer.php            # Site footer
├── sidebar.php           # Sidebar
├── searchform.php        # Search form
├── 404.php               # 404 error page
├── assets/
│   ├── css/              # Additional CSS
│   ├── js/
│   │   └── main.js       # Main JavaScript
│   ├── images/           # Theme images
│   └── fonts/            # Custom fonts (if needed)
└── template-parts/       # Reusable template parts
```

### CSS Variables

The theme uses CSS custom properties for easy customization:

```css
:root {
  --color-primary: #333;
  --color-accent: #0073aa;
  --font-primary: sans-serif;
  /* etc */
}
```

Update these in `style.css` after analyzing the Wix site design.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Requirements

- WordPress 6.0+
- PHP 7.4+

## Next Steps

1. **Run the scraper** to extract content and design from Wix site
2. **Analyze design** and update CSS variables in style.css
3. **Import content** (pages, blog posts, images)
4. **Configure Mailchimp** forms with actual embed URLs
5. **Test thoroughly** on all devices
6. **Deploy to production**

## Support

For issues or questions, refer to the main project documentation.

## License

GNU General Public License v2 or later
