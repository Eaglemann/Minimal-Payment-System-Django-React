# CRUD APP
# Frontend is React + Typescript
# Backend is Django

# 

# Start Backend

## Getting started (docker)

```bash
$ docker-compose build backend

$ docker-compose run backend ./manage.py migrate
$ docker-compose run --service-ports backend ./manage.py runserver 0.0.0.0:8000
```

## Getting started (without docker)

**- Requires Python 3.9 -**

```bash
$ python3 -m venv venv
$ source venv/bin/activate

$ pip3 install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver 8000
```

## Creating a superuser to access django admin

```bash
$ ./manage.py createsuperuser
```

## Running the tests

```bash
$ ./manage.py test
```


# Start Frontend


# Frontend

## Getting started (docker)

```bash
$ docker-compose build frontend

$ docker-compose run --service-ports frontend npm start
```

## Getting started (without docker)

**- Requires Node.js 14 -**

```bash
$ npm install
$ npm start
```

## Running the tests

```bash
$ npm test
```



# Endpoints to test






- http://localhost:3000/pay/:sellerHandle
  - This is where sellers send their buyers to pay their invoices, the seller handle is designed to be human readable and map to a single seller.
- http://localhost:3000/seller/:sellerId
  - This is where sellers can go to update their unique handle.


- GET http://localhost:8000/api/sellers/:sellerId
  - Returns seller data using their unique id.
- GET http://localhost:8000/api/sellers/handle/:sellerHandle
  - Returns seller data user their unique handle.
- PUT http://localhost:8000/api/sellers/:sellerId
  - Updates the handle of a seller.

You can drop into the django admin (after creating a superuser) and add a new seller to test with: http://localhost:8000/admin/
