CREATE TABLE spectator (
    spec_id INT PRIMARY KEY,
    spec_name VARCHAR(15),
    category VARCHAR(15) CHECK (category IN ('student', 'senior', 'adult')),
    charge DECIMAL(5, 0)
);

INSERT INTO spectator (spec_id, spec_name, category, charge)
VALUES
    (1, 'mayuri', 'student', 500),
    (2, 'rucha', 'senior', 600),
    (3, 'shraddha', 'adult', 1000),
    (4, 'sharvari', 'student', 500),
    (5, 'pallavi', 'senior', 600),
    (6, 'chandrika', 'student', 500),
    (7, 'nikita', 'adult', 1000);

SELECT * FROM spectator;

CREATE TABLE location (
    loc_id INT PRIMARY KEY,
    stadium VARCHAR(15),
    city VARCHAR(15),
    state VARCHAR(15)
);

INSERT INTO location (loc_id, stadium, city, state)
VALUES
    (1, 'vankhede', 'mumbai', 'maharashtra'),
    (2, 'd y patil', 'vashi', 'maharashtra'),
    (3, 'abc city', 'xyz state', 'abc'),
    (4, 'pqr city', 'pqr state', 'pqr');

CREATE TABLE game (
    game_id INT PRIMARY KEY,
    game_name VARCHAR(15),
    game_type VARCHAR(15)
);


INSERT INTO game (game_id, game_name, game_type)
VALUES
    (1, 'cricket', 'outdoor'),
    (2, 'boxcricket', 'indoor'),
    (3, 'basketball', 'outdoor'),
    (4, 'football', 'outdoor'),
    (5, 'tennis', 'indoor');

CREATE TABLE g_date (
    dt_id INT PRIMARY KEY,
    day VARCHAR(15),
    month VARCHAR(15),
    year VARCHAR(15)
);


INSERT INTO g_date (dt_id, day, month, year)
VALUES
    (1, '2', 'feb', '2004'),
    (2, '6', 'march', '2004'),
    (3, '20', 'may', '2010'),
    (4, '13', 'july', '2006');


-- Create the "game_stat" table
CREATE TABLE game_stat (
    spec_id INT REFERENCES spectator (spec_id),
    loc_id INT REFERENCES location (loc_id),
    game_id INT REFERENCES game (game_id),
    dt_id INT REFERENCES g_date (dt_id),
    charge INT
);

-- Insert values into the "game_stat" table
INSERT INTO game_stat (spec_id, loc_id, game_id, dt_id, charge)
VALUES
    (1, 2, 3, 4, 500),
    (3, 2, 4, 4, 1000),
    (2, 3, 4, 2, 600),
    (5, 1, 3, 4, 500);

-- Retrieve all rows from the "game_stat" table
SELECT * FROM game_stat;



