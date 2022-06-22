from flask import Flask, Blueprint, request, abort, jsonify
from model import db, Interest
from sqlalchemy.exc import SQLAlchemyError
from flask_cors import CORS

interests_blueprint = Blueprint('interests_blueprint', __name__)

cors = CORS(
    interests_blueprint,
    resources=r'*',
    origins=r'*',
    methods=['OPTIONS','PATCH'])


@interests_blueprint.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    #response.headers['Access-Control-Allow-Methods'] = 'OPTIONS' #OPTIONS, PATCH, PUT, DELETE
    #response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@interests_blueprint.route('/interests', methods=['GET'])
def view_interests(limit=5, offset=0):
    interests = Interest.query.order_by(
        Interest.id.desc()).limit(limit).offset(offset).all()
    interests_f = [interest.format() for interest in interests]
    return jsonify({
        'success': True,
        'interests': interests_f,
        'num_interests': len(interests_f)
    })


@interests_blueprint.route('/interests/<int:interest_id>', methods=['GET'])
def get_interest(interest_id):
    interest = Interest.query.filter(
        Interest.id == interest_id).one_or_none()
    if interest is not None:
        interest_f = [interest.format()]
        return jsonify({
            'success': True,
            'modified': interest_id,
            'interests': interest_f,
            'num_interests': 1
        })
    else:
        abort(404)


@interests_blueprint.route('/interests', methods=['POST'])
def create_interest():
    data = request.get_json()
    if len(data) > 0:
        name = data.get('name', None)
        if name is not None:
            interest = Interest(name=name)
            success = False
            try:
                interest.add()
                interest.commit()
                interest.refresh()
                success = True
            except SQLAlchemyError:
                interest.rollback()
            finally:
                interest.close()
                if success:
                    return jsonify({
                        'success': True,
                        'created': interest.id,
                        'interests': [interest.format()],
                        'num_interests': 1
                    })
                else:
                    abort(500)
        else:
            abort(400)
    else:
        abort(400)


@interests_blueprint.route('/interests/<int:interest_id>', methods=['PATCH'])
def update_interest(interest_id):
    data = request.get_json()
    if len(data) > 0:
        name = data.get('name', None)
        if name is not None:
            interest = Interest.query.filter(
                Interest.id == interest_id).one_or_none()
            if interest is not None:
                success = False
                try:
                    interest.name = name
                    interest.commit()
                    success = True
                except SQLAlchemyError:
                    interest.rollback()
                finally:
                    interest_f = [interest.format()]
                    interest.close()
                    if success:
                        return jsonify({
                            'success': True,
                            'modified': interest_id,
                            'interests': interest_f,
                            'num_interests': 1
                        })
                    else:
                        abort(500)
            else:
                abort(400)
        else:
            abort(500)
    else:
        abort(500)


@interests_blueprint.route('/interests/<int:interest_id>', methods=['DELETE'])
def delete_interest(interest_id):
    interest = Interest.query.filter(
        Interest.id == interest_id).one_or_none()
    if interest is not None:
        success = False
        try:
            interest.delete()
            interest.commit()
            success = True
        except SQLAlchemyError:
            interest.rollback()
        finally:
            interest.close()
        if success:
            return jsonify({
                'success': True,
                'deleted': interest_id
            })
        else:
            abort(500)
    else:
        abort(400)
