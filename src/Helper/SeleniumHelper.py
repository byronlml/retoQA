
class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)


###here you can create different selenium methods these are some examples###
# Send Keys
# Clicks
# Wait List



