from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from chromegpt.tools.logging_webelement import LoggingWebElement

class LoggingWebDriver(webdriver.Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, url):
        with open("selenium_commands.log", "a") as f:
            f.write(f"Visited URL: {url}\n")
        super().get(url)

    def find_element(self, by, value):
        element = super().find_element(by, value)
        return LoggingWebElement(element._parent, element._id, by, value)

    def find_elements(self, by, value):
        elements = super().find_elements(by, value)
        return [LoggingWebElement(element._parent, element._id, by, value) for element in elements]


def clear_selenium_commands_log():
    with open("selenium_commands.log", "w") as f:
        f.write("")
