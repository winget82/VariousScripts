#maximize the microstation window on small laptop screen then run this script

import pyautogui as p
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style

#start the clock
time.clock()

#set python window size
os.system("mode con cols=100 lines=10")

#change directory to where images for pyautogui are saved
os.chdir('C:\\Users\\...')

location = input('Are you working from the (H)ome or (O)ffice?')

if location.upper() == 'O':

    p.click(875,9)

    try:
        #maximize microstation view window
        maxwin = p.locateOnScreen('maxwin.PNG', grayscale=True)
        maxwin_center = p.center(maxwin)
        p.moveTo(maxwin_center, duration=1)
        p.click()
    except:
        print(Fore.RED + "maximize window button not found")
        print(Style.RESET_ALL)

    #zoom to extents
    zoomext = p.locateOnScreen('zoomext.PNG', grayscale=True)
    zoomext_center = p.center(zoomext)
    p.moveTo(zoomext_center, duration=1)
    print("zooming to extents")
    p.click()

    #draw fence
    fence = p.locateOnScreen('fence.PNG', grayscale=True)
    fence_center = p.center(fence)
    p.moveTo(fence_center, duration=1)
    p.click()
    print("placing fence")
    #place fence by element
    #select fence type
    ftype = p.locateOnScreen('ftype.PNG', grayscale=True)
    ftype_center = p.center(ftype)
    p.moveTo(ftype_center, duration=1)
    a,b = ftype_center
    #Use variables to move a distance to right of ftype to get into input field
    #whether or not what text is showing in it currently
    a = a + 136
    p.moveTo(a,b)
    p.click()
    p.typewrite('e')
    p.moveTo(771, 295, duration=1)
    p.click()

    #go to main file menu
    p.moveTo(31, 48, duration=1)
    p.click()
    p.moveTo(130, 521, duration=1)
    p.click()

    #give the pop up window time to open before looking for image match
    time.sleep(3)

    #pop up print window file menu
    loc1 = p.locateOnScreen('loc1.PNG', grayscale=True)
    loc1_center = p.center(loc1)
    p.moveTo(loc1_center, duration=1)
    p.click()

    #select printer
    print('selecting printer')
    #loc2 = p.locateOnScreen('loc2.PNG', grayscale=True)
    #loc2_center = p.center(loc2)
    #p.moveTo(loc2_center, duration=1)
    #p.click()
    time.sleep(2)
    p.typewrite('w')

    p.moveTo(1918, 1042, duration=1)
    p.click()
    time.sleep(1)
    p.click()
    time.sleep(1)

    #locate AdobePDF
    loc3 = p.locateOnScreen('loc3.png', grayscale=True)
    loc3_center = p.center(loc3)
    p.moveTo(loc3_center, duration=1)
    p.doubleClick()

    #move to scale input
    time.sleep(1)
    loc4 = p.locateOnScreen('loc4.PNG', grayscale=True)
    loc4_center = p.center(loc4)
    p.moveTo(loc4_center, duration=1)
    a,b = loc4_center
    #Use variables to move a distance to right of loc4 to get into input field
    #whether or not what text is showing in it currently
    a = a + 68
    p.moveTo(a,b)
    #scale input
    print('scaling')
    p.doubleClick()
    p.typewrite('1.44')
    p.typewrite(['enter'])

    #print
    loc5 = p.locateOnScreen('loc5.PNG', grayscale=True)
    loc5_center = p.center(loc5)
    p.moveTo(loc5_center, duration=1)
    p.click()

    t = str(time.clock())
    #final message
    print("dgn printed to pdf in " + t + " seconds...")

    alert = p.confirm(text='Save DGN & Settings?', buttons=['Save','Cancel'])

    if alert == 'Save':
        p.click(34, 49)
        p.typewrite('v')
        p.click(34, 49)
        p.typewrite('s')
        p.click(1879, 8)
        time.sleep(2)
        OKCapture = p.locateOnScreen('OKCapture.PNG', grayscale=True)
        OKCapture_center = p.center(OKCapture)
        time.sleep(3)
        p.moveTo(OKCapture_center, duration=1)
        p.click()

    elif alert == 'Cancel':
        quit()

