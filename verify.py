"""Static integrity checks; does not claim to verify rendered browser behavior."""
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.urls = []
        self.images = []
        self.projects = []
        self.blank_links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        for attr in ('href', 'src'):
            if attr in a: self.urls.append(a[attr])
        if tag == 'img': self.images.append(a)
        if 'data-category' in a: self.projects.append(a['data-category'])
        if tag == 'a' and a.get('target') == '_blank': self.blank_links.append(a)

page = Page()
page.feed((ROOT / 'dist/index.html').read_text(encoding='utf-8'))
assert not [i for i, n in Counter(page.ids).items() if n > 1], 'Duplicate IDs'
for url in page.urls:
    if url.startswith('#'): assert url[1:] in page.ids, f'Missing anchor {url}'
    elif not url.startswith(('https:', 'http:', 'mailto:')):
        assert (ROOT / 'dist' / url).is_file(), f'Missing file {url}'
assert all(i.get('alt') for i in page.images), 'Missing image description'
assert all('noopener' in a.get('rel', '') for a in page.blank_links), 'Unprotected new tab'
assert len(page.projects) == 5, 'Missing recovered project'
assert Counter(page.projects) == {'frontend': 2, 'fullstack': 3}, 'Unexpected filter categories'
manifest = json.loads((ROOT / '.openai/hosting.json').read_text(encoding='utf-8'))
assert manifest['static']['directory'] == 'dist'
recovery = json.loads((ROOT / 'recovery/projects.json').read_text(encoding='utf-8'))
assert len(recovery['projects']) == 5
for project in recovery['projects']:
    assert (ROOT / 'recovery' / project['image']).is_file()
    assert (ROOT / 'recovery' / project['optimizedImage']).is_file()

def luminance(hex_color):
    channels = [int(hex_color[i:i+2], 16) / 255 for i in (1,3,5)]
    rgb = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(rgb, (.2126, .7152, .0722)))

pairs = {
    'light content/surface': ('#172336', '#f7f8fb'),
    'light secondary/surface': ('#526075', '#f7f8fb'),
    'light primary button': ('#ffffff', '#2553d8'),
    'light secondary/tag': ('#526075', '#eef1f6'),
    'light secondary/project panel': ('#526075', '#e4eaf3'),
    'dark content/surface': ('#edf2fb', '#101721'),
    'dark secondary/panel': ('#a9b8ce', '#17212f'),
    'dark secondary/tag': ('#a9b8ce', '#253246'),
    'dark primary button': ('#10224a', '#9ebaff'),
    'contact secondary': ('#c4d1ef', '#172d62'),
}
ratios = {}
for name, (fg, bg) in pairs.items():
    a, b = sorted((luminance(fg), luminance(bg)))
    ratio = (b + .05) / (a + .05)
    assert ratio >= 4.5, f'Insufficient contrast: {name} = {ratio:.2f}'
    ratios[name] = round(ratio, 2)
print(json.dumps({'local_links':'pass', 'image_descriptions':'pass', 'project_count':len(page.projects), 'recovered_originals':'pass', 'contrast':ratios, 'browser_visual_qa':'not verified'}, indent=2))
