from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Secret import USERNAME, PASSWORD

class Linkedin:
	def __init__(self):
		self.driver = webdriver.Firefox(executable_path='C:\\Users\\NaiTuTreaba\\PycharmProjects\\webscrapper\\linkedin\\geckodriver.exe')
		self.driver.get('https://www.linkedin.com/home')
	def login(self):
		button = self.driver.find_element_by_xpath('//*[@id="session_key"]')
		button.send_keys(USERNAME)
		button = self.driver.find_element_by_xpath('//*[@id="session_password"]')
		button.send_keys(PASSWORD)
		button = self.driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button').click()
	def hr(self):
		self.driver.get('https://www.linkedin.com/jobs/search/?keywords=hr')
	def scroll_down(self):
		target = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[1]/div/div') 
		self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', target)
	def data_mining(self):
		items = self.driver.find_elements_by_class_name('artdeco-entity-lockup__title')
		jobs = [jobs.get_attribute('id') for jobs in items]
		for job in jobs:
			item = self.driver.find_element_by_id(job)
			item.click()
			dummy = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[2]/article/div/div[1]/span').text
			print(dummy)



