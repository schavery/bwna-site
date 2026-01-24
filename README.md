# BWNA Website

The official website for the Beaumont-Wilshire Neighborhood Association, built with [Astro](https://astro.build).

## 🚀 Quick Start for Volunteers

**You don't need to be a programmer to update this website!** Most content updates involve editing simple text files.

### What You Need

1. A GitHub account (free)
2. A text editor (even Notepad works, or use GitHub's web editor)
3. 10 minutes to learn the basics

### The Simple Truth

This website is just a folder of text files. When you save a change, the website automatically rebuilds and publishes itself. That's it.

---

## 📝 Common Tasks

### Adding a New Event

1. Create a new file in `src/content/events/` named something like `2026-03-15-spring-cleanup.md`
2. Copy this template and fill in your event details:

```markdown
---
title: "Spring Neighborhood Cleanup"
date: 2026-03-15
time: "9:00 AM - 12:00 PM"
location: "Wilshire Park"
address: "NE 33rd & Skidmore"
type: "community"
---

Join your neighbors for our annual spring cleanup! We'll be picking up litter,
pulling weeds, and beautifying our public spaces.

Bring gloves if you have them. Trash bags and tools provided.

Contact: events@bwnapdx.org
```

3. Save the file and commit to GitHub. The site rebuilds automatically!

### Adding Newsletter Content

For a web-native newsletter article:

1. Create a new file in `src/content/newsletters/` like `2026-01-presidents-message.md`
2. Use this format:

```markdown
---
title: "President's Message"
issue: "Jan-Feb 2026"
author: "Al Ellis"
---

Your article content goes here. Just write normally!

You can have multiple paragraphs.

## Subheadings Work Too

And [links to things](https://example.com) are easy.
```

### Updating Board Member Info

Edit `src/pages/about.astro` and find the `boardMembers` list near the top. Update the relevant entry:

```javascript
{ name: "New Person", role: "Board Member", since: "2026", email: "email@bwnapdx.org" },
```

---

## 🏗️ Project Structure

```
bwna-site/
├── public/              # Static files (images, PDFs, favicon)
│   └── images/
├── src/
│   ├── components/      # Reusable page parts
│   ├── content/         # YOUR CONTENT GOES HERE
│   │   ├── events/      # Event markdown files
│   │   ├── newsletters/ # Newsletter articles
│   │   └── board-members/
│   ├── layouts/         # Page templates
│   ├── pages/           # Website pages
│   └── styles/          # CSS styling
├── astro.config.mjs     # Site configuration
└── package.json         # Dependencies
```

**For content updates, you only need to touch files in `src/content/` and `public/`**

---

## 🤖 Getting Help from AI

One of the best things about this setup is that AI assistants (like Claude) can help you with almost anything:

**Example prompts:**
- "Here's the event details: [paste info]. Can you format this as a markdown event file for our Astro site?"
- "I need to add a new page for the Art & Garden Tour. Can you create the file?"
- "The newsletter PDF is attached. Can you convert the President's Message into a web article?"
- "How do I add an image to the homepage?"

The AI can read all the code and understand exactly how the site works because it's all simple text files.

---

## 💻 For Developers

### Local Development

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Deployment

The site is configured for deployment on [Netlify](https://netlify.com) / [Cloudflare Pages](https://pages.cloudflare.com) / [GitHub Pages](https://pages.github.com).

Push to `main` branch → automatic deployment.

### Content Collections (Future Enhancement)

For type-safe content, configure Astro content collections in `src/content/config.ts`. This enables:
- Validation of frontmatter fields
- Auto-generated types
- Better error messages for content editors

---

## 📧 Questions?

- **Website issues:** Contact the Communications Committee
- **Content questions:** editor@bwnapdx.org
- **Technical help:** [Open a GitHub issue](../../issues)

---

*Built with ❤️ by BWNA volunteers*
