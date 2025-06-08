# 🍽️ Project_Restoran — Restoran Tarmog‘i Veb-ilovasi

## 📌 Tavsif
Project_Restoran — restoran tarmog‘ini uchun ishlab chiqilgan veb-ilova. Ushbu loyiha yordamida restoranlar va filiallar faoliyati, buyurtmalar, mijozlar statistikasi, xodimlarning ish faoliyati, mahsulot va ombor hisoboti, shuningdek moliyaviy hisobotlar samarali tarzda boshqariladi.

## ⚙️ Texnologiyalar
- Python (Django)
- PostgreSQL (ma’lumotlar bazasi)
- HTML, CSS, JavaScript
- Pandas, Scikit-learn (ma’lumotlarni tahlil qilish)
- Matplotlib (grafiklar chizish)

## 🚀 Asosiy funksiyalar
- Restoran va filiallar monitoringi
- Buyurtmalar va mijozlar statistikasini yuritish
- Xodimlarning ish faoliyatini nazorat qilish
- Mahsulot va ombor hisoboti
- Moliyaviy hisobotlarni yaratish va tahlil qilish

## 🖥️ Loyihani ishga tushirish
```bash
# 1. Loyihani klonlash
git clone https://github.com/Habibullo2003/project_restoran.git
cd project_restoran

# 2. Virtual muhit yaratish
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. Kerakli kutubxonalarni o‘rnatish
pip install -r requirements.txt

# 4. Migratsiyalarni bajarish
python manage.py makemigrations
python manage.py migrate

# 5. Serverni ishga tushirish
python manage.py runserver
