from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from . import auth
from .. import User, db
import json
import jwt
import time


@auth.route('/')
def home():
    return 'Auth Home'


@auth.route("/register", methods=["POST"])
def userRegister():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    contact = request.json["contact"]
    type_of_user = request.json["type_of_user"]

    flag = False

    results = db.session.execute(''' SELECT email from users ''')

    for result in results:
        if email == result.email:
            flag = True

    if flag:
        return json.dumps({"message": "Email Already Exists!", "error": True})

    else:
        user = User(
            name=name,
            contact=contact,
            email=email,
            password=password,
            type_of_user=type_of_user
        )
        db.session.add(user)
        db.session.commit()

        return json.dumps({
            "message": "Created Account Successfully!",
            "error": False
        })


# User - Login
@auth.route("/login", methods=["POST"])
def userLogin():
    email = request.json["email"]
    password = request.json["password"]
    type_of_user = request.json["type_of_user"]

    flag = False

    if type_of_user == "user":
        results = db.session.execute(
            ''' SELECT * from users where type_of_user='user'; '''
        )

    elif type_of_user == "owner":
        results = db.session.execute(
            ''' SELECT * from users where type_of_user='owner'; '''
        )

    elif type_of_user == "admin":
        results = db.session.execute(
            ''' SELECT * from users where type_of_user='admin'; '''
        )

    data = []
    for result in results:
        if email == result.email:
            if password == result.password:

                temp_dict = {}
                temp_dict["name"] = result.name
                temp_dict["email"] = result.email
                temp_dict["contact"] = result.contact
                temp_dict["type_of_user"] = result.type_of_user
                data.append(temp_dict)
                flag = True

    if flag:
        payload = {
            "data": data,
            "status": "Logged In",
            "session_expiry": time.time() + 7200
        }

        key = "masai"

        encode = jwt.encode(payload, key)

        return json.dumps({
            "token": encode.decode(),
            "message": "Login Successful!",
            "error": False
        })

    else:
        return json.dumps({"message": "Login Failed!", "error": True})


# User Token Authentication
@auth.route("/token_validate", methods=['POST'])
def userToken():
    token = request.json["token"]

    key = "masai"

    data = jwt.decode(token, key)

    current_time = time.time()

    if data["session_expiry"] < current_time:
        return json.dumps({
            "error": True,
            "message": "Invalid Token"
        })
    else:
        return json.dumps({
            "error": False,
            "message": "Valid Token"
        })
