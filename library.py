import json
from bson.decimal128 import Decimal128
from bson.objectid import ObjectId
from datetime import datetime, date, time
from flask import Response


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, time):
            return obj.isoformat()
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, Decimal128):
            return float(obj.to_decimal())
        return json.JSONEncoder.default(self, obj)


def jsonify(data):
    data = json.dumps(data, cls=APIEncoder)
    data = data.replace(" NaN", " null")
    return Response(data, mimetype="application/json")