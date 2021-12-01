# Заполняем таблицы

1. Таблица стран

   ```sql
   INSERT INTO dbo.country(country_name) VALUES
   ('Россия'), ('США'), ('Турция'), ('Китай'), ('Мексика'), 
   ('Канада'), ('Япония'), ('Австрия'), ('Великобритания'), ('Германия'), 
   ('Малайзия'), ('Тайланд'), ('Италия'), ('Греция'), ('Франция'), 
   ('Испания'), ('Финляндия'), ('Португалия'), ('Нидерланды'), ('Норвегия')
   ```
1. Таблица городов

   ```sql
   INSERT INTO dbo.city(city_name) VALUES
   ('Москва'), ('Санкт-Петербург'), ('Новосибирск'), ('Екатеринбург'), ('Казань'), 
   ('Нижний Новгород'), ('Ростов-на-Дону'), ('Краснодар'), ('Тюмень'), ('Ижевск'), 
   ('Барнаул'), ('Ульяновск'), ('Ярославль'), ('Владивосток'), ('Йошкар-Ола'), 
   ('Нью-Йорк'), ('Лас-Вегас'), ('Сан-Франциско'), ('Чикаго'), ('Лос-Анджелес'), 
   ('Майами'), ('Вашингтон'), ('Орландо'), ('Сан-Диего'), ('Гонолулу'), 
   ('Ки-Уэст'), ('Новый Орлеан'), ('Саванна'), ('Бостон'), ('Филадельфия'), 
   ('Анталья'), ('Аланья'), ('Белек'), ('Кемер'), ('Сиде'), 
   ('Мармарис'), ('Даламан'), ('Фетхие'), ('Бодрум'), ('Кушадасы'), 
   ('Дидим'), ('Чешме'), ('Синоп'), ('Стамбул'), ('Ичмелер'), 
   ('Пекин'), ('Шанхай'), ('Гонконг'), ('Гуанчжоу'), ('Сиань'),
   ('Ханчжоу'), ('Сучжоу'), ('Далянь'), ('Санья'), ('Гуйлинь'), 
   ('Куньмин'), ('Ченде'), ('Шенчьжень'), ('Тяньцзинь'), ('Ухань'), 
   ('Мехико'), ('Экатепек-де-Морелос'), ('Тихуана'), ('Пуэбла-де-Сарагоса'), ('Гвадалахара'), 
   ('Сьюдад-Хуарес'), ('Сапопан'), ('Леон-де-лос-Альдама'), ('Несауалькойотль'), ('Монтеррей'), 
   ('Сан-Луис-Потоси'), ('Наукальпан-де-Хуарес'), ('Мехикали'), ('Эрмосильо'), ('Чиуауа'), 
   ('Торонто'), ('Монреаль'), ('Калгари'), ('Оттава'), ('Эдмонтон'), 
   ('Виннипег'), ('Квебек'), ('Ванкувер'), ('Гамильтон'), ('Галифакс'), 
   ('Лондон'), ('Гатино'), ('Саскатун'), ('Китченер'), ('Уинсор'), 
   ('Токио'), ('Иокогама'), ('Осака'), ('Нагоя'), ('Саппоро'), 
   ('Фукуока'), ('Кавасаки'), ('Кобе'), ('Киото'), ('Сайтама'), 
   ('Хиросима'), ('Сендай'), ('Тиба'), ('Китакюсю'), ('Сакаи'), 
   ('Вена'), ('Грац'), ('Линц'), ('Зальцбург'), ('Инсбрук'), 
   ('Клагенфурт-ам-Вёртерзе'), ('Филлах'), ('Вельс'), ('Санкт-Пёльтен'), ('Дорнбирн'), 
   ('Винер-Нойштадт'), ('Штайр'), ('Фельдкирх'), ('Брегенц'), ('Леондинг'), 
   ('Лондон'), ('Манчестер'), ('Бирмингем'), ('Ливерпуль'), ('Бристоль'), 
   ('Лидс'), ('Брайтон'), ('Виндзор'), ('Блэкпул'), ('Шеффилд'), 
   ('Йорк'), ('Ньюкасл'), ('Солсбери'), ('Ноттингем'), ('Лестер'), 
   ('Берлин'), ('Гамбург'), ('Мюнхен'), ('Кёльн'), ('Франкфурт-на-Майне'), 
   ('Штутгарт'), ('Дюссельдорф'), ('Эссен'), ('Дортмунд'), ('Лейпциг'), 
   ('Бремен'), ('Дрезден'), ('Ганновер'), ('Нюрнберг'), ('Мюнстер'), 
   ('Алор-Сетар'), ('Семпорна'), ('Путраджайя'), ('Сандакан'), ('Куантан'), 
   ('Джохор-Бару'), ('Куала-Тренгану'), ('Кота-Бару'), ('Мири'), ('Кучинг'), 
   ('Кота Кинабалу'), ('Ипох'), ('Малакка'), ('Джорджтаун'), ('Куала-Лумпур'), 
   ('Бангкок'), ('Нонтхабури'), ('Хатъяй'), ('Чиангмай'), ('Сураттхани'), 
   ('Удонтхани'), ('Накхонратчасима'), ('Кхонкэн'), ('Паттайя'), ('Накхонситхаммарат'), 
   ('Накхонсаван'), ('Сукхотхай'), ('Убонратчатхани'), ('Накхонпатхом'), ('Пхукет'), 
   ('Рим'), ('Венеция'), ('Милан'), ('Флоренция'), ('Сорренто'), 
   ('Верона'), ('Позитано'), ('Неаполь'), ('Турин'), ('Палермо'), 
   ('Искья'), ('Болонья'), ('Генуя'), ('Кальяри'), ('Катания'), 
   ('Афины'), ('Салоники'), ('Патры'), ('Лариса'), ('Ираклион'), 
   ('Ахарне'), ('Волос'), ('Кавала'), ('Янина'), ('Трикала'), 
   ('Халкида'), ('Серре'), ('Александруполис'), ('Катерини'), ('Ксанти'), 
   ('Париж'), ('Ницца'), ('Лион'), ('Шамони-Мон-Блан'), ('Монте-Карло'), 
   ('Страсбург'), ('Бордо'), ('Марсель'), ('Экс-ан-Прованс'), ('Канны'), 
   ('Тулуза'), ('Ла-Рошель'), ('Монпелье'), ('Лилль'), ('Авиньон'), 
   ('Барселона'), ('Мадрид'), ('Валенсия'), ('Пальма-де-Майорка'), ('Севилья'), 
   ('Санта-Крус-де-Тенерифе'), ('Гранада'), ('Кордова'), ('Сарагоса'), ('Малага'), 
   ('Сеговия'), ('Аликанте'), ('Бенидорм'), ('Сан-Себастьян'), ('Бильбао'), 
   ('Хельсинки'), ('Эспоо'), ('Тампере'), ('Вантаа'), ('Оулу'), 
   ('Турку'), ('Йювяскюля'), ('Лахти'), ('Куопио'), ('Пори'), 
   ('Коувола'), ('Йоэнсуу'), ('Лаппеэнранта'), ('Вааса'), ('Хямеэнлинна'), 
   ('Лиссабон'), ('Порту'), ('Лориш'), ('Брага'), ('Вила-Нова-ди-Гая'), 
   ('Матозиньюш'), ('Амадора'), ('Гондомар'), ('Алмада'), ('Сейшал'), 
   ('Гимарайнш'), ('Одивелаш'), ('Коимбра'), ('Санта-Мария-да-Фейра'), ('Вила-Франка-ди-Шира'), 
   ('Амстердам'), ('Роттердам'), ('Гаага'), ('Утрехт'), ('Эйндховен'), 
   ('Тилбург'), ('Гронинген'), ('Неймеген'), ('Хертогенбос'), ('Харлем'), 
   ('Арнем'), ('Энсхеде'), ('Амерсфорт'), ('Бреда'), ('Зволле'), 
   ('Осло'), ('Берген'), ('Ставангер'), ('Тронхейм'), ('Фредрикстад'), 
   ('Драммен'), ('Саннвика'), ('Шиен'), ('Кристиансанн'), ('Тромсё'), 
   ('Саннес'), ('Сарпсборг'), ('Олесунн'), ('Тёнсберг'), ('Мосс')
   ```
