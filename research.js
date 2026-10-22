(() => {
  'use strict';
  const en=document.documentElement.lang==='en';
  const cards=[...document.querySelectorAll('.paper')];
  const search=document.querySelector('#paper-search');
  const filters=['topic','type','year'].map(k=>[k,document.querySelector('#paper-'+k)]);
  const params=new URLSearchParams(location.search);
  search.value=params.get('q')||'';
  filters.forEach(([k,s])=>{if([...s.options].some(o=>o.value===params.get(k)))s.value=params.get(k);});
  function render(update=true){
    const q=search.value.trim().toLocaleLowerCase();let count=0;
    for(const card of cards){card.hidden=!(card.textContent.toLocaleLowerCase().includes(q)&&filters.every(([k,s])=>!s.value||card.dataset[k]===s.value));if(!card.hidden)count++;}
    document.querySelector('#paper-count').textContent=en?`${count} of ${cards.length} publications`:`${count} / ${cards.length} 条文献`;
    document.querySelector('#paper-empty').hidden=count>0;
    if(update){const p=new URLSearchParams();if(q)p.set('q',search.value.trim());filters.forEach(([k,s])=>{if(s.value)p.set(k,s.value);});history.replaceState(null,'',location.pathname+(p.size?'?'+p:'')+location.hash);}
  }
  search.addEventListener('input',()=>render());filters.forEach(([,s])=>s.addEventListener('change',()=>render()));
  document.querySelector('#paper-reset').addEventListener('click',()=>{search.value='';filters.forEach(([,s])=>s.value='');render();});
  function revealAnchor(){const id=decodeURIComponent(location.hash.slice(1));const card=cards.find(c=>c.id===id);if(card&&card.hidden){search.value='';filters.forEach(([,s])=>s.value='');render();card.scrollIntoView();}}
  window.addEventListener('hashchange',revealAnchor);render(false);revealAnchor();
})();
