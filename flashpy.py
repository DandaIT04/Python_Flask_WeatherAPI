from re import M
from flask import Flask,redirect,url_for,render_template,request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=535ec0b2677a9801f9167982525a5bbf&units=imperial'

        r = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather['temperature'] = round(weather['temperature']/2.4)

        print(weather)

        return render_template('index.html', weather=weather)

    city = 'Singapore'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=535ec0b2677a9801f9167982525a5bbf&units=imperial'

    r = requests.get(url.format(city)).json()

    weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    weather['temperature'] = round(weather['temperature']/2.4)

    print(weather)

    return render_template('index.html', weather=weather) 

if __name__ == '__main__':
    app.run(debug=True,port=9890,use_reloader=False)