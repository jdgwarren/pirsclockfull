PiRSClock-Full
==============

PiRSClock-Full is a Raspberry Pi Radio Studio Clock written in python using pygame with studio indicators for microphones, telephones etc... It will display a clock in full screen on widescreen (16:9) monitors, displays and TVs.

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

***

Firstly you type:

    sudo nano /usr/local/lib/python2.7/dist-packages/PiRSClock_Full-2.0-py2.7.egg/EGG-INFO/scripts/pirsclockfull

To set colours of the indicators, change the numerical values in ind1colour - ind4colour.

The values are standard RGB

The First value is RED, the second is GREEN and the third is BLUE. The max value is 255 and the min is 0

Example:

    ind1colour = (255, 0, 0)
    
would make the first indicator red in this example.

To change the text in the indicators, change the word in the "quotes" in ind1txt - ind4txt

Example:

    ind1txt = indfont.render("HELLO",True,bgcolour)

This would change the text to HELLO on the first indicator in this example.

## Making it startup automatically when you plug in the Pi

***

This is a modified version of an article at [http://www.raspberrypi-spy.co.uk/2012/06/auto-login-auto-load-lxde/](http://www.raspberrypi-spy.co.uk/2012/06/auto-login-auto-load-lxde/)

Firstly:

    sudo nano /etc/inittab
    
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
