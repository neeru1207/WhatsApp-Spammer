#*****WhatsApp message spammer*****
#Coded by : Neeramitra Reddy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class WhatsAppSpammer():
    def __init__(self,ChromeWebDriverPath,TargetName,TargetMessage,NumberOfMessages,TimeInterval):
    #Let's use Google Chrome as our browser
        self.path = ChromeWebDriverPath
        self.web = webdriver.Chrome(self.path)
        self.TargetName = TargetName
        self.TargetMessage = TargetMessage
        self.NumberOfMessages = NumberOfMessages
        self.TimeInterval = TimeInterval
    def run(self):
        #Opening WhatsappWeb
        self.web.get('http://web.whatsapp.com')
        #After WhatsApp web opens, as you need to scan the QR code, the code will sleep for 20 seconds.
        time.sleep(20)
        x_arg = '//span[contains(text(),' + self.TargetName + ')]'
        elem = self.web.find_element_by_xpath(x_arg)
        elem.click()
        elem = self.web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for i in range(self.NumberOfMessages):
            elem.send_keys(self.TargetMessage)
            elem.send_keys(Keys.RETURN)
            time.sleep(int(self.TimeInterval))
