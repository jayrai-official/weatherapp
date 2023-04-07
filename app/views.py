from django.shortcuts import render
from app.weather import get_current_weather_data

# Create your views here.
def home(request):
    u_city =''
    if request.method == 'POST':
        u_city = request.POST['city']
        city = u_city
    else:
        city = 'Ahmedabad'
    api_key = '1cb5fbb878423f70e009dee0fbfb62d9'
    weather_data = get_current_weather_data(api_key, city)

    data = {
        'name': weather_data['name'],
        'c_country':weather_data['sys']['country'],
        'c_temp': round(weather_data['main']['temp']),
        'c_min_temp': weather_data['main']['temp_min'],
        'c_max_temp': round(weather_data['main']['temp_max']),
        'c_feels_like_temp': round(weather_data['main']['feels_like']),
        'c_pressure': weather_data['main']['pressure'],
        'c_humidity': weather_data['main']['humidity'],
        'c_visibility':float(round((weather_data['visibility'])/1000)),
        'c_type' :weather_data['weather'][0]['description'],
    }
    
    return render(request, 'app/index.html', {'data': data})
