Title: Debugging Hanging Threads In Python
Date: 2022-04-15 20:00
Status: draft
Read: 0 min
Category: tech

While working on one of my first projects, I encountered a peculiar situation while using threads in a python application. We had developed a script
that takes in real-time audio, processes it, and feeds it to an AI Model to finally make a prediction if the audio signal is of a baby crying or not. the first version was quite simple, it worked on a single camera and could detect with decent accuracy if an audio signal contained a baby cry and send an alert to a external system.

This first version was adequate, but then came some design limitations to this application. How do we manage multiple cameras? currently we would have to 
run the script on each camera individually. running the script with arguments defining which camera we want to run the script on. This was not a desirable situation for us. we wanted to encapsulate the management of all the cameras into one script, making it easier to manage and scale.

This lead us to develop a second version of the application. and soon, at first glance, the decision was clear to have a "Multi-thread" application that runs some processes per camera relating to audio collection, model detection and alarm sending.

We designed this new version to accept a json file containing a list of all of the cameras, and from there to spin up some threads to do some processes, and finally send an alert through an API if we have detected a baby cry. In simple terms, it looked something like the following:


```python
#main.py
...
def main():
	...
		for camera in cameras:
			camera_id = camera["id"]
			camera_url = camera["url"]
			username = camera["username"]
			password = camera["password"]
			audio_manager = AudioManager(
				camera_url, camera_id, username, password, filesave_interval
			)
			am_thread = threading.Thread(
				target=audio_manager.start_audio_processing
			)
			am_thread.start()
			cry_detection = CryDetection(audio_manager, api_source)
			ai_thread = threading.Thread(target=cry_detection.run)
			ai_thread.start()
	...
...
	
```

```python 
...
class AudioManager:
	...
	def start_audio_processing(self):
		process = subprocess.Popen(
			f"openRTSP -u"
		)
	...

```
```python
...
class CryDetection:
	def __init__(self, audio_manager, api_source):
		self.audio_manager = audio_manager
		self.api_source = api_source


	def run(self):
		model = loadmodel("./model/LMFB_model_ls.h5")
		while True:
			input_file = file_queue.q.get()
			prediction = model.predict(input_file)
			if prediction > threshold:
				api_source.send()


```