from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


SITE = Path(__file__).resolve().parents[1] / "_site"
ROUTES = (
    "web-starter/",
    "portfolio-ppt/",
    "Unity_Portfolio/web-starter/",
    "Unity_Portfolio/portfolio-ppt/",
)


class References(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.links.extend(attrs[key] for key in ("href", "src", "poster") if attrs.get(key))
        if attrs.get("id"):
            self.ids.add(attrs["id"])


class PublishedSiteTests(unittest.TestCase):
    def test_main_links_use_published_routes(self):
        links = References((SITE / "index.html").read_text()).links
        self.assertEqual([f"./{route}" for route in ROUTES], links)

    def test_existing_routes_serve_content_without_redirects(self):
        for route in ROUTES:
            with self.subTest(route=route):
                text = (SITE / route / "index.html").read_text()
                self.assertIn("<main", text)
                self.assertNotIn('http-equiv="refresh"', text)
                self.assertNotIn("location.replace", text)
                if "portfolio-ppt" in route:
                    self.assertEqual(23, len(re.findall(r'id="slide-\d+"', text)))

    def test_local_assets_and_anchors_exist(self):
        documents = {p.resolve(): References(p.read_text()) for p in SITE.rglob("*.html")}
        for path in SITE.rglob("*"):
            if path.suffix == ".html":
                links = documents[path.resolve()].links
            elif path.suffix == ".css":
                links = [value for _, value in re.findall(r'url\(\s*([\'"]?)(.*?)\1\s*\)', path.read_text(), re.S)]
            elif path.suffix == ".svg":
                links = re.findall(r'(?:xlink:)?href=[\'"]([^\'"]+)', path.read_text())
            else:
                continue
            for link in links:
                url = urlsplit(link)
                if url.scheme or url.netloc:
                    continue
                target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
                if target.is_dir():
                    target /= "index.html"
                with self.subTest(source=path.relative_to(SITE), link=link):
                    self.assertTrue(target.is_relative_to(SITE), "배포 폴더 밖의 경로")
                    self.assertTrue(target.is_file(), "누락된 로컬 파일")
                    if url.fragment and target in documents:
                        self.assertIn(unquote(url.fragment), documents[target].ids)

    def test_only_public_files_are_shipped(self):
        self.assertEqual({"index.html", "web-starter", "portfolio-ppt", "Unity_Portfolio"}, {p.name for p in SITE.iterdir()})
        self.assertEqual(2, len(list(SITE.rglob("*.pdf"))))
        for path in SITE.rglob("*"):
            self.assertNotIn(path.name, {"docs", "src", "scripts", "package.json", "slide-renders", ".DS_Store"})


if __name__ == "__main__":
    unittest.main()
