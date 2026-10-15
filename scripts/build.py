from pathlib import Path
import json,html,os
from urllib.parse import quote
ROOT=Path(__file__).resolve().parent.parent
D=json.loads((ROOT/'data/content.json').read_text(encoding='utf-8'))
PEOPLE=json.loads((ROOT/'data/people.json').read_text(encoding='utf-8'))
PAPERS=json.loads((ROOT/'data/publications.json').read_text(encoding='utf-8'))
ESC=lambda s:html.escape(str(s),quote=True)
LABELS={
'home':('首页','Home'),'research':('研究方向','Research'),'members':('团队成员','Members'),'media':('新闻动态','Media'),'publications':('发表论文','Publications'),'gallery':('实验室相册','Gallery'),'join':('加入我们','Join'),'contact':('联系我们','Contact'),'wei-lu':('陆伟','Wei Lu'),
'skip':('跳转到正文','Skip to content'),'menu':('菜单','Menu'),'close':('关闭菜单','Close menu'),'nav':('主导航','Main navigation'),'language':('切换语言','Switch language'),'photo':('的照片',' portrait'),'no-photo':('照片暂缺','Photo not provided'),'bio':('个人简介','Biography'),'profile':('查看个人简介','View biography'),'faculty':('深圳医学科学院个人主页','SMART faculty profile'),'areas':('研究项目','Research areas'),'career':('教育与工作经历','Education & appointments'),'awards':('奖项与荣誉','Awards & honors'),'papers':('代表性论文','Selected publications'),'year':('年份','Year'),'all':('全部年份','All years'),'search':('搜索论文','Search publications'),'placeholder':('输入关键词、作者或期刊','Keyword, author or journal'),'results':('篇论文','publications'),'empty':('没有找到匹配的论文。','No publications match your search.'),'clear':('清除筛选','Clear filters'),'email':('电子邮箱','Email'),'address':('地址','Address'),'phone':('电话','Phone'),'room':('办公室','Office'),'positions':('招聘职位','Open positions'),'inquiries':('欢迎通过电子邮箱联系我们。','Please contact us by email.'),'top':('返回顶部','Back to top'),'notfound':('页面未找到','Page not found'),'notfoundtext':('你访问的页面不存在或已移动。','The page you requested does not exist or has moved.'),'returnhome':('返回首页','Return home'),'subnav':('展开子菜单','Open submenu'),'years':('按年份浏览','Browse by year')}
NAV=['research','members','media','publications','gallery','join','contact']
LABELS.update({'environment':('研究环境','Research environment'),'methods':('研究方法','Research methods'),'application':('申请材料','Application materials'),'apply':('申请方式','How to apply'),'recruitment':('招聘咨询','Recruitment inquiries'),'academic':('学术联系','Academic inquiries'),'notes':('其他说明','Additional information')})
PAGES=['home']+NAV+['wei-lu','404']

def route(page,lang):
 prefix='zh/' if lang=='zh' else ''
 return prefix+({'home':'index.html','wei-lu':'members/wei-lu/index.html','404':'404.html'}.get(page,page+'/index.html'))

