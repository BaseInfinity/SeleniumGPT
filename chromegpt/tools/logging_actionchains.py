from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

class LoggingActionChains(ActionChains):
    def __init__(self, driver):
        super().__init__(driver)
        self._last_moved_element = None

    def move_to_element(self, to_element):
        self._last_moved_element = to_element
        return super().move_to_element(to_element)

    def click(self, on_element=None):
        with open("selenium_commands.log", "a") as f:
            target_element = on_element or self._last_moved_element
            if target_element and isinstance(target_element, WebElement):
                element_info = self._describe_element(target_element)
                f.write(f"ActionChains Clicked on element: {element_info}\n")
            else:
                f.write("ActionChains Clicked\n")
        return super().click(on_element=on_element)

    def _describe_element(self, element):
        attributes_to_log = ['id', 'name', 'class', 'tag_name', 'text']
        description = []

        for attr in attributes_to_log:
            try:
                value = getattr(element, attr)
                if value:
                    description.append(f"{attr}: {value}")
            except Exception:
                pass

        return ', '.join(description)
