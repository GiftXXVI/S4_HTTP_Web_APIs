from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from model import db, migrate, config, Student, Interest
from api.interests import interests_blueprint
from api.students import students_blueprint
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from api.queries import listInterests_resolver, getInterest_resolver


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

query = ObjectType("Query")
query.set_field("listInterests", listInterests_resolver)
query.set_field("getInterest", getInterest_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


@app.errorhandler(404)
def error_404(error):
    return jsonify({
        'success': False,
        'error': error.code,
        'message': error.description
    }), error.code


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


# @app.errorhandler(AuthError)
# def auth_error(error):
#    error_data = error.format()
#    return jsonify({
#        'success': False,
#        'error': error_data['code'],
#        'message': error_data['message']
#    }), error_data['code']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
