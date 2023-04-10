function goBack() {
    window.history.back();
  }
  
function setUpEvents() {
    let content = document.querySelector(".dropdown");
    let button = document.querySelector(".button-wrapper");
    let svg = document.querySelector(".svg");
    let titleScreen = document.querySelector(".title-screen");

    if (titleScreen !== null) {
        titleScreen.addEventListener("click", function () {
            content.classList.remove("active");
        })
    }
    if (button !== null) {
    button.addEventListener("click", function () {
        content.classList.toggle("active");
        svg.classList.toggle("active");
    })
    }
}

function cookieMenu() { 
    let cookieMenu = document.querySelector(".cookie-menu")
    let cookieReject = document.querySelector(".cookie-reject")
    let cookieAccept = document.querySelector(".cookie-accept")
    let cookieCustomise = document.querySelector(".cookie-customise")
    let cookieToggle = document.querySelector(".cookie-toggle")
    let cookieCustomWrapper = document.querySelector(".cookie-custom-wrapper")
    let cookieSave = document.querySelector(".cookie-save-button")

    if (cookieMenu != null) {
        cookieReject.addEventListener("click", function () { 
            cookieMenu.style.transitionProperty = "none";
            cookieCustomWrapper.style.transitionProperty = "none";
            cookieMenu.style.visibility = "hidden";
            cookieMenu.classList.remove("active");
            cookieCustomWrapper.classList.remove("active");
        })
        cookieAccept.addEventListener("click", function () {
            cookieMenu.style.transitionProperty = "none";
            cookieCustomWrapper.style.transitionProperty = "none";
            cookieMenu.style.visibility = "hidden";
            cookieMenu.classList.remove("active");
            cookieCustomWrapper.classList.remove("active");
        })
        cookieCustomise.addEventListener("click", function () { 
            if (cookieMenu.classList.contains("active")) {
                cookieMenu.style.transitionProperty = "none";
                cookieCustomWrapper.style.transitionProperty = "none";

            } else { 
                cookieMenu.style.transition = "0.3s ease-out";
                cookieCustomWrapper.style.transition = "0.3s ease-out";
            }
            cookieMenu.classList.toggle("active");
            cookieCustomWrapper.classList.toggle("active")
        })
        cookieToggle.addEventListener("click", function () { 
            cookieMenu.classList.add("active");
            cookieMenu.style.transition = "0.3s ease-out";
            cookieCustomWrapper.style.transition = "0.3s ease-out";
            cookieMenu.style.visibility = "visible";
            cookieCustomWrapper.classList.toggle("active");
        })
        cookieSave.addEventListener("click", function () { 
                        cookieMenu.style.transitionProperty = "none";
            cookieCustomWrapper.style.transitionProperty = "none";
            cookieMenu.style.visibility = "hidden";
            cookieMenu.classList.remove("active");
            cookieCustomWrapper.classList.remove("active");
        })
    }
    
}

function scrollReveal() { 
    let reveals = document.querySelectorAll(".reveal")
    for (var i = 0; i < reveals.length; i++) {
        let windowHeight = window.innerHeight
        let revealTop = reveals[i].getBoundingClientRect().top;
        let revealPoint = 450

        if (revealTop < windowHeight - revealPoint) {
            reveals[i].classList.add("active")
        };
    }
}

function buttonHover() {
    function moveBackground() {
        bgs.forEach(background => background.classList.add("active"))
    }
    function resetBackground() {
        bgs.forEach(background => background.classList.remove("active"))
    }
    let buttons = document.querySelectorAll('.section-invite');
    let bgs = document.querySelectorAll(".first-section-bg-pattern");
    buttons.forEach(button => {
        button.addEventListener("mouseover", moveBackground)
        button.addEventListener("mouseleave", resetBackground)
    });
}


function leaderboardCycle() { 
    let arrows = document.querySelectorAll(".lb_svg")
    let count = 1
    let text = document.getElementById("lbtext")
    let globalLB = document.querySelector(".global")
    let serverLB = document.querySelector(".server")

    for (var i = 0; i < arrows.length; i++) {
        arrows[i].addEventListener("click", function () {
            if (count == 1) {
                count = 2
                serverLB.style.visibility = "visible";
                globalLB.style.visibility = "hidden";
                text.innerHTML = "Server Leaderboard";
            } else {
                count = 1
                text.innerHTML = "Global Leaderboard";
                serverLB.style.visibility = "hidden";
                globalLB.style.visibility = "visible";
            }
            console.log(count)
            
        })
    }
    
}
function emailRequest() {
    function addEmail() { 
        let firstName = document.querySelector(".first-name").value
        let surname = document.querySelector(".surname").value
        let email = document.querySelector(".email").value
        return
    }
    let submitButton = document.querySelector(".website-button")
    submitButton.addEventListener("click",addEmail)
}
window.onload = function () { 
    buttonHover()
    setUpEvents();
    leaderboardCycle();
    cookieMenu();
    window.addEventListener("scroll", scrollReveal);
}
