import requests
from flask import Flask, render_template, request
from json import dumps
app = Flask(__name__)

#test comment
url = "https://api.openweathermap.org/data/2.5/weather"
apikey = "2cd5682b8204d1e16c250776bda23fad"


# @app.route("/")
def show_form():
    # return render_template("index.html")
    pass

@app.route('/', methods=["GET","POST"])
def weatherapp():
    if request.method == "GET":
        return render_template("index.html")
    else:
        city_name = request.form.get("city")
        param = {
            "q":city_name,
            "units":"metric",
            "apikey":apikey
        }
        response = requests.get(url, param)
        if response.status_code >= 200 and response.status_code<300:
            data = response.json()
            t = data['main']
            my_data={}
            my_data['temp'] = t['temp']
            my_data["city_name"] = data['name']
            return render_template('index.html', data=my_data)
        else:
            return render_template('index.html', error="City Name Not Found")









if __name__=="__main__":
    app.run(port=5000, debug=True)
