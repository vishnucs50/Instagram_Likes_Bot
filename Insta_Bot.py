import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
    def closeBrowser(self):
        self.driver.close()
    def login(self):

        driver = self.driver
        driver.get("https://www.instagram.com/?hl=en")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@'href='/accounts/login/']")
        login_button.click()
        time.sleep(2)
        user_name_element = driver.find_element_by_xpath("//input[@name='username' ]")
        user_name_element.clear()
        user_name_element.send_keys(self.username)
        pwd_element = driver.find_element_by_xpath("//input[@name='password' ]")
        pwd_element.clear()
        pwd_element.send_keys(self.password)
        pwd_element.send_keys(keys.RETURN)
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body,scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]

        for pic_href in pic_hrefs :
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body,scrollHeight);")
            try:
                driver.find_element_by_link_text("Like").click()
                time.sleep(18)
            except Exception as e:
                time.sleep(2)









        # "//a[@'href'accounts/login']"
        # "//input[@name='username' ]"
        # "//input[@name='password']"

name = input("Enter username: ")
pwd = input("Enter Password: ")
VkIG = InstagramBot(name,pwd)
VkIG.login()
VkIG.like_photo("likes")

hashtags = ['like4like', 'like for like', 'followfor follow', 'landscape']
[VkIG.like_photo(tag) for tag in hashtags]