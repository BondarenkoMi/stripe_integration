Тестовое задание
--

Django + Stripe API приложение. Проект запущен на виртуальной машине cloud.ru и доступен по адресу - http://176.108.250.99/

python 3.10.11 + django 5.2.4

Запуск
--

Для локального запуска:
1. `git clone https://github.com/BondarenkoMi/stripe_integration`
2. Создать .env и прописать там STRIPE_PUBLIC_KEY и STRIPE_SECRET_KEY
3. Создать и активировать виртуальное окружение
4. `cd backend/ && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver`
5. Создать суперпользователя - `python manage.py createsuperuser`


Для запуска через docker-compose:
1. `git clone https://github.com/BondarenkoMi/stripe_integration`
2. Создать .env и прописать там STRIPE_PUBLIC_KEY и STRIPE_SECRET_KEY
3. `docker-compose up -d --build docker-compose exec backend python manage.py migrate`
4. Создать суперпользователя - `docker-compose exec backend python manage.py createsuperuser`

Пути
--

1. /items - Список товаров
2. /items/{id} - Страница товара
3. /items/{id}/checkout - Получение id stripe сессии для оплаты товара
4. /items/{id}/add_to_cart - Добавить товар в корзину
5. /cart - Корзина
6. /cart/checkout - Получение id stripe сессии для оплаты всех товаров в корзине
7. /admin - Админ панель
