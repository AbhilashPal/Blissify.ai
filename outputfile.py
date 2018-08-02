from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpoem
import getfilm
import time
import scrape

def getout(X,Y):
	#getting poems
	poems = getpoem.getpoem(X)

	#getting films
	films = getfilm.getfilm(X)

	#music
	dicti = scrape.getMusic(Y)
	mX=dicti['x']
	mY=dicti['y']
	
	#opening output page
	driver = webdriver.Chrome()         
	driver.set_page_load_timeout(20)
	driver.get("file:///E:/hack2/index.html")
	driver.maximize_window()
	driver.implicitly_wait(50)

	#sending poems
	for i in range(1,6):
		elem =  driver.find_element_by_id("p"+str(i))
		elem.send_keys(poems[i-1])

		elemdash = driver.find_element_by_id("mv"+str(i))
		elemdash.send_keys(films[i-1])
	for i in range(1,len(mX)+1):
		elemdashdash = driver.find_element_by_id("m"+str(i))
		elemdashdash.send_keys(str(mX[i])+"("+str(mY[i])+")")
	

	time.sleep(500)
