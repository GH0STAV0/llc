import mod_driver
import mod_vpn

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import requests
import requests
import io
from pydub import AudioSegment
import time , random
import emoji
import speech_recognition as sr

#https://ltc-earn.com/r/47CF451BF nx20y635a@adhoc-orange.com
login_arry=['r5wzhv2gl@adhoc-yellow.com','0cvyfgegg@adhoc-orange.com','keiyzs2ol@adhoc-white.com','nx20y635a@adhoc-orange.com']
# login_arry=['mooui@adhoc-red.com','lihgh6zyw@adhoc-red.com','lqompzwun@adhoc-white.com','isis@adhoc-red.com']
login_email = random.choice(login_arry)

#print(ser,juj)

def ltc_login():
	try:
		mod_vpn.fnc_vpn ()
		serv,ops=mod_driver.build_driver()
		driver = webdriver.Firefox(service=serv, options=ops)
		extension_path="/root/OUOIO/LTC/src/canvasblocker44b.xpi"
		extension_path_ublock="/root/OUOIO/LTC/src/uBlock0_1.36.2.firefox.xpi"
		driver.install_addon(extension_path, True)
		driver.install_addon(extension_path_ublock, True)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.get("https://ltc-earn.com/home")
		#/html/body/header/nav/div/div/ul/li[5]
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/nav/div/div/ul/li[5]')))
		time.sleep(2)
		getLink_button.click()
		time.sleep(2)
		#/html/body/div[3]/div/div/form/div[1]/input
		#input()
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/form/div[1]/input')))

		getLink_button.click()
		time.sleep(3)

		getLink_button.send_keys(login_email)
		time.sleep(3)
		getLink_button.send_keys(Keys.TAB,"testpassword",Keys.ENTER)
		time.sleep(3)
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usd_balance"]')))
		print(getLink_button.text)
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		capatch(driver)
		pass
	except Exception as e:
		raise e


def audio_fonction(download_link):
	data = open('1.mp3', 'rb').read()
	print("ok"+download_link)
	request = requests.get(download_link)
	#print("ok3"+request.content)
	audio_file = io.BytesIO(request.content)
	#converted_audio = io.BytesIO()
	#audio_file = io.BytesIO(data)
	#input("ezeze")
	sound = AudioSegment.from_mp3(audio_file)
	dst = "test1.wav"
	sound.export(dst, format="wav")
	r = sr.Recognizer()
	with sr.WavFile("test1.wav") as source:
		audio = r.record(source)
	
	audio_output=r.recognize_google(audio)
	print("Transcription: " + audio_output)
	return audio_output







def capatch(driver):
	print("\n # STARTING CAPATCHA  ")
	print(" |")
	driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'without_captcha_button'))))
	main_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'without_captcha_button')))
	#main_button.send_keys(Keys.TAB ,Keys.ENTER,Keys.SPACE)
	#without_captcha_button
	time.sleep(9)
	number_fra=driver.find_elements_by_tag_name("iframe")
	print(str(len(number_fra)))#find_elements_by_class_name
	#driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
	time.sleep(2)
	input('check capatch')
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[2])
	time.sleep(5)
	recaptcha_ok=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rc-anchor-container"]/div[3]/div[1]/div/div')))
	print(" |")
	recaptcha_ok.click()
	time.sleep(5)
	driver.switch_to.default_content()
	time.sleep(5)#input('lets go to audio')
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[8])
	recaptcha_ok=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'recaptcha-audio-button')))
	recaptcha_ok.click()
	time.sleep(3)
	#driver.switch_to.default_content()
	# input('clicked  go to audio')
	eto_firstName=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'audio-source')))
	download_link = eto_firstName.get_attribute('src')
	# print("ok"+download_link)
	audio_output= audio_fonction(download_link)
	input('OOOOOOOOO  go to audio')


	number_fra = driver.find_elements_by_tag_name("iframe")
	for i in range(len(number_fra)):
		try:
			driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[i])
			print("switch"+str(i))
			time.sleep(2)
			eto_firstName=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'audio-source')))
			download_link = eto_firstName.get_attribute('src')
			print("ok"+download_link)
			# audio_fonction(download_link)
			print(" found")
			driver.switch_to.default_content()
			time.sleep(2)
			print(" found")
			break
			
		except Exception as e:
			print(e)
		driver.switch_to.default_content()

	input('cliccccccccccl go to audio')
	recaptcha_ok.click()
	input('lq')
	# try:



def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")





#audio_file="https://www.google.com/recaptcha/api2/payload?p=06AGdBq2729xPL4dTJeSJbmfEIE-LY4qNAyu1eNRDlNQpMrD9xrEJpiTgBHAOVn6gOY3HnsaZZf-o0-jvP5TkT-3el4g4drlQTgKe_AT-a-VfVBkpUj0_dccRF8m1KNRQ_B5dwTGGVO3NDuxzA5ZWZO-gA_N24km6Qjn7iHPcg9EeBO2rUu9xw27HQjhjQGgrHVEO6F3nln7Hw&k=6LcmLT4UAAAAAECBdhLUQg9OiUhoQbeOJzHpfhrS"
#audio_fonction(audio_file)
ltc_login()

init_fire()

# elenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
# driver.get('https://matricula.sistemaeliterio.com.br/Candidate/Registration/bolsao?schoolYear=2020&_ga=2.197375407.1653445941.1571361668-1911282789.1571361668')
# driver.find_element_by_xpath('//*[@id="registration-container"]/form/div[1]/div/div[1]/div[2]/div/div[1]').click()
# driver.find_element_by_xpath('//*[@id="registration-container"]/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[1]').click()
# driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.g-recaptcha#captcha-form"))))
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()