import time
import requests
from bs4 import BeautifulSoup

URL = "https://twitold.shop"
CHECK_INTERVAL = 30  # saniye

BOT_TOKEN = "8569601530:AAGg7Im1TBeXzTcgH0AU5XvfKcD7yIOnU-c"
CHAT_ID = "-5220450192"

PRODUCT_NAME = "Twitter 10.000+ followers accounts OLD 2007-2022"

def telegram_send(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=10
    )

print("📡 Stok takip başlatıldı...")
telegram_send("🟢 Stok takip sistemi aktif.")

while True:
    try:
        r = requests.get(URL, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")

        for row in soup.find_all("tr"):
            if PRODUCT_NAME in row.text:
                cols = row.find_all("td")
                stock = cols[1].text.strip()
                price = cols[2].text.strip()

                if stock != "0":
                    telegram_send(
                        "🔥 **STOK GELDİ!**\n\n"
                        f"📦 Ürün: {PRODUCT_NAME}\n"
                        f"📊 Stok: {stock}\n"
                        f"💰 Fiyat: {price}\n"
                        f"🔗 {URL}"
                    )
                    print("✅ Bildirim gönderildi.")
                    exit()

        print("⏳ Stok hala 0")
        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print("⚠️ Hata:", e)
        time.sleep(30)
