#MADE BY "AMAN PANDEY"
#FIXED BY @MADBOY482
#MODIFIED BY @GODBOYX
import asyncio
import os
import random
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from . import *


# Google Drive ()
CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
    
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "X USER"

CARBONLANG = "auto"
LANG = "en"

@BaseClient.on(X_cmd(pattern="carbon"))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Carbonizing the image..`")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    pcode = deEmojify(pcode)
    code = quote_plus(pcode)  # Converting to urlencoded
    godboy = await edit_or_reply(e, "`Carbonizing...\n25%`")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by godboy482
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await godboy.edit("`Be Patient...\n50%`")
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await godboy.edit("`Processing..\n75%`")
    # Waiting for downloading
    await asyncio.sleep(2)
    await godboy.edit("`Done Dana Done...\n100%`")
    file = "./carbon.png"
    await godboy.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Here we go with ur Karbon.\nCarbonised by Extre USERBOT",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    driver.quit()
    # Removing carbon.png after uploading
    await godboy.delete()


@BaseClient.on(X_cmd(pattern="krb"))
async def carbon_api(e):
    godboy = await edit_or_reply(e, "`Karbonizing The Image....`")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[5:]:
        pcodee = str(pcode[5:])
        if "|" in pcodee:
            pcode, skeme = pcodee.split("|")
        else:
            pcode = pcodee
            skeme = None
    elif textx:
        pcode = str(textx.message)
        skeme = None  # Importing message to module
    pcode = deEmojify(pcode)
    code = quote_plus(pcode)  # Converting to urlencoded
    await godboy.edit("`Meking Carbon...`\n`25%`")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by madboy482
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await godboy.edit("`Be Patient...\n50%`")
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]"
    ).click()
    if skeme is not None:
        k_skeme = driver.find_element_by_xpath(
            "/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]/input"
        )
        k_skeme.send_keys(skeme)
        k_skeme.send_keys(Keys.DOWN)
        k_skeme.send_keys(Keys.ENTER)
    else:
        color_scheme = str(random.randint(1, 29))
        driver.find_element_by_id(("downshift-0-item-" + color_scheme)).click()
    driver.find_element_by_id("export-menu").click()
    driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await godboy.edit("`Processing..\n75%`")
    # Waiting for downloading
    await asyncio.sleep(2.5)
    color_name = driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]/input"
    ).get_attribute("value")
    await godboy.edit("`Done Dana Done...\n100%`")
    file = "./carbon.png"
    await godboy.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="`Here's your carbon!` \n**Colour Scheme: **`{}`".format(color_name),
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    driver.quit()
    await godboy.delete()

