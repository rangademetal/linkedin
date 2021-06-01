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
	def next_page(self):
		dummy = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[1]/div/div/section/div/ul/li[10]/button').text	
		return 25*(int(dummy)-1)
		
	def data_mining(self):
		items = self.driver.find_elements_by_class_name('artdeco-entity-lockup__title')
		jobs = [jobs.get_attribute('id') for jobs in items]
		for job in jobs:
			item = self.driver.find_element_by_id(job)
			item.click()
			dummy = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]/a/h2').text
			# Job description
			print(dummy) 
			dummy = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[2]/article/div/div[1]/span').text
			# job function
			print(dummy)
			dummy = self.driver.find_element_by_xpath(f'//*[@id="{job}"]').text
			# company
			print(dummy)
			dummy = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span[3]').text
			# Location
			print(dummy) 
			# level
			dummy = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/ul/li[1]/div/ul/li[1]/span').text
			print(dummy)
			# number of aplications on the job
			dummy = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/ul/li[1]/div/ul/li[2]/span').text
			print(dummy)
	def next(self, total_jobs, jobs):
		if total_jobs != jobs:
			self.driver.get(f'https://www.linkedin.com/jobs/search/?keywords=hr&start={jobs}')



			



