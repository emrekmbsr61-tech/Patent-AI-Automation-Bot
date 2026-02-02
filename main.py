from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def patent_cek(sirket):
    print(f"\n🔍 {sirket} için patentler okunuyor...")
    options = Options()
    # options.add_argument("--headless") # Gerçekten çalıştığına emin olduğunda bunu aktif et, tarayıcı görünmez olur.
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(f"https://patents.google.com/?assignee={sirket}&sort=new")
        time.sleep(7) # Sayfanın tam yüklenmesi için biraz daha süre verdik

        # Patent başlıklarını yakalıyoruz
        titles = driver.find_elements(By.CSS_SELECTOR, "span#title")
        links = driver.find_elements(By.CSS_SELECTOR, "search-result-item a")

        for i in range(min(3, len(titles))):
            print(f"✅ Bulundu: {titles[i].text}")
            # Linkleri temizleyip terminale basalım
            print(f"🔗 Link: {links[i*2].get_attribute('href')}") 
            print("-" * 20)
            
    finally:
        driver.quit()

takip_listesi = ["Apple", "Tesla"]
for sirket in takip_listesi:
    patent_cek(sirket)