-- -- 코드를 입력하세요
-- SELECT HOUR, COUNT(ANIMAL_ID) AS COUNT FROM (SELECT TO_CHAR(DATETIME, 'HH')*1 AS HOUR, ANIMAL_ID FROM ANIMAL_OUTS) WHERE HOUR between 9 and 20 GROUP BY HOUR ORDER BY HOUR

SELECT to_number(to_char(DATETIME,'hh24')) as HOUR, count(*) as COUNT
from ANIMAL_OUTS 
where to_char(DATETIME,'hh24:mi') between '09:00' and '19:59'
group by to_char(DATETIME,'hh24') 
order by HOUR;