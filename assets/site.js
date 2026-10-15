'use strict';
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');
function closeMenu(){nav?.classList.remove('open');menu?.setAttribute('aria-expanded','false');menu?.setAttribute('aria-label',menu.dataset.open);}
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?menu.dataset.close:menu.dataset.open);nav.classList.toggle('open',open);});
const subButtons=[...document.querySelectorAll('.sub-toggle')];
function closeSubmenus(){subButtons.forEach(b=>{b.setAttribute('aria-expanded','false');b.closest('.nav-item').classList.remove('open');});}
subButtons.forEach(button=>button.addEventListener('click',()=>{const opening=button.getAttribute('aria-expanded')!=='true';closeSubmenus();button.setAttribute('aria-expanded',String(opening));button.closest('.nav-item').classList.toggle('open',opening);}));
document.addEventListener('click',e=>{if(!e.target.closest('.site-header')){closeSubmenus();closeMenu();}});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){const activeSub=subButtons.find(b=>b.getAttribute('aria-expanded')==='true');if(activeSub){closeSubmenus();activeSub.focus();}else if(menu?.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus();}}});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
matchMedia('(min-width:1101px)').addEventListener('change',()=>{closeMenu();closeSubmenus();});
// Language links target the equivalent static page; anchor links are retained as well.
document.querySelectorAll('[data-language][href]').forEach(a=>{a.addEventListener('click',()=>{if(location.hash)a.hash=location.hash;});});
const query=document.querySelector('#paper-query');
const year=document.querySelector('#paper-year');
if(query&&year){
 const items=[...document.querySelectorAll('.publication')];
 const normalize=s=>s.normalize('NFKC').toLowerCase().trim();
 function filter(){const q=normalize(query.value);let count=0;items.forEach(item=>{const visible=(!year.value||item.dataset.year===year.value)&&(!q||normalize(item.dataset.search).includes(q));item.hidden=!visible;if(visible)count++;});document.querySelectorAll('.publication-year').forEach(section=>{section.hidden=![...section.querySelectorAll('.publication')].some(p=>!p.hidden);});document.querySelectorAll('.year-nav a').forEach(a=>{const section=document.querySelector(a.getAttribute('href'));a.hidden=section.hidden;});document.querySelector('#result-number').textContent=count;document.querySelector('#no-results').hidden=count>0;}
 query.addEventListener('input',filter);year.addEventListener('change',filter);
 query.form.addEventListener('reset',()=>{query.value='';year.value='';filter();});
}
