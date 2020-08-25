# YOU NEED TO BE CONNECTED TO THE INTERNET VIA A GERMAN VPN
# I USED WINDSCRIBE. IT's free and it's amazing.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import random
import string
import time
import os

class GET:
	@staticmethod
	def getPassword(length):
		letters = string.ascii_uppercase
		password = ''.join(random.choice(letters) for i in range(length-3))
		password += str(random.randint(100,999))
		return password
	@staticmethod
	def getEmail():
		URL_Email = "https://10minutemail.net/"
		email_page = requests.get(URL_Email)
		handle_email = BeautifulSoup(email_page.content, 'html.parser')
		email = handle_email.find(class_='div-m-0 text-c')
		email = str(email)[84:].replace("\"/></div>", '')
		return email
	@staticmethod
	def getIBAN():
		URL_DATA = 'http://fake-it.ws/fr'
		HANDLE = requests.get(URL_DATA)
		HANDLE = BeautifulSoup(HANDLE.content, 'html.parser')
		BIO = str(HANDLE.find(class_="content"))
		IBAN = BIO[5700:5780]
		IBAN = IBAN[(IBAN.find("value=")+7):]
		IBAN = IBAN[:(IBAN.find("\"/>"))]
		return IBAN
	@staticmethod
	def writeToFile(email, password):
		file = open("netflix_script.txt", 'a')
		write = ''
		write += email + ":" + password + '\n'
		file.write(write)
		file.close()
		print("\t [*] Data Successfully written to File")
class START():
	def __init__(self):
		self.IBAN = GET.getIBAN()
		while 'FR' not in self.IBAN and len(self.IBAN) != 27:
			self.IBAN = GET.getIBAN()	
		self.EMAIL = GET.getEmail()
		self.PASS = GET.getPassword(random.randint(8,16))
	def startDriver(self):
		print("""
			[-] EMAIL    : {}
			[-] PASSWORD : {}
			[-] IBAN     : {}
			""".format(self.EMAIL, self.PASS, self.IBAN))
		PATH = "/opt/WebDrivers/ChromeDriver" # Enter the path to Chrome driver here.
		self.driver = (webdriver.Chrome(PATH))
		self.exec()
	def exec(self):
		URL = "https://www.netflix.com/de-en/"
		putEmail = "//*[@id=\"id_email_hero_fuji\"]"
		getStarted = "//*[@id=\"appMountPoint\"]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div/div/button"
		continueButton = "//*[@id=\"appMountPoint\"]/div/div/div[2]/div/div[2]/button"
		password = "//*[@id=\"appMountPoint\"]/div/div/div[2]/div/form/div[1]/div[2]/ul/li[2]/div/div[1]/label"
		nextCon = "//*[@id=\"appMountPoint\"]/div/div/div[2]/div/form/div[2]/button"
		seeThePlans = "//*[@id=\"appMountPoint\"]/div/div/div[2]/div/div[2]/button"
		continueNext = "//*[@id=\"appMountPoint\"]/div/div/div[2]/div/div[3]/button"
		directDebit = "//*[@id=\"directDebitDisplayStringId\"]/a"
		firstName = "//*[@id=\"id_firstName\"]"
		lastName = "//*[@id=\"id_lastName\"]"
		birthDate = "//*[@id=\"appMountPoint\"]/div/div/div[2]/div/form/div[1]/div[2]/ul[1]/li[3]/div/div[1]/select"
		birthMonth = "//*[@id=\"appMountPoint\"]/div/div/div[2]/div/form/div[1]/div[2]/ul[1]/li[4]/div/div[1]"
		birthYear = "//*[@id=\"id_deDebitBirthYear\"]"
		street = "//*[@id=\"id_deDebitStreet\"]"
		postalCode = "//*[@id=\"id_deDebitPostalCode\"]"
		city = "//*[@id=\"id_deDebitCity\"]"
		setIBAN = "//*[@id=\"id_deDebitAccountNumber\"]"
		startMemberShip = "//*[@id=\"simplicityPayment-START\"]"
		lContinue = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/div[2]/button"
		smartTV = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/ul/li[1]/div"
		tablet  = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/ul/li[2]/div"
		setTopBox  = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/ul/li[4]/div"
		streamingMediaPlayer  = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/ul/li[5]/div"
		playStation  = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/ul/li[6]/div"
		xBox  = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/ul/li[7]/div"
		nContinue = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/div/button"
		profileName1 = "//*[@id=\"id_profile1Name\"]"
		profileName2 = "//*[@id=\"id_profile2Name\"]"
		profileName3 = "//*[@id=\"id_profile3Name\"]"
		profileName4 = "//*[@id=\"id_profile4Name\"]"
		nextContinueButton = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/div/form/div/button"
		continueAfterNames = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/div/form/div/button"
		langNextContinue = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/div[3]/div/button"
		lastConShows = "//*[@id=\"appMountPoint\"]/div/div/div/div[2]/div/div/form/div[2]/div[3]/button"
		try:
			self.driver.get((URL))
			self.driver.implicitly_wait(10)
			WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, putEmail))).send_keys(self.EMAIL)
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, getStarted))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, continueButton))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, password))).send_keys(self.PASS)
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, nextCon))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, seeThePlans))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, continueNext))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, directDebit))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, firstName))).send_keys("Javed")
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, lastName))).send_keys("Bajwa")
			GET.writeToFile(self.EMAIL, self.PASS)
			bDate = str(random.randint(1,25))
			bMont = str(random.randint(1,12))
			bYear = str(random.randint(1985,2002))
			Select(self.driver.find_element_by_xpath(birthDate)).select_by_value(bDate)
			Select(self.driver.find_element_by_xpath(birthMonth)).select_by_value(bMont)
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, birthYear))).send_keys(bYear)
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, street))).send_keys("Some Random Street Name")
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, postalCode))).send_keys(6969)
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, city))).send_keys("Paris")
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, setIBAN))).send_keys(self.IBAN)
			self.driver.implicitly_wait(10)
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, startMemberShip))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, lContinue))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, smartTV))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, tablet))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, setTopBox))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, streamingMediaPlayer))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, playStation))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, xBox))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, nContinue))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, profileName1))).send_keys("Name 1")
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, profileName2))).send_keys("Name 2")
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, profileName3))).send_keys("Name 3")
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, profileName4))).send_keys("Name 4")
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, nextContinueButton))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, continueAfterNames))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, langNextContinue))).click()
			WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, lastConShows))).click()
			time.sleep(10)
			self.driver.close()
		except:
			self.exec()
	def close(self):
		self.driver.close()
# END OF CLASSES
def create(numAccounts):
	for x in range(numAccounts):
		netflix = START()
		netflix.startDriver()
def main():
	print("""
		WELCOME TO NETFLIX ACCOUNT CREATOR BY @THEFLASH2K
		[+] How many accounts do you want to create?
		""")
	numAcc = int(input("\t\t> "))
	print("Creating {} accounts...".format(numAcc))
	create(numAcc)

if __name__ == "__main__":
	main()
