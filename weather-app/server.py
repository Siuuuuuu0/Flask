from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
from translations import translations
from logger import logger, wrapper

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
@wrapper
def get_weather():
    city = request.args.get('city')

    language = request.args.get('language')

    if not bool(city.strip()):
        city = "Moscow"

    weather_data = get_current_weather(language, city)

    logger(language, city)

    if not weather_data["cod"]==200:
        return render_template("city-not-found.html")

    return render_template(
        "weather.html", 
        title = weather_data["name"], 
        status=weather_data["weather"][0]["description"].capitalize(), 
        temp=f"{weather_data['main']['temp']:.1f}", 
        feels_like=f"{weather_data['main']['feels_like']:.1f}", 
        weather_trans=translations[language]['weather'], 
        feels_like_trans=translations[language]['feels_like'], 
        and_trans=translations[language]['and']
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)