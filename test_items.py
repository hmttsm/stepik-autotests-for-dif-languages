#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
	browser.get(link)
#	time.sleep(30)
	basket_button = browser.find_element_by_css_selector(".add-to-basket .btn")
	assert basket_button, "there is no 'add to basket' button"