"""Refresh the five README article cards using the public English blog."""

import argparse
import base64
from dataclasses import asdict, dataclass, replace
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from functools import lru_cache
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ASSETS = Path("assets/readme-blog")
DATA = Path("data/latest-posts.json")
BLOG = "https://danieldias.dev/en/blog"
START = "<!-- BLOG-POST-LIST:START -->"
END = "<!-- BLOG-POST-LIST:END -->"
CATEGORIES = {".NET", "AZURE", "CLOUD", "DATABASE", "AI", "SYSTEM DESIGN", "LEARNING"}
WIDTHS = json.loads((ROOT / ASSETS / "fonts/title-widths.json").read_text())
SHAPES = [
    [(1,1.6),(30,.4),(64,1.8),(99.2,.6),(98.4,26),(99.4,52),(98.5,76),(99.2,97.6),(62,99.4),(30,98.2),(1,99.2),(1.8,74),(.6,50),(1.7,26)],
    [(.6,.6),(34,1.8),(68,.4),(99.4,1.4),(98.5,24),(99.3,50),(98.4,74),(99.4,99),(64,98.2),(32,99.4),(.8,98.4),(1.6,76),(.5,52),(1.6,28)],
]


@dataclass(frozen=True)
class Post:
    title: str
    url: str
    category: str
    published_at: str
    reading_minutes: int = 0

    @property
    def meta(self):
        date = datetime.fromisoformat(self.published_at)
        month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[date.month - 1]
        return f"{date.day} {month} {date.year} · {self.reading_minutes} MIN"


def article_url(url):
    parts = urlsplit(url)
    if (parts.scheme != "https" or parts.netloc != "danieldias.dev"
            or not parts.path.startswith("/en/blog/") or parts.query or parts.fragment):
        raise ValueError(f"Unexpected article URL: {url}")
    return url


def parse_feed(content):
    posts = {}
    for item in ET.fromstring(content).findall("./channel/item"):
        title = " ".join((item.findtext("title") or "").split())
        category = (item.findtext("category") or "").strip().upper()
        url = article_url((item.findtext("link") or "").strip())
        if not title or not category:
            raise ValueError("An article is missing its title or category")
        published = parsedate_to_datetime(item.findtext("pubDate") or "")
        if published.tzinfo is None:
            raise ValueError("Publication dates must include a timezone")
        posts[url] = Post(title, url, category, published.astimezone(timezone.utc).isoformat())
    if not posts:
        raise ValueError("The RSS feed contains no articles; keeping the current cards")
    return sorted(posts.values(), key=lambda post: post.published_at, reverse=True)[:5]


class BlogIndex(HTMLParser):
    def __init__(self):
        super().__init__()
        self.minutes = {}
        self.categories = {}
        self.category = None
        self.field = None
        self.url = None
        self.depth = 0
        self.parts = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        classes = attrs.get("class", "").split()
        if self.depth:
            if tag not in {"br", "img", "hr", "input", "source", "wbr"}:
                self.depth += 1
        if "blog-note__link" in classes:
            self.url = urljoin(BLOG, attrs.get("href", ""))
            self.categories[self.url] = self.category
        if "blog-note__stamp" in classes:
            self.depth = 1
            self.parts = []
            self.field = "category"
        if "blog-note__meta" in classes:
            self.depth = 1
            self.parts = []
            self.field = "minutes"

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if not self.depth:
            return
        self.depth -= 1
        if not self.depth:
            if self.field == "category":
                self.category = "".join(self.parts).strip().upper()
                return
            match = re.search(r"\b([1-9][0-9]*)\s*MIN\b", "".join(self.parts), re.I)
            if self.url and match:
                self.minutes[self.url] = int(match[1])


def fetch(url):
    request = Request(url, headers={"User-Agent": "DeVFirmino-profile/1.0"})
    with urlopen(request, timeout=30) as response:
        return response.read()


def live_posts():
    posts = parse_feed(fetch(BLOG + "/feed.xml"))
    times = BlogIndex()
    times.feed(fetch(BLOG).decode("utf-8"))
    for post in posts:
        if post.url not in times.minutes:
            raise ValueError(f"Missing published reading time for {post.url}; keeping the current cards")
        if times.categories.get(post.url) not in CATEGORIES:
            raise ValueError(f"Missing published category for {post.url}; keeping the current cards")
    return [replace(post, category=times.categories[post.url], reading_minutes=times.minutes[post.url]) for post in posts]


def title_width(text):
    try:
        return sum(WIDTHS[char] for char in text) * 20 - .32 * max(0, len(text) - 1)
    except KeyError as error:
        raise ValueError(f"The title font needs a glyph for {error.args[0]!r}") from error


def title_lines(title):
    lines = []
    line = ""
    for word in title.split():
        if line and title_width(line + " " + word) > 324:
            lines.append(line)
            line = ""
        while title_width(word) > 324:
            end = 1
            while end < len(word) and title_width(word[:end + 1]) <= 324:
                end += 1
            lines.append(word[:end])
            word = word[end:]
        line = (line + " " + word).strip()
    if line:
        lines.append(line)
    return lines


