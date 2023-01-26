#automation code for  ---->  https://testautomationpractice.blogspot.com/
#This script will automate each and every element on the website.
#This will help you to understand each concept of the selenium using python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import cv2
from pyzbar import pyzbar
import time
def using_chrome():
    opt=webdriver.ChromeOptions()
    opt.add_argument("--disable-notification")  #This will disable the notification popups given by the browser

    serv_obj = Service("C:\\Users\\Prerna\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\selenium\\webdriver\\drivers\\chromedriver.exe")  # chromedriver location
    driver = webdriver.Chrome(service=serv_obj,options=opt)
    return driver

#QR CODE SCANNER
def qr_code_scanner(path):
    img_path = path
    img = cv2.imread(img_path, 0)

    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
        bdata = barcode.data.decode("utf-8")
        btype = barcode.type
        text = f"{bdata},{btype}"
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


driver=using_chrome()
driver.implicitly_wait(5) #This will help to synchronise
driver.get("https://testautomationpractice.blogspot.com/") #opening the url
driver.maximize_window() #This will maximise the windowafter opening the url

#ELEMENT-->1   SEARCHBOX
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium") #entering text to the field
driver.find_element(By.XPATH,"//input[@type='submit']").click() #search button
links=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//div//a") #capture all the result link
print("Total number of results are ", len(links))
print("<----RESULT OF SEARCHED ITEM ARE---->")
for le in links:
    print(le.text)
    le.click() #This will click each result link
#switching each browser window and capturing the title of window
window_id=driver.window_handles
print()
print("<----WINDOW TITLE---->")
for i in window_id:
    driver.switch_to.window(i)
    print(driver.title)
#closing all the browser exceot the parent window
for i in window_id:
    driver.switch_to.window(i)
    if driver.title!="Automation Testing Practice":
        driver.close()
driver.switch_to.window(window_id[0])


#ELEMENT-->2   ALERT
driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']").click()
popup=driver.switch_to.alert
popup.accept()#closing popup by accepting the popup

#ELEMENT-->3   DATE PICKER

#Lets suppose we have to enter our birthdate
#date we have to enter
#scrolling till date picker arrives
driver.execute_script("window.scrollBy(0,2000)","")
year="2019"
month="August"
date="29"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    year_captured=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    month_captured=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    if int(year_captured)==int(year) and month_captured==month:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
date_table=driver.find_elements(By.XPATH, "//body[1]/div[5]/table[1]/tbody[1]/tr//td//a")
for i in date_table:
    if i.text==date:
        i.click()
        break


#ELEMENT-->3  DROPDOWN ELEMENTS
#selecting menus

#SELECTING SPEED
drp_element=driver.find_element(By.XPATH,"//select[@id='speed']")
drp_choice=Select(drp_element)
drp_choice.select_by_visible_text("Medium")

#SELECTING FILE
drp_element=driver.find_element(By.XPATH,"//select[@id='files']")
drp_choice=Select(drp_element)
drp_choice.select_by_visible_text("DOC file")

#SELECTING NUMBER
drp_element=driver.find_element(By.XPATH,"//select[@id='number']")
drp_choice=Select(drp_element)
drp_choice.select_by_visible_text("4")

#SELECTING PRODUCT
drp_element=driver.find_element(By.XPATH,"//select[@id='products']")
drp_choice=Select(drp_element)
drp_choice.select_by_visible_text("Bing")

#SELECTING ANIMAL
drp_element=driver.find_element(By.XPATH,"//select[@id='animals']")
drp_choice=Select(drp_element)
drp_choice.select_by_visible_text("Avatar")

#scrolling to text labels
driver.execute_script("window.scrollBy(0,1000)","")

#using correct xpath to get all  visual labels

#countig number of lables
#XPATH ---> //div[@id='Text1']//div[@class='widget-content']//child::span[starts-with(text(),'Message')]
labels=driver.find_elements(By.XPATH,"//div[@id='Text1']//div[@class='widget-content']//child::span[starts-with(text(),'Message')]")
print("No. of labels are ",len(labels))

#using is_displayed() command to check last two labels which are not visual
last_label=driver.find_element(By.XPATH,"//*[@id='Text1']/div[1]/div[7]")
last_label.is_displayed() #false

#USING XPATH AXES

