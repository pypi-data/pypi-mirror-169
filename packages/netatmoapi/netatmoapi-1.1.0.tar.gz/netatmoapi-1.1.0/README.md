# netatmoapi

This is a simple Python 3 wrapper of the Netatmo Connect API.

It contains user authentication and nearly the full functionality of the Netatmo Connect API.

## Installation

You can install the library using [pip](https://pip.pypa.io/en/stable/):

`pip install netatmoapi`

## Preparations
* Netatmo account
* Netatmo Connect App ([read more](https://dev.netatmo.com/apps/createanapp#form))
* At least one Netatmo device

## How to use
```python
# import the API
from netatmoapi import Client
from netatmoapi import Station

# create a client
c = Client(
    "1234567890abcdef12345678", "ABCdefg123456hijklmn7890pqrs", "user@mail", "password"
)

# add a weather station
ws = Station.Weather(c)

# 'getstationsdata()' returns a <requests.Response object>
print(
    ws.getstationsdata("70:ee:50:XX:XX:XX").text
)  # turn it into text using the '.text' attribute
```

## Note
This is **not** in any way an official software made by Netatmo. I've made this purely for personal use and decided to share it to the community.

This is still a very early version and is still missing all the documentation. I would recommend only using this library if you know your way around Python classes. Feel free to edit the code to your needs.