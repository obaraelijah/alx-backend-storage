-- Create an index idx_name_first_score on  table names on the 
-- first letter of name and the score.

CREATE INDEX idx_name_first_score ON names(name(1), score);
