document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ script.js loaded");


  const hamburger = document.getElementById("hamburger");
  const mobileMenu = document.getElementById("mobile-menu");

  if (hamburger && mobileMenu) {
    // Toggle mobile menu
    hamburger.addEventListener("click", () => {
      mobileMenu.classList.toggle("active");
    });

    // Close menu when clicking any link
    mobileMenu.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        mobileMenu.classList.remove("active");
      });
    });



    // Scroll show/hide logic
    let lastScrollTop = 0;
    window.addEventListener("scroll", function () {
      let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      if (scrollTop > lastScrollTop && scrollTop > 100) {
        // Scroll down
        navbar.style.top = "-100px";
      } else {
        // Scroll up
        navbar.style.top = "0";
      }
      lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    });
  } else {
    console.log("❌ Elements not found");
  }
});
