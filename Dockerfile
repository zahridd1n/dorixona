# Python asosidagi rasmni tanlang
FROM python:3.13

# Ishchi katalogni yarating
WORKDIR /app

# Talablar faylini ko'chirish
COPY requirements.txt .

# Talablarni o'rnating
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha kodini ko'chirish
COPY . .

# Django statik fayllarini yig'ish
RUN python manage.py collectstatic --noinput

# Gunicorn'ni ishga tushirish
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
