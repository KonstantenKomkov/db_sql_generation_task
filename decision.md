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
[данных о провайдерах][2] и
[бронях][3].  
Csv:  
[стоимость валют][4],  
[данные о провайдере][5],  
[брони][6].

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
   
   ```sql
   BULK INSERT [provider]
   -- YOUR PATH
   FROM 'D:\Work\TestTasks\Тестовое TravelLine\provider.csv'
   WITH (
       FORMAT='CSV',
       FIRSTROW=2,
       FIELDTERMINATOR = '#',
       ROWTERMINATOR = '\n'
   )
   ```

# Первое представление

```sql
CREATE VIEW my_first_view AS
SELECT
    b.provider_id,
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
    INNER JOIN provider p ON (b.provider_id = p.id_provider)
    INNER JOIN country c ON (p.country_id = c.id)
    INNER JOIN city t ON (p.city_id = t.id)
    INNER JOIN currency_rate d ON (b.id_currency = d.id_currency AND b.creation_date = d.[date])
```

# Второе представление

```sql
CREATE VIEW my_second_view AS
SELECT
    b.provider_id,
    p.provider_name,
    c.country_name,
    t.city_name,
    YEAR(b.creation_date) as creation_year,
    MONTH(b.creation_date) as creation_month,
    SUM(CASE WHEN b.creator != '' THEN 1 ELSE 0 END) * 100 / COUNT(*) as bs_cm,
    SUM(CASE WHEN b.creator = 'BGC' THEN 1 ELSE 0 END) * 100 / COUNT(*) as bs_cm_bgc
FROM
    booking b
    INNER JOIN provider p ON (b.provider_id = p.id_provider)
    INNER JOIN country c ON (p.country_id = c.id)
    INNER JOIN city t ON (p.city_id = t.id)
GROUP BY
    YEAR(b.creation_date),
    MONTH(b.creation_date),
    b.provider_id, p.provider_name,
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
    provider_id,
    provider_name,
    city_name,
    count_booking FROM (
SELECT
    c.country_name,
    b.provider_id,
    p.provider_name,
    t.city_name,
    COUNT(b.provider_id) as count_booking,
    RANK() OVER (PARTITION BY c.country_name ORDER BY c.country_name, COUNT(b.provider_id) DESC) AS rank_result
FROM 
    booking b
    INNER JOIN provider p ON (b.provider_id = p.id_provider)
    INNER JOIN country c ON (p.country_id = c.id)
    INNER JOIN city t ON (p.city_id = t.id)
WHERE
    datediff(day, b.creation_date, b.start_date) < @booking_depth
GROUP BY
    c.country_name,
    b.provider_id,
    p.provider_name,
    t.city_name)
    X
WHERE rank_result <= 5
```

# Последний запрос

```sql
WITH Booking_each_month (provider_id) 
AS
    (SELECT
        provider_id
    FROM
        (SELECT
            b.provider_id,
            RANK() OVER (PARTITION BY b.provider_id ORDER BY MONTH(b.creation_date)) AS rank_result
        FROM
            booking b 
        WHERE
            MONTH(b.creation_date) in (1, 2, 3)
        GROUP BY
            YEAR(b.creation_date),
            MONTH(b.creation_date),
            b.provider_id
        ) X 
    WHERE rank_result = 3)
SELECT
    bo.provider_id,
    p.provider_name,
    c.country_name,
    t.city_name,
    YEAR(bo.creation_date) as creation_year,
    MONTH(bo.creation_date) as creation_month,
    COUNT(bo.provider_id) as count_booking,
    AVG(bo.price*d.rate) as price
FROM
    Booking_each_month bem
    INNER JOIN booking bo ON (bem.provider_id = bo.provider_id)
    INNER JOIN provider p ON (bo.provider_id = p.id_provider)
    INNER JOIN country c ON (p.country_id = c.id)
    INNER JOIN city t ON (p.city_id = t.id)
    INNER JOIN currency_rate d ON (bo.id_currency = d.id_currency AND bo.creation_date = d.[date])
GROUP BY
    YEAR(bo.creation_date),
    MONTH(bo.creation_date),
    bo.provider_id,
    p.provider_name,
    c.country_name,
    t.city_name
ORDER BY
    provider_id,
    creation_year,
    creation_month
```
[1]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/generate_currency_rate.py
[2]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/generate_providers.py
[4]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/currency_rate.csv
[5]: https://github.com/KonstantenKomkov/db_sql_generation_task/blob/main/provider.csv
