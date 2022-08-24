import time
from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# неявное ожидание поиска элементов
driver.implicitly_wait(40)
driver.maximize_window()

##############################################################################################
# Home: добавление комментария
##############################################################################################

# 1. Откройте http://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
ruby = driver.find_element(By.CSS_SELECTOR, 'a[href="https://practice.automationtesting.in/product/selenium-ruby/"]>h3')
ruby.click()

# 4. Нажмите на вкладку "REVIEWS"
reviews = driver.find_element(By.CSS_SELECTOR, 'a[href="#tab-reviews"]')
reviews.click()

# 5. Поставьте 5 звёзд
reviews = driver.find_element(By.CSS_SELECTOR, 'a.star-5')
reviews.click()

# 6. Заполните поле "Review" сообщением: "Nice book!"
comment = driver.find_element(By.CSS_SELECTOR, '#comment')
comment.send_keys("Nice book!")

# 7. Заполните поле "Name"
author = driver.find_element(By.CSS_SELECTOR, '#author')
author.send_keys("Eugene")

# 8. Заполните "Email"
author = driver.find_element(By.CSS_SELECTOR, '#email')
author.send_keys("Eugene@mail.ru")

# 9. Нажмите на кнопку "SUBMIT"
submit_btn = driver.find_element(By.CSS_SELECTOR, 'input[name="submit"]#submit')
submit_btn.click()


driver.quit()
