import pyautogui
import time

#Support summon positions (408, 570) (355, 735) (360, 895) (379, 1041) (367, 1227)
#Okay btn after support (537, 905)
#Attack btn (551, 596)
#Auto btn (139, 627)
#Next btn (595, 592)
#Okay after finish(381, 735)
#backbtn in battle (135, 593)
#url loc (381, 73)

auto_refill = False

#Tracks mouse position on screen
def track():
    while True:
        time.sleep(2)
        print(pyautogui.position())

#Angel halo sequence
def choose_attacks2():

    #Click aglovale portrait
    while True:
        try:
            print("Searching for Aglovale")
            img_loc = pyautogui.locateOnScreen("Images/aglovale.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Aglovale")

    #Click aglovale skill 2 
    while True:
        try:
            print("Searching for Aglovale Skill 2")
            img_loc = pyautogui.locateOnScreen("Images/aglovale_ab2.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Aglovale Skill 2")
    time.sleep(8)
    pyautogui.click(595, 592)
    time.sleep(8)

    #Click swordmaster portrait
    while True:
        try:
            print("Searching for Sword Master")
            img_loc = pyautogui.locateOnScreen("Images/swordmaster.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Sword Master")

    #Click swordmaster skill 2 
    while True:
        try:
            print("Searching for Sword Master Skill 1")
            img_loc = pyautogui.locateOnScreen("Images/swordmaster_ab1.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Sword Master Skill 1")
    time.sleep(8)
    pyautogui.click(595, 592)
    time.sleep(8)


    #Click lily portrait
    while True:
        try:
            print("Searching for Lily")
            img_loc = pyautogui.locateOnScreen("Images/lily.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Lily")

    #Click lily skill 2 
    while True:
        try:
            print("Searching for Lily Skill 2")
            img_loc = pyautogui.locateOnScreen("Images/lily_ab2.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Lily Skill 2")
    time.sleep(8)
    pyautogui.click(595, 592)
    time.sleep(6)

    #pyautogui.click(135, 593)

#Verm stone farm
def choose_attacks():

    #Click aglovale portrait
    while True:
        try:
            print("Searching for Aglovale")
            img_loc = pyautogui.locateOnScreen("Images/aglovale.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Aglovale")

    #Click aglovale skill 2 
    while True:
        try:
            print("Searching for Aglovale Skill 2")
            img_loc = pyautogui.locateOnScreen("Images/aglovale_ab2.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Aglovale Skill 2")
    time.sleep(8)
    pyautogui.click(595, 592)
    time.sleep(8)

    #Click swordmaster portrait
    while True:
        try:
            print("Searching for Sword Master")
            img_loc = pyautogui.locateOnScreen("Images/swordmaster.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Sword Master")

    #Click swordmaster skill 2 
    while True:
        try:
            print("Searching for Sword Master Skill 1")
            img_loc = pyautogui.locateOnScreen("Images/swordmaster_ab1.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Sword Master Skill 1")
    time.sleep(8)
    pyautogui.click(595, 592)
    time.sleep(8)


    #Click lily portrait
    while True:
        try:
            print("Searching for Lily")
            img_loc = pyautogui.locateOnScreen("Images/lily.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Lily")

    #Click lily skill 2 
    while True:
        try:
            print("Searching for Lily Skill 2")
            img_loc = pyautogui.locateOnScreen("Images/lily_ab2.png")
            pyautogui.click(img_loc[0], img_loc[1])
            if img_loc != None:
                print(img_loc)
                break
        except:
            print("Can't find Lily Skill 2")
    time.sleep(8)
    pyautogui.click(595, 592)
    time.sleep(6)

    #pyautogui.click(135, 593)

#Choose summons in order of list, scrolls 5 times
def choose_summon(list_of_summons=[]):
    print("Looking for summons")
    pyautogui.moveRel(0,500)
    for i in range(5):
        for j in list_of_summons:
            try:
                print("Looking for " + j)
                img_loc = pyautogui.locateCenterOnScreen("Images/"+j)
                if img_loc != None:
                    time.sleep(2)
                    pyautogui.click(img_loc)
                    print(img_loc)
                    return
            except Exception:
                if Exception == KeyboardInterrupt:
                    return

                print("Can't find "+ j)

        pyautogui.scroll(-500)

    print("Clicking on first summon location")
    pyautogui.click(408, 570)

def verm_farm():
    #Support summon
    choose_summon()
    time.sleep(2)

    #Support ok btn
    pyautogui.click(537, 905)
    time.sleep(8)

    choose_attacks()

    #Attack btn
    #pyautogui.click(551, 596)
    #time.sleep(2)

    #Auto btn
    #pyautogui.click(139, 627)
    
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
    while True:
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
    verm_farm()

def angel_farm():
    #Support summon
    choose_summon(list_of_summons=["kaguya.png", "blackrabbit.png", "whiterabbit.png"])
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

