/* Scripts extraits du fichier HTML pour le thème Neuros */
document.addEventListener("DOMContentLoaded", function () {
    console.log("Page chargée avec succès");

    // Gestion du lazy load pour Elementor
    const lazyloadRunObserver = () => {
        const lazyloadBackgrounds = document.querySelectorAll(".e-con.e-parent:not(.e-lazyloaded)");
        const lazyloadBackgroundObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    let lazyloadBackground = entry.target;
                    if (lazyloadBackground) {
                        lazyloadBackground.classList.add('e-lazyloaded');
                    }
                    lazyloadBackgroundObserver.unobserve(entry.target);
                }
            });
        }, { rootMargin: '200px 0px 200px 0px' });
        lazyloadBackgrounds.forEach((lazyloadBackground) => {
            lazyloadBackgroundObserver.observe(lazyloadBackground);
        });
    };

    const events = ['DOMContentLoaded', 'elementor/lazyload/observe'];
    events.forEach((event) => {
        document.addEventListener(event, lazyloadRunObserver);
    });

    // Correction pour WooCommerce
    (function() {
        var c = document.body.className;
        c = c.replace(/woocommerce-no-js/, 'woocommerce-js');
        document.body.className = c;
    })();
});
