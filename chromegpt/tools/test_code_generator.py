
from chromegpt.tools.selenium_code_generator import (
    generate_selenium_code,
    wipe_selenium_code,
)

wipe_selenium_code()
generate_selenium_code("selenium_commands.log", "selenium_code.py")

