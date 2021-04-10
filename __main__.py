from ip2geotools.databases.noncommercial import DbIpCity
import sys
if sys.argv[1].lower() == "":
	print("Please Specify An Ip Adress!")
elif sys.argv[1].lower() == "help":
	print("iplook <ip> [city/region/country/latitude/longitude/help]")
else:
	response = DbIpCity.get(str(sys.argv[1]), api_key='free')
	try:
		if sys.argv[2].lower() == 'city':
			print("City: " + str(response.city))
		elif sys.argv[2].lower() == 'region':
			print("Region: " + str(response.region))
		elif sys.argv[2].lower() == 'country':
			print("Country: " + str(response.country))
		elif sys.argv[2].lower() == 'latitude':
			print("Latitude: " + str(response.latitude))
		elif sys.argv[2].lower() == 'longitude':
			print("Longitude: " + str(response.longitude))
		elif sys.argv[2].lower() == "help":
			print("iplook <ip> [city/region/country/latitude/longitude/help]")
		else:
			print("command not found")
			print("iplook <ip> [city/region/country/latitude/longitude/help]")
	except IndexError:
		print("City: " + str(response.city))
		print("Region: " + str(response.region))
		print("Country: " + str(response.country))
		print("Latitude: " + str(response.latitude))
		print("Longitude: " + str(response.longitude))
