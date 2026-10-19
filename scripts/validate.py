from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
ROOT=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=[];self.tags=[];self.text=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if 'id' in a:self.ids.append(a['id'])
  for k in ['href','src']:
   if k in a:self.links.append(a[k])
 def handle_data(self,data):self.text.append(data)
errors=[];pages={p:Page(p.read_text(encoding='utf-8-sig')) for p in ROOT.rglob('*.html') if 'dist' not in p.relative_to(ROOT).parts}
for path,page in pages.items():
 if len(page.ids)!=len(set(page.ids)):errors.append(f'Duplicate ID: {path}')
 for url in page.links:
  part=urlsplit(url)
  if part.scheme or part.netloc:continue
  target=(path.parent/unquote(part.path)).resolve() if part.path else path
  if target.is_dir():target/='index.html'
  if not target.exists():errors.append(f'Broken link: {path.relative_to(ROOT)} -> {url}')
  if part.fragment and target in pages and unquote(part.fragment) not in pages[target].ids:errors.append(f'Broken anchor: {path.relative_to(ROOT)} -> {url}')
 if 'http-equiv="refresh"' in path.read_text(encoding='utf-8-sig'):continue
 h1=[a for tag,a in page.tags if tag=='h1']
 if len(h1)!=1:errors.append(f'Expected one h1: {path}')
 htmlattrs=next(a for tag,a in page.tags if tag=='html')
 lang='zh' if path.relative_to(ROOT).parts[0]=='zh' else 'en'
 if htmlattrs['lang']!=('zh-CN' if lang=='zh' else 'en'):errors.append(f'Language mismatch: {path}')
 switches=[a for tag,a in page.tags if tag=='a' and 'data-language' in a]
 if len(switches)!=2:errors.append(f'Language switch missing: {path}')
 for a in switches:
  dest=(path.parent/a['href']).resolve();expected=ROOT/('zh' if a['data-language']=='zh' else '')/path.relative_to(ROOT/'zh' if lang=='zh' else ROOT)
  if dest!=expected:errors.append(f'Wrong language target: {path}')
 for tag,a in page.tags:
  if tag=='img' and not all(k in a for k in ['alt','width','height','loading']):errors.append(f'Image attributes missing: {path}')
 visible=' '.join(page.text)
 for foreign in ['Simons Center','Mriganka','SUR LAB','surlab.org','smartsmartsmart']:
  if foreign.lower() in visible.lower():errors.append(f'Unexpected reference content: {path}')
 if lang=='en' and re.search(r'[\u4e00-\u9fff]',visible.replace('中文','')):errors.append(f'Chinese leaked into English page: {path}')
for css in (ROOT/'assets').glob('*.css'):
 text=css.read_text(encoding='utf-8-sig')
 for source in re.findall(r'url\([\'\"]?([^\)\'\"]+)',text):
  if not source.startswith(('data:','http')) and not (css.parent/source).exists():errors.append(f'CSS missing asset: {source}')
people=json.loads((ROOT/'data/people.json').read_text(encoding='utf-8'))
research=json.loads((ROOT/'data/content.json').read_text(encoding='utf-8'))['research']['areas']
for lang in ['en','zh']:
 base=ROOT/('zh' if lang=='zh' else '')/'research'
 for area in research:
  path=base/area['id']/'index.html'
  assert path in pages, f'Missing research detail: {path}'
  parsed=pages[path]
  if area.get('video'):
   video=next(a for tag,a in parsed.tags if tag=='video')
   assert all(k in video for k in ['autoplay','muted','loop','playsinline','poster'])
   assert (path.parent/video['poster']).exists()
   assert 'controls' not in video
   assert [tag for tag,a in parsed.tags].index('video')>[tag for tag,a in parsed.tags].index('h1')
   markup=path.read_text(encoding='utf-8')
   assert markup.index(area['paragraphs'][lang][1])<markup.index('<video')<markup.index(area['paragraphs'][lang][2])
   assert all(p in parsed.text for p in area['paragraphs'][lang])
  if area.get('image'):
   assert any(tag=='img' and (path.parent/a['src']).resolve()==ROOT/area['image'] for tag,a in parsed.tags)
assert len(people)==19
assert next(i for i,p in enumerate(people) if p['group']=='Associate Researcher')<next(i for i,p in enumerate(people) if p['group']=='Assistant Researcher')
assert len([p for p in people if p['photo']])==18
assert next(p for p in people if p['id']=='liming-qin')['photo']
assert next(p for p in people if p['id']=='sifei-qin')['email']==''
assert (ROOT/'CNAME').read_text().strip()=='luweilab.com'
assert len(json.loads((ROOT/'data/publications.json').read_text(encoding='utf-8')))==10
for p in (ROOT/'assets/images').rglob('*'):
 if p.is_file() and p.stat().st_size>300_000:errors.append(f'Oversized image: {p.name}')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML files; local links and fragments; both language targets on every page; image references and attributes; domain; 19 members in requested order; 18 photos; 10 publications; image size budget.')
