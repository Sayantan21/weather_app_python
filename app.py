import requests
from flask import Flask, render_template, request
app = Flask(__name__)


url = "https://api.openweathermap.org/data/2.5/weather"
apikey = "2cd5682b8204d1e16c250776bda23fad"


@app.route("/")
def show_form():
    return render_template("index.html")

@app.route('/weatherapp', methods=["POST"])
def weatherapp():
    city_name = request.form.get("city")
    param = {
        "q":city_name,
        "units":"metric",
        "apikey":apikey
    }
    response = requests.get(url, param)
    return response.json()









if __name__=="__main__":
    app.run(port=5000, debug=True)