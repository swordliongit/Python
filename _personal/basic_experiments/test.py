from configparser import ConfigParser
from time import sleep

config = ConfigParser()
config.read("_personal/basic_experiments/test.ini")
DURATION = config.getint("delay", "seconds")

sleep(DURATION)

print("Finally")