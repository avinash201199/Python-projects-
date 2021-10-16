from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 60, 0)

name = input("Enter the name of contact or group you want to text: ")
text = input("Enter the text you want to send: ")
n = int(input("Enter the number of times you want the text to be sent: "))
input(
    "Make sure you have scanned the QR code of whatsapp web. After that, press any key"
)

xarg = '//span[@title = "{}"]'.format(name)
user = wait.until(EC.presence_of_element_located((By.XPATH, xarg)))
user.click()

inp_xpath = '//*[@id="main"]/footer/div[1]/div/div[1]/div[2]/div[1]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

for i in range(n):
    input_box.send_keys(text)
    butn = "_4sWnG"
    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, butn)))
    button.click()
    if i % 10 == 0:
        print(i)
