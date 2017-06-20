document.addEventListener('DOMContentLoaded', function(e) {
    var page_id = document.querySelector('input[name="page_id"]');
    
    if (typeof page_id != 'undefined') {
        if (page_id != null) {
            window.page_id = page_id.value;

            setup_editables();
        }
    }
});
