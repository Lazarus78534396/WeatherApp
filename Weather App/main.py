from flask import Flask,render_template,request
import requests

url = 'http://api.weatherstack.com/current?access_key='
access_key = 'aaccd030b6d03fe72f96830021667240&query='

app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template('home.html')
@app.route('/', methods=['POST','GET'])
def weather_page():
    if request.method == 'POST':
        query = str(request.form['city'])

        w=url+access_key+query
        r = requests.get(w).json()
        temp = r['current']['temperature']
        disc = r['current']['weather_descriptions'][0]
        humidity =  r['current']['humidity']
        country = r['location']['country']
        return render_template('home1.html',q=query,c=country, t=temp,d=disc,h=humidity)
    else:
        return render_template('home.html')
if __name__ == '__main__':
    app.run(debug = True)