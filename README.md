# SolutionsAsService — portfolio

A one-page index of live projects: each card opens the real site. Static site, deployed on Vercel.

## Add or change a project

1. Screenshot the live site at 1440×900 and save two copies in `images/work/`: `<slug>-1200.jpg` (1200×750) and `<slug>-600.jpg` (600×375).
2. Add an entry to `_src/projects.json`: `slug`, `title`, `url`, `group` (`business`, `maps`, `tools` or `guides`), a one-line `line`, optional `tags`, and `"featured": true` to put it in the large top row.
3. Rebuild:

```bash
python _src/build.py
```

The page text lives in `_src/template.html`. Styles are in `css/style.css`, and the filter script is in `js/site.js`.

## To do

- Add a contact email to the Contact section in `_src/template.html`. It currently links to the GitHub org.

Design decisions and the critique rounds are in `DESIGN-LOG.md`.
