from os import getenv


def get_config() -> dict:
    conf = dict()
    db_name = getenv('DB_NAME')
    db_user = getenv('DB_USER')
    db_pass = getenv('DB_PASSWD')
    db_host = getenv('DB_HOST')
    db_port = getenv('DB_PORT')
    app_env = getenv('APP_ENV')
    db_credentials = f'{db_user}:{db_pass}'
    db_socket = f'{db_host}:{db_port}'
    conf["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{db_credentials}@{db_socket}/{db_name}'
    if app_env == 'CONTAINER':
        conf["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///data.db'
    conf["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    conf['SECRET_KEY'] = getenv('APP_KEY')
    return conf