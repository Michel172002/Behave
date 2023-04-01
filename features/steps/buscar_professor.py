from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from bs4 import BeautifulSoup
import time

@given(u'Acessar novamento o sigaa')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="acesso"]/ul/li[2]/a'))).click()
    time.sleep(3)

@when(u'Realizar o login novamente')
def step_impl(context):
    user = 'erick.mr'
    pswd = 'Games2011'

    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[1]/td/input'))).send_keys(user)
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[2]/td/input'))).send_keys(pswd)
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/table/tfoot/tr[2]/td/button'))).click()
    time.sleep(3)

@when(u'abro o menu Ensino')
def step_impl(context):
    ensino = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu_form_menu_discente_j_id_jsp_1383391995_85_menu"]/table/tbody/tr/td[1]')))
    action = ActionChains(context.driver)
    action.move_to_element(ensino).perform()
    time.sleep(3)

@when(u'clico em consultar turma')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cmSubMenuID1"]/table/tbody/tr[16]/td[2]'))).click()
    time.sleep(3)

@when(u'em "ofertadas ao curso" seleciono ADS')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form:selectCurso"]/option[5]'))).click()
    time.sleep(3)

@when(u'busco as turmas disponiveis')
def step_impl(context):
    WebDriverWait(context.driver, 14).until(EC.element_to_be_clickable((By.ID, 'form:buttonBuscar'))).click()
    time.sleep(3)

@when(u'clico em visualizar menu da Turma de Teste de software')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lista-turmas"]/tbody/tr[59]/td[9]/img'))).click()
    time.sleep(3)

@when(u'clico em vizualizar turma')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.ID, 'form:sltbtnViewj_id_20'))).click()

@when(u'salvo o nome do professor da turma em um arquivo txt')
def step_impl(context):
    professor = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="relatorio"]/table/tbody/tr[6]/td'))).text
    with open('professor.txt', 'w') as data:
        data.write(professor)

@when(u'clico em voltar novamente')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="relatorio-rodape"]/p/table/tbody/tr/td[1]/a'))).click()
    time.sleep(3)


@then(u'clico em sair novamente')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="info-sistema"]/div/span[3]/a'))).click()
    time.sleep(3)
