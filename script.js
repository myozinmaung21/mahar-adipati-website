// Header background on scroll
const header = document.querySelector(".site-header");
const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 40);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

// Mobile menu
const toggle = document.querySelector(".menu-toggle");
toggle?.addEventListener("click", () => {
  const open = document.body.classList.toggle("menu-open");
  toggle.setAttribute("aria-expanded", String(open));
});
document.querySelectorAll(".nav-links a").forEach((link) =>
  link.addEventListener("click", () => {
    document.body.classList.remove("menu-open");
    toggle?.setAttribute("aria-expanded", "false");
  })
);

// Reveal-on-scroll
const io = new IntersectionObserver(
  (entries) =>
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        io.unobserve(entry.target);
      }
    }),
  { threshold: 0.12 }
);
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

// Footer year
document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

// Arriving from another page with a link like index.html#services: fonts and images can shift the layout
// after the browser's first jump, so scroll to the section again once the page has finished loading.
const hashTarget = location.hash.length > 1 && document.getElementById(location.hash.slice(1));
if (hashTarget) {
  const goToHash = () => hashTarget.scrollIntoView({ behavior: "smooth" });
  if (document.readyState === "complete") goToHash();
  else window.addEventListener("load", goToHash);
}
