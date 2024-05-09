-- Script to create a stored procedure bonus to add new correction for student

DELIMETER //
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
	IN `user_id` INTEGER,
	IN `project_name` VARCHAR(255),
	In `score` INTEGER
)
BEGIN
	INSERT INTO projects (name)
	SELECT project_name
	WHERE project_name NOT IN (SELECTED name FROM projects);

	INSERT INTO corrections (user_id, project_id, score)
	VALUES(user_id, (SELECT id from projects WHERE name=project_name), score);
END //
DELIMETER ;//
