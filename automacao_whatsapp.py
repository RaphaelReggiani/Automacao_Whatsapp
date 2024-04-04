# Automação de encaminhamento de mensagens no WhatsApp sem bloqueio
# Usando a funcionalidade nativa do WhatsApp de envio de mensagens
# Envio de 3 em 3 mensagens

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)
nav.get("https://web.whatsapp.com")

time.sleep(30)

# Mensagem e lista de contatos

from selenium.webdriver.common.keys import Keys
import pyperclip

mensagem = "Olá, este é o meu primeiro teste com python, me responda se você gostou!"

lista_contatos = ["Numero", "Mae"]

# Enviar a mensagem para o meu número

# Clicar no meu número

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
time.sleep(3)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("Numero")
time.sleep(1)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

# Enviar a mensagem para o Numero

nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem)
time.sleep(2)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(3)

from selenium.webdriver.common.action_chains import ActionChains

numero_contatos = len(lista_contatos)

if numero_contatos % 3 == 0:
    numero_blocos = numero_contatos / 3
else:
    numero_blocos = int((numero_contatos / 3) + 1)
    
for i in range(numero_blocos):
    i_inicial = i * 5
    i_final = (i + 1) * 5 
    lista_enviar = lista_contatos[i_inicial:i_final]
    
    lista_elementos = nav.find_elements ('class name', '_2AOIt')

    for item in lista_elementos:
        mensagem = mensagem.replace("/n", "")
        texto = item.text.replace("/n", "")
    
        if mensagem in texto:
            elemento = item
    
    # Selecionar a caixa de texto da mensagem
    
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_3u9t-').click()
    time.sleep(3)

    # Selecionar encaminhar

    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    time.sleep(1)

    # Selecionar o ícone de encaminhar

    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(2)

    # Selecionar a mensagem para enviar e abre a caixa para encaminhar
    
    for nome in lista_enviar:
        
        # Escrever o nome do contato

        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(2)

        # Apertar enter

        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(3)

        # Apagar

        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)
    
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(10)