def atk_seq(list_images):

    for image_name in list_images:

        #If need to click back:
        if image_name == "back":
            time.sleep(1)
            pyautogui.click(135, 593)
            continue

        #If need to click next
        if image_name == "next":
            time.sleep(1)
            pyautogui.click(595, 592)
            continue


        #If it's a number, pause a bit then continue next loop
        if image_name in ["1","2","3","4","5","6","7","8"]:
            print("Sleeping for "+ image_name + " seconds")
            time.sleep(int(image_name))
            continue

        #Otherwise, search until image located
        while True:
            try:
                print("Searching for "+image_name)
                img_loc = pyautogui.locateCenterOnScreen("Images/"+ image_name, confidence = 0.9)
                if img_loc != None:
                    time.sleep(2)
                    pyautogui.click(img_loc)
                    print(img_loc)
                    break
            except Exception:
                if Exception == KeyboardInterrupt:
                    return
                print("Can't find "+image_name)


def click_ok():
    #Find and click okay
    while True:
        try:
            print("Searching for okay")
            img_loc = pyautogui.locateCenterOnScreen("Images/ok.png", confidence = 0.9)
            if img_loc != None:
                time.sleep(1)
                pyautogui.click(img_loc)
                print(img_loc)
                break
        except Exception:
            if Exception == KeyboardInterrupt:
                return
            print("Can't find ok")

def check_noap():

    try:
        print("Searching for noap")
        img_loc = pyautogui.locateCenterOnScreen("Images/noap.png", confidence = 0.9)
        if img_loc != None:
            time.sleep(1)
            pyautogui.click(img_loc)
            print(img_loc)
            return True
    except Exception:
        if Exception == KeyboardInterrupt:
            return
        print("Can't find noap")
    return False


def refill():
    url = "http://game.granbluefantasy.jp/#item"

    #Type in url
    pyautogui.click(381, 73)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url)
    pyautogui.press("enter")

    atk_seq(list_images=["consumables.png", "halfelixir.png", "use.png"])

def antique_cloth_farm():
    url = "http://game.granbluefantasy.jp/#quest/supporter/704/0"

    for i in range(50):
        #Type in url
        pyautogui.click(381, 73)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(url)
        pyautogui.press("enter")

        choose_summon(list_of_summons=["kaguya.png", "blackrabbit.png", "whiterabbit.png"])

        click_ok()

        time.sleep(3)

        if check_noap():
            refill()
            continue

        click_ok()

        atk_seq(list_images=["lily.png", "lily_ab2.png", "next.png", "2", "swordmaster.png", "swordmaster_ab1.png", "next.png","2", "aglovale.png", "aglovale_ab3.png", "aglovale_ab2.png", "2", "reload.png"])

        click_ok()

        time.sleep(5)


#hard+
def hardplus_dailies():
    url_tia_hard = "http://game.granbluefantasy.jp/#quest/supporter/305011/1"
    url_colo_hard = "http://game.granbluefantasy.jp/#quest/supporter/305021/1"
    url_levi_hard = "http://game.granbluefantasy.jp/#quest/supporter/305031/1"
    url_ygg_hard = "http://game.granbluefantasy.jp/#quest/supporter/305041/1"
    url_chev_hard = "http://game.granbluefantasy.jp/#quest/supporter/305051/1"
    url_cele_hard = "http://game.granbluefantasy.jp/#quest/supporter/305061/1"

    hard_urls = [url_tia_hard, url_colo_hard, url_levi_hard, url_ygg_hard, url_chev_hard, url_cele_hard]

    "Go thru all hard+ stuff"
    for url in hard_urls:

        #Type in url
        pyautogui.click(381, 73)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(url)
        pyautogui.press("enter")

        choose_summon(list_of_summons=["europa.png", "gabriel.png"])

        click_ok()
        
        time.sleep(2)
        if check_noap():
            refill()
            #Type in url
            pyautogui.click(381, 73)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(url)
            pyautogui.press("enter")

            choose_summon(list_of_summons=["europa.png", "gabriel.png"])

            click_ok()
        
        if url != url_cele_hard:   
            atk_seq(list_images=["mechanic.png", "mechanic_ab1.png", "mechanic_ab2.png", "attack.png", "reload.png"])
        else:
            atk_seq(list_images=["mechanic.png", "mechanic_ab1.png", "mechanic_ab2.png", "back.png", "aglovale.png", "aglovale_ab1.png","attack.png", "reload.png"])

        click_ok()

        time.sleep(2)

def gw_dailies():
    url_verm_stone = "http://game.granbluefantasy.jp/#quest/supporter/102441/3"

    gw_urls = [url_verm_stone]

    for url in gw_urls:
        #Type in url
        pyautogui.click(381, 73)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(url)
        pyautogui.press("enter")

        choose_summon(list_of_summons=["kaguya.png", "blackrabbit.png", "whiterabbit.png"])

        click_ok()


#casino buy WIP
def casino_dailies():
    url = "http://game.granbluefantasy.jp/#casino"

    #Type in url
    pyautogui.click(381, 73)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url)
    pyautogui.press("enter")

    #atk_seq("casinocage.png", )

#refill()
#antique_cloth_farm()
#dailies()
#track()
#angel_farm()
hardplus_dailies()