'use strict';
const isEnglish=document.documentElement.lang==='en';
const search=document.querySelector('#training-search');
const domain=document.querySelector('#training-domain');
const cards=[...document.querySelectorAll('.training-card')];
function filterTraining(){const query=search.value.trim().toLocaleLowerCase();let count=0;for(const card of cards){const show=(!domain.value||card.dataset.domain===domain.value)&&(!query||card.textContent.toLocaleLowerCase().includes(query));card.hidden=!show;if(show)count++;}document.querySelector('#training-count').textContent=isEnglish?`${count} ${count===1?'record':'records'}`:`${count} 条记录`;}
search.addEventListener('input',filterTraining);domain.addEventListener('change',filterTraining);
document.querySelectorAll('.training-card img').forEach(img=>img.addEventListener('error',()=>{img.hidden=true;const link=document.createElement('p');link.className='image-error';link.textContent=isEnglish?'Image and credits: official project source':'图片与署名见官方项目来源';img.parentElement.append(link);},{once:true}));
