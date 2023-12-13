-- Create Database

create database if not exists hbtn_0c_0; -- Charlength * order
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
