#!/usr/bin/env python3
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
import time
from subprocess import *
import os, signal
global working
working = False
def dat(update):
    global working
    data = str(update)
	# Orders automatiPopeny get cancelled after a day per zenbot defaults. So, we cancel the proc process after a day, then initiate a sell #2 at 0 markup in case the sell did not complete after a day.
	# A try statement was added here to keep the program from halting. We buy and undercut the market with negative markup on purchases to hopefully profit from hard pumps.
	# This was updated 05:00 3/15/2018
	# WAAAARNING. It is advised to not follow signals blindly.
	# To install: Drop this file in ~/zenbot directory after running git clone https://github.com/deviavir/zenbot.git ~/zenbot
	# Then git clone telethon over this zenbot directory! git clone https://github.com/LonamiWebs/Telethon.git ~/zenbot
	# install dependencies for both programs: Curl, nodejs 8 or 9, git, screen, python3 and python3-pip and lastly mongodb: sudo apt-get install -y curl git screen python3 python3-pip mongodb
	# Install nodejs per this article: https://nodejs.org/en/download/package-manager/
	# Change directories to your ~/zenbot directory: cd ~/zenbot
	# run these commands:
	# npm i
	# pip3 install telethon
	# python3 setup.py install
	# Now configure the settings in the ~/zenbot/api/setings_example file, you must create a telegram account, and create an api key and ID from here: https://my.telegram.org/auth?to=apps
	# Now rename the settings_example file to settings so that it appears as ~/zenbot/api/settings: mv ~/zenbot/api/settings_example ~/zenbot/api/settings
	# Now, copy conf-sample.js into conf.js in your ~/zenbot directory: cp ~/zenbot/conf-sample.js ~/zenbot/conf.js
	# Create a poloniex api key and secret, input your api key and secret into conf.js: nano ~/zenbot/conf.js
	# Lastly, input your telephone number in place of '+ENTERYOURPHONENUMBERFORTELEGRAMHERE' at the bottom of this file.
	# And finally, register at https://cryptoping.tech/ for updates or at cryptoalert: https://cryptoalert.wordpress.com/
	# lastly, launch this python file in screen! screen -S poloniex -m python3 polo.py
	# You should see the output of the bot trying to buy and place instant sell orders at 2% above the current price. For finer tuning, adjust the order_adjust_time in conf.js and the cancel_after time periods.
    try:
        if ("#AMP" in data) and (working == False):
            print("A AMP WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.AMP-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.AMP-BTC", shell=True)
            working = False
        if ("#ARDR" in data) and (working == False):
            print("A ARDR WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.ARDR-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.ARDR-BTC", shell=True)
            working = False
        if ("#BCH" in data) and (working == False):
            print("A BCH WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BCH-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BCH-BTC", shell=True)
            working = False
        if ("#BCN" in data) and (working == False):
            print("A BCN WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BCN-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BCN-BTC", shell=True)
            working = False
        if ("#BCY" in data) and (working == False):
            print("A BCY WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BCY-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BCY-BTC", shell=True)
            working = False
        if ("#BELA" in data) and (working == False):
            print("A BELA WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BELA-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BELA-BTC", shell=True)
            working = False
        if ("#BLK" in data) and (working == False):
            print("A BLK WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BLK-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BLK-BTC", shell=True)
            working = False
        if ("#BTCD" in data) and (working == False):
            print("A BTCD WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BTCD-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BTCD-BTC", shell=True)
            working = False
        if ("#BTM" in data) and (working == False):
            print("A BTM WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BTM-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BTM-BTC", shell=True)
            working = False
        if ("#BTS" in data) and (working == False):
            print("A BTS WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BTS-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BTS-BTC", shell=True)
            working = False
        if ("#BURST" in data) and (working == False):
            print("A BURST WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.BURST-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.BURST-BTC", shell=True)
            working = False
        if ("#CLAM" in data) and (working == False):
            print("A CLAM WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.CLAM-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.CLAM-BTC", shell=True)
            working = False
        if ("#CVC" in data) and (working == False):
            print("A CVC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.CVC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.CVC-BTC", shell=True)
            working = False
        if ("#DASH" in data) and (working == False):
            print("A DASH WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.DASH-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.DASH-BTC", shell=True)
            working = False
        if ("#DCR" in data) and (working == False):
            print("A DCR WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.DCR-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.DCR-BTC", shell=True)
            working = False
        if ("#DGB" in data) and (working == False):
            print("A DGB WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.DGB-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.DGB-BTC", shell=True)
            working = False
        if ("#DOGE" in data) and (working == False):
            print("A DOGE WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.DOGE-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.DOGE-BTC", shell=True)
            working = False
        if ("#EMC2" in data) and (working == False):
            print("A EMC2 WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.EMC2-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.EMC2-BTC", shell=True)
            working = False
        if ("#ETC" in data) and (working == False):
            print("A ETC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.ETC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.ETC-BTC", shell=True)
            working = False
        if ("#ETH" in data) and (working == False):
            print("A ETH WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.ETH-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.ETH-BTC", shell=True)
            working = False
        if ("#EXP" in data) and (working == False):
            print("A EXP WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.EXP-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.EXP-BTC", shell=True)
            working = False
        if ("#FCT" in data) and (working == False):
            print("A FCT WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.FCT-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.FCT-BTC", shell=True)
            working = False
        if ("#FLDC" in data) and (working == False):
            print("A FLDC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.FLDC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.FLDC-BTC", shell=True)
            working = False
        if ("#FLO" in data) and (working == False):
            print("A FLO WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.FLO-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.FLO-BTC", shell=True)
            working = False
        if ("#GAME" in data) and (working == False):
            print("A GAME WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.GAME-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.GAME-BTC", shell=True)
            working = False
        if ("#GAS" in data) and (working == False):
            print("A GAS WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.GAS-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.GAS-BTC", shell=True)
            working = False
        if ("#GNO" in data) and (working == False):
            print("A GNO WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.GNO-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.GNO-BTC", shell=True)
            working = False
        if ("#GNT" in data) and (working == False):
            print("A GNT WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.GNT-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.GNT-BTC", shell=True)
            working = False
        if ("#GRC" in data) and (working == False):
            print("A GRC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.GRC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.GRC-BTC", shell=True)
            working = False
        if ("#HUC" in data) and (working == False):
            print("A HUC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.HUC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.HUC-BTC", shell=True)
            working = False
        if ("#LBC" in data) and (working == False):
            print("A LBC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.LBC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.LBC-BTC", shell=True)
            working = False
        if ("#LSK" in data) and (working == False):
            print("A LSK WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.LSK-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.LSK-BTC", shell=True)
            working = False
        if ("#LTC" in data) and (working == False):
            print("A LTC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.LTC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.LTC-BTC", shell=True)
            working = False
        if ("#MAID" in data) and (working == False):
            print("A MAID WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.MAID-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.MAID-BTC", shell=True)
            working = False
        if ("#NAV" in data) and (working == False):
            print("A NAV WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.NAV-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.NAV-BTC", shell=True)
            working = False
        if ("#NEOS" in data) and (working == False):
            print("A NEOS WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.NEOS-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.NEOS-BTC", shell=True)
            working = False
        if ("#NMC" in data) and (working == False):
            print("A NMC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.NMC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.NMC-BTC", shell=True)
            working = False
        if ("#NXC" in data) and (working == False):
            print("A NXC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.NXC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.NXC-BTC", shell=True)
            working = False
        if ("#NXT" in data) and (working == False):
            print("A NXT WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.NXT-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.NXT-BTC", shell=True)
            working = False
        if ("#OMG" in data) and (working == False):
            print("A OMG WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.OMG-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.OMG-BTC", shell=True)
            working = False
        if ("#OMNI" in data) and (working == False):
            print("A OMNI WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.OMNI-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.OMNI-BTC", shell=True)
            working = False
        if ("#PASC" in data) and (working == False):
            print("A PASC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.PASC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.PASC-BTC", shell=True)
            working = False
        if ("#PINK" in data) and (working == False):
            print("A PINK WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.PINK-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.PINK-BTC", shell=True)
            working = False
        if ("#POT" in data) and (working == False):
            print("A POT WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.POT-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.POT-BTC", shell=True)
            working = False
        if ("#PPC" in data) and (working == False):
            print("A PPC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.PPC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.PPC-BTC", shell=True)
            working = False
        if ("#RADS" in data) and (working == False):
            print("A RADS WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.RADS-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.RADS-BTC", shell=True)
            working = False
        if ("#REP" in data) and (working == False):
            print("A REP WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.REP-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.REP-BTC", shell=True)
            working = False
        if ("#RIC" in data) and (working == False):
            print("A RIC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.RIC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.RIC-BTC", shell=True)
            working = False
        if ("#SBD" in data) and (working == False):
            print("A SBD WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.SBD-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.SBD-BTC", shell=True)
            working = False
        if ("#SC" in data) and (working == False):
            print("A SC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.SC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.SC-BTC", shell=True)
            working = False
        if ("#STEEM" in data) and (working == False):
            print("A STEEM WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.STEEM-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.STEEM-BTC", shell=True)
            working = False
        if ("#STORJ" in data) and (working == False):
            print("A STORJ WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.STORJ-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.STORJ-BTC", shell=True)
            working = False
        if ("#STR" in data) and (working == False):
            print("A STR WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.STR-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.STR-BTC", shell=True)
            working = False
        if ("#STRAT" in data) and (working == False):
            print("A STRAT WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.STRAT-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.STRAT-BTC", shell=True)
            working = False
        if ("#SYS" in data) and (working == False):
            print("A SYS WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.SYS-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.SYS-BTC", shell=True)
            working = False
        if ("#VIA" in data) and (working == False):
            print("A VIA WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.VIA-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.VIA-BTC", shell=True)
            working = False
        if ("#VRC" in data) and (working == False):
            print("A VRC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.VRC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.VRC-BTC", shell=True)
            working = False
        if ("#VTC" in data) and (working == False):
            print("A VTC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.VTC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.VTC-BTC", shell=True)
            working = False
        if ("#XBC" in data) and (working == False):
            print("A XBC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.XBC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.XBC-BTC", shell=True)
            working = False
        if ("#XCP" in data) and (working == False):
            print("A XCP WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.XCP-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.XCP-BTC", shell=True)
            working = False
        if ("#XEM" in data) and (working == False):
            print("A XEM WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.XEM-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.XEM-BTC", shell=True)
            working = False
        if ("#XMR" in data) and (working == False):
            print("A XMR WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.XMR-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.XMR-BTC", shell=True)
            working = False
        if ("#XPM" in data) and (working == False):
            print("A XPM WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.XPM-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.XPM-BTC", shell=True)
            working = False
        if ("#XRP" in data) and (working == False):
            print("A XRP WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.XRP-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.XRP-BTC", shell=True)
            working = False
        if ("#XVC" in data) and (working == False):
            print("A XVC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.XVC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.XVC-BTC", shell=True)
            working = False
        if ("#ZEC" in data) and (working == False):
            print("A ZEC WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.ZEC-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.ZEC-BTC", shell=True)
            working = False
        if ("#ZRX" in data) and (working == False):
            print("A ZRX WAS FOUND!!!")
            working = True
            wait = Popen("./zenbot.sh trade --strategy=cryptoping --min_periods=5 --period=5m --periodLength=5m poloniex.ZRX-BTC", shell=True)
            sStdout, sStdErr = wait.communicate()
            time.sleep(60)
            wait = Popen("./zenbot.sh sell --markup_sell_pct=0 poloniex.ZRX-BTC", shell=True)
            working = False
    except exception as e:
        print(e)
data = "null"
def load_settings(path='api/settings'):
    """Loads the user settings located under `api/`"""
    result = {}
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            value_pair = line.split('=')
            left = value_pair[0].strip()
            right = value_pair[1].strip()
            if right.isnumeric():
                result[left] = int(right)
            else:
                result[left] = right

    return result

settings = load_settings()


session_name = "botbotbot"
client = TelegramClient(session_name,
                        int(settings['api_id']),
                        settings['api_hash'],
                        proxy=None,
                        update_workers=4,
                        spawn_read_thread=False)
if True:
    client.start(phone='+ENTERYOURPHONENUMBERFORTELEGRAMHERE')
else:
    client.start()

client.add_update_handler(dat)
print('(Press Ctrl+C to stop this)')
client.idle()
