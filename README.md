# Car API
A RESTful API to retrieve and create car data.


## Installation

You can easily install via Docker;

```
git clone https://adhorrig/flask-rest-api
bash build.sh
```

`build.sh` runs the below for you;

```
docker build -t flask-container:latest .
docker run -d -p 5000:5000 flask-container
```

Alternatively, you can follow the below steps;

```
git clone https://adhorrig/flask-rest-api
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python src/db.py
python src/seed.py
python src/app.py
```

Note, if you are *not* running through Docker, you will need to remove `, host='0.0.0.0'` from line 137 in `app.py`

## Endpoints

#### Get Cars

This endpoint returns details for all cars.

```shell
curl -i http://localhost:5000/cars
```

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "last_updated": "2018-01-21T22:12:33.948846+00:00",
    "make": "Nissan",
    "model": "Micra",
    "price": 500,
    "year": 2004
  },
  {
    "id": 2,
    "last_updated": "2018-01-21T22:12:33.957004+00:00",
    "make": "Nissan",
    "model": "Micra",
    "price": 400,
    "year": 2004
  },
  {
    "id": 3,
    "last_updated": "2018-01-21T22:12:33.961886+00:00",
    "make": "Ford",
    "model": "Fiesta",
    "price": 300,
    "year": 2002
  }
]
```


#### Get Car

This endpoint returns the details for a single car.

```shell
curl -i http://localhost:5000/cars/1
```

> The above command returns JSON structured like this:

```json
{
  "id": 1,
  "last_updated": "2018-01-21T22:12:33.948846+00:00",
  "make": "Nissan",
  "model": "Micra",
  "price": 500,
  "year": 2004
}
```

#### Create Car

This endpoint creates a car.

```shell
curl -i -H "Content-Type: application/json" -X POST -d '{"make":"BMW", "model":"Mac 4", "year":"2016", "chasis_id":"ABC1234A", "price":500.00}' http://localhost:5000/car
```

> The above command returns JSON structured like this:

```json
{"chasis_id": "ABC1234A", "make": "BMW", "price": 500, "model": "Mac 4", "year": 2016}
```

#### Average Price

This endpoint returns the price of a car.

```shell
curl -i -H "Content-Type: application/json" -X POST -d '{"make":"Ford", "model":"Fiesta", "year":"2002"}' http://localhost:5000/avg
```

> The above command returns JSON structured like this:

```json
{"average_price": 300.0}
```

#### Update Car


This endpoint updates the price of a car.

```shell
curl -X PUT -H "Content-Type: application/json" -d '{"price":500}' http://localhost:5000/cars/1
```

> The above command returns JSON structured like this:

```json
{
  "id": 1,
  "last_updated": "2018-01-22T12:41:45.785164+00:00",
  "make": "Nissan",
  "model": "Micra",
  "price": 500,
  "year": 2004
}
```

#### Delete Car


This endpoint deletes a car.

```shell
curl -X "DELETE" http://localhost:5000/cars/delete/25
```

> The above command returns JSON structured like this:

```json
{
  "result": true
}
```

## Testing

There are several tests which are done against the API, unittests. If you are running the app from within a container, you will need to run the tests with;

```shell
 docker exec -it ${CONTAINER_ID} python src/tests.py
```

Or;

```shell
docker exec -it ${CONTAINER_ID} python -m unittest discover
```

You can find out your container id by running;

```shell
docker ps
```

However, if you are not running the app from within a container - you can run the tests with;

```shell
python src/tests.py
```

Or;

```shell
python -m unittest discover
```

## Questions or difficulty?

Feel free to email me at adhorrig@gmail.com :).