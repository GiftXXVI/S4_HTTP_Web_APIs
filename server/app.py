from flask import Flask, redirect, request
from flask_cors import CORS
from flask_migrate import Migrate
from model import db, migrate, config, Student, Interest
from api.interests import interests_blueprint
from api.students import students_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config["SQLALCHEMY_DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    app.config['SECRET_KEY'] = config['SECRET_KEY']
    db.init_app(app)
    migrate = Migrate(app, db)
    return app


app = create_app()
app.register_blueprint(interests_blueprint)
app.register_blueprint(students_blueprint)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization, true')
    response.headers.add(
        'Access-Control-Allow-Methods', 'GET, OPTIONS, PATCH, DELETE, POST')
    return response


@app.errorhandler(404)
def error_404(error):
    message = 'not found'
    return jsonify({
        'success': False,
        'error': 404,
        'message': message.lower()
    }), 404


@app.errorhandler(401)
def error_401(error):
    message = 'unauthorized'
    return jsonify({
        'success': False,
        'error': 401,
        'message': message.lower()
    }), 401


@app.errorhandler(403)
def error_403(error):
    message = 'forbidden'
    return jsonify({
        'success': False,
        'error': 403,
        'message': message.lower()
    }), 401


@app.errorhandler(405)
def error_405(error):
    message = 'not allowed'
    return jsonify({
        'success': False,
        'error': 405,
        'message': message.lower()
    }), 405


@app.errorhandler(422)
def error_422(error):
    message = 'unprocessable'
    return jsonify({
        'success': False,
        'error': 422,
        'message': message.lower()
    }), 422


@app.errorhandler(400)
def error_400(error):
    message = 'bad request'
    return jsonify({
        'success': False,
        'error': 400,
        'message': message.lower()
    }), 400


@app.errorhandler(500)
def error_500(error):
    message = 'server error'
    return jsonify({
        'success': False,
        'error': 500,
        'message': message.lower()
    }), 500


@app.errorhandler(AuthError)
def auth_error(error):
    error_data = error.format()
    return jsonify({
        'success': False,
        'error': error_data['code'],
        'message': error_data['message']
    }), error_data['code']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)