#XPATH
#name ---> //empid[normalize-space()='101']//following::name
#designation ---> //empid[normalize-space()='101']//following::designation
#email ---> //empid[normalize-space()='101']//following::email

name=driver.find_elements(By.XPATH,"//empid[normalize-space()='101']//following::name")
designation=driver.find_elements(By.XPATH,"//empid[normalize-space()='101']//following::designation")
email=driver.find_elements(By.XPATH,"//empid[normalize-space()='101']//following::email")
print()
print("<----EMPLOYEE DETAILS---->")
print()
for i in range(0,3):
    print(name[i].text)
    print(designation[i].text)
    print(email[i].text)
    print()


#ELEMENT-->4   HTML TABLE

#counting number of rows
rs=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody//tr")
rows=len(rs)
print("NUMBER OF ROWS ",rows)
print()

#counting number of column
clm=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody//tr[1]//th")
column=len(clm)
print("NUMBER OF COLUMNS ",column)
print()

#printing the table
for r in range(2,rows+1):
    for c in range(1,column+1):
        cell=driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody//tr["+str(r)+"]//td["+str(c)+"]")
        print(cell.text,end="      ")
    print("\n")


#using hover mouse action to get a tooltip
act=ActionChains(driver)
element=driver.find_element(By.XPATH,"//input[@id='age']")
act.move_to_element(element).perform()
#passing value
element.send_keys("Prerana Maurya")

#ELEMENT-->5  frame
#FRAMES--->An inline frame (iframe) is a HTML element that loads another HTML page within the document.


#but in this website the source url is expired so we cannot locate the elements inside the frame
frame=driver.find_element(By.XPATH,"//iframe[@id='frame-one1434677811']")
driver.switch_to.frame(frame)
#switching to default content
driver.switch_to.default_content()

#Double click
double_cl_ele=driver.find_element(By.XPATH,"//input[@id='field2']")
act.double_click(double_cl_ele).perform()

#drag and drop
source_ele=driver.find_element(By.XPATH,"//div[@id='draggable']")
target_ele=driver.find_element(By.XPATH,"//div[@id='droppable']")
act.drag_and_drop(source_ele,target_ele).perform()
mr_john=driver.find_element(By.XPATH,"//li[1]")
mrs_mary=driver.find_element(By.XPATH,"//li[2]")
trash=driver.find_element(By.XPATH,"//div[@id='trash']")
act.drag_and_drop(mr_john,trash).perform()
act.drag_and_drop(mrs_mary,trash).perform()

#slider
slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
act.drag_and_drop_by_offset(slider,100,0).perform()

#Resizing the image
resize=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
act.drag_and_drop_by_offset(resize,10,0).perform()



#<-----------QR CODE SCANNING------------->
#QR 1

img=driver.find_element(By.XPATH,"//div[@id='HTML12']//img[1]")
time.sleep(3)
a=img.get_attribute("src")

# open new window with execute_script()
driver.execute_script("window.open('');") #opens new window
# switch to new window with switch_to.window()
driver.switch_to.window(driver.window_handles[1])
driver.get(a)

#saving the screenshot in a particular path to scan it
driver.save_screenshot(r"C:\Users\Prerna\PycharmProjects\selenium_automation\selenium_automation\qr1.png")
path=r"C:\Users\Prerna\PycharmProjects\selenium_automation\selenium_automation\qr1.png"
#calling the qr code scanner function
qr_code_scanner(path)

driver.close()
driver.switch_to.window(driver.window_handles[0])

#QR 2

img=driver.find_element(By.XPATH,"//div[@id='HTML4']//img")
time.sleep(3)
a=img.get_attribute("src")

# open new window with execute_script()
driver.execute_script("window.open('');") #opens new window
# switch to new window with switch_to.window()
driver.switch_to.window(driver.window_handles[1])
driver.get(a)

#saving the screenshot in a particular path to scan it
driver.save_screenshot(r"C:\Users\Prerna\PycharmProjects\selenium_automation\selenium_automation\qr2.png")
path=r"C:\Users\Prerna\PycharmProjects\selenium_automation\selenium_automation\qr2.png"
#calling the qr code scanner function
qr_code_scanner(path)

driver.close()
driver.switch_to.window(driver.window_handles[0])
#QR3
#you can do it with yourself just for practice

driver.quit()

#This project is made by
#NAME--> Prerana Maurya


















































































































