from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://34.142.128.73:8237/")
    page.goto("http://34.142.128.73:8237/login")
    page.get_by_placeholder("输入用户名/邮箱地址").click()
    page.get_by_placeholder("输入用户名/邮箱地址").fill("wuqingyang")
    page.get_by_placeholder("输入密码").click()
    page.get_by_placeholder("输入密码").fill("Qwe123456")
    page.get_by_role("button", name="登录").click()
    page.get_by_role("button", name="安全漏洞种类").click()
    page.get_by_role("menuitem", name="安全漏洞种类").click()
    page.get_by_role("link", name="查看更多项目").click()
    page.get_by_role("link", name="TestXss").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)