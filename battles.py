import time
import pyautogui

def angel_farm():
    #Support summon
    choose_summon()
    time.sleep(2)

    #Support ok btn
    pyautogui.click(537, 905)
    time.sleep(8)

    choose_attacks()

    #Find and click okay
    while True:
        time.sleep(1)
        try:
            print("Searching for okay")
            img_loc = pyautogui.locateOnScreen("Images/ok.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find ok")

    #Find and click play again
    for i in range(50):
        #If emp, just click
        if i == 5:
            pyautogui.click(537, 905)
        time.sleep(1)
        try:
            print("Searching for playagain")
            img_loc = pyautogui.locateOnScreen("Images/playagain.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find playagain")
    
    time.sleep(5)

    #If dim halo nm pops up, click close and sleep for 5
    try:
        print("Looking for Dimensional Halo")
        img_loc = pyautogui.locateOnScreen("Images/close.png")
        pyautogui.click(img_loc[0], img_loc[1])
        if img_loc != None:
            print(img_loc)
            time.sleep(5)
    except:
        print("Can't find No Dimensional Halo")
    

    #If friend req, click cancel and sleep for 5
    try:
        print("Looking for Friend Req")
        img_loc = pyautogui.locateOnScreen("Images/cancel.png")
        pyautogui.click(img_loc[0], img_loc[1])
        if img_loc != None:
            print(img_loc)
            time.sleep(5)
    except:
        print("Can't find Friend Req")

    #If autorefill is true
    if auto_refill:
        try:
            print("Looking for Refill Use BTN")
            img_loc = pyautogui.locateOnScreen("Images/use.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                time.sleep(2)
                try:
                    print("Looking for ok")
                    img_loc = pyautogui.locateOnScreen("Images/ok.png")
                    pyautogui.click(img_loc[0], img_loc[1])
                    if img_loc != None:
                        print(img_loc)
                except:
                    print("Can't find ok")
        except:
            print("Can't find Friend Req")

    angel_farm()