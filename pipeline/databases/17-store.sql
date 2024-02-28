-- Create the trigger
DELIMITER //
CREATE TRIGGER decrease_item_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the item in the items table
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE item_name = NEW.item_name;
END;
//
DELIMITER ;