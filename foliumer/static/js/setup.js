var __fade_in = ' animated fadeIn';
var __fade_out = ' animated fadeOut';


var Setup = function(elem) {
    var _this = this;

    _this.db = {};

    _this.elem = elem;
    _this.steps = elem.querySelectorAll('.step-by-step-step');

    /**
     * Initializer
     *
     * Runs at instantiation.
     */
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

    /**
     * Will start the setup.
     */
    _this.start = function() {
        _this.activate_step(_this.steps[0]);
    };

    /**
     * Get the ID of the current step.
     *
     * @return Int | null
     */
    _this.get_current_step_id = function () {
        for (var i = 0; i < _this.steps.length; i++) {
            var step = _this.steps[i];

            if (step.getAttribute('data-active') == '1')
                return parseInt(step.getAttribute('data-step-id'));
        }

        return null;
    };

    /**
     * Make the setup go to the next step.
     */
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
                /* Making the error handler none-proprietary by
                 * making it possible for other developers to create a custom
                 * error handler.
                 */
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
            /* Making the finish action none-proprietary by
             * making it possible for other developers to create custom
             * finish actions.
             */
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

    /**
     * Make the setup go to the previous step.
     */
    _this.previous_step = function () {
        var current_id = _this.get_current_step_id();

        if (current_id == null)
            return;

        var prev_id = current_id - 1;
        _this.activate_step(_this.steps[prev_id]);
    };

    /**
     * Activate a single step,
     * will deactivate all other steps.
     */
    _this.activate_step = function(step) {
        for (var i = 0; i < _this.steps.length; i++) {
            var _step = _this.steps[i];

            if (_step == step)
                continue;

            _this.deactivate_step(_step);
        }

        step.className = step.className.replace(__fade_out, '');
        step.className += __fade_in;
        step.setAttribute('data-active', '1');
    };

    /**
     * Deactivate a single step.
     */
    _this.deactivate_step = function(step) {
        if (step.className.indexOf(__fade_in) > -1) {
            step.className = step.className.replace(__fade_in, '');
            step.className += __fade_out;
        }
        step.setAttribute('data-active', '0');
    }

    _this.init();
};
