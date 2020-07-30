"""AI_Sunday.py: basic AI"""

import speech_recognition
#import robot speaking
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_speak = pyttsx3.init()
robot_brain = ""
#Robot voice recognition
while True:
	with speech_recognition.Microphone() as mic:
		print("Sunday: I'm listening")
		audio = robot_ear.listen(mic)
	print("Sunday: ...")

	try: 
		you = robot_ear.recognize_google(audio)
	except:
		you == ""

	print("You: " + you)

#Robot brain to control and give the respond to user
	if you =="":
		robot_brain ="I can't hear you, sir. Please try again"

	elif "hey Sunday" in you:
		robot_brain = "Hello Duy Minh"

	elif "introduce yourself" in you or "who are you" in you:
		robot_brain = "Hi. My name is Sunday. I am your personal Assistant was created by Duy Minh Pham. You can command me to perform various tasks such as calculating sums or opening application etcetra. I will help you in my ability"

	elif "what is today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")

	elif you == "what time is it":
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")

	elif "president" in you:
		robot_brain = "Donald Trump"

	elif "bye" in you:
		robot_brain = "Bye sir. Have a wonderful day"
		print("Sunday: " + robot_brain)
		robot_speak.say(robot_brain)
		robot_speak.runAndWait()
		break

	else:
		robot_brain = "I'm fine. Thanks"

#Robot give the respond to the user and speak it out loud
	print("Sunday: " + robot_brain)
	robot_speak.say(robot_brain)
	robot_speak.runAndWait()
