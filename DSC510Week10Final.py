# DSC 510
# Week 10
# Programming Assignment 10.1 Final Project
# Author Monica Santana
# 8/7/2023
import requests

# OpenWeatherMap api call
api_url = 'https://api.openweathermap.org/data/2.5/weather?'
# OpenWeatherMap personal api key
api_key = '757899d190231671df266789a05141ef'


# function for user to lookup by city and state name
def city_lookup():
    city_name = input('Please enter the city, state name for your forecast: ')\
        .lower()
# api call for city name and converting units from Kelvin to Fahrenheit
    city_url = api_url + 'appid=' + api_key + '&q=' + city_name +\
        '&units=imperial'
# try blocks to establish connections to webservice and user indication if error
    try:
        response = requests.get(city_url)
    except requests.HTTPError:
        print('There was an HTTP error')
    except requests.ConnectionError:
        print('There was a connection error')
    else:
        resp_json = response.json()
        format_weather(resp_json)


# function for user to lookup by zip code
def zipcode_lookup():
    zipcode_num = input('Please enter zip code for your weather forecast: ')
# api call for zip code and converting units from Kelvin to Fahrenheit
    zip_url = api_url + 'appid=' + api_key + '&q=' + zipcode_num + \
        '&units=imperial'
# try blocks to establish connections to webservice and user indication if error
    try:
        response = requests.get(zip_url)
    except requests.HTTPError:
        print('There was an HTTP error')
    except requests.ConnectionError:
        print('There was a connection error')
    else:
        resp_json = response.json()
        format_weather(resp_json)


# function to display weather forecast in a readable format for the user
def format_weather(resp_json):
    location_name = resp_json['name']
    location_country = resp_json['sys']['country']
    current_temp = resp_json['main']['temp']
    feels_like = resp_json['main']['feels_like']
    temp_max = resp_json['main']['temp_max']
    temp_min = resp_json['main']['temp_min']
    sky_condition = resp_json['weather'][0]['main']
    sky_description = resp_json['weather'][0]['description']
    current_pressure = resp_json['main']['pressure']
    current_humidity = resp_json['main']['humidity']

    print("Current Forecast for", location_name, location_country)
    print('{:25}{:25}'.format('Category', 'Status'))
    print('----------------------------------')
    print(f'Temperature              {current_temp}', '°F')
    print(f'Feels Like               {feels_like}', '°F')
    print(f'High                     {temp_max}', '°F')
    print(f'Low                      {temp_min}', '°F')
    print(f'Condition                {sky_condition}')
    print(f'Description              {sky_description}')
    print(f'Pressure                 {current_pressure}', 'hPa')
    print(f'Humidity                 {current_humidity}' '%')
    print('-----------------------------------')


def main():
    # while loop to allow user to run the program as many times as needed
    cont = 'yes'
    while cont.lower() == 'yes':
        city_or_zip = input('Do you want to use a city,state or zipcode for '
                            'the weather? If city type "1", zipcode type "2". ')
    # if statements and try blocks to catch bad user input for keys and values
        if city_or_zip == '1':
            try:
                city_lookup()
            except (KeyError, ValueError):
                print('That city/state was not found, please enter valid names')

        elif city_or_zip == '2':
            try:
                zipcode_lookup()
            except (KeyError, ValueError):
                print('Please enter a valid zipcode')

        else:
            print('Please type "1" or "2"')

    # if statement to allow user to press any key to quit the program
        cont = input('Do you want another forecast? Type "yes" or press '
                     'any key to quit: ')
        if cont == 'no':
            break


if __name__ == '__main__':
    main()
