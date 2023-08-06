# semp (Selenium-Made-Simple)
Semp is a markup language for selenium library which makes web manipulation easier and faster!

<img src="https://user-images.githubusercontent.com/73137174/192388381-40cc3879-b6bf-4954-b153-7e2c85e6b222.png" alt="drawing" width="200"/>

## Advantages of semp:
- Easy to understand
- Faster coding (no worries about syntax)
- Create web bots easier
- External .semp files
- Directly start from terminal

## How To Use:
browser / starts browser (browser used in line 1 is not in loop) \
goto *webaddress / go to website \
findelement (options: byname, byid, byxpath, bycssselector) *argument / find element by it's properties \
sendkeys *keys / send keys to element\
clearelement / clear element \
clickelement / click element \
submitelement / submit element \
doubleclickelement / Double-click element \
scroll *xcoordinate *ycoordinate / scroll to specified coordinate \
scroll toelement / scroll to selected element \
alert (options: accept, dismiss) / Accept or dismiss alert pop-up \
getscreenshot *filesource / Save screenshot of full-page \
quit / quit browser \
killbrowser/ kill browser \
quitsemp / quit semp \
sleep *second / waiting time until next process starts \
browser / starts browser again after quiting (used other than 1st line)

## Example .semp files:
[Example 1](https://github.com/dogumer/semp/blob/main/examples/example1.semp)
[Example 2](https://github.com/dogumer/semp/blob/main/examples/example2.semp)

## Libraries used in semp
[SeleniumHQ](https://github.com/SeleniumHQ) - [Selenium](https://github.com/SeleniumHQ/selenium) \
[Boni Garcia](https://github.com/bonigarcia/) - [WebDriverManager](https://github.com/bonigarcia/webdrivermanager)
