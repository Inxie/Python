INSERT INTO users (first_name, last_name, email)
VALUES
("Monique", "Rousseau", "moniqueprousseau@gmail.com"),
("Leslie", "Rousseau", "lprousseau@aol.com"),
("Kenneth", "Rousseau", "kvrousseau@gmail.com");

SELECT * FROM users;

SELECT * FROM users WHERE email = "moniqueprousseau@gmail.com";

SELECT * FROM users WHERE id = 3;

UPDATE users SET last_name = "Pancakes" WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name;