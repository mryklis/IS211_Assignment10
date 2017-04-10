CREATE TABLE artists (
	artist_id INTEGER PRIMARY KEY ASC,
	artist TEXT
);

CREATE TABLE albums (
	album_id INTEGER PRIMARY KEY ASC,
	album TEXT,
	artist_id INT
	FOREIGN KEY(artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE songs (
	song_id INTEGER PRIMARY KEY ASC,
	song TEXT,
	track_num INT,
	duration TIME,
	album_id INT
	FOREIGN KEY(album_id) REFERENCES albums(album_id)
);