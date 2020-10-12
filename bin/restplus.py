import logging
import traceback

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version='1.0', title='API Demo',
          description='A simple demo to url analizing')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not True:
        return {'message': message}, 500

