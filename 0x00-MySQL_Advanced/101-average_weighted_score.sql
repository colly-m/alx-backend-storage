-- Script to create a stored procedure to compute
--Also stores the avarage weighted score for all students

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers
BEGIN
	UPDATE users set average_score = (SELECT
	SUM(corrections.score * project.weight) / SUM(projects.weight)
	FROM corrections
	INNER JOIN projects
	ON projects.id = corrections.project_id
	WHERE corrections.user_id = users.id);
END //
DELIMITER ;
