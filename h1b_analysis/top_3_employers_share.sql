
SELECT EMPLOYER_NAME, NumApps, NumApps/(SELECT COUNT(id) 
																					FROM h1bdata.data
                                                                                    WHERE YEAR=2016 AND EMPLOYER_NAME is not NULL)*100 AS PercentOfTotal
FROM

	(SELECT EMPLOYER_NAME, COUNT(id) AS NumApps
	FROM h1bdata.data
	WHERE YEAR = 2016
	GROUP BY EMPLOYER_NAME) AS grouped
    
WHERE EMPLOYER_NAME IN ('INFOSYS LIMITED', 'WIPRO LIMITED', 'TATA CONSULTANCY SERVICES LIMITED')
GROUP BY EMPLOYER_NAME;
