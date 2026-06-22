import time
import json
import os

LOG_FILE = "bank_transactions.log"

if __name__ == "__main__":
    print("="*60)
    print("REAL-TIME BIG DATA ANALYTICS")
    print("Log Stream Fraud Detection Motoru Aktif...")
    print("="*60)
    time.sleep(1)

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        
        processed_count = 0
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1) 
                continue
            
            processed_count += 1
            try:
                tx = json.loads(line.strip())
                
                if tx['amount'] > 13000.0 and tx['category'] in ['Elektronik', 'Eğlence']:
                    print(f"\n[ALARM - {tx['timestamp']}] ŞÜPHELİ FİNANSAL HAREKET!")
                    print(f"Müşteri: {tx['customer_id']}")
                    print(f"Tutar  : {tx['amount']} TL")
                    print(f"Kategori: {tx['category']}")
                    print(f"Konum  : {tx['location']}")
                    print("-" * 60)
                else:
                    if processed_count % 10 == 0:
                        print(f"Toplam {processed_count} finansal işlem anlık olarak tarandı. Durum: Güvenli.")
                        
            except Exception as e:
                pass