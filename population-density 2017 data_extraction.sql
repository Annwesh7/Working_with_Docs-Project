/*
The following query will extract population density of each entity for the year 2017
*/

SELECT *
FROM Tutorial_Project.dbo.Sheet1$population_density
WHERE YEAR = 2017
ORDER BY Entity 