def make(page,lang):
 idx=0 if lang=='zh' else 1
 t=lambda k:LABELS[k][idx]
 v=lambda value:value[lang]
 dest=ROOT/route(page,lang)
 rel=lambda path:Path(os.path.relpath(ROOT/path,dest.parent)).as_posix()
 link=lambda p,l=lang:rel(route(p,l))
 asset=lambda p:rel(p)
 canonical='https://luweilab.com/'+route(page,lang).replace('index.html','')
 title=v(D['brand']) if page=='home' else t(page if page!='404' else 'notfound')+' | '+v(D['brand'])
 def img(person,eager=False):
  if not person['photo']:return f'<div class="portrait missing-photo" role="img" aria-label="{ESC(v(person["name"])+t("no-photo"))}"></div>'
  return f'<img class="portrait" src="{asset(person["photo"])}" alt="{ESC(v(person["name"])+t("photo"))}" width="240" height="300" loading="{"eager" if eager else "lazy"}" decoding="async">'
 def email(p):return f'<a class="email" href="mailto:{ESC(p["email"])}">{ESC(p["email"])}</a>' if p['email'] else '<div class="email empty-field"></div>'
 def person(p,pi=False):
  name=f'<a href="{link("wei-lu")}">{ESC(v(p["name"]))}</a>' if pi else ESC(v(p['name']))
  return f'<article class="person {"principal" if pi else ""}" id="{p["id"]}">{img(p,pi)}<h3>{name}</h3><p class="role">{ESC(v(D["pi"]["title"]) if pi else v(p["role"]))}</p>{email(p)}'+(f'<a class="profile-link" href="{link("wei-lu")}">{t("profile")} <span aria-hidden="true">→</span></a>' if pi else '')+'</article>'
 nav=''
 for n in NAV:
  active=' aria-current="page"' if n==page or (page=='wei-lu' and n=='members') else ''
  sub=''
  if n in ['research','members']:
   entries=[(link('research')+'#'+a['id'],v(a['title'])) for a in D['research']['areas']] if n=='research' else [(link('wei-lu'),t('wei-lu')),(link('members'),t('members'))]
   sub=f'<button class="sub-toggle" aria-expanded="false" aria-controls="sub-{n}" aria-label="{t("subnav")} · {t(n)}"><span aria-hidden="true">⌄</span></button><ul class="submenu" id="sub-{n}">' + ''.join(f'<li><a href="{u}">{ESC(s)}</a></li>' for u,s in entries)+'</ul>'
  nav+=f'<li class="nav-item"><a href="{link(n)}"{active}>{t(n)}</a>{sub}</li>'
 language=f'<div class="language-switch" role="group" aria-label="{t("language")}"><a href="{link(page,"zh")}" lang="zh-CN" hreflang="zh-CN" data-language="zh" {"aria-current=\"true\"" if lang=="zh" else ""}>中文</a><span aria-hidden="true">/</span><a href="{link(page,"en")}" lang="en" hreflang="en" data-language="en" {"aria-current=\"true\"" if lang=="en" else ""}>EN</a></div>'
 header=f'<header class="site-header"><div class="header-inner"><a class="brand" href="{link("home")}">{v(D["brand"])}</a><nav id="main-nav" aria-label="{t("nav")}"><ul class="nav-list">{nav}</ul></nav>{language}<button class="menu-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="{t("menu")}" data-open="{t("menu")}" data-close="{t("close")}"><span></span><span></span><span></span></button></div></header>'
 footer=f'<footer class="site-footer"><span>© 2026 {v(D["brand"])}</span><span>{v(D["institute"])}</span></footer>'
 body=''
 if page=='home':
  body=f'<main id="content" class="home-main"><div class="hero-copy"><h1>{v(D["home"]["title"])}</h1><p>{v(D["home"]["intro"])}</p><a class="outline-button" href="{link("research")}">{v(D["home"]["button"])}</a></div></main>'
 elif page=='research':
  paragraphs=''.join(f'<p>{ESC(v(p))}</p>' for p in D['research']['intro'])+f'<h2>{t("methods")}</h2><p>{ESC(v(D["research"]["methods"]))}</p>'
  aside=f'<aside class="research-aside"><h2>{t("areas")}</h2><ul>'+''.join(f'<li><a href="#{a["id"]}">{ESC(v(a["title"]))}</a></li>' for a in D['research']['areas'])+'</ul></aside>'
  sections=''.join(f'<section class="research-section" id="{a["id"]}"><span class="section-number" aria-hidden="true">0{i+1}</span><div><h2>{ESC(v(a["title"]))}</h2><p>{ESC(v(a["text"]))}</p></div></section>' for i,a in enumerate(D['research']['areas']))
  body=f'<main id="content" class="page research-page"><h1 class="page-title">{t(page)}</h1><div class="research-overview"><div class="prose">{paragraphs}</div>{aside}</div><div class="research-sections">{sections}</div></main>'
 elif page=='members':
  groups=[]
  for p in PEOPLE[1:]:
   if p['group'] not in groups:groups.append(p['group'])
  cards=person(PEOPLE[0],True)
  for group in groups:
   members=[p for p in PEOPLE if p['group']==group]
   heading=v(members[0]['role'])
   if lang=='en' and len(members)>1:heading+='s'
   cards+=f'<section class="member-group"><h2>{ESC(heading)}</h2><div class="people-grid">'+''.join(person(p) for p in members)+'</div></section>'
  body=f'<main id="content" class="page members-page"><h1 class="page-title">{t(page)}</h1>{cards}</main>'
 elif page=='wei-lu':
  p=PEOPLE[0]
  career=''.join(f'<li><span class="career-year">{ESC(row[0])}</span><div><strong>{ESC(v(row[1]))}</strong><span>{ESC(v(row[2]))}</span></div></li>' for row in D['pi']['career'])
  body=f'<main id="content" class="page"><h1 class="page-title">{t(page)}</h1><div class="bio-layout"><aside class="bio-photo">{img(p,True)}<p>{ESC(v(D["pi"]["title"]))}</p>{email(p)}<a class="profile-link" href="https://smart.org.cn/faculty/luwei">{t("faculty")} ↗</a></aside><div class="prose"><h2>{t("bio")}</h2>'+''.join(f'<p>{ESC(v(x))}</p>' for x in D['pi']['bio'])+f'<h2>{t("career")}</h2><ul class="career">{career}</ul><h2>{t("awards")}</h2><ul>'+''.join(f'<li>{ESC(v(x))}</li>' for x in D['pi']['awards'])+'</ul></div></div></main>'
 elif page=='publications':
  years=sorted(set(p['year'] for p in PAPERS),reverse=True)
  controls=f'<form class="publication-tools" role="search" onsubmit="return false"><div class="search-field"><label for="paper-query">{t("search")}</label><input id="paper-query" type="search" placeholder="{t("placeholder")}" autocomplete="off"></div><div><label for="paper-year">{t("year")}</label><select id="paper-year"><option value="">{t("all")}</option>'+''.join(f'<option value="{y}">{y}</option>' for y in years)+f'</select></div><button type="reset" class="reset-button">{t("clear")}</button></form><p class="result-count" aria-live="polite"><span id="result-number">{len(PAPERS)}</span> {t("results")}</p>'
  sections=''
  for y in years:
   papers=''
   for p in [x for x in PAPERS if x['year']==y]:
    search=ESC(' '.join([p['title']['en'],p['title']['zh'],p['authors'],p['journal'],str(y)]).lower())
    papers+=f'<article class="publication" data-year="{y}" data-search="{search}" id="{p["id"]}"><h3>{ESC(v(p["title"]))}</h3><p class="authors">{ESC(p["authors"])}</p><p class="citation"><em>{ESC(p["journal"])}</em> <span>{ESC(p["details"])}</span> <span>({y})</span></p></article>'
   sections+=f'<section class="publication-year" id="year-{y}"><h2>{y}</h2><div>{papers}</div></section>'
  yearlinks=f'<aside class="year-nav" aria-label="{t("years")}">'+''.join(f'<a href="#year-{y}">{y}</a>' for y in years)+'</aside>'
  body=f'<main id="content" class="page"><h1 class="page-title">{t(page)}</h1><p class="section-caption">{t("papers")}</p>{controls}<div class="publications-layout"><div>{sections}<p id="no-results" hidden>{t("empty")}</p></div>{yearlinks}</div></main>'
 elif page in ['media','gallery']:
  body=f'<main id="content" class="page blank-page"><h1 class="page-title">{t(page)}</h1><div class="reserved-content"></div></main>'
 elif page=='join':
  h=D['hiring']
  positions=''.join(f'<li>{ESC(v(p))}</li>' for p in h['positions'])
  materials=''.join(f'<li>{ESC(v(p))}</li>' for p in h['materials'])
  body=f'<main id="content" class="page"><h1 class="page-title">{t(page)}</h1><div class="join-layout"><div class="prose"><p class="join-intro">{ESC(v(h["intro"]))}</p><h2>{t("positions")}</h2><ul class="position-list">{positions}</ul><h2>{t("environment")}</h2><p>{ESC(v(h["culture"]))}</p><p>{ESC(v(h["methods"]))}</p><h2>{t("application")}</h2><ol class="application-list">{materials}</ol><h2>{t("apply")}</h2><p>{ESC(v(h["submit"]))}</p><h2>{t("notes")}</h2><p>{ESC(v(h["notes"]))}</p></div><aside class="join-contact"><h2>{t("recruitment")}</h2><a href="mailto:{D["contact"]["hiring_email"]}">{D["contact"]["hiring_email"]}</a><p class="join-address">{v(D["institute"])}<br>{v(D["contact"]["address"])}</p><a href="{link("wei-lu")}">{t("wei-lu")} · {t("profile")} →</a></aside></div></main>'
 elif page=='contact':
  body=f'<main id="content" class="page"><h1 class="page-title">{t(page)}</h1><div class="contact-layout"><div><h2>{t("wei-lu")}</h2><p class="contact-role">{v(D["pi"]["title"])}</p><dl><dt>{t("academic")}</dt><dd><a href="mailto:{D["contact"]["email"]}">{D["contact"]["email"]}</a></dd><dt>{t("recruitment")}</dt><dd><a href="mailto:{D["contact"]["hiring_email"]}">{D["contact"]["hiring_email"]}</a><br><a class="profile-link" href="{link("join")}">{t("apply")} →</a></dd><dt>{t("address")}</dt><dd>{v(D["institute"])}<br>{v(D["lab_name"])}<br>{v(D["contact"]["address"])}</dd><dt>{t("phone")}</dt><dd class="empty-field">{D["contact"]["phone"]}</dd><dt>{t("room")}</dt><dd class="empty-field">{D["contact"]["room"]}</dd></dl></div><img class="contact-campus" src="{asset('assets/images/contact/smart-campus-1400.webp')}" alt="{'深圳医学科学院园区效果图' if lang=='zh' else 'Architectural rendering of the SMART campus'}" width="1200" height="675" loading="eager" decoding="async"></div></main>'
 else:
  body=f'<main id="content" class="page blank-page"><h1 class="page-title">{t("notfound")}</h1><p>{t("notfoundtext")}</p><a class="text-button" href="{link("home")}">{t("returnhome")}</a></main>'
 desc=v(D['home']['intro'])
 alternate=''.join(f'<link rel="alternate" hreflang="{l}" href="https://luweilab.com/{route(page,"zh" if l=="zh-CN" else "en").replace("index.html","")}">' for l in ['en','zh-CN','x-default'])
 preload=f'<link rel="preload" as="image" href="{asset("assets/images/backgrounds/home-neurons.webp")}" media="(min-width: 761px)"><link rel="preload" as="image" href="{asset("assets/images/backgrounds/home-neurons-mobile.webp")}" media="(max-width: 760px)">' if page=='home' else ''
 doc=f'''<!doctype html>
<html lang="{'zh-CN' if lang=='zh' else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{ESC(title)}</title><meta name="description" content="{ESC(desc)}"><meta name="theme-color" content="#14251d"><link rel="canonical" href="{canonical}">{alternate}<meta property="og:title" content="{ESC(title)}"><meta property="og:description" content="{ESC(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:type" content="website"><meta property="og:image" content="https://luweilab.com/assets/images/backgrounds/home-neurons.webp"><link rel="icon" type="image/svg+xml" href="{asset('assets/favicon.svg')}">{preload}<link rel="stylesheet" href="{asset('assets/site.css')}"><script src="{asset('assets/site.js')}" defer></script></head>
<body class="{'home' if page=='home' else 'interior'}" data-language="{lang}"><a class="skip-link" href="#content">{t('skip')}</a>{header}{body}{footer}</body></html>'''
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(doc,encoding='utf-8')

for lang in ['en','zh']:
 for page in PAGES:make(page,lang)
# Maintain incoming links from the previous site without preserving its implementation.
for lang in ['en','zh']:
 for old,new in {'team':'members','recruitment':'join','news':'media'}.items():
  p=ROOT/('zh/' if lang=='zh' else '')/old/'index.html';p.parent.mkdir(parents=True,exist_ok=True)
  url=Path(os.path.relpath(ROOT/route(new,lang),p.parent)).as_posix()
  label=LABELS[new][0 if lang=='zh' else 1]
  p.write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={url}"><title>{label}</title><a href="{url}">{label}</a></html>',encoding='utf-8')
urls=['https://luweilab.com/'+route(p,l).replace('index.html','') for l in ['en','zh'] for p in PAGES if p!='404']
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>',encoding='utf-8')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://luweilab.com/sitemap.xml\n',encoding='utf-8')
(ROOT/'CNAME').write_text('luweilab.com\n',encoding='utf-8');(ROOT/'.nojekyll').touch()
print('Built',len(PAGES)*2,'bilingual pages and 6 legacy redirects.')
