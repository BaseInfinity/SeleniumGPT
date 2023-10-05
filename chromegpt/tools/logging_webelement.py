from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

class LoggingWebElement(WebElement):
    def __init__(self, parent, id_, by=None, value=None):
        super().__init__(parent, id_)
        self._by = by
        self._value = value

    def click(self):
        self._log(f"Clicking on element located by {self._by}='{self._value}'")
        super().click()

    def send_keys(self, *value):
        readable_keys = self._translate_keys(value)
        self._log(f"Sending keys {readable_keys} to element located by {self._by}='{self._value}'")
        super().send_keys(*value)

    def find_element(self, by, value):
        element = super().find_element(by, value)
        return LoggingWebElement(element._parent, element._id, by, value)

    def find_elements(self, by, value):
        elements = super().find_elements(by, value)
        return [LoggingWebElement(element._parent, element._id, by, value) for element in elements]

    def _log(self, message):
        with open("selenium_commands.log", "a") as f:
            f.write(message + "\n")

    def _translate_keys(self, keys):
        special_keys = {
            '\ue009': 'Keys.CONTROL',
            '\ue017': 'Keys.END',
            '\ue006': 'Keys.ENTER',
            # Add other special keys as needed
        }
        return [special_keys.get(key, key) for key in keys]
