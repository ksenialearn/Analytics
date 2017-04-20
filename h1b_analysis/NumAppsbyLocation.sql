SELECT lon, lat, COUNT(id) AS NumApps
FROM h1bdata.data
WHERE YEAR = 2016 AND lon is not NULL
GROUP BY lon, lat
ORDER BY NumApps DESC;
