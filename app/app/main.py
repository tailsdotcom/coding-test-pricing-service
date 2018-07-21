from flask import Flask
from flask_restplus import Api


app = Flask(__name__)
api = Api(app=app,
          title='Tails Pricing Service',
          description='Tails.com interview test implementation',
          version='beta',
          default='pricing',
          default_label='Pricing Services')

# import endpoints in the api module
from .api import api

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
