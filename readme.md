# Тестовое задание

Описание таблиц.

Таблица [dbo].[booking] содержит брони.

id\_booking [int]  - ID брони (уникальный ключ)
id\_provider [int] - ID провайдера (ссылка на таблицу [dbo].[provider])
creation\_date [date] - дата создания брони
start\_date [date] - дата заезда
status [int] - статус брони
nights [int] - количество ночей
price [float] - сумма брони
id\_currency [nvarchar] (3) - валюта брони 
id\_source [int] - источник брони (ссылка на таблицу [dbo].[source])
creator [nvarchar](3) - канал брони, в случае если source\_name = ‘BS-CHANNEL\_MANAGER’, если source\_name != ‘BS-CHANNEL\_MANAGER’, то значение равно пустой строке

Таблица [dbo].[provider] содержит информацию по провайдерам (гостиницам).

id\_provider [int] - ID провайдера (уникальный ключ)
id\_country  [int] - ID страны (ссылка на [dbo].[country])
id\_city  [int] - ID города (ссылка на [dbo].[city])
provider\_name  [nvarchar](100) - название отеля

Таблица [dbo].[country]  содержит название стран.

Таблица [dbo].[city]  содержит название городов.

Таблица [dbo].[currency\_rate] содержит информацию о курсе валюты в рубли на определенную дату.

id\_currency [char](3) - валюта
[date] [datetime] - дата, на которую актуален курс
[rate] [float] - курс валюты в рубли



Создание таблиц

CREATE TABLE [dbo].[booking](
id\_booking [int] NOT NULL PRIMARY KEY,
id\_provider [int] NOT NULL,
creation\_date [date] NOT NULL,
start\_date [date] NOT NULL,
status [int] NOT NULL,
nights [int] NOT NULL,
price [float] NOT NULL,
id\_currency [nvarchar] (3) NOT NULL,
id\_source [int] NOT NULL,
creator [nvarchar](3) NOT NULL
)

CREATE TABLE [dbo].[provider](
id\_provider [int] NOT NULL PRIMARY KEY,
id\_country  [int] NOT NULL,
id\_city  [int] NOT NULL,
provider\_name  [nvarchar](100) NOT NULL
)

CREATE TABLE [dbo].[country](
id\_country [int] NOT NULL PRIMARY KEY,
country\_name  [nvarchar](100) NOT NULL
)

CREATE TABLE [dbo].[city](
id\_city [int] NOT NULL PRIMARY KEY,
city\_name  [nvarchar](100) NOT NULL
)

CREATE TABLE [dbo].[source](
id\_source [int] NOT NULL PRIMARY KEY,
source\_name  [nvarchar](100) NOT NULL
)

CREATE TABLE [dbo].[currency\_rate](
id\_currency [char](3) NOT NULL,
[date] [datetime] NOT NULL,
[rate] [float] NOT NULL
)






Задания:

1) **Заполнить таблицы данными.**

*[dbo].[booking]* 

`	`Кол-во данных: 500 000

`	`creation\_date: 01.01.2018 - 01.03.2018

`	`id\_provider: соответствует набору в таблице [dbo].[provider]

id\_currency: должны быть брони с различными валютами (коды валют можно посмотреть тут <http://vch.ru/zifrovye_i_bukvennye_kody_valyut_mira.html>)

creator:  если source\_name != ‘BS-CHANNEL\_MANAGER’ , то значение пустая строка (‘’). В случае, когда source\_name = ‘BS-CHANNEL\_MANAGER’ должы быть записи со значением ‘BGC’ (но не все).

`	`остальные данные могут быть заполнены рандомно

*[dbo].[provider]*

`	`Кол-во данных: 10 000

`	`id\_country: соответствует набору в таблице [dbo].[country]

id\_city: соответствует набору в таблице [dbo].[city]

остальные данные могут быть заполнены рандомно

*[dbo].[country]*

`	`Кол-во данных: 20

*[dbo].[city]*

`	`Кол-во данных: 300

*[dbo].[source]*

`	`Кол-во данных: 10

`	`Должен содержать ‘BS-CHANNEL\_MANAGER’, остальное может быть заполнено рандомно

*[dbo].[currency\_rate]*

`	`Кол-во данных: на каждую дату создания брони (01.01.2018 - 01.03.2018) должна быть запись перевода в валюты, которые имеются в таблице [dbo].[booking]

`	`id\_currency: можно посмотреть тут <http://vch.ru/zifrovye_i_bukvennye_kody_valyut_mira.html>

`	`date: в пределах 01.01.2018 - 01.03.2018

`	`остальные данные могут быть заполнены рандомно

1) **Создать view, где будет содержаться следующая информация:**

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

1) **Создать view, который содержал бы следующую информацию:**

ID провайдера

Название провайдера

Страна

Город

Год создания брони

Месяц создания брони

Доля броней среди всех броней провайдера, где source\_name =  ‘BS-CHANNEL\_MANAGER’

Доля броней среди всех броней провайдера, где source\_name =  ‘BS-CHANNEL\_MANAGER’ и creator = ‘BGC’ 

1) **Создать функцию, которая на вход принимает параметр booking\_depth [int] и возвращает топ 5 провайдеров по количеству броней по каждой стране, с условием, что разница между датой создания брони и датой заезда меньше, чем booking\_depth.**

Страна

ID провайдера

Название провайдера

Город

Количество броней, где разница между датой создания брони и датой заезда меньше, чем booking\_depth.

1) **Подсчитать среднее количество броней и среднюю сумму броней в месяц с условием,что у провайдера есть хотя бы одна бронь каждый месяц. Если в какой то из месяцев броней нет, такой провайдер не должен выводится.**

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
