# django-mail-downloader

**Описание програмы**

Программа разработана для чтения информации с нескольких email (Gmail, Yandex, Mail.ru).  
На данный момент программа ограничена в количестве выгружаемых сообщений для демонстрации.

**Порядок запуска программы**

1. Копируем репозиторий.
  
3. Из корня проекта запускаем команду ``` docker-compose build ```  для сборки образов проекта. В него входит база данных - PostgreSQL. Проект с авторизацией Django, Redis.

![image](https://github.com/user-attachments/assets/70f11765-0eff-4a03-9dd9-e98646aefba2)


4. После успешной сборки выполняем команду ``` docker-compose up ```

**Тестирование**

В даной программе доступны следующие урлы:

```
http://127.0.0.1:8000/email-accounts/
```

```
http://127.0.0.1:8000/messages/
```

1. Проходим по ``` http://127.0.0.1:8000/email-accounts/ ```

![image](https://github.com/user-attachments/assets/6477e313-7174-442f-86a2-fb5ce394f9d6)


2. Выбираем провайдера, вводим логин и пароль от почты который создан в настройках самой почты для входа из сторонних приложение

(Обязательно ставим галочку)

![image](https://github.com/user-attachments/assets/87725a09-821f-4ff6-90ec-df24e6f7029f)



![image](https://github.com/user-attachments/assets/0593bdbb-0d89-4e4c-b4f2-164d7ecc85fa)


После успешного добавления в базу данных мы увидем

![image](https://github.com/user-attachments/assets/1d7804a8-95c2-46e3-8a1a-c502e813cb69)


3. Переходим ``` http://127.0.0.1:8000/messages/ ``` и нажимаем кнопку Import Messages

![image](https://github.com/user-attachments/assets/79e38031-02be-44d8-adc1-76e357aa131e)

И начинается загрузка сообщений

![image](https://github.com/user-attachments/assets/0dade328-f499-4282-9760-2729ac8a52aa)


Если мы добавили несколько email то полоса загруски покажет нам по какой происходит импорт

![image](https://github.com/user-attachments/assets/5489bcb2-c61a-420b-a0de-ba5d7869d81c)


По данным из бд мы видим, что импорт прошёл по всем аккаунтам которые мы предоставили

![image](https://github.com/user-attachments/assets/b4d83318-1a92-4d9c-9296-bfa43e87d0b9)



