
# Drink Partners API

![Travis Build](https://travis-ci.com/henriquebraga/drink-partners.svg?token=Hz2UvRp98GSpoFSdrKgh&branch=master)
[![codecov](https://codecov.io/gh/henriquebraga/drink-partners/branch/master/graph/badge.svg?token=ex1RxllagJ)](https://codecov.io/gh/henriquebraga/drink-partners)

REST API responsible for managing partners

# Install dependencies

1. Create virtualenv:

```bash
    virtualenv drink_partner -p python3
```

2. Install dependencies using `pip`

```bash
 make requirements-dev
```

## Tests

1. Install docker or download mongodb

   [Docker for Mac](https://docs.docker.com/docker-for-mac/install/) 
   
   [Docker for Linux](https://docs.docker.com/engine/install/ubuntu/)
   
   [Docker for Windows](https://docs.docker.com/docker-for-windows/)
   
   [Mongodb for Mac](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
   
   [Mongodb for Linux](https://docs.mongodb.com/manual/administration/install-on-linux/)

2. Run docker-compose for project dependencies:

```bash
docker-compose up
 ```
3. To run all suite tests:

```bash
make test
```

4. To execute specific tests:

```bash
make test-matching Q=[test_name_or_test_class_name] 
```

5. To execute test coverage:

```bash
make test-coverage
```

## Running application

1. Run service dependencies:

```bash
docker compose-up
```

2. Run application:

```bash
make run
```

## Documentation (Swagger)

1. Execute steps `Running application` above

2. Access doc endpoint:

```bash
127.0.0.1/docs/
```

3. Set token by clicking in `Authorize` button and adding token `test`

## Deploy

1. Clone [repository](https://github.com/henriquebraga/drink-partners)

2. Install [Heroku](https://devcenter.heroku.com/articles/heroku-cli)

3. Configure account for heroku. If you already have one just login

```bash
    heroku login
```

### Create App

To create app in your Heroku account:

```bash
heroku create app drink_partners
```

### Set environment variables

```bash
heroku config:set GUNICORN_WORKERS=5 --app drink-partners

heroku config:set PORT=443 --app drink-partners

heroku config:set SIMPLE_SETTINGS=drink_partners.settings.production.py--app drink-partners

heroku config:set MONGODB_URI=mongodb://<address-mongodb> ---app drink-partners

heroku config:set MOTOR_DB=<database-name> ---app drink-partners
```

### Configure MongoDB

If you do not have a MongoDB server available, you could the service using `Add-ons` from Heroku.

1. Access you personal account in `https://id.heroku.com/login`
2. Filter for the app name you have created (e.g: `drink-partners`)
3. Click on Menu `Resources`
4. In `Add-ons`, search for `mongodb` and click on `mLab MongoDB`
5. It will automatically configure your mongodb for application

In this case, it will generate `MONGODB_URI` env var automatically. You can check use command `heroku config` as below:

```bash
heroku config
GUNICORN_WORKERS: 1
MONGODB_URI: mongodb://heroku_123:some_password@ds059215.mlab.com:59215/heroku_0dmrmq8z
```

The URI has the following pattern:

`mongodb://<user>:<password>@<mongodb_address>/<database_name>`

If you do so, you will need to set env var `MOTOR_DB` with the content from database name. In this example, database name is `heroku_0dmrmq8z`.

```bash
heroku config:set MOTOR_DB=heroku_0dmrmq8z ---app drink-partners
```

### Deploy Application

Deploy your application to heroku with command:

```bash
git push heroku master
```

### Check logs

```bash
heroku logs
```
