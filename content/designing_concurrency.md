Title: Designing concurrent applications
Date: 2022-04-15 20:00
Status: published
Read: 0 min
Category: tech

While working on one of my first projects, I encountered a peculiar situation while using threads in a python application. We had developed a script
that takes in real-time audio, processes it, and feeds it to an AI Model to finally make a prediction if the audio signal is of a baby crying or not. the first version was quite simple, it worked on a single camera and could detect with decent accuracy if an audio signal contained a baby cry and send an alert through an API.

This first version was adequate, but then came some design limitations to this application. How do we manage multiple cameras? currently we would have to 
run the script on each camera individually. running the script with arguments defining which camera we want to run the script on. This was not a desirable situation for us. we wanted to encapsulate the management of all the cameras into one script, making it easier to manage and scale.

This lead us to develop a second version of the application. and soon, at first glance, the decision was clear to have a "concurrent" application that runs some processes per camera relating to audio collection, model detection and alarm sending.

We designed this new version to accept a json file containing a list of all of the cameras, and from there to spin up some threads to do some processes, and finally send an alert through an API if we have detected a baby cry.

Soon I would one of the pains of software development, understanding the underlying decision you made in your application that you yourself probably didn't understand that well.

I designed this concurrent application with the following

![MyImage]({attach}images/threads.png)