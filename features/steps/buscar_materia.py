from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from bs4 import BeautifulSoup
import time

url = 'https://sigaa.ifsc.edu.br/sigaa/public/home.jsf'

@given(u'Acessar o sistema Sigaa do ifsc')
def step_impl(context):
    context.driver.get(url)
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="acesso"]/ul/li[2]/a'))).click()
    time.sleep(3)

@when(u'Realizo o login no sistema')
def step_impl(context):
    user = ''
    pswd = ''

    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[1]/td/input'))).send_keys(user)
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[2]/td/input'))).send_keys(pswd)
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/table/tfoot/tr[2]/td/button'))).click()
    time.sleep(3)

@when(u'expando o menu Ensino')
def step_impl(context):
    ensino = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu_form_menu_discente_j_id_jsp_1383391995_85_menu"]/table/tbody/tr/td[1]')))
    action = ActionChains(context.driver)
    action.move_to_element(ensino).perform()
    time.sleep(3)

@when(u'clico em Consultar Estrutura curricular')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cmSubMenuID1"]/table/tbody/tr[15]/td[2]'))).click()
    time.sleep(3)


@when(u'busco o curso de ADS de canoinhas')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="busca:curso"]'))).click()
    time.sleep(1)
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="busca:curso"]/option[19]'))).click()
    time.sleep(1)
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="busca"]/table/tfoot/tr/td/input[1]'))).click()
    time.sleep(3)


@when(u'clico em Relatorio da Estrutura curricular do curso ADS 2021.1')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.ID, 'resultado:relatorio'))).click()
    time.sleep(3)


@when(u'salvo as materias em um arquivo txt')
def step_impl(context):
    table = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="relatorio"]/table/tbody/tr[13]/td/table')))
    content_html = table.get_attribute('outerHTML')
    soup = BeautifulSoup(content_html, 'html.parser')
    
    with open('materias.txt', 'w') as data:
        line = ''
        for row in soup.find_all('tr'):
            line = ''
            for column in row.find_all('td'):
                line = line + column.text
            data.write(';' + line + ';' + '\n')

@when(u'clico em voltar')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="relatorio-rodape"]/p/table/tbody/tr/td[1]/a'))).click()
    time.sleep(3)

@then(u'clico em sair')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="info-sistema"]/div/span[3]/a'))).click()
    time.sleep(3)