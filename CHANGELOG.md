Drink_Partners 1.4.0 (2020-05-06)
=================================

Features
--------

- Document create partner endpoint in swagger


Drink_Partners 1.3.0 (2020-05-05)
=================================

Features
--------

- Add create index id for partners command


Drink_Partners 1.2.0 (2020-05-05)
=================================

Features
--------

- Set token to authenticate as environment variable


Drink_Partners 1.1.0 (2020-05-05)
=================================

Features
--------

- Remove safety lib
- Update readme with retryWrites step when using mlab (MongoDB) from heroku


Drink_Partners 1.0.1 (2020-05-05)
=================================

Bugfixes
--------

- Use update with upsert instead of insert when creating partner


Drink_Partners 1.0.0 (2020-05-05)
=================================

Features
--------

- Add MongoDB steps to execute indexes
- Configure application to be deployed on Heroku


Drink_Partners 0.21.0 (2020-05-04)
==================================

Features
--------

- Set `coordinates`for `Address`/`CoverageArea` fields as required


Drink_Partners 0.20.0 (2020-05-04)
==================================

Features
--------

- Implement search nearest partner by coordinate endpoint


Drink_Partners 0.19.0 (2020-05-04)
==================================

Features
--------

- Validate fields on partner create view


Drink_Partners 0.18.0 (2020-05-03)
==================================

Features
--------

- Create partner search by latitude and longitude coordinates view structure
- Implement search nearest partner from latitude longitude mongodb backend
- Implement search nearest partner given coordinate to PartnerSearchView


Drink_Partners 0.17.0 (2020-05-03)
==================================

Features
--------

- Document get partner by endpoint in swagger
- Implement swagger


Drink_Partners 0.16.0 (2020-05-02)
==================================

Features
--------

- Refactor moving partner views constructor to super class
- Refactor moving one view class per file


Drink_Partners 0.15.0 (2020-05-02)
==================================

Features
--------

- Implement partner create view


Drink_Partners 0.14.0 (2020-05-02)
==================================

Features
--------

- Implement logs in application


Drink_Partners 0.13.0 (2020-05-02)
==================================

Features
--------

- Configure application logging


Bugfixes
--------

- Fix initialize mongoDB when starting application


Drink_Partners 0.12.0 (2020-05-01)
==================================

Features
--------

- Implement backend pool for partners


Drink_Partners 0.11.1 (2020-05-01)
==================================

Features
--------

- Start mongodb when initialize app


Drink_Partners 0.11.0 (2020-05-01)
==================================

Features
--------

- Create MongoDB Client
- Implement get partners view


Drink_Partners 0.10.0 (2020-05-01)
==================================

Features
--------

- Create MongoDB Client


Drink_Partners 0.9.0 (2020-04-30)
=================================

Features
--------

- Create Authentication middleware
- Create Static Authentication Backend


Bugfixes
--------

- Add authentication Pool


Drink_Partners 0.8.0 (2020-04-30)
=================================

Features
--------

- Implement API version middleware


Drink_Partners 0.7.0 (2020-04-30)
=================================

Features
--------

- Implement error exception middleware


Drink_Partners 0.6.0 (2020-04-30)
=================================

Features
--------

- Implement healthcheck route


Drink_Partners 0.5.0 (2020-04-30)
=================================

Features
--------

- Add `make check-vulnerabilities` step to CI build
- Add `make lint` step to CI build


Drink_Partners 0.4.0 (2020-04-29)
=================================

Features
--------

- Create Travis CI flow


Drink_Partners 0.3.0 (2020-04-29)
=================================

Features
--------

- Run web application


Drink_Partners 0.2.0 (2020-04-29)
=================================

Features
--------

- Add pyproject file
- Initial project structure
