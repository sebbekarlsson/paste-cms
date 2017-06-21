document.addEventListener('DOMContentLoaded', function(e) {
    var main_menu = document.getElementById('main-menu');

    if (typeof main_menu == 'undefined')
        return;

    if (main_menu == null)
        return;

    var main_menu_height = parseInt(getComputedStyle(main_menu).height.replace('px', ''));
    main_menu.style.top = - main_menu_height + 'px';

    var main_menu_button = main_menu.querySelector('.drop-menu-button');

    main_menu_button.addEventListener('click', function(e) {
        var tmp_data = {
            'dy': 0,
            'menu': main_menu,
            'menu_height': main_menu_height
        };

        var drop = true;

        if (parseInt(tmp_data['menu'].style.top.replace('px', '')) < 0) {
            drop = true;
        } else {
            drop = false;
        }

        var inter = setInterval(function() {
            if (drop)
                tmp_data['dy'] += 0.1;
            else
                tmp_data['dy'] -= 0.1;



            if (tmp_data['dy'] > 0) {
                if (tmp_data['dy'] - 0.001 < 0) {
                    tmp_data['dy'] = 0.001;
                } else {
                    tmp_data['dy'] -= 0.001;
                }
            }

            if (tmp_data['dy'] < 0) {
                if (tmp_data['dy'] + 0.001 > 0) {
                    tmp_data['dy'] = 0.001;
                } else {
                    tmp_data['dy'] += 0.001;
                }
            }


            var next_top = parseInt(tmp_data['menu'].style.top.replace('px', '')) + tmp_data['dy'];

            if (next_top >= 0 && drop) {
                next_top = 0;
                clearInterval(inter);
            }

            if (!drop && next_top <= -tmp_data['menu_height']) {
                next_top = -tmp_data['menu_height'];
                clearInterval(inter);
            }

            tmp_data['menu'].style.top = next_top + 'px';
        }, 0, tmp_data);
    });
});
