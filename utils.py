from api.models import People
from flask import jsonify

id = "id"
title = "title"
content = "content"
views = "views"
timestamp = "timestamp"


def queries_to_json(queries):
    store_arr = []
    for qu in queries:
        store_arr.append(qu.to_dict())
    return jsonify(store_arr)


# Filters only values which have matching property value
def EQUAL(property, value):
    if property == id:
        return People.query.filter(People.id == value).all()
    elif property == title:
        return People.query.filter(People.title == value).all()
    elif property == content:
        return People.query.filter(People.content == value).all()
    elif property == views:
        return People.query.filter(People.views == value).all()
    elif property == timestamp:
        return People.query.filter(People.timestamp == value).all()


def NOT(queries):
    final_queries = []
    store = People.query.all()
    for query in store:
        if query not in queries:
            final_queries.append(query)
    return final_queries


def GREATER_THAN(property, value):
    if property == id or property == title or property == content:
        print("Invalid property!")
    elif property == views:
        return People.query.filter(People.views > value)
    elif property == timestamp:
        return People.query.filter(People.timestamp > value)


def LESS_THAN(property, value):
    if property == id or property == title or property == content:
        print("Invalid property!")
    elif property == views:
        return People.query.filter(People.views < value)
    elif property == timestamp:
        return People.query.filter(People.timestamp < value)


def AND(first_queries, second_queries):
    final_queries = []
    for query in first_queries:
        if query in second_queries:
            final_queries.append(query)
    return final_queries


def OR(first_queries, second_queries):
    final_queries = first_queries
    for query in second_queries:
        if query not in final_queries:
            final_queries.append(query)
    return final_queries


def separate_query(query):
    first_end = query.find(")")
    return query[0:first_end + 1], query[first_end+2:]


def apply_query(query):
    start = 0
    end = query.find("(")
    function_name = query[start:end]

    if function_name in ["EQUAL", "GREATER_THAN", "LESS_THAN"]:
        return eval(query)

    elif function_name == "NOT":
        func = query.replace("NOT(", "")
        queries = apply_query(func[:-1])
        return NOT(queries)

    #  combined operator
    elif function_name == "OR" or function_name == "AND":
        # separate the operator into two parts
        first, second = separate_query(query[end + 1:-1])
        first_queries = apply_query(first)
        second_queries = apply_query(second)
        if function_name == "AND":
            return AND(first_queries, second_queries)
        else:
            return OR(first_queries, second_queries)
