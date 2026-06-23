
(function(){
const lang=localStorage.getItem('language')||navigator.language.slice(0,2)||'en';
window.setLanguage=function(l){localStorage.setItem('language',l);location.reload();}
console.log('Multilingual support enabled:',lang);
})();
