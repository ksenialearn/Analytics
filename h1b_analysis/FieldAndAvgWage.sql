
SELECT SOC_NAME, COUNT(id) AS NumberApplications, COUNT(id)/(SELECT COUNT(id) FROM h1bdata.data)*100 AS ShareOfTotalAsPercent, 
			AVG(PREVAILING_WAGE),  STDDEV(PREVAILING_WAGE)
FROM h1bdata.data
WHERE YEAR = 2016
GROUP BY SOC_NAME
ORDER BY COUNT(id) DESC;