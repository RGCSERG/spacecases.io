const burger = document.querySelector(".profile-pic");

burger.addEventListener("click", () => {
  if (burger.classList.contains("active")) {
    gsap.to(".links", { x: "100%" });
    gsap.to(".line", { stroke: "white" });
    gsap.set("body", { overflow: "auto" });
    gsap.set("body", { overflowX: "hidden" });
  } else {
    gsap.to(".links", { x: "0%" });
    gsap.to(".line", { stroke: "black" });
    gsap.fromTo(
      ".links a",
      { opacity: 0, y: 0 },
      { opacity: 1, y: 20, delay: 0.25, stagger: 0.25 }
    );
    gsap.set("body", { overflow: "hidden" });
  }
  burger.classList.toggle("active");
});

const videos = gsap.utils.toArray(".video");
gsap.set(videos, { opacity: 0 });



document.addEventListener('DOMContentLoaded', () => {
  let mousePosX = 0,
      mousePosY = 0,
      mouseCircle = document.getElementById('mouse');

  document.onmousemove = (e) => {
      mousePosX = e.pageX;
      mousePosY = e.pageY;
  }

  let delay = 6,
      revisedMousePosX = 0,
      revisedMousePosY = 0;

  function delayMouseFollow() {
      requestAnimationFrame(delayMouseFollow);

      revisedMousePosX += (mousePosX - revisedMousePosX) / delay;
      revisedMousePosY += (mousePosY - revisedMousePosY) / delay; 

      mouseCircle.style.top = revisedMousePosY + 'px';
      mouseCircle.style.left = revisedMousePosX + 'px';
  }
  delayMouseFollow();
});