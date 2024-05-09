-- Script to create a function that divides first by second number
-- Returning 0 if second number is equal to 0

DELIMITER //
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS INT
BEGIN
    DECLARE result INT;

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END;//
DELIMITERS ://