1. Таблица названий провайдеров
   ```sql
   INSERT INTO dbo.source(source_name) VALUES
   ('BS-CHANNEL_MANAGER'), ('TL-CHANNEL_MANAGER'), ('BL-CHANNEL_MANAGER'), ('RC-CHANNEL_MANAGER'), ('CH-CHANNEL_MANAGER'), 
   ('GB-CHANNEL_MANAGER'), ('BNOVO-CHANNEL_MANAGER'), ('OMS-CHANNEL_MANAGER'), ('KK-CHANNEL_MANAGER'), ('AS-CHANNEL_MANAGER')
   ```
1. Если для заполнения первых трёх таблиц можно использовать MS Excel и генерировать запросы используя функцию сложения строк, то для генерации данных таблиц: броней, данных о провайдере и стоимости валют нужно использовать автоматизацию:  
[стоимости валют][1],
[данных о провайдерах][2]
Csv:  
[стоимости валют][3],  
[данные о провайдерах][4],  
[брони][5].

   ```sql
   BULK INSERT currency_rate
   -- YOUR PATH
   FROM 'D:\TestTasks\currency_rate.csv'
   WITH (
       FORMAT='CSV',
       FIRSTROW=2,
       FIELDTERMINATOR = ',',
       ROWTERMINATOR = '\n'
   );
   ```
   
   Изменил значение сепаратора (FIELDTERMINATOR), предварительно проверив, что символ # не используется в названии отелей.  
   ```sql
   BULK INSERT [provider]
   -- YOUR PATH
   FROM 'D:\TestTasks\provider.csv'
   WITH (
       CODEPAGE = 'ACP',
       FORMAT='CSV',
       FIRSTROW=2,
       FIELDTERMINATOR = '#',
       ROWTERMINATOR = '\n'
   )
   ```
   
   Файловая загрузка данных для последней таблицы.
   
     ```sql
   BULK INSERT booking
   -- YOUR PATH
   FROM 'D:\TestTasks\booking.csv'
   WITH (
       FORMAT='CSV',
       FIRSTROW=2,
       FIELDTERMINATOR = ',',
       ROWTERMINATOR = '\n'
   )
   ```

