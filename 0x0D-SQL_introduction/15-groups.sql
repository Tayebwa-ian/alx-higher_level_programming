-- lists the number of records with the same score in the table second_table
-- SQL statement
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY SCORE
ORDER BY number DESC;
