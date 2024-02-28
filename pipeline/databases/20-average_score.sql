-- store average score
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser ()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id_val INT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN user_cursor;
    user_loop: LOOP
        FETCH user_cursor INTO user_id_val;
        IF done THEN
            LEAVE user_loop;
        END IF;
        DECLARE avg_score DECIMAL(10, 2);
        SELECT AVG(score) INTO avg_score
        FROM corrections
        WHERE user_id = user_id_val;
        INSERT INTO user_scores (user_id, average_score)
        VALUES (user_id_val, avg_score)
        ON DUPLICATE KEY UPDATE average_score = avg_score;

    END LOOP user_loop;

    CLOSE user_cursor;
END //

DELIMITER ;