from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}"
    )

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port="8000", debug=True)