from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from flask import Flask
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
from selenium.webdriver.chrome.options import Options


ans = []
cu = ['USDT','BNB','BTC','ETH']

class Bot():
    def scrap(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        self.browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
        self.browser.set_window_size(1024, 600)
        self.browser.maximize_window()
        for c in cu:
            self.browser.get("https://p2p.binance.com/en/trade/buy/{}".format(c))
            time.sleep(4)
            if(c == 'USDT'):
                self.browser.find_element_by_xpath('//main/div[4]/div/div/div[2]/div[2]/div').click()
       
                k = self.browser.find_element_by_xpath('//main/div[4]/div/div/div[2]/div[2]/div[3]/div/div/input')
                k.send_keys("INR")
                k.send_keys(Keys.ENTER)
                time.sleep(3)
            temp = []
            for i in range(4):
                t = {}
                try:
                    t["name"] = self.browser.find_element_by_xpath('//main/div[5]/div/div[2]/div[{}]/div/div/div/div/a'.format(i+1)).text
                    t["price"] = self.browser.find_element_by_xpath('//main/div[5]/div/div[2]/div[{}]/div/div[2]/div/div/div'.format(i+1)).text
                except:
                    pass
                temp.append(t)
            f = {}
            f[c] = temp
            ans.append(f)
           
        print(ans)

@app.route('/api',methods=['GET'])
def all():
    b = Bot()
    b.scrap()
    return {1:ans}
if __name__ == "__main__":
    app.run()
