-- store average score
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;
    INSERT INTO user_scores (user_id, average_score)
    VALUES (user_id, avg_score)
    ON DUPLICATE KEY UPDATE average_score = avg_score;

END //

DELIMITER ;