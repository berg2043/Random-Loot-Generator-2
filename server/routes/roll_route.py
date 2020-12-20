from flask_restful import Resource
from flask import request
from ..modules.Roller_JSON import roller


class RollRouter(Resource):
  def get(self):
    return roller(int(request.args["cr"]),request.args["group"])
