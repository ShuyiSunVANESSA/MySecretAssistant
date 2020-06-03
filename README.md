# HOW TO START
Install docker https://docs.docker.com/get-docker/
Navigate to the repository 'cd MySecretAssistant'
Bring the application up by 'docker-compose up'

## Test locally
Try hitting this endpoint 'http://localhost:5000'
Try hitting this endpoint 'http://localhost:5000/periods'

# Device Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List my recent 5 period records

**Definition**

`GET /period`

**Response**

- `200 OK` on success

```json
[
    {
        "start_date": "2020/01/01",
        "duration":  "5",
        "created_date": "yyyy/mm/dd"
    },
    {
        "start_date": "2020/02/01",
        "duration":  "5",
        "created_date": "yyyy/mm/dd"
    },
]
```

### Period lookup for specific date

**Definition**

`GET /period`

**Query Parameters**

- `"username":string` unique identifier of user
- `"date":string` yyyy/mm/dd

**Response**

- `200 OK` on success

```json
[
    {
        "date": "2020/01/01",
        "menstrual_period":  "true",
        "future_prediction": "true",
        "average_duration": "4",
        "average_frequency": "20"
    }
]
```

### Registering a new period

**Definition**

`POST /period`

**Arguments**
```json
{
    "username": "agong",
    "date": "2020/01/01",
}
```

**Response**

- `201 Created` on success

```json
{
    "username": "agong",
    "date": "2020/01/01",
    "created_date": "2020/01/01",
    "average_duration": "4",
    "average_frequency": "20",
    "next_period_date": "2020/02/01"
}
```

## Update period record

`PUT /period/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
    "username": "agong",
    "replace_date": "2020/01/01",
    "updated_date": "2020/01/05"
}
```

## Delete a period

**Definition**

`DELETE /devices/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success
