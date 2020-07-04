from . import admin
from .. import User, db
import random
import json


@admin.route('/')
def home():
    return 'Admin Home'