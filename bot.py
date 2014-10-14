# main bot script for the dewlluminati bot
# Let's aim to keep it simple by moving all command lists to json files under /lib/
# we'll load the command lists at bot start and cache it

#import shit
import json
import irc
from irc.client import SimmpleIRCClient
import sys
import logging 
import re
import os
import time
from datetime import datetime
import stat
import random
import signal

#Globals and enums

TWITCH_KRAKEN_API = "https://api.twitch.tv/kraken"
TWITCH_V3_HEADER = {"Accept":"application/vnd.twitchtv.v3+json"}
SERVER = none
CHANNEL = none
OAUTH = none
PASSWORD = none
USERNAME = none


all_commands = none
devs = none
help_for_commands = none


#Load settings for the bot at start time
#NOTE - settings.json will be hidden + protective once we get it properly made
def load_settings(filename):
	global SERVER, OAUTH, PASSWORD, USERNAME
	
	with open(filename, 'r') as hF:
		settings = json.load(hF)

	SERVER  = settings["server"]
	OAUTH = settings["oauth"]
	PASSWORD = settings["password"]
	USERNAME = settings["username"]
	CHANNEL = settings["channel"] 

#load Devs list 
#this is for special commands I suppose
def load_devs(filename):
	with open(filename, 'r') as hF:
		devs = json.load(hF)
		return devs


#load command list + the helper for when we call !help
def load_help(filename):
	with open(filename, 'r') as hF:
		help_for_commands = json.load(hF)
		return help_for_commands
