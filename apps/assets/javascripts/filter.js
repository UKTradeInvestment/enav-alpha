(function ($) {
    var tabItem = $('.filters-tab--item'),
        filterOptions = $('.filters-options');

    tabItem.click(function (event) {
        event.preventDefault();

        var clickTab = $(this);
        var selectedGroup = $(filterOptions).first().data("group", $(event.target).data("group"))[0];

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