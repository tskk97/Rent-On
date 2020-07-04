from . import user
from .. import User, db
import random
import json


@user.route('/')
def home():
    return 'User Home'
