function backdrop_is_active() {
    var backdrop = document.getElementById('backdrop');

    return backdrop.getAttribute('active') == 1;
}


function toggle_backdrop() {
    var backdrop = document.getElementById('backdrop');
    var state = true;

    backdrop.innerHTML = '';
    backdrop.setAttribute('style', '');

    if (backdrop.hasAttribute('active'))
        state = backdrop.getAttribute('active') == '1';

    if (state) {
        backdrop.setAttribute('active', '0');
    } else {
        backdrop.setAttribute('active', '1');
    }
}

function toggle_global_spinner() {
    var backdrop = document.getElementById('backdrop');
    
    toggle_backdrop();

    if (backdrop_is_active()) {
        backdrop.setAttribute('style', [
            'display: flex;',
            'justify-content: center;',
            'align-items: center;'
        ].join(''));

        insert_spinner(backdrop);
    }
}

document.addEventListener('DOMContentLoaded', function(e) {
    toggle_backdrop();
});
