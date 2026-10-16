from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def buscar_preco_kabum(nome_produto):
    """
    Busca o preço de um produto no site Kabum
    :param nome_produto: Termo de busca (ex: "Notebook Gamer")
    :return: Dicionário com 'sucesso', 'preco', 'url', 'erro'
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Remova ou comente esta linha se quiser ver o Chrome abrindo sozinho!
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 15)

    try:
        # Acessa o Kabum
        driver.get("https://www.kabum.com.br")

        # Espera o campo de busca e digita
        campo_busca = wait.until(EC.presence_of_element_located((By.ID, "input-busca")))
        campo_busca.clear()
        campo_busca.send_keys(nome_produto)

        # Clica no botão de busca ou envia Enter
        try:
            botao = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "botao-buscar")))
            botao.click()
        except Exception:
            campo_busca.submit()

        # Espera o primeiro resultado
        primeiro_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".productCard"))
        )
        preco_element = primeiro_link.find_element(By.CLASS_NAME, "priceCard")
        preco_texto = preco_element.text.replace('R$', '').replace('.', '').replace(',', '.').strip()

        # Pega o link do produto
        link_tag = primeiro_link.find_element(By.TAG_NAME, "a") if primeiro_link.tag_name != "a" else primeiro_link
        url = link_tag.get_attribute('href')

        return {
            "sucesso": True,
            "preco": float(preco_texto),
            "url": url,
            "mensagem": f"Preço encontrado no Kabum: R$ {preco_texto}"
        }
    except TimeoutException:
        return {
            "sucesso": False,
            "erro": "Tempo esgotado esperando elementos",
            "mensagem": "Site demorou muito para carregar."
        }
    except NoSuchElementException as e:
        return {
            "sucesso": False,
            "erro": str(e),
            "mensagem": "Produto não encontrado no Kabum."
        }
    except Exception as e:
        return {
            "sucesso": False,
            "erro": str(e),
            "mensagem": "Erro desconhecido na automação."
        }
    finally:
        driver.quit()