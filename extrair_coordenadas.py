import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


ARQUIVO_ENTRADA = "links.txt"
ARQUIVO_SAIDA = "pontos.csv"


def extrair_coordenadas(driver, url):
    """Abre o link no Google Maps e retorna (lat, lon)"""
    driver.get(url)
    time.sleep(6)  # espera carregar

    current_url = driver.current_url

    # 1. Padrão com @lat,long
    if "@" in current_url:
        try:
            parte = current_url.split("@")[1].split(",")
            lat = float(parte[0])
            lon = float(parte[1])
            return lat, lon
        except:
            pass

    # 2. Padrão com query=lat,long
    if "query=" in current_url:
        try:
            parte = current_url.split("query=")[1].split("&")[0]
            lat, lon = parte.split(",")
            return float(lat), float(lon)
        except:
            pass

    # 3. Padrão com !3dLAT!4dLON
    if "!3d" in current_url and "!4d" in current_url:
        try:
            lat = current_url.split("!3d")[1].split("!")[0]
            lon = current_url.split("!4d")[1].split("!")[0]
            return float(lat), float(lon)
        except:
            pass

    return None


def processar_links():
    # Configurações do Chrome headless e silencioso
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Lê e limpa os links
    with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f:
        links = []
        for linha in f:
            url = linha.strip().strip('"').strip("'").rstrip(",")
            if url:
                links.append(url)

    resultados = []

    for i, link in enumerate(links, start=1):
        print(f"[{i}/{len(links)}] Acessando: {link}")
        coords = extrair_coordenadas(driver, link)
        if coords:
            print(f"   -> Coordenadas: {coords[0]}, {coords[1]}")
            resultados.append([f"Ponto {i}", coords[0], coords[1], link])
        else:
            print("   -> Não consegui extrair coordenadas")
            resultados.append([f"Ponto {i}", "", "", link])

    driver.quit()

    # Salva CSV
    with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nome", "Latitude", "Longitude", "Link Original"])
        writer.writerows(resultados)

    print(f"\n✅ Arquivo '{ARQUIVO_SAIDA}' criado com sucesso!")


if __name__ == "__main__":
    processar_links()
