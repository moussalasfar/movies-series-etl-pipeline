CREATE TABLE series_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    serie_name VARCHAR(255),
    season_episode VARCHAR(100),
    categories VARCHAR(255),
    serie_rate FLOAT,
    description TEXT,
    country VARCHAR(100),
    duration VARCHAR(50),
    movie_link TEXT,
    UNIQUE (serie_name, season_episode)  -- Assurez l'unicité de la série par son nom et son épisode
);


CREATE TABLE movies_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(100),
    categories VARCHAR(255),
    movie_rate FLOAT,
    description TEXT,
    country VARCHAR(100),
    release_date DATE,
    duration INT,
    movie_link TEXT,
    UNIQUE (movie_name, release_date)  -- Limite de 150 caractères pour l'index sur movie_name
);



