function save_page() {
    var page_id = document.querySelector('input[name="page_id"]');
    
    if (typeof page_id == 'undefined')
        return;

    if (page_id == null)
        return;

    var obj = {};

    obj['page_id'] = page_id.value;

    var editables = document.querySelectorAll('.admin-editable');

    obj['editables'] = [];
    
    for (var i = 0; i < editables.length; i++) {
        var editable = {
            "editable_id": editables[i].getAttribute('data-editable-id'),
            "text": editables[i].innerText
        };

        obj['editables'].push(editable);
    }

    wpost('/save/', JSON.stringify(obj), function(data) {
        console.log(data);
    });
}


function setup_editables() {
    var page_id = document.querySelector('input[name="page_id"]');
    
    if (typeof page_id == 'undefined')
        return;

    if (page_id == null)
        return;

    page_id = page_id.value;

    console.log(page_id);

    if (typeof window.editor == 'undefined')
        window.editor = {};

    var editables = document.querySelectorAll('.admin-editable');
    
    // Making sure all editables has an identifier
    for (var i = 0; i < editables.length; i++) {
        var editable = editables[i];
        
        editable.setAttribute('data-editable-id', page_id + '_' + i);
    }
    
    // initializing the editor
    window.editor = new MediumEditor('.admin-editable', {
        // options go here
    });
}
