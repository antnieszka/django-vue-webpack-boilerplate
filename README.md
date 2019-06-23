# A Django - Vue.js project

Django 2.2 + Vue.js 2 + Webpack 4

## Backend setup

``` bash

# when running for the first time

# using pipenv
pip install --user pipenv  # if not yet installed
pipenv install -r requirements.txt

# using virtualenv
python -m venv venv
. venv/bin/activate # or on windows: venv\Scripts\activate.bat
pip install -r requirements.txt

# run database migrations
python manage.py migrate

# run server (127.0.0.1:8000 by default)
python manage.py runserver

```

## Frontend setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:3000
# Django backend should be started too (localhost:8000)
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
