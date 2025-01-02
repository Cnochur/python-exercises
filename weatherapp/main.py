import requests, time
import os

api_key = os.environ['WEATHER_API']
base_url = f'http://api.openweathermap.org/data/2.5/weather?q='
curr_time = time.strftime("%a, %d %b %Y %H:%M:%S")

def get_weather_data():

    # VALIDATING INPUT
    try:
        city_name = input("\nEnter city name (or type 'quit' to exit): ")

        if city_name == "quit":
            print("Goodbye....")
            quit()

        url = f'{base_url}{city_name}&appid={api_key}&units=metric'

        # VALIDATING RESPONSE
        response = requests.get(url)
        if response.status_code != 200:
            print("Error!!")
            return None
        
        # VALIDATING DATA
        data = response.json()
        if data.get("cod") != 200:
            print("Error!!")

        return data

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except ValueError as error:
        print(f"Value error: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def get_results(data):

	name = data["name"]
	weather = data["weather"][0]["main"]
	weather_desc = data["weather"][0]["description"]
	temp = data["main"]["temp"]
	feels_like = data["main"]["feels_like"]

	return name, weather, weather_desc, temp, feels_like

def main():

	while True:

		print("\n-=_= WeatherApp =_=_")

		data = get_weather_data()
		weather_info = get_results(data)

		print('\n---------------------------------\n================================')
		print(f"\n\nLocation: {weather_info[0]}\nToday: {weather_info[1]} - {weather_info[2]}\nTemperature: {weather_info[3]}\nFeels like: {weather_info[4]}\n")
		print(f'\n================================\n{curr_time}\n---------------------------------\n')

if __name__ == "__main__":
	main()
