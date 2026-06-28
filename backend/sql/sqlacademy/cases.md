
![1782570590335](image/cases/1782570590335.png)


# Товары, купленные более одного раза

Определить товары, которые покупали более 1 раза

```SQL
select DISTINCT g.good_name from goods g 
join Payments p on p.good = g.good_id
GROUP BY g.good_id
HAVING COUNT(*) > 1
```

# Кто покупал картошку

Определить, кто из членов семьи покупал картошку (potato)

```SQL
select distinct status from FamilyMembers
join Payments on Payments.family_member = FamilyMembers.member_id
join Goods on Goods.good_id = Payments.good
where Goods.good_name = 'potato';
```



# Траты членов семьи в 2005 году

Определить, сколько потратил в 2005 году каждый из членов семьи. В результирующей выборке не выводите тех членов семьи, которые ничего не потратили.

Используйте конструкцию "as costs" для отображения затраченной суммы членом семьи. Это необходимо для корректной проверки.

Поля в результирующей таблице: member_name, status, costs

```SQL
SELECT fm.member_name, fm.status, SUM(p.unit_price * p.amount) as costs FROM Payments p
JOIN FamilyMembers fm on fm.member_id = p.family_member
WHERE p.date >= '2005-01-01'
AND p.date < '2006-01-01'
GROUP BY fm.member_name, fm.status;
```
