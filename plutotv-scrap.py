from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://pluto.tv/latam/on-demand/618da9791add6600071d68b0")
    print(page.title())
    browser.close()
