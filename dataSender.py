import subprocess
import json 



# temperature_token = "WYJBKxxxxj9V4a9irpW"
# humidity_token = "IG4D3bxxxxODWZs6CCQM"
# pressure_token = "mynhxxxxOcisM4VND"
# lux_token = "kJnGiMBSxxxxYuWC9j"
# ambient_temperature_token = "rGK8Fxxxx9cDDPQ9IFw"
# moisture_token="PDCq94xxx2FtrC8Ep"
# link ="https://demo.thingsboard.io"


temperature_token = "pDToxxtbmrUucxVza8p5"
humidity_token = "Kt7d6TxxUYctrr6COhL"
pressure_token = "9Slyxxvr101h7Wjp0B"
lux_token = "ENG6uupKvrvLxxAPSwp"
ambient_temperature_token = "pDTosrtxxxVza8p5"
moisture_token="siJMKHNPxxx8Xk8Fa5s1XhE"
 
link = "http://104.148.xxx.203:8080/devices"




with open("inputs.json") as json_file:

	k = json.load(json_file)
	for p in k['data']:
		# k="curl -v -X POST -d \"{\"ts\":"+str(p["timestamp"])+", \"values\":{\"temrrrrrrature\":\""+str(p['value'])+"\"}}\" https://demo.thingsboard.io/api/v1/"+str(temperature_token)+"/telemetry --header \"Content-Type:application/json\""

		k="curl -v -X POST -d \"{\"ts\":1234567, \"values\":{\"key1\":\"1223\", \"key2\":\"232323\"}}\" "+str(p['value'])+"/api/v1/"+str(temperature_token)+"/telemetry --header \"Content-Type:application/json\""
		subprocess.call(k, shell=True)
		
		
	# '''			
		if(p['type'] == "temperature"):
			print(" --------------------------------------- Temperature ==============================")
			# print(p["value"])
			# print(p["timestamp"])			
			k="curl -v -X POST -d \"{\"ts\":"+str(p["timestamp"])+", \"values\":{\"Temperature\":\""+str(p['value'])+"\"}}\" "+str(link)+"/api/v1/"+str(temperature_token)+"/telemetry --header \"Content-Type:application/json\""
			subprocess.call(k, shell=True)
                                                                                            
		
		elif(p['type'] == "pressure"):
			# print(p["value"])
			# print(p["timestamp"])			
			print(" --------------------------------------- Pressure ==============================")
			pre = int(p['value'])/80
			k="curl -v -X POST -d \"{\"ts\":"+str(p["timestamp"])+", \"values\":{\"Pressure\":\""+str(pre)+"\"}}\" "+str(link)+"/api/v1/"+str(pressure_token)+"/telemetry --header \"Content-Type:application/json\""
			subprocess.call(k, shell=True)
		
		elif(p['type'] == "lux"):
			# print(p["value"])
			# print(p["timestamp"])			
			print(" --------------------------------------- LUX ==============================")

			k="curl -v -X POST -d \"{\"ts\":"+str(p["timestamp"])+", \"values\":{\"LUX\":\""+str(p['value'])+"\"}}\" "+str(link)+"/api/v1/"+str(lux_token)+"/telemetry --header \"Content-Type:application/json\""
			subprocess.call(k, shell=True)
	
		elif(p['type'] == "humidity"):
			# print(p["value"])
			# print(p["timestamp"])			
			print("  --------------------------------------- Humidity ==============================")

			k="curl -v -X POST -d \"{\"ts\":"+str(p["timestamp"])+", \"values\":{\"Humidity\":\""+str(p['value'])+"\"}}\""+str(link)+"/api/v1/"+str(humidity_token)+"/telemetry --header \"Content-Type:application/json\""
			subprocess.call(k, shell=True)
		
		elif(p['type'] == "ambient_temperature"):
			# print(p["value"])
			# print(p["timestamp"])		
			print(" --------------------------------------- Ambient Temperature ==============================")
			
			k="curl -v -X POST -d \"{\"ts\":"+str(p["timestamp"])+", \"values\":{\"Ambient_Temperature\":\""+str(p['value'])+"\"}}\" "+str(link)+"/api/v1/"+str(ambient_temperature_token)+"/telemetry --header \"Content-Type:application/json\""
			subprocess.call(k, shell=True)
	
		elif(p['type'] == "moisture"):
			# print(p["value"])
			# print(p["timestamp"])		
			print(" --------------------------------------- Moisture ==============================")
			
			k="curl -v -X POST -d \"{\"ts\":"+str(p["timestamp"])+", \"values\":{\"Moisture\":\""+str(p['value'])+"\"}}\" "+str(link)+"/api/v1/"+str(moisture_token)+"/telemetry --header \"Content-Type:application/json\""
			subprocess.call(k, shell=True)
		


	# '''
		
# k="curl -v -X POST -d \"{\"ts\":1234567, \"values\":{\"key1\":\"1223\", \"key2\":\"232323\"}}\" https://demo.thingsboard.io/api/v1/"+str(temperature_token)+"/telemetry --header \"Content-Type:application/json\""
# subprocess.call(k, shell=True)		
		
		
		
		
		
		
# {"ts":1451649600512, "values":{"key1":"value1", "key2":"value2"}}		
		
		
		
		
		
		
'''

pressure
lux
humidity
moisture
timestamp
ambient_temperature

'''
 


 

# print(testing(1))

# {"success":true,"data":[{"_id":"5c9db78875b61e000482b3c4","node":"sadaf1","type":"pressure","value":844,"timestamp":1553840008162,
# "_msgid":"92d71100.3e3df"},{"_id":"5c9db78875b61e000482b3c5","node":"sadaf1","type":"lux","value":18.37,"timestamp":1553840008162,








