import os
import requests
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BOT_USER_PASSWORD = os.environ.get("BOT_USER_PASSWORD", "supersecret_bot_user_Password")


FLAG = os.environ.get("CHALLENGE_FLAG", "flag_missing_in_chall_config")


def botuser(post_id, base_url="http://127.0.0.1:5000"):
    try:
        if base_url[-1] != "/":
            base_url += "/"
        url = base_url + "botlogin"

        r = requests.get(url + "?id=" + BOT_USER_PASSWORD)

        cookie = r.cookies.get_dict()

        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(chrome_options=options)
        try:
                driver.get(base_url)
                driver.add_cookie({"name": "session", "value": cookie["session"]})
                driver.add_cookie({"name": "flag", "value": FLAG})
                driver.get(base_url + "post?id=" + str(post_id))
        except Exception as e:
                print(e)
        finally:
                driver.close()
                driver.quit()

    except Exception as e:
        traceback.print_exc()
