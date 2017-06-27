function is_loggedin() {
    var input = document.querySelector('input[name="user_id"]');

    if (typeof input == 'undefined')
        return false;

    if (input == null)
        return false;

    return input.value != '';
}
