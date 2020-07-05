from . import user
from .. import User, db, User_Property_Rel
import random
import json


@user.route('/')
def home():
    return 'User Home'


# show properties
@user.route('/show_property')
def show_property():
    try:
        results = db.session.execute(
            ''' SELECT * FROM property WHERE isAvailable = 1 '''
        )
        data = []
        for result in results:
            temp_dict = {}
            temp_dict["id"] = result.id
            temp_dict["address"] = result.address
            temp_dict["city"] = result.city
            temp_dict["state"] = result.state
            temp_dict["zip_code"] = result.zip_code
            temp_dict["isAvailable"] = result.isAvailable
            temp_dict["created_at"] = result.created_at
            temp_dict["area"] = result.area
            temp_dict["number_bedrooms"] = result.number_bedrooms
            temp_dict["amenities"] = result.amenities
            temp_dict["furnish"] = result.furnish
            temp_dict["owner_id"] = result.owner_id
            data.append(temp_dict)

        return json.dumps({"data": data}, default=str)
    except:
        return json.dumps({
            "message": "Some unknown error occured!",
        })


# user request to owner
@user.route('/<user_id>/<property_id>/<owner_id>')
def select_property(user_id, property_id, owner_id):
    status = "enquiry"
    try:
        prop_user_rel = User_Property_Rel(
            user_id=int(user_id),
            property_id=int(property_id),
            owner_id=int(owner_id),
            status=status
        )
        db.session.add(prop_user_rel)
        db.session.commit()

        results = db.session.execute(
            ''' SELECT * FROM users WHERE id = "%d" ''' % (int(owner_id))
        )
        data = []
        for result in results:
            temp_dict = {}
            temp_dict["name"] = result.name
            temp_dict["contact"] = result.contact
            temp_dict["email"] = result.email
            data.append(temp_dict)

        return json.dumps({"data": data}, default=str)
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


# check request status
@user.route('/status/<user_id>/')
def status(user_id):
    results = db.session.execute(
        '''SELECT * FROM property_user_rel WHERE id = "%d"''' % (int(user_id))
    )
    data = []
    for result in results:
        temp_dict = {}
        temp_dict["property_id"] = result.property_id
        temp_dict["owner_id"] = result.owner_id
        temp_dict["status"] = result.status
        data.append(temp_dict)

    return json.dumps({"data": data}, default=str)
