CREATE TABLE IF NOT EXISTS addresses (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(10),
    zipcode VARCHAR(20),
    country VARCHAR(50),
    valid BOOLEAN DEFAULT false
);

INSERT INTO addresses 
(first_name, last_name, address, city, state, zipcode, country, valid)
VALUES
('Ben', 'Doe', '69 Young street', 'Mount Juliet', 'TN', '37122', 'USA', false),
('Brad', 'Fields', '8430 Lake lane', 'Phoenixville', 'PA', '19460', 'USA', false),
('John', 'Baldwin', '67 Snake hill dr.', 'Dallas', 'GA', '30132', 'USA', false),
('Mark', 'Newton', '241 N. Victoria Ave.', 'Dorchester center', 'MA', '02124', 'USA', false),
('Derek', 'Parker', '731 Brickyard st', 'Worcester', 'MA', '01604', 'USA', false),
('Michael', 'Stoken', '9115 Sycamore circle', 'Portage', 'IN', '46368', 'USA', false),
('Joseph', 'Tanner', '231 Kent drive', 'Cincinnati', 'OH', '45211', 'USA', false),
('Neil', 'Spencer', '9125 Hudson street', 'Orange Park', 'FL', '32065', 'USA', false),
('Ross', 'Pitt', '622 Bayberry rd.', 'Tuscaloosa', 'AL', '35405', 'USA', false),
('Jude', 'Bauer', '80 White avenue', 'Riverview', 'FL', '33569', 'USA', false),
('Zack', 'Burton', '57 Young dr', 'Cary', 'NC', '27511', 'USA', false),
('Matthew', 'Henderson', '659 South Country Club street', 'Stone mountain', 'GA', '30083', 'USA', false);
