-- store average score
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser$$

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE average_score DECIMAL(10, 1);

    SELECT AVG(score) INTO average_score
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users SET average_score = average_score WHERE id = user_id;
END$$

DELIMITER ;
