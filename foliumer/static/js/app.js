document.addEventListener('DOMContentLoaded', function(e) {
    var page_route = document.querySelector('input[name="page_route"]');
    
    if (typeof page_route != 'undefined') {
        if (page_route != null) {
            if (page_route.value != '') {
                window.page_route = page_route.value;

                if (window.page_route == '')
                    window.page_route = 'INDEX';

                setup_editables();
            } else {
                if (page_route.value != '') {
                    console.error("No `page_route` set for this page.");
                    console.error("Please set the value of <input name='page_route'/>");
                }
            }
        }
    }
});
