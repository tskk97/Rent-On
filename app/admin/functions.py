from flask import request
from . import admin
from .. import User, db, Property, User_Property_Rel
import random
import json


@admin.route('/')
def home():
    return 'Admin Home'


# user edit
@admin.route("/edit_user", methods=["POST"])
def user_edit():
    user_id = int(request.json["user_id"])
    name = request.json["name"]
    email = request.json["email"]
    contact = request.json["contact"]
    type_of_user = request.json["type_of_user"]

    try:
        if type_of_user == "admin":
            obj = User.query.filter_by(id=user_id).first()
            obj.name = name
            obj.email = email
            obj.contact = contact
            db.session.commit()
            return json.dumps({
                "message": "User Updated Successfully!",
            })
        else:
            return json.dumps({
                "message": "Only admin can edit the user!",
            })
    except TypeError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except ValueError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except:
        return json.dumps({
            "message": "Some unknown error occured!",
        })


# owner edit
@admin.route("/edit_owner", methods=["POST"])
def owner_edit():
    owner_id = int(request.json["owner_id"])
    name = request.json["name"]
    email = request.json["email"]
    contact = request.json["contact"]
    type_of_user = request.json["type_of_user"]

    try:
        if type_of_user == "admin":
            obj = User.query.filter_by(id=owner_id).first()
            obj.name = name
            obj.email = email
            obj.contact = contact
            db.session.commit()
            return json.dumps({
                "message": "Owner Updated Successfully!",
            })
        else:
            return json.dumps({
                "message": "Only admin can edit the Owner!",
            })
    except TypeError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except ValueError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except:
        return json.dumps({
            "message": "Some unknown error occured!",
        })


# total owners
@admin.route("/owners")
def owners():
    try:
        results = db.session.execute(''' SELECT * FROM users WHERE type_of_user = "owner" ''')
        data = []
        for result in results:
            temp_dict = {}
            temp_dict["owner_id"] = result.id
            temp_dict["name"] = result.name
            temp_dict["email"] = result.email
            temp_dict["contact"] = result.contact
            temp_dict["type_of_user"] = result.type_of_user
            data.append(temp_dict)

        return json.dumps({"data": data}, default=str)
    except:
        return 'Some unknown error occured!'


# total users
@admin.route("/users")
def users():
    try:
        results = db.session.execute(''' SELECT * FROM users WHERE type_of_user = "user" ''')
        data = []
        for result in results:
            temp_dict = {}
            temp_dict["user_id"] = result.id
            temp_dict["name"] = result.name
            temp_dict["email"] = result.email
            temp_dict["contact"] = result.contact
            temp_dict["type_of_user"] = result.type_of_user
            data.append(temp_dict)

        return json.dumps({"data": data}, default=str)
    except:
        return 'Some unknown error occured!'


# delete user
@admin.route('/delete_user', methods=['POST'])
def user_delete():
    user_id = int(request.json['user_id'])
    type_of_user = request.json['type_of_user']

    try:
        if type_of_user == 'admin':

            results = db.session.execute(''' SELECT * from property_user_rel WHERE user_id = "%d" ''' % (user_id))

            for result in results:
                if user_id == result.user_id:
                    property_user_rel = User_Property_Rel.query.filter_by(user_id=user_id).first_or_404(description='There is no data with id {}'.format(user_id))
                    db.session.delete(property_user_rel)
                    db.session.commit()
                else:
                    pass

            user = User.query.filter_by(id=user_id).first_or_404(description='There is no data with id {}'.format(user_id))
            db.session.delete(user)
            db.session.commit()
            return json.dumps({
                "message": "User Deleted Successfully!",
            })
        else:
            return json.dumps({
                "message": "Only admin can delete the users!",
            })
    except TypeError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except ValueError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except:
        return json.dumps({
            "message": "Some unknown error occured!",
        })


# delete owner
@admin.route('/delete_owner', methods=['POST'])
def owner_delete():
    owner_id = int(request.json['owner_id'])
    type_of_user = request.json['type_of_user']

    try:
        if type_of_user == 'admin':

            results = db.session.execute(''' SELECT * from property_user_rel WHERE owner_id = "%d" ''' % (owner_id))

            for result in results:
                if owner_id == result.owner_id:
                    property_user_rel = User_Property_Rel.query.filter_by(owner_id=owner_id).first_or_404(description='There is no data with id {}'.format(owner_id))
                    db.session.delete(property_user_rel)
                    db.session.commit()
                else:
                    pass

            prop = Property.query.filter_by(owner_id=owner_id).first_or_404(description='There is no data with id {}'.format(owner_id))
            db.session.delete(prop)
            db.session.commit()

            owner = User.query.filter_by(id=owner_id).first_or_404(description='There is no data with id {}'.format(owner_id))
            db.session.delete(owner)
            db.session.commit()
            return json.dumps({
                "message": "Owner Deleted Successfully!",
            })
        else:
            return json.dumps({
                "message": "Only admin can delete the Owner!",
            })
    except TypeError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except ValueError:
        return json.dumps({
            "message": "Please enter an integer value",
        })
    except:
        return json.dumps({
            "message": "Some unknown error occured!",
        })
