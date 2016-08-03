(function ($) {
    var tabItem = $('.filters-tab--item'),
        filterOptions = $('.filters-options');

    tabItem.click(function (event) {
        event.preventDefault();

        var clickTab = $(this);
        filterOptions.hide();
        var selector = '.filters-options' + '[data-field="' + $(event.target).data("group") + '"]';
        var selectedGroup = $(selector)[0];
        
        if (clickTab.hasClass('active')) {
            $(tabItem).removeClass('active');
            $(selectedGroup).hide();
        } else {
            $(tabItem).removeClass('active');
            clickTab.addClass('active');
            $(selectedGroup).show();
        }

    });
})(jQuery);