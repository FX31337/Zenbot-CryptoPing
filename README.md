	# THIS WAS DEVELOPED FOR POLO EXCHANGE BUT FEEL FREE TO EDIT THE PAIRS AT YOUR OWN RISK. I AM NOT LIABLE FOR ANY LOSSES USING THIS SOFTWARE.
	# Orders automatically get cancelled after 6 hours, then initiate a sell #2 at 0 markup in case the sell did not complete.
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
	# 
	# Instany buy 0.25% loss, but instant. Maker mode non post-only.
	# Then wait for trailing stop sell and then program exit.
	# ***Make sure to copy everything from this github repository over the zenbot files! All the repositories go into one single root folder!***
	# 
	# 
	# 


***MY BTC DONATION ADDRESS! :D Keep the development rolling!***
```1Ppitsjie6EcRTpfJEXmEYzUaoJgBdvhAg```
