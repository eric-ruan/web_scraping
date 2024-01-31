# webdriver permite simular o uso do navegador
from selenium import webdriver
# O By serve para encontrar as informações no site
from selenium.webdriver.common.by import By
# openpyxl serve para manipular a planilha
import openpyxl

# Acessar o site: https://www.magazineluiza.com.br/busca/iphone/
driver = webdriver.Chrome()
driver.get('https://www.magazineluiza.com.br/busca/iphone/')

# Coletar os nomes dos produtos
nome_produto = driver.find_elements(By.XPATH, "//h2[@class='sc-fvwjDU ehjgcW']")

# Coletar o preço a vista com desconto
preco_a_vista = driver.find_elements(By.XPATH, "//p[@class='sc-kpDqfm eCPtRw sc-bOhtcR dOwMgM']")

# Coletar o tipo de pagamento no desconto
tipo_de_desconto = driver.find_elements(By.XPATH, "//span[@class='sc-hoLEA gGdgvl']")

# Coletar a porcentagem de desconto
desconto = driver.find_elements(By.XPATH, "//span[@class='sc-eXsaLi fErFMt']")

# Coletar o preço a prazo
preco_a_prazo = driver.find_elements(By.XPATH, "//p[@class='sc-kpDqfm cZTiGu sc-gvZAcH KJKeb']")

# Link do produto
links = driver.find_elements(By.XPATH, '//li[@class="sc-kTbCBX ciMFyT"]/a')

# Criando a planilha
workbook = openpyxl.Workbook()
# Criando a página 'produtos'
workbook.create_sheet('produtos')
# Selecionando a página
sheet_produtos = workbook['produtos']
# Criando colunas
sheet_produtos['A1'].value = 'produto'
sheet_produtos['B1'].value = 'preco_a_vista'
sheet_produtos['C1'].value = 'tipo_de_desconto'
sheet_produtos['D1'].value = '% de desconto'
sheet_produtos['E1'].value = 'preco_a_prazo'
sheet_produtos['F1'].value = 'parcelas'
sheet_produtos['G1'].value = 'link_do_produto'

# Inserindo dados na planilha
for produto, precoavista, tipodedesconto, desc, precoaprazo, link in zip(nome_produto, preco_a_vista, tipo_de_desconto, desconto, preco_a_prazo, links):
    prazo_e_parcela = precoaprazo.text
    prazo_e_parcela = prazo_e_parcela.split()
    prazo = prazo_e_parcela[1] + prazo_e_parcela[2]
    parcelas = prazo_e_parcela[4] + ' ' + prazo_e_parcela[5] + ' ' + prazo_e_parcela[6] + ' ' + prazo_e_parcela[7] + ' ' + prazo_e_parcela[8] + ' ' + prazo_e_parcela[9]
    link_produto = link.get_attribute('href')
    
    sheet_produtos.append([produto.text, precoavista.text, tipodedesconto.text, desc.text, prazo, parcelas, link_produto])
    workbook.save('produtos.xlsx')