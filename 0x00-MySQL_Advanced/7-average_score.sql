-- Script to create a stored procedure that computes and stores avarage scores

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUSer(IN `user_id` INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT AVG(score)
			    FROM corrections
			    WHERE corrections.user_id = user_id)
	WHERE id = user_id;
END //
DELIMITER ;//