# Первое представление

```sql
CREATE VIEW [dbo].[my_first_view] AS
SELECT
    b.id_provider,
    p.provider_name,
    c.country_name,
    t.city_name,
    b.creation_date,
    b.start_date,
    b.nights,
    b.price,
    b.id_currency,
    b.price * d.rate as sum_rub
FROM
    booking b
    INNER JOIN provider p ON (b.id_provider = p.id_provider)
    INNER JOIN country c ON (p.id_country = c.id_country)
    INNER JOIN city t ON (p.id_city = t.id_city)
    INNER JOIN currency_rate d ON (b.id_currency = d.id_currency AND b.creation_date = d.[date])
```

# Второе представление

```sql
CREATE VIEW [dbo].[my_second_view] AS
SELECT
    b.id_provider,
    p.provider_name,
    c.country_name,
    t.city_name,
    YEAR(b.creation_date) as creation_year,
    MONTH(b.creation_date) as creation_month,
    SUM(CASE WHEN b.creator != '' THEN 1 ELSE 0 END) * 100 / COUNT(*) as bs_cm,
    SUM(CASE WHEN b.creator = 'BGC' THEN 1 ELSE 0 END) * 100 / COUNT(*) as bs_cm_bgc
FROM
    booking b
    INNER JOIN provider p ON (b.id_provider = p.id_provider)
    INNER JOIN country c ON (p.id_country = c.id_country)
    INNER JOIN city t ON (p.id_city = t.id_city)
GROUP BY
    YEAR(b.creation_date),
    MONTH(b.creation_date),
    b.id_provider, p.provider_name,
    c.country_name,
    t.city_name
```

# Функция, которая возвращает топ 5 провайдеров по количеству броней

```sql
CREATE PROC
    top_five @booking_depth INT
AS
SELECT
    country_name,
    id_provider,
    provider_name,
    city_name,
    count_booking FROM (
SELECT
    c.country_name,
    b.id_provider,
    p.provider_name,
    t.city_name,
    COUNT(b.id_provider) as count_booking,
    RANK() OVER (PARTITION BY c.country_name ORDER BY c.country_name, COUNT(b.id_provider) DESC) AS rank_result
FROM 
    booking b
    INNER JOIN provider p ON (b.id_provider = p.id_provider)
    INNER JOIN country c ON (p.id_country = c.id_country)
    INNER JOIN city t ON (p.id_city = t.id_city)
WHERE
    datediff(day, b.creation_date, b.start_date) < @booking_depth
GROUP BY
    c.country_name,
    b.id_provider,
    p.provider_name,
    t.city_name)
    X
WHERE rank_result <= 5
```

# Последний запрос

```sql
WITH Booking_each_month (id_provider) 
AS
    (SELECT
        id_provider
    FROM
        (SELECT
            b.id_provider,
            RANK() OVER (PARTITION BY b.id_provider ORDER BY MONTH(b.creation_date)) AS rank_result
        FROM
            booking b 
        WHERE
            MONTH(b.creation_date) in (1, 2, 3)
        GROUP BY
            YEAR(b.creation_date),
            MONTH(b.creation_date),
            b.id_provider
        ) X 
    WHERE rank_result = 3)
SELECT
    bo.id_provider,
    p.provider_name,
    c.country_name,
    t.city_name,
    YEAR(bo.creation_date) as creation_year,
    MONTH(bo.creation_date) as creation_month,
    COUNT(bo.id_provider) as count_booking,
    AVG(bo.price*d.rate) as price
FROM
    Booking_each_month bem
    INNER JOIN booking bo ON (bem.id_provider = bo.id_provider)
    INNER JOIN provider p ON (bo.id_provider = p.id_provider)
    INNER JOIN country c ON (p.id_country = c.id_country)
    INNER JOIN city t ON (p.id_city = t.id_city)
    INNER JOIN currency_rate d ON (bo.id_currency = d.id_currency AND bo.creation_date = d.[date])
GROUP BY
    YEAR(bo.creation_date),
    MONTH(bo.creation_date),
    bo.id_provider,
    p.provider_name,
    c.country_name,
    t.city_name
ORDER BY
    id_provider,
    creation_year,
    creation_month
```
[1]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/generate_currency_rate.py
[2]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/generate_providers.py
[3]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/currency_rate.csv
[4]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/provider.csv
[5]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/generate_booking.py
