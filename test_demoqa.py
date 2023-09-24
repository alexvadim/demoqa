from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

browser = webdriver.Chrome()
browser.implicitly_wait(10)

def test1():
    with open('test.json', 'r') as test:
        test = json.loads(test.read())
    url = 'https://demoqa.com/'
    browser.get('https://demoqa.com/')
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div').click()
    browser.get('https://demoqa.com/elements')
    browser.find_element(By.XPATH, '//*[@id="item-1"]').click()
    browser.get('https://demoqa.com/checkbox')
    browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button').click()
    browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
    browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
    element = browser.find_element(By.XPATH,'//*[@id="result"]').text
    assert element == 'You have selected :\nwordFile', 'Ошибка!'


