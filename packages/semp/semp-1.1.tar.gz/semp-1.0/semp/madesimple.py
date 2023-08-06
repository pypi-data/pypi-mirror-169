from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
import sys

try:
    file = open(str(sys.argv[1]))
except:
    print("Error: No valid file name")
    quit()
thenum = file.readlines()
starter = thenum[0]

if starter.split()[0] == "browser":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("Driver error")
    quit()
while True:
    for num in range(len(thenum)):
        line = thenum[num]
        try:
            action = line.split()[0]
        except:
            pass
        try:
            second = line.split()[1]
        except:
            pass
        try:
            third = line.split()[2]
        except:
            pass
        if action == "goto":
            driver.get(second)
        elif action == "findelement":
                if second == "byname":
                    theelement = driver.find_element(By.NAME, third)
                elif second == "byid":
                    theelement = driver.find_element(By.ID, third)
                elif second == "byxpath":
                    theelement = driver.find_element(By.XPATH, third)
                elif second == "bycssselector":
                    theelement = driver.find_element(By.CSS_SELECTOR, third)
                else:
                    print("Invalid argument in line " + str(num + 1) + ": " + str(second))
                    quit()
        elif action == "sendkeys":
            theelement.send_keys(second)
        elif action == "clearelement":
            theelement.clear()
        elif action == "clickelement":
            theelement.click()
        elif action == "submitelement":
            theelement.submit()
        elif action == "doubleclickelement":
            theelement.double_click()
        elif action == "scroll":
            if second == "toelement":
                desired_y = (theelement.size['height'] / 2) + theelement.location['y']
                current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
                scroll_y_by = desired_y - current_y
                driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            else:
                try:
                    xcor = int(second)
                    ycor = int(third)
                    driver.scroll_by_amount(xcor, ycor)
                except:
                    print("Invalid argument in line " + str(num + 1))
                    quit()
        elif action == "alert":
            try:
                if second == "accept":
                    pass #Alert.(driver).accept()
                elif second == "dismiss":
                    pass #Alert.(driver).dismiss()
                else:
                    print("Invalid argument in line " + str(num + 1))
                    quit()
            except:
                pass
        elif action == "getscreenshot":
            try:
                driver.save_screenshot(second)
            except:
                print("Invalid file name: " + str(second))
                quit()
        elif action == "quit":
            driver.quit()
        elif action == "killbrowser":
            driver.kill()
        elif action == "refreshpage":
            driver.refresh()
        elif action == "quitsemp":
            quit()
        elif action == "sleep":
            try:
                waiter = int(second)
                time.sleep(waiter)
            except:
                print("Invalid argument in line " + str(num + 1) + ": " + str(second))
                quit()
        elif action == "browser":
            if num != 0:
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            else:
                pass
        else:
            print("Invalid argument in line " + str(num + 1) + ": " + str(action))
            quit()