@lru_cache
def fonts():
    rules = []
    for filename, family, weight in [
        ("zilla-slab-600-latin.woff2", "Zilla", 600),
        ("cutive-mono-400-latin.woff2", "Cutive", 400),
        ("courier-prime-400-latin.woff2", "Courier", 400),
    ]:
        encoded = base64.b64encode((ROOT / ASSETS / "fonts" / filename).read_bytes()).decode("ascii")
        rules.append(f"@font-face{{font-family:{family};font-weight:{weight};src:url(data:font/woff2;base64,{encoded}) format('woff2')}}")
    return "".join(rules)


def render_card(post, index, height):
    sheet_height = height - 20
    points = " ".join(f"{10 + x * 3.8:.2f},{8 + y * sheet_height / 100:.2f}" for x, y in SHAPES[index % 2])
    tilt = "-.3" if index % 2 == 0 else ".25"
    title = "".join(f'<tspan x="38" y="{80 + 29 * i}">{escape(line)}</tspan>' for i, line in enumerate(title_lines(post.title)))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{height}" viewBox="0 0 400 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(post.title)}</title>
<desc id="desc">{escape(post.category)}. {escape(post.meta)}.</desc>
<style>{fonts()}
.title{{font:600 20px Zilla,Georgia,serif;letter-spacing:-.32px;fill:#26211C}}
.label{{font:13.5px Cutive,monospace;letter-spacing:2.43px;fill:#79513C}}
.meta{{font:13.5px Courier,monospace;letter-spacing:1.08px;fill:#4A3F35}}
</style>
<defs>
<clipPath id="sheet"><polygon points="{points}"/></clipPath>
<pattern id="rules" width="400" height="30" patternUnits="userSpaceOnUse"><path d="M0 29.5H400" stroke="#4A3E3D" stroke-opacity=".062"/></pattern>
<pattern id="grain" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="1" fill="#4A3E3D" fill-opacity=".028"/></pattern>
<filter id="shadow" x="-10%" y="-15%" width="120%" height="140%"><feDropShadow dx="0" dy="3" stdDeviation="0" flood-color="#37291D" flood-opacity=".05"/><feDropShadow dx="0" dy="5" stdDeviation="3" flood-color="#37291D" flood-opacity=".08"/></filter>
</defs>
<g transform="rotate({tilt} 200 {height / 2:g})">
<polygon points="{points}" fill="#FBF4E6" filter="url(#shadow)"/>
<g clip-path="url(#sheet)"><path d="M10 8h380v{sheet_height}H10Z" fill="url(#rules)"/><path d="M10 8h380v{sheet_height}H10Z" fill="url(#grain)"/></g>
<text class="label" x="38" y="42">{escape(post.category)}</text>
<path d="M348 37h14m-5-5 5 5-5 5" fill="none" stroke="#A84A28" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
<text class="title">{title}</text>
<text class="meta" x="38" y="{height - 33}">{escape(post.meta.upper())}</text>
</g></svg>
'''


def render_readme(readme, posts):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must contain exactly one pair of blog markers")
    before, remainder = readme.split(START)
    _, after = remainder.split(END)
    lines = []
    for start in range(0, len(posts), 2):
        lines.append("<p>")
        for index in range(start, min(start + 2, len(posts))):
            post = posts[index]
            alt = escape(f"{post.title}. {post.meta}.", quote=True)
            lines.append(f'<a href="{escape(post.url, quote=True)}"><img src="{ASSETS}/post-{index + 1}.svg" alt="{alt}" width="400"></a>')
        lines.append("</p>")
    return before + START + "\n" + "\n".join(lines) + "\n" + END + after


def outputs(root, posts):
    if not 1 <= len(posts) <= 5 or len({post.url for post in posts}) != len(posts):
        raise ValueError("Expected one to five distinct articles")
    result = {}
    for start in range(0, len(posts), 2):
        row = posts[start:start + 2]
        height = 216 + 29 * max(0, max(len(title_lines(post.title)) for post in row) - 3)
        for index, post in enumerate(row, start):
            article_url(post.url)
            if not post.title.strip() or post.category not in CATEGORIES or post.reading_minutes <= 0:
                raise ValueError("Incomplete article metadata")
            result[ASSETS / f"post-{index + 1}.svg"] = render_card(post, index, height)
    result[Path("README.md")] = render_readme((root / "README.md").read_text(), posts)
    result[DATA] = json.dumps([asdict(post) for post in posts], ensure_ascii=False, indent=2) + "\n"
    return result


def refresh(root, posts, check=False):
    expected = outputs(root, posts)
    changed = [path for path, content in expected.items() if not (root / path).exists() or (root / path).read_text() != content]
    obsolete = [path.relative_to(root) for path in (root / ASSETS).glob("post-*.svg") if path.relative_to(root) not in expected]
    if check:
        if changed or obsolete:
            raise ValueError("Stale generated files: " + ", ".join(map(str, changed + obsolete)))
        return []
    for path in changed:
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_suffix(target.suffix + ".tmp")
        temporary.write_text(expected[path])
        temporary.replace(target)
    for path in obsolete:
        (root / path).unlink()
    return changed + obsolete


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check the committed snapshot without network access")
    args = parser.parse_args()
    posts = [Post(**post) for post in json.loads((ROOT / DATA).read_text())] if args.check else live_posts()
    changed = refresh(ROOT, posts, check=args.check)
    print(f"Verified {len(posts)} article cards" if args.check else f"Updated {len(changed)} files for {len(posts)} articles")


if __name__ == "__main__":
    main()
