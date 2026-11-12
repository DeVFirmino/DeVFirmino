# README article cards

`update_blog_posts.py` uses Python's standard library. It reads the English RSS
feed for the latest five titles, links and publication dates, then uses the
blog index's displayed categories and reading times. A failed fetch, empty feed or
missing metadata stops the update before any files are written.

```sh
python3 tools/update_blog_posts.py
python3 -m unittest discover -s tests -v
python3 tools/update_blog_posts.py --check
```

The daily GitHub Actions job runs the same updater. Pull requests run the tests
and an offline consistency check against `data/latest-posts.json`. The updater
only replaces content between the `BLOG-POST-LIST` markers and its numbered
article SVGs. The project cards and the rest of the profile remain independent.

Article cards use embedded Zilla Slab, Cutive Mono and Courier Prime fonts.
`assets/readme-blog/fonts/title-widths.json` contains advance widths in em units
from the bundled Zilla Slab font. Longer titles grow both cards in their row;
an unsupported glyph fails the refresh so the font can be updated deliberately.
The bundled fonts and those embedded in the static project cards retain their
SIL Open Font License notices in the same directory.

The static project cards use the site's paper, olive backsheet and hatched tags.
Each has a separate phone layout selected by a README `picture` element.
Their repository links wrap the images; related article links remain in the
expandable list below them because links inside SVG images are not interactive.
