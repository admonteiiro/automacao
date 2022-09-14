from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    #acessar o site de login
    pagina.goto("https://sso.dynatrace.com/#email-verification-page")
    #colocar o e-mail
    pagina.fill('//*[@id="email_verify"]', "barretto@fastchannel.com")
    pagina.locator('//*[@id="next_button"]').click()
    #colocar a senha
    pagina.fill('//*[@id="password_login"]', "fdte22Fdte44")
    pagina.locator('//*[@id="no_captcha_submit"]').click()
    time.sleep(7)
    #abrir o "Problems"
    pagina.locator('//html/body/div[4]/div[1]/div/div[2]/div/div/div[3]/div[1]/div/div/a[3]').click()
    #abrir filtro
    pagina.locator('id=dt-filter-field-0').click()
    #clicar "severity"
    pagina.locator('//html/body/div[2]/div[3]/div/div/dt-option[2]/span').click()
    #clicar "erro"
    pagina.locator('//html/body/div[2]/div[3]/div/div/dt-option[3]/span').click()
    #clicar "impact level"
    pagina.locator('//html/body/div[2]/div[3]/div/div/dt-option[3]/span').click()
    #clicar "services"
    pagina.locator('//html/body/div[2]/div[3]/div/div/dt-option[2]/span').click()
    #clicar "Text"
    pagina.locator('//html/body/div[2]/div[3]/div/div/dt-option[8]/span').click()
    #escrever "Multiple service problems"
    pagina.fill('//html/body/app-root/ng-component/app-shell/main/pr-problems-overview/page-content/div/dt-quick-filter/dt-filter-field/div/div[3]/input', "Multiple service problems")
    pagina.keyboard.press("Enter")
    #clicar na data
    pagina.locator('//html/body/app-root/ng-component/app-shell/header/div/div/app-shell-top-bar/shell-app-second-gen-top-bar-content/div[2]/global-time-frame-selector/div/time-frame-selector/div/a/span/span').click()
    #selecionar período
    pagina.fill('//html/body/app-root/ng-component/app-shell/header/div/div/app-shell-top-bar/shell-app-second-gen-top-bar-content/div[2]/global-time-frame-selector/div/time-frame-selector/div/div/div/input', "-90d to now")
    pagina.keyboard.press("Enter")
    pagina.locator('//html/body/app-root/ng-component/app-shell/main/pr-problems-overview/page-content/div/dt-quick-filter/dt-drawer-container/div/div/dt-card/div[2]/pr-problems-table/dt-container-breakpoint-observer/dt-table/dt-expandable-row[1]/div[1]/dt-cell[2]/dt-info-group/div/dt-info-group-title/a').click()
    #show more
    pagina.locator('id=gwt-uid-31').click()
    #coletando a div
    categoria = pagina.locator('div.gwt-Label dYk-Lc')
    sub1 = pagina.locator('div.dYk-Mc')
    sub2 = pagina.locator('div.dYk-Mc')
    print(categoria)
    print(sub1)
    print(sub2)
