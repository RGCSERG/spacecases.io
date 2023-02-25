function goBack() {
    window.history.back();
  }
  
function setUpEvents() { 
    let content = document.querySelector(".dropdown");
    let button = document.querySelector(".button-wrapper");
    let svg = document.querySelector(".svg")

    button.addEventListener("click", function() { 
        content.classList.toggle("active");
        svg.classList.toggle("active")
    })
}

function leaderboardCycle() { 
    var arrows = document.querySelectorAll(".lb_svg")
    var count = 1
    var text = document.getElementById("lbtext")
    var globalLB = document.querySelector(".global")
    var serverLB = document.querySelector(".server")

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
window.onload = function(){ 
    setUpEvents();
    leaderboardCycle();
}
