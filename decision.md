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
```sql

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
