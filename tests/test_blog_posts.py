from dataclasses import replace
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

from tools import update_blog_posts as blog


class BlogPostsTests(unittest.TestCase):
    def post(self, title="A practical example", slug="example", minutes=6):
        return blog.Post(title, blog.BLOG + "/" + slug, "AI", "2026-10-10T09:00:00+00:00", minutes)

    def test_feed_selects_five_newest_unique_articles(self):
        items = [f"<item><title>Article {day}</title><link>{blog.BLOG}/post-{day}</link>"
                 f"<category>System Design</category><pubDate>Sat, {day:02d} Oct 2026 09:00:00 GMT</pubDate></item>"
                 for day in range(1, 8)]
        posts = blog.parse_feed("<rss><channel>" + "".join(items + [items[-1]]) + "</channel></rss>")
        self.assertEqual(["Article 7", "Article 6", "Article 5", "Article 4", "Article 3"], [post.title for post in posts])
        self.assertTrue(all(post.category == "SYSTEM DESIGN" for post in posts))

    def test_invalid_feed_cannot_erase_existing_articles(self):
        with self.assertRaisesRegex(ValueError, "no articles"):
            blog.parse_feed("<rss><channel/></rss>")
        with self.assertRaises(ET.ParseError):
            blog.parse_feed("<html>Service unavailable")

    def test_article_links_cannot_leave_the_english_blog(self):
        for url in ["javascript:alert(1)", "https://example.com/en/blog/post", blog.BLOG + "/post?redirect=1"]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                blog.article_url(url)

    def test_reading_time_comes_from_the_matching_published_article(self):
        parser = blog.BlogIndex()
        parser.feed('<a class="blog-note__link" href="/en/blog/first">First</a>'
                    '<span class="blog-note__meta">3 Oct 2026 · <b>16</b> MIN</span>'
                    '<a class="blog-note__link" href="/en/blog/second">Second</a>'
                    '<span class="blog-note__meta">2 Oct 2026 · 7 MIN</span>')
        self.assertEqual({blog.BLOG + "/first": 16, blog.BLOG + "/second": 7}, parser.minutes)

    def test_live_category_uses_the_site_instead_of_legacy_rss_tags(self):
        feed = (f'<rss><channel><item><title>Pods</title><link>{blog.BLOG}/pods</link>'
                '<category>Kubernetes</category><pubDate>Sat, 10 Oct 2026 09:00:00 GMT</pubDate></item></channel></rss>').encode()
        page = (b'<a class="blog-note__stamp"><span class="pp-tag">CLOUD</span></a>'
                b'<a class="blog-note__link" href="/en/blog/pods">Pods</a>'
                b'<span class="blog-note__meta">10 Oct 2026 - 3 MIN</span>')
        with patch.object(blog, "fetch", side_effect=[feed, page]):
            posts = blog.live_posts()
        self.assertEqual("CLOUD", posts[0].category)
        self.assertEqual(3, posts[0].reading_minutes)

    def test_missing_live_metadata_fails_before_any_files_are_written(self):
        feed = (f'<rss><channel><item><title>Post</title><link>{blog.BLOG}/missing</link>'
                '<category>AI</category><pubDate>Sat, 10 Oct 2026 09:00:00 GMT</pubDate></item></channel></rss>').encode()
        with patch.object(blog, "fetch", side_effect=[feed, b"<html>No articles</html>"]):
            with self.assertRaisesRegex(ValueError, "Missing published reading time"):
                blog.live_posts()

    def test_refresh_preserves_other_sections_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = "# Profile\n" + blog.START + "\nOld list\n" + blog.END + "\n## Code\nKeep my projects.\n"
            (root / "README.md").write_text(readme)
            self.assertTrue(blog.refresh(root, [self.post()]))
            updated = (root / "README.md").read_text()
            self.assertTrue(updated.startswith("# Profile\n" + blog.START))
            self.assertTrue(updated.endswith(blog.END + "\n## Code\nKeep my projects.\n"))
            self.assertEqual(1, updated.count('<a href="'))
            self.assertEqual([], blog.refresh(root, [self.post()]))
            self.assertEqual([], blog.refresh(root, [self.post()], check=True))

    def test_long_titles_grow_both_cards_in_the_row_without_truncating(self):
        long = self.post("How a distributed database handles repeated requests " * 4)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(blog.START + "\n" + blog.END)
            result = blog.outputs(root, [long, self.post(slug="short")])
            first = ET.fromstring(result[blog.ASSETS / "post-1.svg"])
            second = ET.fromstring(result[blog.ASSETS / "post-2.svg"])
            self.assertGreater(int(first.attrib["height"]), 216)
            self.assertEqual(first.attrib["height"], second.attrib["height"])
            spans = first.findall('.//{http://www.w3.org/2000/svg}tspan')
            self.assertEqual(long.title.strip(), " ".join(span.text for span in spans))
            self.assertLess(float(spans[-1].attrib["y"]), int(first.attrib["height"]) - 33)

    def test_very_long_words_stay_inside_the_card(self):
        lines = blog.title_lines("A " + "Database" * 30)
        self.assertTrue(all(blog.title_width(line) <= 324 for line in lines))
        self.assertEqual("A" + "Database" * 30, "".join(lines).replace(" ", ""))

    def test_titles_are_escaped_in_svg_and_readme(self):
        post = self.post('Queues & retries: "send" < "ack"')
        svg = ET.fromstring(blog.render_card(post, 0, 216))
        self.assertEqual(post.title, svg.find("{http://www.w3.org/2000/svg}title").text)
        readme = blog.render_readme(blog.START + "\n" + blog.END, [post])
        self.assertIn('&amp;', readme)
        self.assertIn('&quot;send&quot;', readme)
        self.assertNotIn('< "ack"', readme)

    def test_invalid_snapshot_and_missing_markers_leave_files_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("A README with no markers")
            with self.assertRaises(ValueError):
                blog.refresh(root, [self.post()])
            self.assertEqual(["README.md"], [path.name for path in root.iterdir()])
            with self.assertRaises(ValueError):
                blog.refresh(root, [replace(self.post(), reading_minutes=0)])
            self.assertEqual("A README with no markers", (root / "README.md").read_text())

    def test_check_detects_drift_without_overwriting_it(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(blog.START + "\n" + blog.END)
            blog.refresh(root, [self.post()])
            card = root / blog.ASSETS / "post-1.svg"
            card.write_text("Changed manually")
            with self.assertRaisesRegex(ValueError, "Stale generated files"):
                blog.refresh(root, [self.post()], check=True)
            self.assertEqual("Changed manually", card.read_text())

    def test_smaller_feed_removes_only_obsolete_article_cards(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(blog.START + "\n" + blog.END)
            blog.refresh(root, [self.post(), self.post(slug="second")])
            code = root / blog.ASSETS / "code-1.svg"
            code.write_text("Keep the project card")
            blog.refresh(root, [self.post()])
            self.assertFalse((root / blog.ASSETS / "post-2.svg").exists())
            self.assertEqual("Keep the project card", code.read_text())


if __name__ == "__main__":
    unittest.main()
