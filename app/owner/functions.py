from . import owner
from .. import User, db, Property
import random
import json
import time
from flask import Flask
from flask import request
from flask_mysqldb import MySQL


@owner.route('/')
def home():
    return 'Owner Home'


# add property
@owner.route('/add_property', methods=["POST"])
def property_add():
    address = request.json["address"]
    city = request.json["city"]
    state = request.json["state"]
    zip_code = request.json["zip_code"]
    created_at = time.strftime('%Y-%m-%d %H:%M:%S')
    area = request.json["area"]
    number_bedrooms = request.json["number_bedrooms"]
    amenities = request.json["amenities"]
    furnish = request.json["furnish"]
    isAvailable = int(request.json["isAvailable"])
    owner_id = int(request.json["owner_id"])

    try:
        property_ = Property(
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            created_at=created_at,
            area=area,
            number_bedrooms=number_bedrooms,
            amenities=amenities,
            furnish=furnish,
            isAvailable=isAvailable,
            owner_id=owner_id
        )
        db.session.add(property_)
        db.session.commit()

        return json.dumps({
            "message": "Added Property Successfully!",
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


# delete property
@owner.route('/delete_property', methods=['POST'])
def property_delete():
    property_id = int(request.json['property_id'])
    type_of_user = request.json['type_of_user']

    try:
        if type_of_user == 'owner' or type_of_user == 'admin':
            prop = Property.query.filter_by(id=property_id).first_or_404(description='There is no data with id {}'.format(property_id))
            db.session.delete(prop)
            db.session.commit()
            return json.dumps({
                "message": "Property Deleted Successfully!",
            })
        else:
            return json.dumps({
                "message": "Only owner can delete the Property!",
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


# edit property
@owner.route("/edit_property", methods=["POST"])
def property_edit():
    property_id = int(request.json['property_id'])
    type_of_user = request.json['type_of_user']
    address = request.json["address"]
    city = request.json["city"]
    state = request.json["state"]
    zip_code = request.json["zip_code"]
    created_at = time.strftime('%Y-%m-%d %H:%M:%S')
    area = request.json["area"]
    number_bedrooms = request.json["number_bedrooms"]
    amenities = request.json["amenities"]
    furnish = request.json["furnish"]
    isAvailable = int(request.json["isAvailable"])
    owner_id = int(request.json["owner_id"])

    try:
        if type_of_user == "owner" or type_of_user == "admin":
            obj = Property.query.filter_by(id=property_id).first()
            obj.address = address
            obj.city = city
            obj.state = state
            obj.zip_code = zip_code
            obj.created_at = created_at
            obj.area = area
            obj.number_bedrooms = number_bedrooms
            obj.amenities = amenities
            obj.furnish = furnish
            obj.isAvailable = isAvailable
            obj.owner_id = owner_id
            db.session.commit()
            return json.dumps({
                "message": "Property Updated Successfully!",
            })
        else:
            return json.dumps({
                "message": "Only owner can delete the Property!",
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
