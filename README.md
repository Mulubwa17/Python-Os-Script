# Python-Os-Script
A simple script that opens your daily essential apps on your workstation with one command

## Requirements
python

### Instructions
To run the script :

- run command python App.py if you are using python2,this will open your desired application
- run command python3 App.py if you are using python3,this will open your desired application

### Adding more apps (make sure your know the command-line name of the app to initiate it)
To add more apps to the scripts :
 - add line under these two commands: <br>
 `t1 = Thread(target=app1, args=(('google-chrome',)) )` <br>
 `t2 = Thread(target=app1 , args=(('code',)) )` <br>

e.g `` t3 = Thread(target=app1, args=(('firefox',)) ) ``

- finally initialise your script thread by adding it under these two commands: <br>
 `t1.start()` <br>
 `t2.start()` <br>

e.g `` t3.start()``

### Your final Script should look like this :

##### A simple script that opens your daily essential application with one simple command
import os
from threading import Thread

def app1(my_app_name):

  os.system(my_app_name)


def main(): <br>
 t1 = Thread(target=app1, args=(('google-chrome',)) ) <br>
 t2 = Thread(target=app1 , args=(('code',)) ) <br>
 t3 = Thread(target=app1, args=(('firefox',)) ) <br>
 t1.start() <br>
 t2.start() <br>
 t3.start() <br>


if __name__ == '__main__': <br>
 main()
 
