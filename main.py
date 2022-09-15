from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    page = navegador.new_page()
    #acessar o site de login
    page.goto("https://sso.dynatrace.com/#email-verification-page")

    #colocar o e-mail
    page.fill('//*[@id="email_verify"]', "barretto@fastchannel.com")
    page.locator('//*[@id="next_button"]').click()

    #colocar a senha
    page.fill('//*[@id="password_login"]', "fdte22Fdte44")
    page.locator('//*[@id="no_captcha_submit"]').click()
    time.sleep(2)

    #abrir o "Problems"
    page.locator('//html/body/div[4]/div[1]/div/div[2]/div/div/div[3]/div[1]/div/div/a[3]').click()

    #abrir filtro
    page.locator('id=dt-filter-field-0').click()

    #clicar "severity"
    page.locator('//html/body/div[2]/div[3]/div/div/dt-option[2]/span').click()

    #clicar "erro"
    page.locator('//html/body/div[2]/div[3]/div/div/dt-option[3]/span').click()

    #clicar "impact level"
    page.locator('//html/body/div[2]/div[3]/div/div/dt-option[3]/span').click()

    #clicar "services"
    page.locator('//html/body/div[2]/div[3]/div/div/dt-option[2]/span').click()

    #clicar "Text"
    page.locator('//html/body/div[2]/div[3]/div/div/dt-option[8]/span').click()

    #escrever "Multiple service problems"
    page.fill('//html/body/app-root/ng-component/app-shell/main/pr-problems-overview/page-content/div/dt-quick-filter/dt-filter-field/div/div[3]/input', "Multiple service problems")
    page.keyboard.press("Enter")

    #clicar na data
    page.locator('//html/body/app-root/ng-component/app-shell/header/div/div/app-shell-top-bar/shell-app-second-gen-top-bar-content/div[2]/global-time-frame-selector/div/time-frame-selector/div/a/span/span').click()

    #selecionar período
    page.fill('//html/body/app-root/ng-component/app-shell/header/div/div/app-shell-top-bar/shell-app-second-gen-top-bar-content/div[2]/global-time-frame-selector/div/time-frame-selector/div/div/div/input', "-90d to now")
    page.keyboard.press("Enter")
    time.sleep(2)
    #abrir primeiro erro

    page.locator('//html/body/app-root/ng-component/app-shell/main/pr-problems-overview/page-content/div/dt-quick-filter/dt-drawer-container/div/div/dt-card/div[2]/pr-problems-table/dt-container-breakpoint-observer/dt-table/dt-expandable-row[2]/div[1]/dt-cell[2]/dt-info-group/div/dt-info-group-title/a').click()
    #show more
    page.locator('id=gwt-uid-31').click()

    #coletando dados da div
    rows = page.locator("div.dYk-Cc")
    texts = rows.all_text_contents()
    count = rows.count()
    for i in range(count):
        print(rows.nth(i).text_content())
    texts = rows.evaluate_all("list => list.map(element => element.textContent)")

    rows = page.locator("div.dIc-x")
    texts = rows.all_text_contents()
    count = rows.count()
    for i in range(count):
        print(rows.nth(i).text_content())
    texts = rows.evaluate_all("list => list.map(element => element.textContent)")

    page.go_back()
    time.sleep(5)

    page.locator('//html/body/app-root/ng-component/app-shell/main/pr-problems-overview/page-content/div/dt-quick-filter/dt-drawer-container/div/div/dt-card/div[2]/pr-problems-table/dt-container-breakpoint-observer/dt-table/dt-expandable-row[2]/div[1]/dt-cell[2]/dt-info-group/div/dt-info-group-title/a').click()
    page.locator('id=gwt-uid-31').click()
    rows = page.locator("div.dYk-Cc")
    texts = rows.all_text_contents()
    count = rows.count()
    for i in range(count):
        print(rows.nth(i).text_content())
    texts = rows.evaluate_all("list => list.map(element => element.textContent)")

    rows = page.locator("div.dIc-x")
    texts = rows.all_text_contents()
    count = rows.count()
    for i in range(count):
        print(rows.nth(i).text_content())
    texts = rows.evaluate_all("list => list.map(element => element.textContent)")


