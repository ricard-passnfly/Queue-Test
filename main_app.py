from flask import Flask


app = Flask(__name__)


################
# BLUEPRINTS
################

from API.API import api_blueprint
app.register_blueprint(api_blueprint)

app.run()
