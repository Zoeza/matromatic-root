/* Scripts pour Matromatic - Neuros Theme */
document.addEventListener("DOMContentLoaded", function () {
    console.log("Page chargée avec succès");

    // Animation du texte du hero
    const heroText = document.querySelector("#hero h1");
    if (heroText) {
        heroText.style.opacity = "0";
        setTimeout(() => {
            heroText.style.opacity = "1";
            heroText.style.transition = "opacity 2s ease-in-out";
        }, 500);
    }

    // Interaction sur les liens du menu
    const menuLinks = document.querySelectorAll("nav ul li a");
    menuLinks.forEach(link => {
        link.addEventListener("mouseover", function () {
            this.style.color = "#f14f44";
        });
        link.addEventListener("mouseout", function () {
            this.style.color = "white";
        });
    });

    // Intégration d'Owl Carousel
    if (typeof jQuery !== "undefined") {
        jQuery(document).ready(function () {
            jQuery(".owl-carousel").owlCarousel({
                loop: true,
                margin: 10,
                nav: true,
                responsive: {
                    0: { items: 1 },
                    600: { items: 2 },
                    1000: { items: 3 }
                }
            });
        });
    }
});
