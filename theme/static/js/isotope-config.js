var $container = $('#isotope-container');

$container.isotope({
    itemSelector: '.isotope-item',
    layoutMode: 'masonry',
    animationEngine: 'best-available',
    masonry: {
        columnWidth: 210,
    }
});
