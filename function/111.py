from function.browser import Browser
from time import sleep


a = Browser("Chrome")
a.open("http://www.baidu.com")
a.loc_method_select("id")
a.send_key("kw", "selenium")
a.click("su")
sleep(1)
a.clear("kw")
sleep(1)


a.open("http://www.hao123.com")
# a.close()
# sleep(1)
a.quit()

