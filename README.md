# 🧼 Raya — сайт-визитка клининговой компании

Сайт-визитка для компании **Raya**, предоставляющей услуги профессиональной уборки.

---

## 🛠️ Требования

- Установленный **Docker**
- Установленный **Docker Compose**

---

## 🚀 Запуск проекта локально

1. Клонируй репозиторий:

   ```sh
   git clone https://github.com/yourusername/raya.git
   cd raya/backend


2. Переименуй `.env-test` → `.env` и укажи свои настройки:

   ```env
   POSTGRES_DB=raya_db
   POSTGRES_USER=raya_user
   POSTGRES_PASSWORD=superpassword
   POSTGRES_HOST=db_raya
   POSTGRES_PORT=5432

   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```

3. Запусти контейнеры:

   ```sh
   sudo docker-compose -f docker/docker-compose.yml up -d --build
   ```

4. Миграции и сборка статики выполняются автоматически через `entrypoint.sh`

5. Загрузить демо-данные (если есть `db.json`):

   ```sh
   sudo docker-compose exec web_raya python manage.py loaddata db.json
   ```

6. Проект будет доступен по адресу:

   [http://127.0.0.1:8084](http://127.0.0.1:8084)

---

## 🌐 Запуск проекта на сервере (production)

1. Клонируй проект на сервер:

   ```sh
   git clone https://github.com/yourusername/raya.git
   cd raya/backend
   ```

2. Переименуй `.env-test` → `.env` и заполни продакшн-данные

3. Запусти продакшн-версию:

   ```sh
   sudo docker-compose -f docker/docker-compose-prod.yml up -d --build
   ```

4. Загрузка данных:

   ```sh
   sudo docker-compose -f docker/docker-compose-prod.yml exec web_kiki python manage.py loaddata db.json
   ```

5. Настройка SSL (если нужно):

   **Остановить nginx:**

   ```sh
   sudo docker-compose -f docker/docker-compose-prod.yml stop nginx
   ```

   **Получить сертификат:**

   ```sh
   sudo certbot certonly --standalone -d kiki.kg -d www.kiki.kg
   ```

   **Запустить nginx:**

   ```sh
   sudo docker-compose -f docker/docker-compose-prod.yml start nginx
   ```

---

## 📦 Стек

* Django
* PostgreSQL
* Redis
* Docker
* Nginx + Certbot (опционально)
* Bootstrap / HTML / CSS

---

## 📞 Контакты

* Телефон: +996 558 00 03 50
* Email: [raya@example.com](mailto:raya@example.com)
* Адрес: г. Ош, Кыргызстан
