-- create trigger that resets the atribute
DELIMITER //

CREATE TRIGGER email_changed_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//

DELIMITER ;