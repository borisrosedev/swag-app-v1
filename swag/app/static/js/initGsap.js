console.log("✅ [custom gsap] activated");
gsap.registerPlugin(ScrollTrigger);


export function initGsapAnimations() {
  const main = document.getElementsByTagName("main")[0];

  console.log("main", main)

  if (main.classList.contains("landing__main")) {
    gsap.to(".landing__h1", { y: -50 });
    //gsap.from(".home__hero-section .custom-card", homeHerosectionCustomCardAnimation)
    return;
  }

  if (
    document.getElementsByTagName("main")[0].classList.contains("home__main")
  ) {
    gsap.utils.toArray(".home__hero-section .custom-card").forEach((card) => {
      gsap.from(card, {
        scrollTrigger: {
          trigger: card,
          start: "top 80%",
          end: "bottom 30%",
          toggleActions: "restart pause resume none",
          once: false,
          //markers: true,
        },
        scale: 0.7,
        duration: 2,
        ease: "power2.out",
      });
    });

    return;
  }

  if (main.classList.contains("dashboard__main")){
    alert('dashboard')
  }

}

