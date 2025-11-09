from flask import jsonify, make_response
from werkzeug.http import HTTP_STATUS_CODES


# API request errors
# default message
def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    return make_response(jsonify(payload), status_code)


# bad request
def bad_request(message):
    return error_response(400, message)


# unauthorized request
def unauthenticated(message):
    return error_response(401, message)


# forbidden request
def unauthorized(message):
    return error_response(403, message)


# too many request
def ratelimited(message):
    return error_response(429, message)


# redirect request
def conflict(message):
    return error_response(409, message)