from selenium import webdriver
from selenium import 
class Linkedin:
	def __init__(self):
		self.driver = webdriver.Firefox(executable_path='C:\\Users\\NaiTuTreaba\\PycharmProjects\\webscrapper\\linkedin\\geckodriver.exe')
		self.driver.get('https://www.linkedin.com/home')
	def login(self):
		button = self.driver.find_element_by_xpath('//*[@id="session_key"]').click()
		button.send_keys('test')
