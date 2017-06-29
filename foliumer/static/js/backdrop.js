var __fade_in = ' animated fadeIn';
var __fade_out = ' animated fadeOut';


function backdrop_is_active() {
    var backdrop = document.getElementById('backdrop');

    return backdrop.getAttribute('active') == 1;
}


function toggle_backdrop() {
    var backdrop = document.getElementById('backdrop');

    if (typeof backdrop == 'undefined')
        return;

    if (backdrop == null)
        return;

    if (!backdrop)
        return;

    var state = true;

    backdrop.innerHTML = '';
    backdrop.setAttribute('style', '');

    if (backdrop.hasAttribute('active'))
        state = backdrop.getAttribute('active') == '1';

    if (state) {
        backdrop.setAttribute('active', '0');
        backdrop.className = backdrop.className.replace(__fade_in, '');
        backdrop.className += __fade_out;
    } else {
        backdrop.setAttribute('active', '1');
        backdrop.className = backdrop.className.replace(__fade_out, '');
        backdrop.className += __fade_in;
    }
}

function toggle_global_spinner() {
    var backdrop = document.getElementById('backdrop');
    
    toggle_backdrop();

    if (backdrop_is_active()) {
        backdrop.setAttribute('style', [
            'display: flex;',
            'justify-content: center;',
            'align-items: center;',
            'pointer-events: all;'
        ].join(''));

        insert_spinner(backdrop);
    }
}

function backdrop_error(message) {
    var backdrop = document.getElementById('backdrop');
    
    toggle_backdrop();

    if (backdrop_is_active()) {
        backdrop.setAttribute('style', [
            'display: flex;',
            'justify-content: center;',
            'align-items: center;'
        ].join(''));

        backdrop.innerHTML = [
            '<div class="card backdrop-content">',
            '<h3>Error</h3>',
            '<p>' + message + '</p>',
            '</div>'
        ].join('');

        backdrop.querySelector('div').addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
}

document.addEventListener('DOMContentLoaded', function(e) {
    var backdrop = document.getElementById('backdrop');

    if (typeof backdrop == 'undefined')
        return;

    if (backdrop == null)
        return;

    if (!backdrop)
        return;

    backdrop.addEventListener('click', function(e) {
        toggle_backdrop();
    });

    toggle_backdrop();
});
