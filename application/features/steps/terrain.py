from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['version'] = 'latest'
    desired_capabilities['platform'] = 'WINDOWS'
    desired_capabilities['name'] = 'Testing Selenium with Lettuce'

    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="https://key:secret@hub.testingbot.com/wd/hub"
    )