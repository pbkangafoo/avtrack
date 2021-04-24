# avtrack
 status tracker for imvu avatars

## What does avtrack do?

On the chat platform IMVU, people can change their status but you don't necessarily see which one they have. So when someone changes the status e. g. to DND or away, they will be displayed as offline. Therefore you can use to avtrack to check the status of a certain avatar and you know whether they are really offline or just do not want to get disturbed.

## Requirements

For using avtrack you need to have the "requests" library. You can install it using pip: 

> _python -m pip install requests_

## Parameters

* -u - use username
* -c - use cid instead of username
* -d - delay between each check in seconds
* -v - display the status whether it changed or not

## Usage examples

Keeping track and display every x seconds the status using name:

> python avtrack.py -u _username_ -v -d <seconds>
 
Keeping track and display only when the status changed using CID:

> python avtrack.py -c _cid_ -d 60
 
## Screenshot

![Screenshot](https://github.com/pbkangafoo/avtrack/blob/main/avtrack_screenshot.JPG "avtrack screenshot")
