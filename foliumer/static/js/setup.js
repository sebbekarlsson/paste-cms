var __fade_in = ' animated fadeIn';
var __fade_out = ' animated fadeOut';


var Setup = function(elem) {
    var _this = this;

    _this.db = {};
    
    _this.elem = elem;
    _this.steps = elem.querySelectorAll('.step-by-step-step');

    _this.init = function () {

        for (var i = 0; i < _this.steps.length; i++) {
            var step = _this.steps[i];
            var step_prev_btn = step.querySelector('[data-type="prev"]');
            var step_next_btn = step.querySelector('[data-type="next"]');
            
            if (step_prev_btn != null)
                step_prev_btn.addEventListener('click', function(e) { _this.previous_step(); });

            if (step_next_btn != null)
                step_next_btn.addEventListener('click', function(e) { _this.next_step(); });

            step.setAttribute('data-active', '0');
            step.setAttribute('data-step-id', i);
        } 
    };

    _this.start = function() {
        _this.activate_step(_this.steps[0]);
    };

    _this.get_current_step_id = function () {
        for (var i = 0; i < _this.steps.length; i++) {
            var step = _this.steps[i];
            
            if (step.getAttribute('data-active') == '1')
                return parseInt(step.getAttribute('data-step-id'));
        }

        return null;
    };

    _this.next_step = function () {
        var current_id = _this.get_current_step_id();

        if (current_id == null)
            return;

        var errors = [];

        if (typeof _this.next_step_action != 'undefined') {
            if (_this.next_step_action != null && _this.next_step_action) {
                errors = _this.next_step_action(_this.steps[current_id]);
            }
        }

        if (typeof errors == 'undefined')
            errors = [];
        
        if (errors.length > 0) {
            for (var i = 0; i < errors.length; i++) {
                if (typeof _this.handle_error != 'undefined') {
                    if (_this.handle_error != null && _this.handle_error) {
                        _this.handle_error(errors[i]);
                    }
                }
            }

            return;
        }

        var next_id = current_id + 1;

        if (next_id >= _this.steps.length) {
            if (typeof _this.handle_finish != 'undefined') {
                if (_this.handle_finish != null && _this.handle_finish) {
                    _this.handle_finish(_this.steps[current_id]);
                }
            }
            _this.deactivate_step(_this.steps[current_id]);
        } else {
            _this.activate_step(_this.steps[next_id]);
        }
    };

    _this.previous_step = function () {
        var current_id = _this.get_current_step_id();

        if (current_id == null)
            return;

        var prev_id = current_id - 1;
        _this.activate_step(_this.steps[prev_id]);
    };

    _this.activate_step = function(step) {
        for (var i = 0; i < _this.steps.length; i++) {
            var _step = _this.steps[i];

            if (_step == step)
                continue;
            
            if (_step.className.indexOf(__fade_in) > -1) {
                _step.className = _step.className.replace(__fade_in, '');
                _step.className += __fade_out;
            }
            _step.setAttribute('data-active', '0');
        }

        step.className = step.className.replace(__fade_out, '');
        step.className += __fade_in;
        step.setAttribute('data-active', '1');
    };

    _this.deactivate_step = function(step) {
        step.className = step.className.replace(__fade_in, '');
        step.className += __fade_out;
        step.setAttribute('data-active', '0');
    }

    _this.init();
};
