import webbrowser
import time

def break_alarm():
	user_alarm = int(input('How many minutes are you working: ')) 
	user_breaks = int(input('Number of breaks: '))
	user_song = input('Insert a youtube song link or use default? (y/n) ')
	if (user_song == 'y'):
		alarm_song = input('youtube song url link: ')
	else:
		alarm_song = 'https://www.youtube.com/watch?v=9E6b3swbnWg'

	alarm_count = 0 

	while alarm_count < user_breaks: 
		time.sleep(10) 
		webbrowser.open(alarm_song)
		alarm_count = alarm_count + 1 
	 
	while True: 
	 	user_quit = input('Do you want to restart timer or quit? (y/n) ')
	 	if (user_quit == 'y'):
	 		break_alarm() 
	 	else:
	 		return False 

break_alarm()