elif location.upper() == 'H':

    p.click(1475,8)

    try:
        #maximize microstation view window
        maxwin = p.locateOnScreen('maxwinH.PNG', grayscale=True)
        maxwin_center = p.center(maxwin)
        p.moveTo(maxwin_center, duration=1)
        p.click()
    except:
        print(Fore.RED + "maximize window button not found")
        print(Style.RESET_ALL)

    #zoom to extents
    zoomext = p.locateOnScreen('zoomextH.PNG', grayscale=True)
    zoomext_center = p.center(zoomext)
    p.moveTo(zoomext_center, duration=1)
    print("zooming to extents")
    p.click()

    #draw fence
    fence = p.locateOnScreen('fenceH.PNG', grayscale=True)
    fence_center = p.center(fence)
    p.moveTo(fence_center, duration=1)
    p.click()
    print("placing fence")
    #place fence by element
    #select fence type
    time.sleep(1)
    ftype = p.locateOnScreen('ftypeH.PNG', grayscale=True)
    ftype_center = p.center(ftype)
    p.moveTo(ftype_center, duration=1)
    a,b = ftype_center
    #Use variables to move a distance to right of ftype to get into input field
    #whether or not what text is showing in it currently
    a = a + 136
    p.moveTo(a,b)
    p.click()
    p.typewrite('e')
    p.moveTo(837, 220, duration=1)
    p.click()

    #go to main file menu
    p.moveTo(23, 34, duration=1)
    p.click()
    p.moveTo(50, 419, duration=1)
    p.click()

    #give the pop up window time to open before looking for image match
    time.sleep(5)

    #pop up print window file menu
    loc1 = p.locateOnScreen('loc1H.PNG', grayscale=True)
    loc1_center = p.center(loc1)
    p.moveTo(loc1_center, duration=1)
    p.click()

    #select printer
    print('selecting printer')
    time.sleep(2)
    p.typewrite('w')

    p.moveTo(1917, 1052, duration=1)
    p.click()
    time.sleep(2)
    p.click()
    time.sleep(1)

    #locate AdobePDF
    loc3 = p.locateOnScreen('loc3H.png', grayscale=True)
    loc3_center = p.center(loc3)
    p.moveTo(loc3_center, duration=1)
    p.doubleClick()

    #move to scale input
    time.sleep(1)
    loc4 = p.locateOnScreen('loc4H.PNG', grayscale=True)
    loc4_center = p.center(loc4)
    p.moveTo(loc4_center, duration=1)
    a,b = loc4_center
    #Use variables to move a distance to right of loc4 to get into input field
    #whether or not what text is showing in it currently
    a = a + 68
    p.moveTo(a,b)
    #scale input
    print('scaling')
    p.doubleClick()
    p.typewrite('1.44')
    p.typewrite(['enter'])

    #print
    loc5 = p.locateOnScreen('loc5H.PNG', grayscale=True)
    loc5_center = p.center(loc5)
    p.moveTo(loc5_center, duration=1)
    p.click()

    t = str(time.clock())
    #final message
    print("dgn printed to pdf in " + t + " seconds...")

    alert = p.confirm(text='Save DGN & Settings?', buttons=['Save','Cancel'])

#    if alert == 'Save':
#        p.click(34, 49)
#        p.typewrite('v')
#        p.click(34, 49)
#        p.typewrite('s')
#        p.click(1879, 8)
#        time.sleep(2)
#        OKCapture = p.locateOnScreen('OKCapture.PNG', grayscale=True)
#        OKCapture_center = p.center(OKCapture)
#        time.sleep(2)
#        p.moveTo(OKCapture_center, duration=1)
#        p.click()

#    elif alert == 'Cancel':
#        quit()

else:
    quit()

#TypeError: 'NoneType' object is not subscriptable
