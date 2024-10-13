import requests

url = "http://13.61.10.12:8000/api/v1/register/"

data = {
    "password": "Admin33",
    "last_login": "2024-10-02T23:03:27.144281Z",
    "is_superuser": "false",
    "username": "vbchssshjds",
    "first_name": "ddfdssdf",
    "is_staff": "false",
    "is_active": "false",
    "date_joined": "null",
    "email": "fvvggssgdffd@dev.com",
    "name": "cbhsdsc",
    "last_name": "cdscdscd",
    "phone_number": "+998900069233",
    "sex": "null",
    "age": "null",
    "width": "null",
    "weight": "null",
    "groups": [],
    "user_permissions": []
}

res = requests.post(url, data)
print(res.status_code)
print(res.text)