CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS VARCHAR(255)
BEGIN
    DECLARE result VARCHAR(255);
    
    IF b = 0 THEN
        SET result = CONCAT('SafeDiv(', a, ', ', b, ')0');
    ELSE
        SET result = CONCAT('SafeDiv(', a, ', ', b, ')', a / b);
    END IF;
    
    RETURN result;
END;