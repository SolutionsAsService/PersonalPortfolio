"""Build index.html from _src/template.html and _src/projects.json.

To add a site: put a 1440x900 screenshot through the image step (see README),
add an entry to projects.json, then run:  python _src/build.py
"""
import html
import json
import pathlib

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent / "site"

data = json.loads((SRC / "projects.json").read_text(encoding="utf-8"))
groups = {g["id"]: g["label"] for g in data["groups"]}
projects = data["projects"]


def host(url):
    return url.split("//", 1)[1].rstrip("/")


def card(p, n, featured=False):
    e = html.escape
    tags = "".join(f"<li>{e(t)}</li>" for t in [groups[p["group"]]] + p.get("tags", []))
    sizes = "(max-width: 760px) 100vw, 50vw" if featured else "(max-width: 760px) 100vw, (max-width: 1100px) 50vw, 33vw"
    return f"""
        <li class="card{' card--feature' if featured else ''}{' card--wide' if p.get('wide') else ''}" data-group="{p['group']}" id="work-{p['slug']}">
          <a href="{e(p['url'])}" target="_blank" rel="noopener" aria-labelledby="t-{p['slug']} g-{p['slug']}">
            <span class="bar" aria-hidden="true"><i></i><i></i><i></i><span>{e(host(p['url']))}</span></span>
            <img src="images/work/{p['slug']}-600.jpg" srcset="images/work/{p['slug']}-600.jpg 600w, images/work/{p['slug']}-1200.jpg 1200w" sizes="{sizes}" width="600" height="375" alt="" loading="{'eager' if featured else 'lazy'}" />
            <span class="meta">
              <span class="plate">No. {n:02d}</span>
              <span class="title" id="t-{p['slug']}">{e(p['title'])}</span>
              <span class="line">{e(p['line'])}</span>
              <span class="go" id="g-{p['slug']}">Visit {e(host(p['url']))}<span class="sr-only"> (opens in a new tab)</span></span>
            </span>
          </a>
          <ul class="tags">{tags}</ul>
        </li>"""


featured = [p for p in projects if p.get("featured")]
rest = [p for p in projects if not p.get("featured")]
numbered = {p["slug"]: i + 1 for i, p in enumerate(featured + rest)}

strip = "".join(
    f'<a href="#work-{p["slug"]}" class="slice" style="background-image:url(images/work/{p["slug"]}-600.jpg)"><span class="sr-only">{html.escape(p["title"])}</span></a>'
    for p in featured + rest
)
filters = "".join(
    f'<button type="button" class="chip" data-filter="{g["id"]}" aria-pressed="false">{html.escape(g["label"])} <span>{sum(p["group"] == g["id"] for p in projects)}</span></button>'
    for g in data["groups"]
)

out = (SRC / "template.html").read_text(encoding="utf-8")
out = out.replace("{{count}}", str(len(projects)))
out = out.replace("{{strip}}", strip)
out = out.replace("{{filters}}", filters)
out = out.replace("{{featured}}", "".join(card(p, numbered[p["slug"]], True) for p in featured))
out = out.replace("{{rest}}", "".join(card(p, numbered[p["slug"]]) for p in rest))
assert "{{" not in out, "unfilled placeholder"
(ROOT / "index.html").write_text(out, encoding="utf-8", newline="\n")
print("built index.html with", len(projects), "projects")
