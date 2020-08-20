# A simple script that opens your daily essential application with one simple command
import os
from threading import Thread

def app1(my_app_name):

  os.system(my_app_name)


def main():
 t1 = Thread(target=app1, args=(('google-chrome',)) )
 t2 = Thread(target=app1 , args=(('code',)) )
 t1.start()
 t2.start()


if __name__ == '__main__':
 main()