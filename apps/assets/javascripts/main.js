(function ($) {
    "use strict";
    function insertParam(key, value) {
        key = escape(key); value = escape(value);
        var kvp = document.location.search.substr(1).split('&');
        if (kvp === '') {
            document.location.search = '?' + key + '=' + value;
        }
        else {
            var i = kvp.length; var x; while (i--) {
                x = kvp[i].split('=');
                if (x[0] == key) {
                    x[1] = value;
                    kvp[i] = x.join('=');
                    break;
                }
            }
            if (i < 0) {
                kvp[kvp.length] = [key, value].join('=');
            }
            document.location.search = kvp.join('&');
        }
    }

    var element = document.getElementById("solution");
    if(element) {
        element.addEventListener("change", function(evnt) {
            var el = evnt.target;
            var value = el[el.selectedIndex].value;
            insertParam('solution', value);
        }, false);
    }

    /**
     * Modifies structure if Javascript if enabled
     */
    var setLayout  = function() {
        if(javascriptEnable()) {
            $('.filters').removeClass('column-one-third');
            $('.list-market').removeClass('column-two-thirds');
        }
    };

    /**
     * Check if Javascript is enable
     * @returns {boolean}
     */
    var javascriptEnable = function() {
        var body = document.body;
        body.className = body.className.replace('no-js','js-enabled');
        return body.classList.contains('js-enabled');
    };

    /**
     * Initialisation
     */
    var init = function() {
        setLayout();
    };

    $(init);

})(jQuery);