from . import owner
from .. import User, db
import random
import json


@owner.route('/')
def home():
    return 'Owner Home'
