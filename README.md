# PASTE-CMS
> A simple copy-paste, edit-text-only cms.

> __NO LONGER MAINTAINED, PLEASE SEE:__ [https://github.com/sebbekarlsson/nilms](https://github.com/sebbekarlsson/nilms)

> All this CMS provides is route / page management and a wysiwyg editor
> for editable areas created by the template developer.

## Development steps of a simple paste-site
* [Theme developer creates templates](screenshots/develop_template.png)
* [Theme developer creates editable areas for the site admin, inside the templates.](screenshots/develop_template.png)
* [Site admin creates routes / pages and selects which template these pages should use.](screenshots/admin_routes.png)
* [Site admin can whenever she wants edit the editable areas using the wysiwyg editor.](screenshots/w.png)

## Running the CMS in production
> `coming soon`
> Will put instructions here soon.

## Running the CMS as a developer
* 0:
> copy the `config.example.json` to `config.json` and edit it and fill in
> your data.

* 1: Make sure you have the dependencies:

> `sass gem for ruby`

        gem install sass

* 2: execute

        python setup.py develop

* 3: execute

        foliumer-develop

* 4:
> The CMS should be up and running at `http://localhost:5000`

* NOTE:
> When killing the develop-process (`foliumer-develop`), make sure you also run:

        pkill -f sass

> To kill the sass process as well.
