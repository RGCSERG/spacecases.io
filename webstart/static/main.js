let text = document.getElementById('front-text');
let buttons = document.querySelector('.front-buttons')
let case2 = document.getElementById('case2');
let case1 = document.getElementById('case');
let header = document.querySelector('.header')

window.addEventListener('scroll', () => {
    let value = window.scrollY;

    text.style.marginTop = value * 2 + 'px';
    //case1.style.left = value * -1.5 + 'px';
    //case2.style.left = value * 1.5 + 'px';
    //case2.style.opacity = 1 - (value*0.001)*2;
    //case1.style.opacity = 1 - (value*0.01)*2;
    text.style.opacity = 1 - (value * 0.001) * 2;
    buttons.style.opacity = 1 - (value * 0.001) * 3;

    if (value > 400) {
        header.style.top = "-100px";
    } else { 
        header.style.top = "0"
    }
})

const menu = document.querySelector(".burger-menu");
const pfp = document.querySelector(".profile-pic");

pfp.addEventListener("click", () => { 
    
    menu.classList.toggle("active");
    pfp.classList.toggle("active");
})
