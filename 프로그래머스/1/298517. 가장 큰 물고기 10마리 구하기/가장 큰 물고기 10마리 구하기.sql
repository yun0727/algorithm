-- 코드를 작성해주세요
SELECT ID, IFNULL (LENGTH,10) AS LENGTH
FROM FISH_INFO
WHERE LENGTH > 10
ORDER BY LENGTH DESC
LIMIT 10