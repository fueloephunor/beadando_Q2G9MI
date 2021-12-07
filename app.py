""" Import """
from flask import Flask
from hotel_controller import hotel_api

app = Flask(__name__)
app.register_blueprint(hotel_api)


@app.route("/")
def my_webpage():
    """ my webpage """
    return "<h1>Welcome to my hotel service webpage</h1>"


if __name__ == "__main__":
    print("Hello")

app.run(port=5000, debug=False)