-- Script to create an index on a table names and the first letter of name

CREATE INDEX idx_name_first ON name(name(1));
