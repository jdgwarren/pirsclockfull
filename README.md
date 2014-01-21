PiRSClock-Basic
==============

PiRSClock-Full is a Raspberry Pi Radio Studio Clock written in python using pygame. It will display a clock in full screen on most monitors, displays and TVs along with status indicators for microphones, telephones etc...

This was designed specifically for the Raspberry Pi. This version includes configurable indicators for microphones, telephones etc... for use in a radio studio.

## Development Status

***

PiRSClock-Full is currently stable and ready for use.

## Installation for Raspberry Pi

***

It's recommended to use Debian Wheezy or above for this project and a 4GB or more SD Card.
For reliability I recommend to only use this Pi for the clock.

Note: The Pi will have the most accuracy in time keeping when it has a constant connection to the internet.

Once you have copied the Debian Wheezy Image to your SD Card and booted your Pi for the first time, a prompt will come up called:
    
    Raspberry Pi Software Configuration Tool (raspi-config)

You need to select:

    1 Expand Filesystem
Then

    <Ok>

Next we need to:

    3 Enable Boot to Desktop/Scratch

and select:

    Console Text console

**THIS PART IS IMPORTANT TO GET THE RIGHT TIMEZOME**

Select:

    4 Internationalisation Options

Then:

    I2 Change Time Zone

You will have a list of continents/geographical areas, select your one. Then select a region or city in your time zone.

When you are done select:

    <Finish>
    
Then Reboot.

Once you have rebooted and logged in lets make sure everything is up to date:

    sudo apt-get update
    
Then

    sudo apt-get upgrade
    
Now we need to get setuptools:

    sudo apt-get install python-setuptools
    
And finally we install PiRSClock-Basic:

    sudo easy_install PiRSClock-Full
    
and there we have it!

## Running it

***

All we have to do is:

    pirsclockfull
    
To quit just hold down keys Q and T at the same time.

## Custom configuration

Custom configuration guide will go here. Stay tuned...

## Making it startup automatically when you plug in the Pi

***

This is a modified version of an article at [http://www.raspberrypi-spy.co.uk/2012/06/auto-login-auto-load-lxde/](http://www.raspberrypi-spy.co.uk/2012/06/auto-login-auto-load-lxde/)

Firstly:

    sudo nano /etc/initab
    
Scroll down to:

    1:2345:respawn:/sbin/getty --noclear 38400 tty1
    
and add a # infront of that so it looks like this:

    #1:2345:respawn:/sbin/getty --noclear 38400 tty1
    
Then add this underneath (pi is the username I use in this example):

    1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1
    
We press together Ctrl and O (Letter O)

Press Enter to save.

Then Ctrl and X to exit.

Next we:

    sudo nano /etc/profile
    
and add to the bottom:

    sudo pirsclockfull

Then Ctrl and O

Enter

Ctrl and X

    sudo reboot
    
To test it.
    
It should now automatically display after you reboot and every time you turn it on. Remember hold Q and T to get back to the command line if needed.
