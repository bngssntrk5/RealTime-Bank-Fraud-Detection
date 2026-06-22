import time
import random
import json
from datetime import datetime
from faker import Faker

fake = Faker('tr_TR')
LOG_FILE = "bank_transactions.log"

def generate_transaction():
    categories = ['Market', 'Elektronik', 'Giyim', 'Restoran', 'Akaryakıt', 'Eğlence']
    cities = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Kocaeli']
    
    is_fraud = random.choice([True, False, False, False, False])
    if is_fraud:
        amount = round(random.uniform(13001.0, 15000.0), 2)
        category = random.choice(['Elektronik', 'Eğlence'])
    else:
        amount = round(random.uniform(10.0, 5000.0), 2)
        category = random.choice(categories)

    return {
        "transaction_id": fake.uuid4(),
        "customer_id": f"CUST-{random.randint(10000, 99999)}",
        "amount": amount,
        "category": category,
        "location": random.choice(cities),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    print("[BANK CORE] Ziraat Bankası Ana İşlem Motoru Başlatıldı...")
    print("Canlı işlemler 'bank_transactions.log' dosyasına yazılıyor...\n")
    
    while True:
        tx = generate_transaction()
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(tx, ensure_ascii=False) + "\n")
            
        print(f"İşlem Gönderildi: {tx['customer_id']} | {tx['amount']} TL | {tx['category']}")
        time.sleep(random.uniform(0.3, 0.9)) 