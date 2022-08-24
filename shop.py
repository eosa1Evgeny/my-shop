import time
from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# неявное ожидание поиска элементов
driver.implicitly_wait(40)
wait = WebDriverWait(driver, 40)
driver.maximize_window()

##############################################################################################
#  логин в систему
##############################################################################################
# 1. Откройте http://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
# 2. Нажмите на вкладку "My Account Menu"
acc_link = driver.find_element(By.LINK_TEXT, "My Account")
acc_link.click()
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
email_login = driver.find_element(By.CSS_SELECTOR, '#username')
email_login.send_keys("eugene8@mail.ru")
# 4. В разделе "Password", введите пароль для логина # данные можно взять из предыдущего теста
pwd_login = driver.find_element(By.CSS_SELECTOR, '#password')
pwd_login.send_keys("133#$66dsajLLsdsjhsdlslI%")
# 5. Нажмите на кнопку "Login"
btn_reg = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="login"]')))
btn_reg.click()
# 6. Добавьте проверку, что на странице есть элемент "Logout"
text_logout = wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'li>a[href="https://practice.automationtesting.in/my-account/customer-logout/"]'), "Logout"))
if text_logout:
    print("Logout обнаружен")
else:
    print("Logout не обнаружен ")
    exit()



##############################################################################################
# Shop: отображение страницы товара
##############################################################################################
# Нажмите на вкладку "Shop"
shop_link = driver.find_element(By.LINK_TEXT, "Shop")
shop_link.click()

# Откройте книгу "HTML 5 Forms"
img_html = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Mastering HTML5 Forms"]')))
img_html.click()

# Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
title_book = driver.find_element(By.CSS_SELECTOR, 'h1.product_title')
title_book = title_book.text
assert title_book == "HTML5 Forms"
print("загловок: HTML5 Forms")

##############################################################################################
# Shop: количество товаров в категории
##############################################################################################
# Нажмите на вкладку "Shop"
shop_link = driver.find_element(By.LINK_TEXT, "Shop")
shop_link.click()

# Откройте категорию "HTML"
shop_link = driver.find_element(By.LINK_TEXT, "HTML")
shop_link.click()

# Добавьте тест, что отображается три товара
count_book = driver.find_element(By.CSS_SELECTOR, 'li.cat-item-19>span.count')
count_book = int(count_book.text.replace('(', '').replace(')', ''))
assert count_book == 3
print("3 товара в разделе HTML")

##############################################################################################
# Shop: сортировка товаров
##############################################################################################
# 3. Нажмите на вкладку "Shop"
shop_link = driver.find_element(By.LINK_TEXT, "Shop")
shop_link.click()

# Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# Используйте проверку по value
select_value = driver.find_element(By.CSS_SELECTOR, 'select.orderby>option[value="menu_order"]')
assert select_value.get_attribute("selected")
print("Default sorting установлен по умолчанию")

# Отсортируйте товары по цене от большей к меньшей
# в селекторах используйте класс Select
sorting = driver.find_element(By.CSS_SELECTOR, 'select.orderby')
select = Select(sorting)
select.select_by_value("price-desc")

# Снова объявите переменную с локатором основного селектора сортировки
# т.к после сортировки страница обновится
# Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# Используйте проверку по value
select_value = driver.find_element(By.CSS_SELECTOR, 'select.orderby>option[value="price-desc"]')
assert select_value.get_attribute("selected")
print("Селект от большей к меньшей установлен.")



##############################################################################################
# Shop: отображение, скидка товара
##############################################################################################
# Нажмите на вкладку "Shop"
shop_link = driver.find_element(By.LINK_TEXT, "Shop")
shop_link.click()

# Откройте книгу "Android Quick Start Guide"
img_html = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Android Quick Start Guide"]')))
img_html.click()

# Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
old_price = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.price>del>span')))
assert old_price.text == "₹600.00"
print("старая цена:", old_price.text)

# Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
new_price = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.price>ins>span')))
assert new_price.text == "₹450.00"
print("новая цена:", new_price.text)

# Добавьте явное ожидание и нажмите на обложку книги
android_book = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[title="Android Quick Start Guide"]')))
android_book.click()

# Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
android_img = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[title="Android Quick Start Guide"]')))

# Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close_img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.pp_close')))
close_img.click()


##############################################################################################
# Shop: проверка цены в корзине
##############################################################################################
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("https://practice.automationtesting.in/")
# 2. Нажмите на вкладку "Shop"
shop_link = driver.find_element(By.LINK_TEXT, "Shop")
shop_link.click()
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
add_book = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/?add-to-cart=182"]')
add_book.click()
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# Используйте для проверки assert
item_text = WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.wpmenucartli"), "1 Item₹180.00"))
assert item_text
print('item_text количество товаров = "1 Item", а стоимость = "₹180.00')

# 5. Перейдите в корзину
cart = driver.find_element(By.CSS_SELECTOR, 'a.wpmenucart-contents')
cart.click()

# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
text_subtotal = WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr>td[data-title="Subtotal"]>span' ), "₹180.00"))
assert text_subtotal
print('в Subtotal отобразилась стоимость ')

# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
text_total = WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr>td[data-title="Total"]>span' ), "₹180.00"))
assert text_total
print('в total отобразилась стоимость ')



##############################################################################################
# Shop: работа в корзине
##############################################################################################
# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# 2. Нажмите на вкладку "Shop"
shop_link = driver.find_element(By.LINK_TEXT, "Shop")
shop_link.click()
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# После добавления 1-й книги добавьте sleep
# Для 2K монитора добавил скроллинг 900
driver.execute_script("window.scrollBy(0, 900);")
add_book = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/?add-to-cart=182"]')
add_book.click()
time.sleep(3)
add_book = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/?add-to-cart=180"]')
add_book.click()
# здесь тоже слип, иначе вторая книга не успевает попасть в корзину
time.sleep(5)
# 4. Перейдите в корзину
cart = driver.find_element(By.CSS_SELECTOR, 'a.wpmenucart-contents')
cart.click()

# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
time.sleep(3)
del_book = driver.find_element(By.CSS_SELECTOR, 'td.product-remove>a')
del_book.click()

# 6. Нажмите на Undo (отмена удаления)
undo_link = driver.find_element(By.LINK_TEXT, "Undo?")
undo_link.click()

# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
#  Предварительно очистите поле с помощью локатор_поля.clear()
quantity_JS = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1)>td>.quantity>input')
# так тоже работает:
# quantity_JS.send_keys(Keys.DELETE)
quantity_JS.clear()
quantity_JS.send_keys(3)

# 8. Нажмите на кнопку "UPDATE BASKET"
update = driver.find_element(By.CSS_SELECTOR, 'input[name="update_cart"]')
update.click()

# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
assert int(quantity_JS.get_attribute("value")) == 3
print("value = ", quantity_JS.get_attribute("value"))

# 10. Нажмите на кнопку "APPLY COUPON"
# Перед нажатимем добавьте sleep
time.sleep(5)
coupon = driver.find_element(By.CSS_SELECTOR, 'input[name="apply_coupon"]')
coupon.click()
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
text_coupon = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, 'ul.woocommerce-error>li' ), "Please enter a coupon code."))
assert text_coupon
print('отобразилась: Please enter a coupon code.')


##############################################################################################
# Shop: покупка товара
##############################################################################################
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop_link = driver.find_element(By.LINK_TEXT, "Shop")
shop_link.click()
# Для 2K монитора добавил скроллинг 400
driver.execute_script("window.scrollBy(0, 400);")

# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
add_book = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/?add-to-cart=182"]')
add_book.click()

# 4. Перейдите в корзину
# здесь тоже слип, иначе книга не успевает попасть в корзину
time.sleep(5)
cart = driver.find_element(By.CSS_SELECTOR, 'a.wpmenucart-contents')
cart.click()

# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
checkout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://practice.automationtesting.in/checkout/"]')))
checkout.click()

# 6. Заполните все обязательные поля
# Перед заполнением first name, добавьте явное ожидание
# Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# Что-бы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
first_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="billing_first_name"]')))
first_name.send_keys("Vasiliy")

last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="billing_last_name"]')
last_name.send_keys("Pumpkin")

email = driver.find_element(By.CSS_SELECTOR, 'input[name="billing_email"]')
email.send_keys("vasiliy@mail.ru")

phone = driver.find_element(By.CSS_SELECTOR, 'input[name="billing_phone"]')
phone.send_keys("+78546678585")

address = driver.find_element(By.CSS_SELECTOR, 'input[name="billing_address_1"]')
address.send_keys("Lenina st. d1 kv1")

city = driver.find_element(By.CSS_SELECTOR, 'input[name="billing_city"]')
city.send_keys("Saratov")

postcode = driver.find_element(By.CSS_SELECTOR, 'input[name="billing_postcode"]')
postcode.send_keys("418700")

country = driver.find_element(By.CSS_SELECTOR, 'div#s2id_billing_country')
country.click()
country_input = driver.find_element(By.CSS_SELECTOR, '#s2id_autogen1_search')
country_input.send_keys("Albania")
country_find = driver.find_element(By.CSS_SELECTOR, 'li.select2-results-dept-0.select2-result.select2-result-selectable')
country_find.click()

postcode = driver.find_element(By.CSS_SELECTOR, 'input[name="billing_state"]')
postcode.send_keys("Albania state")

# 7. Выберите способ оплаты "Check Payments"
# 2k монитор
driver.execute_script("window.scrollBy(0, 1200);")
time.sleep(5)
check_payments = driver.find_element(By.CSS_SELECTOR, 'input[value="cheque"]')
check_payments.click()

# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
# 8. Нажмите PLACE ORDER
place_order = driver.find_element(By.CSS_SELECTOR, 'input#place_order')
place_order.click()

# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
text_order = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, 'p.woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
assert text_order
print('отобразилась: Thank you. Your order has been received..')

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
text_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, 'tfoot>:nth-child(3)>td'), "Check Payments"))
assert text_check
print('отобразилась: Check Payments')


##############################################################################################
driver.quit()

