from flask import Flask

app = Flask(__name__)

from application_poker import routes
