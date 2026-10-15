from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'dist';OUT.mkdir(exist_ok=True)
for p in ROOT.iterdir():
 if p.name in ['assets','zh','research','members','media','publications','gallery','join','contact','team','recruitment','news']:
  shutil.copytree(p,OUT/p.name,dirs_exist_ok=True)
 elif p.name in ['index.html','404.html','CNAME','robots.txt','sitemap.xml','.nojekyll']:
  shutil.copy2(p,OUT/p.name)
print('Packaged static site into dist/')
