const menu = document.querySelector(".burger-menu");
const pfp = document.querySelector(".profile-pic");

pfp.addEventListener("click", () => { 
    menu.classList.toggle("active");
    pfp.classList.toggle("active");
})
