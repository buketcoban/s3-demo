# LocalStack S3 Demo

Bu proje, AWS S3 servislerinin yerel geliştirme ortamında test edilmesini sağlamak amacıyla hazırlanmıştır. LocalStack altyapısı kullanılarak, Amazon S3 ile yapılan temel işlemler (bucket oluşturma, dosya yükleme vb.) simüle edilmiştir.

## Proje Yapısı

- `main.py` — S3 bucket oluşturma ve örnek bir dosyayı yükleme işlemini gerçekleştiren Python betiği.
- `c1da64ab-...txt` — Örnek olarak yüklenen test dosyası.

## Gereksinimler

- Python 3.8 veya üzeri
- Docker
- LocalStack
- pip ile kurulabilir `boto3` kütüphanesi

## Kurulum ve Kullanım

1. LocalStack konteynerini başlatın:
   ```bash
    docker-compose up -d

2. Gerekli Python paketlerini yükleyin:
   ```bash
     pip install boto3

3. Python'u çalıştırın:
   ```bash
    python main.py

## Açıklamalar

LocalStack, AWS servislerini lokal ortamda taklit eden bir çözümdür.
Bu demo, S3'e özel bir kullanım senaryosunu örneklemektedir.
Gerçek AWS anahtarlarına ihtiyaç duyulmaz; LocalStack kendi endpoint’leri üzerinden çalışır.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
