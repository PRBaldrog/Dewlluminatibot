# main bot script for the dewlluminati bot
# Let's aim to keep it simple by moving all command lists to json files under /lib/
# we'll load the command lists at bot start and cache it


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
