navItems = document.querySelectorAll(".nav-item");
navItems.forEach((navItem) => {
  navItem.addEventListener("click", () => {
    navItems.forEach((element) => {
      element.classList.remove("active");
    });
    navItem.classList.add("active");
  });
});
