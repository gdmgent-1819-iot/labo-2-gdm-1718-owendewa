#Import the necessary
from sense_hat import SenseHat
import requests 
import json
import sys
import os
# create SenseHat instance
sense = SenseHat()
try:
	# funtion to fetch a new person
	def getPerson():
		#define globals 
		global name
		global gender
		global location
		# Make a get request to get the latest position of the international space station from the opennotify api.
		json_data = requests.get("https://randomuser.me/api/").json()
		#give value to globals
		name = json_data['results'][0]['name']['first'];
		gender = json_data['results'][0]['gender'];
		location = json_data['results'][0]['location']['city'];	
		#append the new json data to data.json
		with open ('data.json','a') as f:
			collected_data = json.dump(json_data, f);
			repr(collected_data);
	#show the fetched data partially on the sense hat
	def showMessage():
		sense.show_message(name)
		sense.show_message(gender)
		sense.show_message(location)
	#create like function
	def like():
		person = {
			'naam': name,
			'gender': gender,
			'locatie': location,
			'choice': 'like',
		}
		writeUser(person)	
	#create dislike function
	def dislike():
		person = {
			'naam': name,
			'gender': gender,
			'locatie': location,
			'choice': 'dislike'
		}
		writeUser(person)
	#create append file function for like and dislike
	def writeUser(user):
		#append current person to history.json
		with open ('history.json','a') as f:
			collected_data = json.dump(user, f);
			repr(collected_data);
		#restart the python script from within after the user
		#likes or dislikes
		os.execl(sys.executable, sys.executable, * sys.argv)
			
	getPerson()	
	showMessage()	
	sense.stick.direction_left = like
	sense.stick.direction_right = dislike
	while True:
		pass
except (KeyboardInterrupt, SystemExit):
	sense.clear()
	print('\n' + 'Stopped Tinder')
	sys.exit(0)

#Owen De Waele NMD
