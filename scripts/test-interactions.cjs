'use strict';
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
class Element{
 constructor(){this.hidden=false;this.value='';this.attrs={};this.dataset={};this.events={};this.classes=new Set();this.classList={add:n=>this.classes.add(n),remove:n=>this.classes.delete(n),toggle:(n,v)=>v?this.classes.add(n):this.classes.delete(n)};}
 setAttribute(k,v){this.attrs[k]=v;}getAttribute(k){return this.attrs[k];}addEventListener(k,fn){this.events[k]=fn;}focus(){this.focused=true;}closest(){return this.parent;}querySelectorAll(){return this.children||[];}
 fire(k,e={}){this.events[k]?.(e);}
}
for(const lang of ['en','zh']){
 const html=fs.readFileSync(path.join(root,lang==='zh'?'zh':'','publications/index.html'),'utf8');
 const items=[...html.matchAll(/<article class="publication" data-year="([^"]+)" data-search="([^"]+)"/g)].map(m=>{const e=new Element();e.dataset={year:m[1],search:m[2]};return e;});
 assert.equal(items.length,10);
 const years=[...new Set(items.map(p=>p.dataset.year))];
 const sections=years.map(y=>{const e=new Element();e.id='year-'+y;e.children=items.filter(p=>p.dataset.year===y);return e;});
 const yearLinks=sections.map(s=>{const e=new Element();e.attrs.href='#'+s.id;return e;});
 const query=new Element(),year=new Element(),result=new Element(),empty=new Element(),form=new Element(),menu=new Element(),nav=new Element();query.form=form;menu.dataset={open:'Menu',close:'Close menu'};menu.attrs['aria-expanded']='false';
 const sub=[new Element(),new Element()];sub.forEach(e=>{e.attrs['aria-expanded']='false';e.parent=new Element();});
 const language=new Element();const document=new Element();
 const single={'#paper-query':query,'#paper-year':year,'#result-number':result,'#no-results':empty,'.menu-toggle':menu,'#main-nav':nav};sections.forEach(s=>single['#'+s.id]=s);
 document.querySelector=s=>single[s];document.querySelectorAll=s=>({'.sub-toggle':sub,'.publication':items,'.publication-year':sections,'.year-nav a':yearLinks,'[data-language][href]':[language]})[s]||[];
 const breakpoint=new Element();
 vm.runInNewContext(fs.readFileSync(path.join(root,'assets/site.js'),'utf8'),{document,matchMedia:()=>breakpoint,location:{hash:'#year-2024'}});
 query.value='alcohol';query.fire('input');assert.equal(result.textContent,1);
 query.value='睡眠';query.fire('input');assert.equal(result.textContent,2);
 query.value='';year.value='2024';year.fire('change');assert.equal(result.textContent,2);assert.equal(sections.filter(s=>!s.hidden).length,1);
 query.value='not-a-real-paper';query.fire('input');assert.equal(result.textContent,0);assert.equal(empty.hidden,false);assert.equal(yearLinks.filter(e=>!e.hidden).length,0);
 form.fire('reset');assert.equal(result.textContent,10);assert.equal(empty.hidden,true);assert.equal(yearLinks.filter(e=>!e.hidden).length,years.length);
 menu.fire('click');assert.equal(menu.attrs['aria-expanded'],'true');assert.ok(nav.classes.has('open'));document.fire('keydown',{key:'Escape'});assert.equal(menu.attrs['aria-expanded'],'false');assert.ok(menu.focused);
 sub[0].fire('click');assert.equal(sub[0].attrs['aria-expanded'],'true');sub[1].fire('click');assert.equal(sub[0].attrs['aria-expanded'],'false');assert.equal(sub[1].attrs['aria-expanded'],'true');document.fire('keydown',{key:'Escape'});assert.equal(sub[1].attrs['aria-expanded'],'false');assert.ok(sub[1].focused);
 language.fire('click');assert.equal(language.hash,'#year-2024');
 console.log('PASS '+lang+': multilingual search, year filter, zero-results state, reset, visible year anchors, mobile menu, submenu exclusivity, Escape focus, language anchor preservation.');
}
