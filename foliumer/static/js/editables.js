function save_page() {
    toggle_global_spinner();

    var obj = {};

    obj['page_route'] = window.page_route;

    var editables = document.querySelectorAll('.admin-editable');

    obj['editables'] = [];

    for (var i = 0; i < editables.length; i++) {
        var editable = {
            "editable_id": editables[i].getAttribute('data-editable-id'),
            "text": editables[i].innerHTML
        };

        obj['editables'].push(editable);
    }

    wpost('/save/', JSON.stringify(obj), function(data) {
        setTimeout(function(){
            toggle_global_spinner();
        }, 1000);
    });
}

function setup_editables() {
    if (typeof window.editor == 'undefined')
        window.editor = {};

    wget('/pagedata/' + window.page_route, function(pagedata) {
        window.page = JSON.parse(pagedata);

        var editables = document.querySelectorAll('.admin-editable');

        // Making sure all editables has an identifier
        for (var i = 0; i < editables.length; i++) {
            var editable = editables[i];

            if (!editable.hasAttribute('data-editable-id')) {
                editable.setAttribute('data-editable-id', window.page_route + '_' + i);
            } else {
                if (window.page['editables'] != null) {
                    for (var ii = 0; ii < window.page['editables'].length; ii++) {
                        if (window.page['editables'][ii]['editable_id'] == editable.getAttribute('data-editable-id'))
                            editable.innerHTML = window['page']['editables'][ii]['text'];
                    }
                }
            }
        }

        // initializing the editor
        window.editor = new MediumEditor('.admin-editable', {
            // options go here
        });
    });
}
