from flask_restful import Resource
from flask import request
from ..modules.Roller_JSON import roller
import traceback


class RollRouter(Resource):
  def get(self):
    try:
      res = roller(int(request.args["cr"]),request.args["group"])
      return res
    except:
      print('-------Roller Get Error---------')
      traceback.print_exc()
      print(request.args)
      return {}, 500
