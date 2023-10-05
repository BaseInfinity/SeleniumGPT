import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def generate_selenium_code(log_file, test_file):
    key_map = {
        '\ue009a': ('Keys.CONTROL', 'a'),
        'Keys.END': 'Keys.END',
        'Keys.ENTER': 'Keys.ENTER',
    }

    with open(log_file, 'r') as log, open(test_file, 'w') as test:
        # Write the initial setup for the Selenium test
        test.write("from selenium import webdriver\n")
        test.write("from selenium.webdriver.common.by import By\n")
        test.write("from selenium.webdriver.common.keys import Keys\n\n")
        test.write("from selenium.webdriver.common.action_chains import ActionChains\n\n")
        test.write("driver = webdriver.Chrome()\n\n")
        test.write("driver.implicitly_wait(10)\n\n")

        for line in log:
            if "Visited URL:" in line:
                url = line.split("Visited URL:")[1].strip()
                test.write(f"driver.get('{url}')\n")
            elif "Clicking on element located by" in line or "Sending keys" in line:
                components = line.split("by")[1].split("=")
                by = components[0].strip()
                value = "=".join(components[1:]).strip().strip("'")
                if "Clicking on element located by" in line:
                    test.write(f"driver.find_element(By.{by.upper()}, \"{value}\").click()\n")
                elif "Sending keys" in line:
                    keys = line.split("keys")[1].split("to")[0].strip(" []").strip("'")
                    # Check if the key is in our map
                    if keys in key_map:
                        mapped_value = key_map[keys]
                        if isinstance(mapped_value, tuple):
                            keys_sequence = ", ".join(mapped_value)
                            test.write(f"driver.find_element(By.{by.upper()}, \"{value}\").send_keys({keys_sequence})\n")
                        else:
                            test.write(f"driver.find_element(By.{by.upper()}, \"{value}\").send_keys({mapped_value})\n")
                    else:
                        test.write(f"driver.find_element(By.{by.upper()}, \"{value}\").send_keys(\"{keys}\")\n")

            elif "ActionChains Clicked on element:" in line:
                text = re.search(r"text: (.+?)(,|$)", line).group(1).strip()
                tag_name = re.search(r"tag_name: (\w+),", line).group(1).strip()
                test.write(f"element = driver.find_element(By.XPATH, \"//{tag_name}[text()='{text}']\")\n")
                test.write("element.click()\n")

        # Close the driver at the end of the test
        test.write("\ndriver.quit()\n")

def wipe_selenium_code():
    with open("selenium_code.py", "w") as f:
        f.write("")
