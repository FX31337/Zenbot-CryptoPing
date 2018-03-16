#!/usr/bin/env python3
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
import time
import subprocess
import os, signal
def dat(update):
    data str(update)
	# Orders automatically get cancelled after a day per zenbot defaults. So, we cancel the proc process after a day, then initiate a sell #2 at 0 markup in case the sell did not complete after a day.
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
        if "#AMP" in data:
            print("A AMP WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.AMP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.AMP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.AMP-BTC", shell=True)
        if "#ARDR" in data:
            print("A ARDR WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.ARDR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.ARDR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.ARDR-BTC", shell=True)
        if "#BCH" in data:
            print("A BCH WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BCH-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BCH-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BCH-BTC", shell=True)
        if "#BCN" in data:
            print("A BCN WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BCN-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BCN-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BCN-BTC", shell=True)
        if "#BCY" in data:
            print("A BCY WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BCY-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BCY-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BCY-BTC", shell=True)
        if "#BELA" in data:
            print("A BELA WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BELA-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BELA-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BELA-BTC", shell=True)
        if "#BLK" in data:
            print("A BLK WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BLK-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BLK-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BLK-BTC", shell=True)
        if "#BTCD" in data:
            print("A BTCD WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BTCD-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BTCD-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BTCD-BTC", shell=True)
        if "#BTM" in data:
            print("A BTM WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BTM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BTM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BTM-BTC", shell=True)
        if "#BTS" in data:
            print("A BTS WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BTS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BTS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BTS-BTC", shell=True)
        if "#BURST" in data:
            print("A BURST WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.BURST-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.BURST-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.BURST-BTC", shell=True)
        if "#CLAM" in data:
            print("A CLAM WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.CLAM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.CLAM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.CLAM-BTC", shell=True)
        if "#CVC" in data:
            print("A CVC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.CVC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.CVC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.CVC-BTC", shell=True)
        if "#DASH" in data:
            print("A DASH WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.DASH-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.DASH-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.DASH-BTC", shell=True)
        if "#DCR" in data:
            print("A DCR WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.DCR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.DCR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.DCR-BTC", shell=True)
        if "#DGB" in data:
            print("A DGB WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.DGB-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.DGB-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.DGB-BTC", shell=True)
        if "#DOGE" in data:
            print("A DOGE WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.DOGE-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.DOGE-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.DOGE-BTC", shell=True)
        if "#EMC2" in data:
            print("A EMC2 WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.EMC2-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.EMC2-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.EMC2-BTC", shell=True)
        if "#ETC" in data:
            print("A ETC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.ETC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.ETC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.ETC-BTC", shell=True)
        if "#ETH" in data:
            print("A ETH WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.ETH-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.ETH-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.ETH-BTC", shell=True)
        if "#EXP" in data:
            print("A EXP WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.EXP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.EXP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.EXP-BTC", shell=True)
        if "#FCT" in data:
            print("A FCT WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.FCT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.FCT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.FCT-BTC", shell=True)
        if "#FLDC" in data:
            print("A FLDC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.FLDC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.FLDC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.FLDC-BTC", shell=True)
        if "#FLO" in data:
            print("A FLO WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.FLO-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.FLO-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.FLO-BTC", shell=True)
        if "#GAME" in data:
            print("A GAME WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.GAME-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.GAME-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.GAME-BTC", shell=True)
        if "#GAS" in data:
            print("A GAS WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.GAS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.GAS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.GAS-BTC", shell=True)
        if "#GNO" in data:
            print("A GNO WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.GNO-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.GNO-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.GNO-BTC", shell=True)
        if "#GNT" in data:
            print("A GNT WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.GNT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.GNT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.GNT-BTC", shell=True)
        if "#GRC" in data:
            print("A GRC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.GRC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.GRC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.GRC-BTC", shell=True)
        if "#HUC" in data:
            print("A HUC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.HUC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.HUC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.HUC-BTC", shell=True)
        if "#LBC" in data:
            print("A LBC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.LBC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.LBC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.LBC-BTC", shell=True)
        if "#LSK" in data:
            print("A LSK WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.LSK-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.LSK-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.LSK-BTC", shell=True)
        if "#LTC" in data:
            print("A LTC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.LTC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.LTC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.LTC-BTC", shell=True)
        if "#MAID" in data:
            print("A MAID WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.MAID-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.MAID-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.MAID-BTC", shell=True)
        if "#NAV" in data:
            print("A NAV WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.NAV-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.NAV-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.NAV-BTC", shell=True)
        if "#NEOS" in data:
            print("A NEOS WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.NEOS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.NEOS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.NEOS-BTC", shell=True)
        if "#NMC" in data:
            print("A NMC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.NMC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.NMC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.NMC-BTC", shell=True)
        if "#NXC" in data:
            print("A NXC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.NXC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.NXC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.NXC-BTC", shell=True)
        if "#NXT" in data:
            print("A NXT WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.NXT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.NXT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.NXT-BTC", shell=True)
        if "#OMG" in data:
            print("A OMG WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.OMG-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.OMG-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.OMG-BTC", shell=True)
        if "#OMNI" in data:
            print("A OMNI WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.OMNI-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.OMNI-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.OMNI-BTC", shell=True)
        if "#PASC" in data:
            print("A PASC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.PASC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.PASC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.PASC-BTC", shell=True)
        if "#PINK" in data:
            print("A PINK WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.PINK-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.PINK-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.PINK-BTC", shell=True)
        if "#POT" in data:
            print("A POT WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.POT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.POT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.POT-BTC", shell=True)
        if "#PPC" in data:
            print("A PPC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.PPC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.PPC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.PPC-BTC", shell=True)
        if "#RADS" in data:
            print("A RADS WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.RADS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.RADS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.RADS-BTC", shell=True)
        if "#REP" in data:
            print("A REP WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.REP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.REP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.REP-BTC", shell=True)
        if "#RIC" in data:
            print("A RIC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.RIC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.RIC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.RIC-BTC", shell=True)
        if "#SBD" in data:
            print("A SBD WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.SBD-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.SBD-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.SBD-BTC", shell=True)
        if "#SC" in data:
            print("A SC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.SC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.SC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.SC-BTC", shell=True)
        if "#STEEM" in data:
            print("A STEEM WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.STEEM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.STEEM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.STEEM-BTC", shell=True)
        if "#STORJ" in data:
            print("A STORJ WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.STORJ-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.STORJ-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.STORJ-BTC", shell=True)
        if "#STR" in data:
            print("A STR WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.STR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.STR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.STR-BTC", shell=True)
        if "#STRAT" in data:
            print("A STRAT WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.STRAT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.STRAT-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.STRAT-BTC", shell=True)
        if "#SYS" in data:
            print("A SYS WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.SYS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.SYS-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.SYS-BTC", shell=True)
        if "#VIA" in data:
            print("A VIA WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.VIA-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.VIA-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.VIA-BTC", shell=True)
        if "#VRC" in data:
            print("A VRC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.VRC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.VRC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.VRC-BTC", shell=True)
        if "#VTC" in data:
            print("A VTC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.VTC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.VTC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.VTC-BTC", shell=True)
        if "#XBC" in data:
            print("A XBC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.XBC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.XBC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.XBC-BTC", shell=True)
        if "#XCP" in data:
            print("A XCP WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.XCP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.XCP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.XCP-BTC", shell=True)
        if "#XEM" in data:
            print("A XEM WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.XEM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.XEM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.XEM-BTC", shell=True)
        if "#XMR" in data:
            print("A XMR WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.XMR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.XMR-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.XMR-BTC", shell=True)
        if "#XPM" in data:
            print("A XPM WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.XPM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.XPM-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.XPM-BTC", shell=True)
        if "#XRP" in data:
            print("A XRP WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.XRP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.XRP-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.XRP-BTC", shell=True)
        if "#XVC" in data:
            print("A XVC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.XVC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.XVC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.XVC-BTC", shell=True)
        if "#ZEC" in data:
            print("A ZEC WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.ZEC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.ZEC-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.ZEC-BTC", shell=True)
        if "#ZRX" in data:
            print("A ZRX WAS FOUND!!!")
            subprocess.call("./zenbot.sh buy --markdown_buy_pct=0 poloniex.ZRX-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=2 poloniex.ZRX-BTC", shell=True)
            time.sleep(15)
            subprocess.call("./zenbot.sh sell --markup_sell_pct=0 poloniex.ZRX-BTC", shell=True)
    except exception as e:
        print(e)
data "null"
def load_settings(path='api/settings'):
    """Loads the user settings located under `api/`"""
    result {}
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            value_pair line.split('=')
            left value_pair[0].strip()
            right value_pair[1].strip()
            if right.isnumeric():
                result[left] int(right)
            else:
                result[left] right

    return result

settings load_settings()


session_name "botbotbot"
client TelegramClient(session_name,
                        int(settings['api_id']),
                        settings['api_hash'],
                        proxy=None,
                        update_workers=4,
                        spawn_read_thread=False)
if True:
    client.start(phone='+1YOURPHONENUMBER')
else:
    client.start()

client.add_update_handler(dat)
print('(Press Ctrl+C to stop this)')
client.idle()

