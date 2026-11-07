# cloudbookassociates.com

Website of **Cloudbook Associates LLP**, accounting, tax and compliance, Thiruvallam, Thiruvananthapuram.

- Plain HTML and CSS, no frameworks, no tracking, no third-party requests. Fonts are self-hosted.
- The enquiry form opens WhatsApp or email with the message filled in; nothing is stored by the site.
- SEO: a page per service, compliance calendar, titles and descriptions, canonical URLs, Open Graph image, `AccountingService` / `Service` / `FAQPage` / `BreadcrumbList` structured data, `sitemap.xml` and `robots.txt`.

## Editing

All content (firm details, services, FAQs, the compliance calendar) is in `_build/build.py`. Edit it, then run:

```bash
python3 _build/build.py
```

and commit the generated `.html`, `sitemap.xml` and `robots.txt` files. Styles are in `assets/site.css`, the small script in `assets/site.js`.

## Hosting

GitHub Pages from the `main` branch, root folder, with the custom domain `cloudbookassociates.com` (and `www`).
