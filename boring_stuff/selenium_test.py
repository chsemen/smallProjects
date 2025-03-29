from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox()
browser = webdriver.Chrome()
s = 'https://pypi.org/search/?q=boring%20stuff'
s='https://www.google.com/search?q=boring+stuff'
# s='https://ya.ru/search/?text=boring+stuff'

# browser.get('https://nostarch.com')
browser.get(s)
# htmlElem = browser.find_element(by=By.NAME, value='html')
# htmlElem = browser.find_element(by=By.XPATH, value='//*[@id="block-system-main"]/div')
htmlElem = browser.find_element(by=By.XPATH, value='/html/body')
#block-system-main > div

# htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scrolls to bottom
# htmlElem.send_keys(Keys.HOME) # scrolls to top

page_source = browser.page_source

with open('saved_page.html', 'w', encoding='utf-8') as f:
    f.write(page_source)

input('Press Enter to exit...')

browser.quit()