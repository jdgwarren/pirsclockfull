#! /usr/bin/env python
import pygame , sys , math, time, os
import RPi.GPIO as GPIO
from pygame.locals import *
os.environ['SDL_VIDEODRIVER']="fbcon"

# Setting up the GPIO and inputs with pull up
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, GPIO.PUD_UP)

pygame.init()
bg = pygame.display.set_mode()

pygame.mouse.set_visible(False)

# Change colour to preference (R,G,B) 255 max value
bgcolour       = (0,   0,   0  )
clockcolour    = (255, 255, 255)
ind1colour     = (255, 0,   0  )
ind2colour     = (255, 255, 0  )
ind3colour     = (0,   255, 0  )
ind4colour     = (0,   255, 255)
offcolour      = (16,  16,  16 )

# Scaling to the right size for the display
digiclocksize  = int(bg.get_height()/3.5)
digiclockspace = int(bg.get_height()/10.5)
dotsize        = int(bg.get_height()/90)
hradius        = bg.get_height()/2.5
secradius      = hradius - (bg.get_height()/26)
indtxtsize     = int(bg.get_height()/5)
indboxy        = int(bg.get_height()/6)
indboxx        = int(bg.get_width()/2.5)

# Coords of items on display
xclockpos      = int(bg.get_width()*0.2875)
ycenter        = int(bg.get_height()/2)
xtxtpos        = int(bg.get_width()*0.75)
xindboxpos     = int(xtxtpos-(indboxx/2))
ind1y          = int((ycenter*0.4)-(indboxy/2))       
ind2y          = int((ycenter*0.8)-(indboxy/2))
ind3y          = int((ycenter*1.2)-(indboxy/2))
ind4y          = int((ycenter*1.6)-(indboxy/2))
txthmy         = int(ycenter-digiclockspace)
txtsecy        = int(ycenter+digiclockspace)

# Fonts  
clockfont     = pygame.font.Font(None,digiclocksize)
indfont       = pygame.font.Font(None,indtxtsize)

# Indicator text - edit text in quotes to desired i.e. "MIC" will show MIC on display
ind1txt       = indfont.render("MIC",True,bgcolour)
ind2txt       = indfont.render("PHONE",True,bgcolour)
ind3txt       = indfont.render("ON AIR",True,bgcolour)
ind4txt       = indfont.render("DOOR",True,bgcolour)

# Indicator positions
txtposind1 = ind1txt.get_rect(centerx=xtxtpos,centery=ycenter*0.4)
txtposind2 = ind2txt.get_rect(centerx=xtxtpos,centery=ycenter*0.8)
txtposind3 = ind3txt.get_rect(centerx=xtxtpos,centery=ycenter*1.2)
txtposind4 = ind4txt.get_rect(centerx=xtxtpos,centery=ycenter*1.6)

# Parametric Equations of a Circle to get the markers
# 90 Degree ofset to start at 0 seconds marker
# Equation for second markers
def paraeqsmx(smx):
    return xclockpos-(int(secradius*(math.cos(math.radians((smx)+90)))))

def paraeqsmy(smy):
    return ycenter-(int(secradius*(math.sin(math.radians((smy)+90)))))

# Equations for hour markers
def paraeqshx(shx):
    return xclockpos-(int(hradius*(math.cos(math.radians((shx)+90)))))

def paraeqshy(shy):
    return ycenter-(int(hradius*(math.sin(math.radians((shy)+90)))))

# This is where pygame does its tricks
while True :
    pygame.display.update()

    bg.fill(bgcolour)

    # Retrieve seconds and turn them into integers
    sectime = int(time.strftime("%S",time.localtime(time.time())))

    # To get the dots in sync with the seconds
    secdeg  = (sectime+1)*6

    # Draw second markers
    smx=smy=0
    while smx < secdeg:
        pygame.draw.circle(bg, clockcolour, (paraeqsmx(smx),paraeqsmy(smy)),dotsize)
        smy += 6  # 6 Degrees per second
        smx += 6

    # Draw hour markers
    shx=shy=0
    while shx < 360:
        pygame.draw.circle(bg, clockcolour, (paraeqshx(shx),paraeqshy(shy)),dotsize)
        shy += 30  # 30 Degrees per hour
        shx += 30

    # Retrieve time for digital clock
    retrievehm    = time.strftime("%H:%M",time.localtime(time.time()))
    retrievesec   = time.strftime("%S",time.localtime(time.time()))

    digiclockhm   = clockfont.render(retrievehm,True,clockcolour)
    digiclocksec  = clockfont.render(retrievesec,True,clockcolour)

    # Align it
    txtposhm      = digiclockhm.get_rect(centerx=xclockpos,centery=txthmy)
    txtpossec     = digiclocksec.get_rect(centerx=xclockpos,centery=txtsecy)

    # Function for the indicators
    if GPIO.input(11):
        pygame.draw.rect(bg, offcolour,(xindboxpos, ind1y, indboxx, indboxy))
    else:
        pygame.draw.rect(bg, ind1colour,(xindboxpos, ind1y, indboxx, indboxy))

    if GPIO.input(12):
        pygame.draw.rect(bg, offcolour,(xindboxpos, ind2y, indboxx, indboxy))
    else:
        pygame.draw.rect(bg, ind2colour,(xindboxpos, ind2y, indboxx, indboxy))

    if GPIO.input(13):
        pygame.draw.rect(bg, offcolour,(xindboxpos, ind3y, indboxx, indboxy))
    else:
        pygame.draw.rect(bg, ind3colour,(xindboxpos, ind3y, indboxx, indboxy))

    if GPIO.input(15):
        pygame.draw.rect(bg, offcolour,(xindboxpos, ind4y, indboxx, indboxy))
    else:
        pygame.draw.rect(bg, ind4colour,(xindboxpos, ind4y, indboxx, indboxy))
    
    # Render the text
    bg.blit(digiclockhm, txtposhm)
    bg.blit(digiclocksec, txtpossec)
    bg.blit(ind1txt, txtposind1)
    bg.blit(ind2txt, txtposind2)
    bg.blit(ind3txt, txtposind3)
    bg.blit(ind4txt, txtposind4)
    
    time.sleep(0.04)
    pygame.time.Clock().tick(25)
    for event in pygame.event.get() :
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Pressing q+t to exit
        elif event.type == KEYDOWN:
            if event.key == K_q and K_t:
                pygame.quit()
                sys.exit()
