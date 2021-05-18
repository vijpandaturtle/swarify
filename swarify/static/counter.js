var counterDisplayElem = document.querySelector('.counter-display');
var counterMinusElem = document.querySelector('.counter-minus');
var counterPlusElem = document.querySelector('.counter-plus');

var count = 0;

updateDisplay();

counterPlusElem.addEventListener("click",()=>{
    count++;
    updateDisplay();
}) ;

counterMinusElem.addEventListener("click",()=>{
    count--;
    updateDisplay();
});

function updateDisplay(){
    counterDisplayElem.innerHTML = count;
};

