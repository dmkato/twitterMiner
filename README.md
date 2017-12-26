## Twitter Miner

### Purpose
Gather information about individuals based on their twitter accounts

### Goals
* Gather and store tweets in Postgres DB
* Determine most used words/general sentiment
* Collect data from facebook

### Tech Stack
* Python
* PostGreSQL

### Useful Links
* (launchctl plist format)[https://alvinalexander.com/mac-os-x/launchd-plist-examples-startinterval-startcalendarinterval]
* (launchctl syntax)[https://babodee.wordpress.com/2016/04/09/launchctl-2-0-syntax/]


### Useful commands
* load plist
    * launchctl bootstrap gui/501 /Users/danielkato/Code/twitterMiner/me.dmkato.frankstweets.plist
* unload plist
    * launchctl unload /Users/danielkato/Code/twitterMiner/me.dmkato.frankstweets.plist
* list jobs
    * launchctl list | grep me
