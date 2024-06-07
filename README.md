# Social Networking API

## Prerequisites

- Docker
- Docker Compose

## Installation Steps

### Running the Project with Docker

To run this project using Docker, follow these steps:

1. Clone the repository:

        git clone https://github.com/chetanpagare31/Accuknox.git

        cd Accuknox

2. Build and run the containers:

        docker-compose up --build

    This command will:
        Build the Docker images.
        Start the MySQL and Django containers.
        Apply migrations.
    After completion of this build you can test each api over Postman/Thunder-client as given below

3. The application will be available at `http://localhost:8000`.

## Postman Collection to test the APIs

[Download the Postman Collection]( Social_Networking_APP.postman_collection.json)

## To Test APIs 

### Signup:

Method: POST

URL: http://localhost:8000/api/signup/

Body (JSON)
```json
    {
        "username": "Devansh",
        "email": "devansh@gmail.com",
        "password": "Devansh@123"
    }
```
Sample Response:
    {
        "username": "Devansh",
        "email": "devansh@gmail.com"
    }



### SignIn:
 Method: POST
 
 URL: http://localhost:8000/api/signin/
 
 Body (JSON):
 ```json
    {
        "email": "chetan@gmail.com",
        "password": "Chetan@123"
    }
```
Sample Response:
```json
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzgxOTkyNiwiaWF0IjoxNzE3NzMzNTI2LCJqdGkiOiJhN2VjNWIwZDY4NzE0YmE2ODk2YWQwOGI2MzcwY2FkOCIsInVzZXJfaWQiOjF9.GFg5JURCaoSyuVSXMunMitRK1LKt8jTUNFHg5NKmRKs",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3NzMzODI2LCJpYXQiOjE3MTc3MzM1MjYsImp0aSI6IjIyYTU5MWZiZDQ2OTQxM2Y4YTc0MzNmMTIzZGE2ZTA5IiwidXNlcl9pZCI6MX0.fTxcDDXqCRSuEfhaN5AILzD9J8FT6SEGRnCRR4ElyJs",
        "user": {
            "id": 1,
            "username": "chetan",
            "email": "chetan@gmail.com"
        }
    }
```

### Get users:
Method: GET

URL: http://localhost:8000/api/get_users/

Headers:
Key: Authorization
Value: Bearer <your_jwt_token> (replace <your_jwt_token> with a valid token)

Sample Response:
```json
[
    {
        "id": 1,
        "username": "chetan",
        "email": "chetan@gmail.com"
    },
    {
        "id": 2,
        "username": "vickyp",
        "email": "vicky@gmail.com"
    },
    {
        "id": 3,
        "username": "amarp",
        "email": "amar@gmail.com"
    },
    {
        "id": 4,
        "username": "Rakshit",
        "email": "rakshit@gmail.com"
    },
    {
        "id": 5,
        "username": "amit",
        "email": "amit@gmail.com"
    },
    {
        "id": 6,
        "username": "mit",
        "email": "mit@gmail.com"
    },
    {
        "id": 7,
        "username": "Sumit",
        "email": "sumit@gmail.com"
    },
    {
        "id": 8,
        "username": "Raj",
        "email": "raj@gmail.com"
    },
    {
        "id": 9,
        "username": "aditya",
        "email": "aditya@gmail.com"
    },
    {
        "id": 10,
        "username": "Saurav",
        "email": "saurav@gmail.com"
    },
    {
        "id": 11,
        "username": "Hemant",
        "email": "hemant@gmail.com"
    },
    {
        "id": 12,
        "username": "Kunal",
        "email": "kunal@gmail.com"
    },
    {
        "id": 13,
        "username": "Maddy",
        "email": "maddy@gmail.com"
    },
    {
        "id": 14,
        "username": "Darshan",
        "email": "darshan@gmail.com"
    },
    {
        "id": 15,
        "username": "Ronak",
        "email": "ronak@gmail.com"
    },
    {
        "id": 16,
        "username": "Aman",
        "email": "aman@gmail.com"
    },
    {
        "id": 17,
        "username": "Devansh",
        "email": "devansh@gmail.com"
    }
]
```
### refresh token:
Method: POST

URL: http://localhost:8000/api/friend_request/

