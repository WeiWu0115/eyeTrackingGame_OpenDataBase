'use strict';
const isEnglish=document.documentElement.lang==='en';
const search=document.querySelector('#training-search');
const domain=document.querySelector('#training-domain');
const cards=[...document.querySelectorAll('.training-card')];
function filterTraining(){const query=search.value.trim().toLocaleLowerCase();let count=0;for(const card of cards){const show=(!domain.value||card.dataset.domain===domain.value)&&(!query||card.textContent.toLocaleLowerCase().includes(query));card.hidden=!show;if(show)count++;}document.querySelector('#training-count').textContent=isEnglish?`${count} ${count===1?'record':'records'}`:`${count} 条记录`;}
search.addEventListener('input',filterTraining);domain.addEventListener('change',filterTraining);
document.querySelectorAll('.training-card img').forEach(img=>img.addEventListener('error',()=>{img.parentElement.classList.add('image-placeholder');img.parentElement.dataset.placeholder=isEnglish?'Image placeholder':'配图占位';img.src=(isEnglish?'../assets/image-placeholder.svg':'assets/image-placeholder.svg')+'?v=20261016-gray';img.alt=isEnglish?'Image placeholder':'配图占位';},{once:true}));
