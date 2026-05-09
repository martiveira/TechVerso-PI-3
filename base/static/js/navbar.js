document.addEventListener("DOMContentLoaded", () => {
  const openBtn   = document.getElementById("openMenu");
  const closeBtn  = document.getElementById("closeMenu");
  const mobileMenu = document.getElementById("mobileMenu");

  if (openBtn && closeBtn && mobileMenu) {
    openBtn.addEventListener("click", () => {
      mobileMenu.classList.add("open");
      document.body.style.overflow = "hidden";
    });

    closeBtn.addEventListener("click", closeMobileMenu);

    // Close when a link is tapped
    mobileMenu.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", closeMobileMenu);
    });

    // Close on Escape key
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeMobileMenu();
    });
  }

  function closeMobileMenu() {
    if (mobileMenu) {
      mobileMenu.classList.remove("open");
      document.body.style.overflow = "";
    }
  }

  // Close if screen resizes to desktop
  window.addEventListener("resize", () => {
    if (window.innerWidth >= 992) closeMobileMenu();
  });
});