Body (JSON):
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzgxOTkyNiwiaWF0IjoxNzE3NzMzNTI2LCJqdGkiOiJhN2VjNWIwZDY4NzE0YmE2ODk2YWQwOGI2MzcwY2FkOCIsInVzZXJfaWQiOjF9.GFg5JURCaoSyuVSXMunMitRK1LKt8jTUNFHg5NKmRKs"
}
```
Sample Response:
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3NzM2NTEyLCJpYXQiOjE3MTc3MzM1MjYsImp0aSI6IjAyOGI1YjJmOGViZDQ4OWY5ODQzODAxZjQ5ODRiODYxIiwidXNlcl9pZCI6MX0.q-zfW2H0BT-94qeFumfvQyt9PK6f_1Xgk4p4zY1CLXM"
}
```
### search users:
Method: GET

URL: http://localhost:8000/api/search_users/?query=a

Headers:
Key: Authorization
Value: Bearer <your_jwt_token> (replace <your_jwt_token> with a valid token)

Sample Response:
```json
{
    "count": 14,
    "next": "http://localhost:8000/api/search_users/?page=2&q=a",
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "chetan",
            "email": "chetan@gmail.com"
        },
        {
            "id": 3,
            "username": "amarp",
            "email": "amar@gmail.com"
        },
        {
            "id": 4,
            "username": "Rakshit",
            "email": "rakshit@gmail.com"
        },
        {
            "id": 5,
            "username": "amit",
            "email": "amit@gmail.com"
        },
        {
            "id": 8,
            "username": "Raj",
            "email": "raj@gmail.com"
        },
        {
            "id": 9,
            "username": "aditya",
            "email": "aditya@gmail.com"
        },
        {
            "id": 10,
            "username": "Saurav",
            "email": "saurav@gmail.com"
        },
        {
            "id": 11,
            "username": "Hemant",
            "email": "hemant@gmail.com"
        },
        {
            "id": 12,
            "username": "Kunal",
            "email": "kunal@gmail.com"
        },
        {
            "id": 13,
            "username": "Maddy",
            "email": "maddy@gmail.com"
        }
    ]
}
```


### send friend request:
Method: POST

URL: http://localhost:8000/api/friend_request/

Headers:
Key: Authorization
Value: Bearer <your_jwt_token>
Body (JSON):
```json
{
    "to_user": "Devansh"
}
```
Sample Response:
```json
{
    "id": 12,
    "from_user": "chetan",
    "status": "pending",
    "timestamp": "2024-06-07T04:16:38.581253Z"
}
```
### list of pending request:
Method: GET

URL: http://localhost:8000/api/list_pending_request/

Headers:
Key: Authorization
Value: Bearer <your_jwt_token>

Sample Response:
```json
[
    {
        "id": 10,
        "from_user": "Maddy",
        "status": "pending",
        "timestamp": "2024-06-06T11:05:19.165171Z"
    },
    {
        "id": 11,
        "from_user": "Devansh",
        "status": "pending",
        "timestamp": "2024-06-07T03:51:51.873702Z"
    }
]
```
### list of friends:
Method: GET

URL: http://localhost:8000/api/list_friends/

Headers:
Key: Authorization
Value: Bearer <your_jwt_token>

Sample Response:
```json
[
    {
        "id": 9,
        "username": "aditya",
        "email": "aditya@gmail.com"
    },
    {
        "id": 10,
        "username": "Saurav",
        "email": "saurav@gmail.com"
    },
    {
        "id": 15,
        "username": "Ronak",
        "email": "ronak@gmail.com"
    },
    {
        "id": 16,
        "username": "Aman",
        "email": "aman@gmail.com"
    },
    {
        "id": 17,
        "username": "Devansh",
        "email": "devansh@gmail.com"
    }
]
```
### accept/reject friend request:
Method: PATCH

URL: http://localhost:8000/api/manage_friend_request/

Headers:
Key: Authorization
Value: Bearer <your_jwt_token>
Body (JSON):
```json
{
    "from_user": "Devansh",
    "status": "accepted"
}
```
Sample Response:
{
    "id": 11,
    "from_user": "Devansh",
    "status": "accepted",
    "timestamp": "2024-06-07T03:51:51.873702Z"
}
