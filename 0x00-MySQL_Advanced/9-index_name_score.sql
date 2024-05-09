-- Script to create an index on the table names
-- and first letter of name and the score

CREATE TABLE idx_name_first_score ON names(name(1), score);
