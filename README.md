# Real-Time Bank Fraud Detection & Big Data Analytics Simülation

Bu proje, finansal kurumlarda saniyede yüzlerce işlem akarken oluşabilecek **Dolandırıcılık (Fraud)** vakalarını milisaniyeler bazında yakalayan gerçek zamanlı bir büyük veri analiz mimarisi simülasyonudur.

## Sistem Mimarisi & Mantığı

Proje, kurumsal büyük veri dünyasındaki **Event-Driven (Olay Güdümlü)** ve **Microservices** mimarilerini taklit edecek şekilde iki bağımsız servisten oluşur:

1. **Banka Çekirdek Sistemi (`bank_core.py`):** Canlı ATM/POS ve Mobil şube işlemlerini taklit ederek saniyede birden fazla finansal veri üretir ve bunları anlık log akışına (`bank_transactions.log`) yazar.
2. **Fraud Tespit Motoru (`fraud_detector.py`):** Üretilen log akışını canlı olarak tarayarak (Stream Tailing), önceden belirlenmiş risk kurallarına (Örn: 13.000 TL üzeri Eğlence/Elektronik harcamaları) uyan şüpheli işlemleri anında yakalar ve alarm üretir.

## Projeyi Çalıştırma

Projeyi izlemek için iki farklı terminal (CMD) penceresi açılır:

**Terminal 1 (Canlı Veri Akışı):**

```bash
python bank_core.py
```
