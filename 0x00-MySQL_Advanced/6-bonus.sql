-- Script to create a store procedure AddBonus to add a student's correction

DELIMITER $$

DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
	IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER
)
BEGIN
    DECLARE project_id INTEGER;

    INSERT INTO projects (name)
    SELECT project_name
    FROM dual
    WHERE NOT EXISTS (SELECT name FROM projects WHERE name = project_name);

    SELECT id INTO project_id FROM projects WHERE name = project_name;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES(user_id, project_id, score);

END $$

DELIMITER ;
