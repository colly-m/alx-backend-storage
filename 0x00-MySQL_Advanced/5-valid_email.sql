-- Script to create a trigger that resets attribute valid_email
-- Only when email has been changed

DELIETER $$
CREATE TRIGGER new_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
	SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITTER ;$$
