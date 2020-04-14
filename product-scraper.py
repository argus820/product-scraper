from selenium import webdriver

class productInfo:
    def __init__(self,name,price):
        self.name=name
        self.price=price

def selector(url):
    def amazon():
        return "amazon\t"+driver.find_element_by_id("priceblock_ourprice").text

    def rakuten():
        return "rakuten\t"+driver.find_element_by_class_name("price2").text

    if "amazon" in url:
        return amazon()
    else:
        return rakuten()

l=[]
name=input("please input prices name\n")
while True:
    url=input("please input url\n")

    driver= webdriver.Chrome("c:\chromedriver.exe")
    driver.get(url)
    price=selector(url)
    driver.quit()

    l.append(price)

    mode=input("please input mode single character. continue=c,end=e\n")
    if mode=="e":
        break
    elif not mode=="c":
        print("error")
        exit()

print(name)
for i in range(len(l)):
    print(l[i])
