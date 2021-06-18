import time
from selenium import webdriver

PROMISED_DOWN = 30
PROMISED_UP = 10
TWITTER_USER = 'twitter username'
TWITTER_PASS = 'password'
CHROME_DRIVER_PATH = "C:/Users/manit/OneDrive/Desktop/web development/CHROME/chromedriver_win32/" \
                     "chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        self.speed_up = 0
        self.speed_down = 0
        start_test = self.driver.find_element_by_class_name("start-text")
        start_test.click()

    def get_internet_speed(self):
        time.sleep(60)
        self.speed_down = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.speed_up = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        # return self.speed_up, self.speed_down

    def tweet_at_provider(self):
        if self.speed_down < self.down or self.speed_up < self.up:
            msg = f'Hey @Apfiber.net why is my internet speed {self.speed_down}/{self.speed_up} when I pay for' \
                   f' {self.down}/{self.up} in EastGodavari'
            self.driver.get('https://twitter.com/home')
            time.sleep(2)
            username = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            username.send_keys(TWITTER_USER)
            password = self.driver.find_element_by_name("session[password]")
            password.send_keys(TWITTER_PASS)
            time.sleep(2)
            signin = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span')
            signin.click()
            time.sleep(2)
            tweet = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            tweet.send_keys(msg)
            tweet_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_button.click()



internetspeedbot = InternetSpeedTwitterBot()
internetspeedbot.get_internet_speed()
internetspeedbot.tweet_at_provider()

