#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

#%%
CHROMEDRIVER_PATH = r"C:\Users\User\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

def scrape_percentiles_selenium(url):
    options = Options()
    options.add_argument("--window-size=1920,1080")

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(5)  # esperar carregar o HTML

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    rows = soup.select("table.stats_table tr")
    data = []

    for row in rows:
        stat_name_tag = row.find("th", {"data-stat": "statistic"})
        per90_tag = row.find("td", {"data-stat": "per90"})
        percentile_tag = row.find("div", align="right")

        if stat_name_tag and per90_tag and percentile_tag:
            stat_name = stat_name_tag.get_text(strip=True)
            per90 = per90_tag.get_text(strip=True)
            percentile = percentile_tag.get_text(strip=True)
            data.append([stat_name, per90, percentile])

    df = pd.DataFrame(data, columns=["Estatística", "Por 90", "Percentil"])
    return df


if __name__ == "__main__":
    urls = {
        "Luciano Rodriguez": "https://fbref.com/en/players/8ccc9220/Luciano-Rodriguez",
        "Facundo Colidio": "https://fbref.com/en/players/69a6523a/Facundo-Colidio"
    }

    all_data = []

    for player, url in urls.items():
        df = scrape_percentiles_selenium(url)
        df.insert(0, "Jogador", player)
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)

    print(final_df)
    final_df.to_csv("jogadores.csv", index=False, encoding="utf-8-sig")
#%%