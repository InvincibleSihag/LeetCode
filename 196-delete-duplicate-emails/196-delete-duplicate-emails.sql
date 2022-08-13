# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

# DELETE FROM Person WHERE COUNT()

delete from Person where id not in (select minid from (select min(id) as minid from Person group by Person.email) as a);

