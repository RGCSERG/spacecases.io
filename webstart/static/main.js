let text = document.getElementById('front-text');
let buttons = document.querySelector('.front-buttons')
let case2 = document.getElementById('case2');
let case1 = document.getElementById('case');
let header = document.querySelector('.header')
const menu = document.querySelector(".burger-menu");
const pfp = document.querySelector(".profile-pic");
window.addEventListener('scroll', () => {
    let value = window.scrollY;

    text.style.marginTop = value * 2 + 'px';
    //case1.style.left = value * -1.5 + 'px';
    //case2.style.left = value * 1.5 + 'px';
    //case2.style.opacity = 1 - (value*0.001)*2;
    //case1.style.opacity = 1 - (value*0.01)*2;
    text.style.opacity = 1 - (value * 0.001) * 3;
    buttons.style.opacity = 1 - (value * 0.001) * 4;
    menu.style.top = -(value) + '%'

    if (value > 0) {
        menu.classList.add("no-transition")
    } else { 
        menu.classList.remove("no-transition")
    }
    if (value > 844) {
        header.style.top = "-100px";
        menu.classList.remove("active");
    } else { 
        header.style.top = "0"
    }
})
pfp.addEventListener("click", () => {
    menu.classList.remove('no-transition')
    menu.classList.toggle("active");
    pfp.classList.toggle("active");
})

function goBack() {
    window.history.back();
  }
  
function setUpEvents() { 
    let content = document.querySelector(".dropdown");
    let button = document.getElementById("button");

    button.addEventListener("click", function() { 
        content.classList.toggle("active");
    })
}

window.onload = function(){ 
    setUpEvents();
}