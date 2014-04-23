var $container = $('#isotope-container');

$container.isotope({
    itemSelector: '.item',
    layoutMode: 'cellsByRow',
    animationEngine: 'best-available',
    cellsByRow: {
        columnWidth: 74,
        rowWidth: 74
    }
});
