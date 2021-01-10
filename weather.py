import requests

def weather(city):
	url="https://www.metaweather.com/api/location/search/?query="+city

	response=requests.get(url)
	wo=response.json()
	if len(wo[0])<1:
		print("Error  city not found..........")
	else:

		woeid=wo[0]["woeid"]
		woeid1=str(woeid)

		url2="https://www.metaweather.com/api/location/"+woeid1+"/"

		response2=requests.get(url2)

		wo2=response2.json()

		date=input("Enter date(YYYY-MM-DD): ")
		f=0

		for i in wo2["consolidated_weather"]:
			if i["applicable_date"]==date:
				weather_state=i["weather_state_name"]
				wind_direction=i["wind_direction_compass"]
				temp=i["the_temp"]
				min_temp=i["min_temp"]
				max_temp=i["max_temp"]
				air_pressure=i["air_pressure"]
				humidity=i["humidity"]
				accuracy=i["predictability"]
				visibility=i["visibility"]
				f=1
				break
			else:
				continue
		if f==1:	
			print("City: "+city+"\n")
			print("Date: "+date+"\n")
			print("Weather State: "+weather_state+"\n")
			print("Wind Direction: "+wind_direction+"\n")
			print("Temparature: "+str(temp)+"C"+"\n")
			print("Minimum Temparature: "+str(min_temp)+"C"+"\n")
			print("Maximum Temparature: "+str(max_temp)+"C"+"\n")
			print("Air Pressure: "+str(air_pressure)+"mBar"+"\n")
			print("Humidity: "+str(humidity)+"%"+"\n")
			print("Visibility: "+str(visibility)+" km"+"\n")
			print("Accuracy: "+str(accuracy)+"%"+"\n")
		else:
			print("Date not found.........")




while (1):

	city=input("Enter the city of your choice: ")
	city.lower()
	weather(city)

	n=int(input("Press '1' to Stop '2' to Continue: "))
	if n==1:
		print("Thankyou for using this weather app........")
		break
	elif n==2:
		continue
	else:
		print("Invalid Choice code ended......")
		break


