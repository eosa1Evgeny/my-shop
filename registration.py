# вынес регистрацию в отдельный файл
import time
from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# неявное ожидание поиска элементов
driver.implicitly_wait(40)
wait = WebDriverWait(driver, 40)
driver.maximize_window()

# 1. Откройте http://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

# 2. Нажмите на вкладку "My Account Menu"
acc_link = driver.find_element(By.LINK_TEXT, "My Account")
acc_link.click()

# 3. В разделе "Register", введите email для регистрации
email_reg = driver.find_element(By.CSS_SELECTOR, '#reg_email')
email_reg.send_keys("eugene8@mail.ru")

# 4. В разделе "Register", введите пароль для регистрации
# составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# почту и пароль сохраните, потребуюутся в дальнейшем
time.sleep(5)
pwd_reg = driver.find_element(By.CSS_SELECTOR, '#reg_password')
pwd_reg.send_keys("133#$66dsajLLsdsjhsdlslI%")

# 5. Нажмите на кнопку "Register"
text_strong = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.woocommerce-password-strength.strong"), "Strong"))
print("text_strong: ", text_strong)
btn_reg = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="register"]')))
btn_reg.click()

time.sleep(5)
driver.quit()