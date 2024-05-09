-- Script to create a function that divides first by second number
-- Returning 0 if second number is equal to 0

DELIMITER //
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END;//
DELIMITERS ://
