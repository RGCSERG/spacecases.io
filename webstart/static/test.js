let text = document.getElementById('text');
let case2 = document.getElementById('case2');
let case1 = document.getElementById('case');

window.addEventListener('scroll', () => {
    let value = window.scrollY;

    text.style.marginTop = value * 2.5 + 'px';
    case1.style.left = value * -1.5 + 'px';
    case2.style.left = value * 1.5 + 'px';
    //case2.style.opacity = 1 - (value*0.001)*2;
    //case1.style.opacity = 1 - (value*0.01)*2;
    text.style.opacity = 1 - (value * 0.001) * 2;
    console.log(value)
})

const menu = document.querySelector(".burger-menu");
const pfp = document.querySelector(".profile-pic");

pfp.addEventListener("click", () => { 
    menu.classList.toggle("active");
    pfp.classList.toggle("active");
})
