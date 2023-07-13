-- Create table users if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
    -- Unique identifier for each user
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    
    -- Email of the user (maximum 255 characters)
    email VARCHAR(255) NOT NULL UNIQUE,
    
    -- Name of the user (maximum 255 characters)
    name VARCHAR(255)
);
