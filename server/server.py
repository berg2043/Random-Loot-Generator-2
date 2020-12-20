import flask
import flask_restful
from .routes.roll_route import RollRouter

# Globals
app = flask.Flask(__name__,static_folder='./../public')
api = flask_restful.Api(app)

# Routes
api.add_resource(RollRouter, '/api/roll')

# Static
@app.route('/')
def home():
  return app.send_static_file('index.html')