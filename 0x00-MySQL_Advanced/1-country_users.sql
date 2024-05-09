-- Sceipt to create a table users with country ENUM

CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
