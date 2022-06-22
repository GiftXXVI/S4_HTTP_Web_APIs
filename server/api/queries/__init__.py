from model import db,Interest
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def listInterests_resolver(obj, info):
    try:
        interests = [interest.format() for interest in Interest.query.all()]
        payload = {
            "success": True,
            "interests": interests
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getInterest_resolver(obj, info, id):
    try:
        interest = Interest.query.filter(Interest.id==id).format()
        print(interest)
        payload = {
            "success": True,
            "interest": interest
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    print(payload)
    return payload