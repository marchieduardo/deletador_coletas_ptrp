from playwright.sync_api import sync_playwright
from time import sleep

print('ATENÇÃO!!! Interaja somente com o terminal!')
sleep(5)

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    # login
    page.goto('https://ptrp.com.br')
    page.get_by_role('textbox', name='Nome de usuário ou E-mail').fill(input('Digite seu e-mail: '))
    page.get_by_role('textbox', name='Senha' ).fill(input('Digite sua senha: '))
    page.get_by_role('button', name='Entrar').click()
    try:
        page.wait_for_selector('text=Painel Inicial')
    except:
        print("Erro ao fazer login. Verifique usuário e senha.")
        browser.close()
        exit()

    # seleção de cliente
    page.goto('https://ptrp.com.br/clientes')
    page.get_by_role('textbox', name='Buscar...').fill(input('Digite seu CNPJ formatado: '))
    page.get_by_role('button', name='').click()
    try:
        page.wait_for_selector('text=Mostrando 1 registro')
    except:
        print('Erro ao buscar CNPJ. Verifique o CNPJ digitado.')
        browser.close()
        exit()
    page.get_by_role('link', name='').click()

    # exclusão
    page.goto('https://ptrp.com.br/coletas')
    while True:
        page.get_by_role('link', name='Todos').click()
        try:
            page.locator('tr.data.element-link td').first.click()
            page.once('dialog', lambda dialog: dialog.accept())
            for c in range(2):
                page.get_by_role('link', name=' Excluir').click()
        except:
            print('Todas as coletas deletadas!')
            browser.close()
            exit()
