use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product;

-- 2. Выбрать названия всех автоматизированных складов
SELECT name FROM test.store WHERE is_automated=1;

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT SUM(total) FROM sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT DISTINCT store_id FROM sale WHERE quantity>0;

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT store_id FROM store NATURAL LEFT JOIN test.sale WHERE sale_id IS NULL;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
SELECT name, AVG(sale.total/sale.quantity) FROM product NATURAL JOIN sale GROUP BY name;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
SELECT ANY_VALUE(name) FROM product NATURAL JOIN sale GROUP BY product_id HAVING COUNT(DISTINCT store_id)=1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
SELECT ANY_VALUE(name) FROM store NATURAL JOIN sale GROUP BY product_id HAVING COUNT(DISTINCT store_id)=1;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
SELECT * FROM sale WHERE total = (SELECT MAX(total) FROM sale);

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
SELECT date FROM (SELECT date, SUM(total) as total FROM sale GROUP BY date) n 
WHERE total = (SELECT MAX(total) FROM (SELECT date, SUM(total) as total FROM sale GROUP BY date) m) ORDER BY date LIMIT 1;

-- Professor's variant
-- select date from sale group by date order by sum(total) DESC, date ASC LIMIT 1
