from model import db,Interest

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