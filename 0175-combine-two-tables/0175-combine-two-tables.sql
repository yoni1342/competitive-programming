# Write your MySQL query statement below
SELECT Person.firstname, Person.lastname, Address.city, Address.state
From Address RIGHT JOIN Person on Address.personId=Person.personId;