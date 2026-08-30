

from playwright.sync_api import sync_playwright,Page,expect,playwright
from pages.orange_login import LoginPage


def test_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        lp = LoginPage(page)
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        expect (page.locator("//input[@placeholder='Username']")).to_be_visible()
        expect(page.locator("//input[@placeholder='Password']")).to_be_visible()
        expect(page.locator("//button[normalize-space()='Login']")).to_be_visible()
        expect(page.locator("//button[normalize-space()='Login']")).to_be_enabled()
        lp.login(
            "Admin",
            "admin123"
        )


        expect(page.locator("//p[normalize-space()='Time at Work']")).to_have_text("Time at Work")
        page.screenshot(path = "screenshots/img.png")
        browser.close()