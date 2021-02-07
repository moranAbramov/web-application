from api import db
from api.models import People


OPPOSITE_FUNCTION = {"EQUAL": "NOT_EQUAL", "GREATER_THAN": "LESS_THAN", "LESS_THAN": "GREATER_THAN"}


id = "id"
title = "title"
content = "content"
views = "views"
timestamp = "timestamp"


def EQUAL(property, value):
    if property == id:
        People.query.filter(People.id != value).delete()
    elif property == title:
        People.query.filter(People.title != value).delete()
    elif property == content:
        People.query.filter(People.content != value).delete()
    elif property == views:
        People.query.filter(People.views != value).delete()
    elif property == timestamp:
        People.query.filter(People.timestamp != value).delete()
    db.session.commit()


def NOT_EQUAL(property, value):
    if property == id:
        People.query.filter(People.id == value).delete()
    elif property == title:
        People.query.filter(People.title == value).delete()
    elif property == content:
        People.query.filter(People.content == value).delete()
    elif property == views:
        People.query.filter(People.views == value).delete()
    elif property == timestamp:
        People.query.filter(People.timestamp == value).delete()
    db.session.commit()


def GREATER_THAN(property, value):
    if property == id or property == title or property == content:
        print("Invalid property!")
    elif property == views:
        People.query.filter(People.views < value).delete()
    elif property == timestamp:
        People.query.filter(People.timestamp < value).delete()
    db.session.commit()


def LESS_THAN(property, value):
    if property == id or property == title or property == content:
        print("Invalid property!")
    elif property == views:
        People.query.filter(People.views > value).delete()
    elif property == timestamp:
        People.query.filter(People.timestamp > value).delete()
    db.session.commit()


# in order to evaluate a and b when performing eval(AND(a, b))
def AND(a, b):
    return None


def apply_query(query):
    start = 0
    end = query.find("(")
    function_name = query[start:end]
    if function_name in ["EQUAL", "GREATET_THAN", "LESS_THAN", "AND", "NOT_EQUAL"]:
        eval(query)
    elif function_name == "NOT":
        func = query.replace("NOT(", "")
        end = func.find("(")
        function_name = func[start:end]
        new_method = func.replace(function_name, OPPOSITE_FUNCTION[function_name])
        apply_query(new_method[:-1])
    # TODO
    elif function_name == "OR":
        return None
