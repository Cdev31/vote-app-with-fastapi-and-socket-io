CREATE DATABASE votedb;

USE votedb;

CREATE TABLE users(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(12) NOT NULL,
    dui CHAR(12) NOT NULL,
    UNIQUE ( email ),
    UNIQUE( password ),
    UNIQUE ( dui )
);

CREATE TABLE surveys (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    user_id INTEGER NOT NULL,
    start_hour TIME NOT NULL,
    start_date DATE NOT NULL,
    end_hour TIME NOT NULL,
    end_date DATE NOT NULL,
    active BOOLEAN NOT NULL,
    status ENUM('Active', 'Completed', 'Canceled'),
    CONSTRAINT FK_USER FOREIGN KEY ( user_id ) REFERENCES users( id ),
    CONSTRAINT CHECK_DATE CHECK( start_date <= end_date )
);

CREATE TABLE surveys_option (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    survey_id INTEGER NOT NULL,
    CONSTRAINT FK_SURVEY FOREIGN KEY ( survey_id ) REFERENCES surveys( id )
);

CREATE TABLE voters (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(255) NOT NULL,
    dui CHAR(12) NOT NULL,
    UNIQUE ( email ),
    UNIQUE ( dui )
);

CREATE TABLE votes(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    surveys_option_id INTEGER NOT NULL,
    voter_id INTEGER NOT NULL,
    CONSTRAINT FK_SURVEYS_OPTION FOREIGN KEY ( surveys_option_id ) REFERENCES surveys_option ( id ),
    CONSTRAINT FK_VOTER FOREIGN KEY ( voter_id ) REFERENCES voters( id )
);

/* Triggers of check users */
DELIMITER //

CREATE TRIGGER validate_users BEFORE INSERT ON users
FOR EACH ROW 
BEGIN
    IF NEW.dui NOT REGEXP '^[0-9]{8}-[0-9]$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid dui format';
    END IF;
    IF NEW.email NOT REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'invalid email format';
    END IF;
    IF NEW.phone_number NOT REGEXP '^[0-9]{4}-[0-9]{4}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'invalid phone number format';
    END IF;
END //

DELIMITER ;

DELIMITER //
CREATE TRIGGER validate_voters BEFORE INSERT ON voters
FOR EACH ROW 
BEGIN
    IF NEW.dui NOT REGEXP '^[0-9]{8}-[0-9]$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid dui format';
    END IF;
    IF NEW.email NOT REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'invalid email format';
    END IF;
END //

DELIMITER ;

/* Get list of triggers */
SELECT TRIGGER_NAME, EVENT_MANIPULATION, EVENT_OBJECT_TABLE, ACTION_TIMING
FROM information_schema.triggers
WHERE TRIGGER_SCHEMA = 'votedb';
