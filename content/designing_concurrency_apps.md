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

The application looked like the following:

![MyImage]({attach}images/threads.png)

and zooming in, the launched threads contained code that did the following:

```python
...
def audio_processing():
    # Start openRTSP to capture the audio stream and save it to the current path every x seconds
    subproces.Popen(f'openRTSP -a -P {interval} rtsp://localhost:443/stream/profile0 ')
    # In parralel, convert the raw audio to wav format
    while True:
        audio_file = get_audio_file()
        convert_to_wav(audio_file)
        time.sleep(interval)
        
...

```

```python
...
def cry_detection():
    while True:
        file = get_next_wav_file()
        prediction = model.predict(file)
        time.sleep(interval)
        ...
...
```

Soon after testing this new version, I stopped getting any logs printed to the console after a few minutes. I had no clue what the problem was, seemed like the application just hangs after a few minutes?

After googling around, I found a handy tool called gdb (The GNU Debugger). In short, gdb allows you to see what is going on "inside" another program while it executes or what it was doing at the moment it crashed.

I launch the script and attach the gdb debugger on the process ID (PID)
```bash
$ gdb python 4901
(gdb) where
```

after a few minutes, I get the following logging info:

```bash
#1  do_futex_wait (sem=sem@entry=0x5a5e960, abstime=0x0, clockid=0) at sem_waitcommon.c:112
#2  0x00007fefcd3ba4e8 in __new_sem_wait_slow (sem=0x5a5e960, abstime=0x0, clockid=0)
    at sem_waitcommon.c:184
#3  0x0000000000597dc8 in PyThread_acquire_lock_timed ()
#4  0x000000000065a6e2 in ?? ()
#5  0x000000000065a542 in ?? ()
#6  0x00000000005dcba0 in ?? ()
#7  0x0000000000574c35 in _PyEval_EvalFrameDefault ()
#8  0x000000000050d373 in _PyFunction_Vectorcall ()
#9  0x000000000050ef8a in PyObject_VectorcallMethod ()
#10 0x0000000000630991 in ?? ()
#11 0x0000000000630857 in Py_FinalizeEx ()
#12 0x00000000005fce7d in Py_RunMain ()
#13 0x00000000005fcc6d in Py_BytesMain ()
#14 0x00007fefcd0340b3 in __libc_start_main (main=0x508a70, argc=3, argv=0x7ffd41cda448, 
    init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7ffd41cda438)
    at ../csu/libc-start.c:308
#15 0x00000000005fcb7e in _start ()

```

I'm no expert, but what I can get from this stack trace is that the application is trying to acquire the interpretor lock, but  it seems to be timing out? I assume this has something to do with python's GIL. 

But what is going on anyway? dealing with this problem made me revisit concurrency as a whole, I realised that I did not understand the topic as well as I thought.

First of all, what is concurrency and how do we acheive it?

To quote wikipedia, "concurrency is the ability of different parts or units of a program, algorithm, or problem to be executed out-of-order or in partial order, without affecting the final outcome. This allows for parallel execution of the concurrent units, which can significantly improve overall speed of the execution in multi-processor and multi-core systems".

To achieve concurrency in Python, there are 3 options.


- Pre-emptive multitasking (threading)
- Cooperative multitasking (asyncio)
- Multiprocessing (multiprocessing)