from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
question=input("""Enter the error or question, minimize the browser window that follows and sit back!!! : """)
driver=webdriver.Firefox()
print("Just a sec...")
driver.get('http://www.google.com')
search=driver.find_element_by_class_name('gsfi')
search.click()
search.send_keys(question+" site:www.stackoverflow.com")
search.send_keys(Keys.RETURN)
print("A little more...")
driver.implicitly_wait(20)
questionclick=driver.find_element_by_class_name("r")
questionclick.click()
print("Be patient.. \n\n\n")
driver.implicitly_wait(25)
answer = driver.find_elements_by_class_name("post-text")
votcount = driver.find_elements_by_class_name("vote-count-post")
for i in range(len(answer)):
    if(i==0):
        print("Question is \n")
    else:
        print("Answer: \n")
    print(answer[i].text)
    print("\n")
    print("Upvotes:" + votcount[i].text)
    print("\n")
print("Enter the number of the answer you want.. ")
n = int(input(''))
print("--"*20)
print("The chosen answer is: ")
print(answer[n].text)
print("--"*20)
print("\n\n\n#done")
driver.close()
