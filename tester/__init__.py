from flask import Flask
from flask import jsonify

from tester.TestRun import test as t
import Services.getStandards as gstd
import Services.PairingService as ps
import Services.RatingService as rs
import Services.PhraseService as pps
import DatabaseLayer.converseWithDB as cdb

from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] =  headers
            print resp.headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

from bson.json_util import dumps


# @app.route('/' , methods=['GET', 'OPTIONS'])
# @cross_origin()
# def index():
#     return jsonify(t.testFeed())
#
#
# @app.route('/normalizeDB' , methods=['GET', 'OPTIONS'])
# @cross_origin()
# def normalize():
#     return jsonify(t.normalizeDB())
#
#
#
# @app.route('/getColors' , methods=['GET', 'OPTIONS'])
# @cross_origin()
# def getColors():
#     return jsonify(gstd.getColors())
#
#
#
#
# @app.route('/getTypes' , methods=['GET', 'OPTIONS'])
# @cross_origin()
# def getTypes():
#     return jsonify(gstd.getTypes())
#
#
#
# @app.route('/getFeed' , methods=['POST', 'OPTIONS'])
# @cross_origin()
# def getFeed():
#     content = request.json
#     print content
#
#     return jsonify(t.testFeed(content))
#
#
# @app.route('/getFeedFromPhrase' , methods=['POST', 'OPTIONS'])
# @cross_origin()
# def getFeedFromPhrase():
#     content = request.json
#     print content
#     print content["phrase"]
#
#     return jsonify(pps.getPhraseProducts(content))
#
# @app.route('/pairProduct' , methods=['POST', 'OPTIONS'])
# @cross_origin()
# def productPairing():
#     content = request.json
#     print content
#     product = content["product"]
#     gender = content["gender"]
#
#     return jsonify(ps.pairProduct(product, gender))
#
#
# @app.route('/rateProduct' , methods=['POST', 'OPTIONS'])
# @cross_origin()
# def productRating():
#     content = request.json
#     print content
#     record = content["record"]
#     userprefs = content["userprefs"]
#
#     return jsonify(rs.getRatings(record, userprefs))
#

@app.route('/testdb' , methods=['POST', 'OPTIONS'])
@cross_origin()
def testDB():

    return dumps(cdb.getFullData("looksmash_db", "jabong_data"))



