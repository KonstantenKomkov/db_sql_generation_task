# Тестовое задание

## Описание таблиц

Таблица **[dbo].[booking]** содержит брони.  

 id_booking [int]  - ID брони (уникальный ключ)  
 id_provider [int] - ID провайдера (ссылка на таблицу [dbo].[provider])  
 creation_date [date] - дата создания брони  
 start_date [date] - дата заезда  
 status [int] - статус брони  
 nights [int] - количество ночей  
 price [float] - сумма брони  
 id_currency [nvarchar] (3) - валюта брони   
 id_source [int] - источник брони (ссылка на таблицу [dbo].[source])  
 creator \[nvarchar\](3) - канал брони, в случае если source_name = ‘BS-CHANNEL_MANAGER’, если source_name != ‘BS-CHANNEL_MANAGER’, то значение равно пустой строке
  
Таблица **[dbo].[provider]** содержит информацию по провайдерам (гостиницам).  
  
  id_provider [int] - ID провайдера (уникальный ключ)  
  id_country [int] - ID страны (ссылка на [dbo].[country])  
  id_city [int] - ID города (ссылка на [dbo].[city])  
  provider_name \[nvarchar\](100) - название отеля

Таблица **[dbo].[country]** содержит название стран.

Таблица **[dbo].[city]** содержит название городов.

Таблица **[dbo].[currency_rate]** содержит информацию о курсе валюты в рубли на определенную дату.

  id_currency \[char\](3) - валюта  
  [date] [datetime] - дата, на которую актуален курс  
  [rate] [float] - курс валюты в рубли

## Создание таблиц

```sql
CREATE TABLE [dbo].[booking](  
  id_booking [int] NOT NULL PRIMARY KEY,  
  id_provider [int] NOT NULL,  
  creation_date [date] NOT NULL,  
  start_date [date] NOT NULL,  
  status [int] NOT NULL,  
  nights [int] NOT NULL,  
  price [float] NOT NULL,  
  id_currency [nvarchar] (3) NOT NULL,  
  id_source [int] NOT NULL,  
  creator [nvarchar](3) NOT NULL  
)
```
```sql
CREATE TABLE [dbo].[provider](  
  id_provider [int] NOT NULL PRIMARY KEY IDENTITY(1,1),  
  id_country [int] NOT NULL,  
  id_city [int] NOT NULL,  
  provider_name [nvarchar](100) NOT NULL  
)
```
```sql
CREATE TABLE [dbo].[country](  
  id_country [int] NOT NULL PRIMARY KEY IDENTITY(1,1),  
  country_name [nvarchar](100) NOT NULL  
)
```
```sql
CREATE TABLE [dbo].[city](  
  id_city [int] NOT NULL PRIMARY KEY IDENTITY(1,1),  
  city_name [nvarchar](100) NOT NULL  
)
```
```sql
CREATE TABLE [dbo].[source](  
  id_source [int] NOT NULL PRIMARY KEY IDENTITY(1,1),  
  source_name [nvarchar](100) NOT NULL  
)
```
```sql
CREATE TABLE [dbo].[currency_rate](  
  id_currency [char](3) NOT NULL,  
  [date] [datetime] NOT NULL,  
  [rate] [float] NOT NULL  
)
```

## Задание

1. Заполнить таблицы данными.  
**[dbo].[booking]**  
Кол-во данных: 500 000  
creation_date: 01.01.2018 - 01.03.2018  
id_provider: соответствует набору в таблице [dbo].[provider]  
id_currency: должны быть брони с различными валютами (коды валют можно посмотреть тут <http://vch.ru/zifrovye_i_bukvennye_kody_valyut_mira.html>)  
creator:  если source_name != ‘BS-CHANNEL_MANAGER’ , то значение пустая строка (‘’). В случае, когда source_name = ‘BS-CHANNEL_MANAGER’ должы быть записи со значением ‘BGC’ (но не все).  
Остальные данные могут быть заполнены рандомно.

   **[dbo].[provider]**  
Кол-во данных: 10 000  
id_country: соответствует набору в таблице [dbo].[country]  
id_city: соответствует набору в таблице [dbo].[city]  
Остальные данные могут быть заполнены рандомно.

   **[dbo].[country]**  
Кол-во данных: 20

   **[dbo].[city]**  
Кол-во данных: 300

   **[dbo].[source]**  
Кол-во данных: 10  
Должен содержать ‘BS-CHANNEL_MANAGER’, остальное может быть заполнено рандомно

   **[dbo].[currency_rate]**  
Кол-во данных: на каждую дату создания брони (01.01.2018 - 01.03.2018) должна быть запись перевода в валюты, которые имеются в таблице [dbo].[booking]  
id_currency: можно посмотреть тут <http://vch.ru/zifrovye_i_bukvennye_kody_valyut_mira.html>  
date: в пределах 01.01.2018 - 01.03.2018  
Остальные данные могут быть заполнены рандомно.

1. Создать view, где будет содержаться следующая информация:  
ID провайдера  
Название провайдера  
Страна  
Город  
Дата создания брони  
Дата заезда в брони  
Количество ночей  
Сумма брони в исходной валюте  
Валюта брони  
Сумма брони в рублях (конвертация происходит по дате создания брони)

1. Создать view, который содержал бы следующую информацию:  
ID провайдера  
Название провайдера  
Страна  
Город  
Год создания брони  
Месяц создания брони  
Доля броней среди всех броней провайдера, где source_name =  ‘BS-CHANNEL_MANAGER’  
Доля броней среди всех броней провайдера, где source_name =  ‘BS-CHANNEL_MANAGER’ и creator = ‘BGC’  

1. Создать функцию, которая на вход принимает параметр booking_depth [int] и возвращает топ 5 провайдеров по количеству броней по каждой стране, с условием, что разница между датой создания брони и датой заезда меньше, чем booking_depth.  
Страна  
ID провайдера  
Название провайдера  
Город  
Количество броней, где разница между датой создания брони и датой заезда меньше, чем booking_depth.  

1. Подсчитать среднее количество броней и среднюю сумму броней в месяц с условием,что у провайдера есть хотя бы одна бронь каждый месяц. Если в какой то из месяцев броней нет, такой провайдер не должен выводится.  
ID провайдера  
Название провайдера  
Страна  
Город  
Год создания брони  
Месяц создания брони  
Среднее количество броней  
Средняя сумма броней  
Каждый скрипт не должен выполняться дольше минуты.  

Для оптимизации можно создавать индексы.
