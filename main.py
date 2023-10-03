import python_weather
import sys
import asyncio
import os


async def get_weather(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)

        return print(f'Current weather is {weather.current.kind}, {weather.current.temperature}℃, wind speed is {weather.current.wind_speed} km/h and wind direction is {weather.current.wind_direction} for {weather.current.date} in {str.capitalize(city)}\n'
                     f'\nOther info: \nCurrent visibility: {weather.current.visibility} km\nCurrent humidity: {weather.current.humidity} km/h\nUltraviolet rate: {weather.current.ultraviolet.name}')


async def get_forecast(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        choice = input('Forecast or hourly forecast? 1/2 >> ')
        if choice == '1':
            for forecast in weather.forecasts:
                print(f'Date: {forecast.date}\n'
                      f'Primary temperature: {forecast.temperature}℃\nLowest temperature: {forecast.lowest_temperature}℃\nHighest temperature: {forecast.highest_temperature}℃')

        if choice == '2':
            for forecast in weather.forecasts:
                forecast

            for hour in forecast.hourly:
                print(
                    f'\nTime: {hour.time.hour!r}:{hour.time.minute!r}\nTemperature: {hour.temperature!r}℃\nKind: {hour.description!r}\nFeels like: {hour.feels_like!r}℃\nWind direction: {hour.wind_direction.name!r} or {hour.wind_direction.degrees!r} deg.\nWind speed: {hour.wind_speed!r} km/h\nWind gusts: {hour.wind_gust!r} km/h\nPressure: {hour.pressure!r} hPa\nVisibility: {hour.visibility!r}\nUltraviolet rate: {hour.ultraviolet.name}\n')

if len(sys.argv) == 1:
    print('Welcome to Weaterate!\n'
          '___HELP___\n'
          '     COMMANDS: \n'
          '         -gf: get temperature for next three days and hourly forecast\n'
          '         -gw: get current weather\n'
          '     USE: \n'
          '         python(3) [path to main.py] [city (if city name has spaces, please, make sure that name is in "''")] [command]')

if len(sys.argv) > 1:
    city = sys.argv[1]
    global_choice = sys.argv[2]


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    if len(sys.argv) > 1:
        if global_choice == '-gf':
            loop = asyncio.get_event_loop()
            loop.run_until_complete(get_forecast(city))
            loop.close()
        elif global_choice == '-gw':
            loop = asyncio.get_event_loop()
            loop.run_until_complete(get_weather(city))
            loop.close()
        else:
            print('invalid choice: try -h for help')
