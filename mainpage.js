//var shiftWindow = function() { scrollBy(0, -50) };
//if (location.hash) shiftWindow();
//window.addEventListener("hashchange", shiftWindow);

var shiftWindow = function() { scrollBy(0, -180) };
if (location.hash) shiftWindow();
window.addEventListener("hashchange", shiftWindow);

function yahooWeather() {
	window.open("https://www.yahoo.com/news/weather/");
}