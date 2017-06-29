var SETUP_DB = {};


var __fade_in = ' animated fadeIn';
var __fade_out = ' animated fadeOut';


function action_form(step) {
    var errors = [];

    if (step.getAttribute('data-name') == 'admin_form') {
        var username_input = step.querySelector('#admin_username');
        var password_input = step.querySelector('#admin_password');
        var password_confirm = step.querySelector('#admin_password_confirm');

        if (password_input.value != password_confirm.value)
            errors.push('Passwords does not match');

        if (errors.length == 0) {
            SETUP_DB['admin'] = {};
            SETUP_DB['admin']['username'] = username_input.value;
            SETUP_DB['admin']['password'] = password_input.value;
        }
    }

    return errors;
}

function action_next(e) {
    errors = [];
    var step = e.target.parentNode.parentNode;

    if (step.hasAttribute('data-name'))
        errors = action_form(step);

    if (errors.length > 0) {
        for (var i = 0; i < errors.length; i++) {
            backdrop_error(errors[i]);
        }

        return;
    }

    step.className = step.className.replace(__fade_in, '');
    step.className += __fade_out;

    setTimeout(function() {
        step.setAttribute('data-active', '0');

        var steps = step.parentNode.querySelectorAll('.step-by-step-step');

        for (var i = 0; i < steps.length; i++) {
            var _step = steps[Math.min(steps.length - 1, i + 1)];
            var prev_step = steps[Math.max(0, i - 1)];

            if (prev_step == step) {
                _step.setAttribute('data-active', '1');
                _step.className += __fade_in;
                
                break;
            }
        }
    }, 600);
}

document.addEventListener('DOMContentLoaded', function(e) {
    var setup = document.getElementById('setup');
    var steps = setup.querySelectorAll('.step-by-step-step');

    for (var i = 0; i < steps.length; i++) {
        var step = steps[i];
        var button_next = step.querySelector('#step-next');

        button_next.addEventListener('click', function(e) { action_next(e); });
    }
});
