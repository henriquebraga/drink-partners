
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

