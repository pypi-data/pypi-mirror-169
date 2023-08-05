"""
only alive for testing, since unit test do not init app.config.from_object('config.TestConfig')
writes an .env with test config and loads it
"""
import os
from os import path, remove, environ
from dotenv import load_dotenv
from eisenradio.api import api

try:
    from flask import current_app
except ImportError:
    pass

this_script_dir = path.dirname(__file__)


def write_config_test():
    global this_script_dir
    # get root of app, rip off one subdir .go up
    app_root = path.dirname(this_script_dir)
    radio_db_dir = path.join(app_root, 'app_writeable', 'db')

    # Secrets that actually belong to an encrypted vault; ci app encryption
    db_path_test = path.join(radio_db_dir, 'eisenradio_test.db')
    secret_num = '9fc2e5bd8372430fb6a1012af0b51f37'

    list_test = [
        'DATABASE=' + db_path_test,
        'FLASK_ENV=development',
        'DEBUG=True',
        'TESTING=True',
        'SECRET_KEY=' + secret_num
    ]

    remove_config()
    with open(path.join(this_script_dir, '.env'), 'w') as writer:
        for line in list_test:
            writer.write(line + '\n')
        writer.flush()

    load_config_os()
    current_app.config.update(SECRET_KEY=os.environ['SECRET_KEY'],
                              DATABASE=path.abspath(db_path_test),
                              FLASK_ENV=os.environ['FLASK_ENV'],
                              DEBUG=os.environ['DEBUG'],
                              TESTING=os.environ['TESTING'],
                              PYTEST=True
                              )
    print(api.config)
    print('')


def load_config_os(new_path=None):
    global this_script_dir
    if new_path is not None:
        this_script_dir = new_path
    load_dotenv(path.join(this_script_dir, '.env'))


def remove_config(new_path=None):
    global this_script_dir
    if new_path is not None:
        this_script_dir = new_path
    try:
        remove(path.join(this_script_dir, '.env'))
    except OSError:
        pass
