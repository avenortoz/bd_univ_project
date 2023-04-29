--Відповідність посада - зарплата:
CREATE FUNCTION GetJobTitleAndSalary()
RETURNS TABLE
AS
RETURN
    SELECT 
        JobTitle, 
        AVG(Salary) AS AverageSalary 
    FROM Employees 
    GROUP BY JobTitle;
