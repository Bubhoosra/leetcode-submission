# Write your MySQL query statement below
SELECT second.id
FROM weather second, weather first
where second.temperature>first.temperature and DATEDIFF(second.recordDate,first.recordDate)=1 