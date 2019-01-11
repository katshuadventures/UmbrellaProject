from flask import Flask, render_template, url_for
from flask import request, redirect
from weather import Weather, Unit

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/')
def mainpage_url():
	return url_for('mainpage.html')

@app.route('/mainpage.html', methods = ['POST'])
def mainpage():
	if request.method == 'POST':
		degree_sign= u'\N{DEGREE SIGN}'
		weather = Weather(unit=Unit.FAHRENHEIT)
		city = request.form['city']
		location = weather.lookup_by_location(city)
		place = location.location
		forecasts = location.forecast
		condition = location.condition
		umbrella_codes = [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 35, 37, 38, 39, 40, 45, 47]
		cloudy_codes = [20, 23, 24, 26, 27, 28, 29, 30, 44]
		sunny_codes = [31, 32, 33, 34, 36]
		snow_codes = [7, 13, 14, 15, 16, 17, 18, 25, 41, 42, 43, 46]
		if int(condition.code) in umbrella_codes:
			today_message = 'Grab your umbrella'
		else:
			today_message = "No umbrella needed"
		if place.region:
			city = place.city + ', ' + place.region
		else:
			city = place.city + ', ' + place.country
		def day(forecast):
			months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
			forecast_month = str(months[forecast.date[3:6]])
			forecast_date = forecast.date[:2]
			return forecast.day + ' ' + forecast_month + '/' + forecast_date
		def image(forecast):
			code = int(forecast.code)
			if code in umbrella_codes:
				image = "https://raw.githubusercontent.com/katshuadventures/UmbrellaProject/master/umbrella%20copy.gif"
				alt = "Raining"
			elif code in cloudy_codes:
				image = "https://raw.githubusercontent.com/katshuadventures/UmbrellaProject/master/cloudy%20copy.gif"
				alt = "Cloudy"
			elif code in sunny_codes:
				image = "https://raw.githubusercontent.com/katshuadventures/UmbrellaProject/master/sun%20copy.gif"
				alt = "Sunny"
			elif code in snow_codes:
				image = "https://raw.githubusercontent.com/katshuadventures/UmbrellaProject/master/Snowflake.gif"
				alt = "Snowing"
			else:
				image = "https://raw.githubusercontent.com/katshuadventures/UmbrellaProject/master/severeweather.png"
				alt = "Severe Weather"
			return [image, alt]
		def temp(forecast):
			return str(forecast.low) + degree_sign + ' - ' + str(forecast.high) + degree_sign + '\n' + forecast.text
		def need_umbrella(forecast):
			message = 'Umbrella \u2717'
			if int(forecast.code) in umbrella_codes:
				message = "Umbrella \u2705"
			return message

		return render_template('mainpage.html', city = city, umbrellaneed = today_message, forecast = condition.text, mainimage = image(condition)[0],
			day1 = day(forecasts[0]), image1 = image(forecasts[0])[0], alt1 = image(forecasts[0])[1], temp1 = temp(forecasts[0]), umbrella1 = need_umbrella(forecasts[0]),
			day2 = day(forecasts[1]), image2 = image(forecasts[1])[0], alt2 = image(forecasts[1])[1], temp2 = temp(forecasts[1]), umbrella2 = need_umbrella(forecasts[1]),
			day3 = day(forecasts[2]), image3 = image(forecasts[2])[0], alt3 = image(forecasts[2])[1], temp3 = temp(forecasts[2]), umbrella3 = need_umbrella(forecasts[2]),
			day4 = day(forecasts[3]), image4 = image(forecasts[3])[0], alt4 = image(forecasts[3])[1], temp4 = temp(forecasts[3]), umbrella4 = need_umbrella(forecasts[3]),
			day5 = day(forecasts[4]), image5 = image(forecasts[4])[0], alt5 = image(forecasts[4])[1], temp5 = temp(forecasts[4]), umbrella5 = need_umbrella(forecasts[4]),
			day6 = day(forecasts[5]), image6 = image(forecasts[5])[0], alt6 = image(forecasts[5])[1], temp6 = temp(forecasts[5]), umbrella6 = need_umbrella(forecasts[5]),
			day7 = day(forecasts[6]), image7 = image(forecasts[6])[0], alt7 = image(forecasts[6])[1], temp7 = temp(forecasts[6]), umbrella7 = need_umbrella(forecasts[6]),
			)

@app.route('/index.html')
def home_url():
	return redirect('/')


if __name__ == '__main__':
	app.run(debug = True)