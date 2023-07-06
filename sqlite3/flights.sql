CREATE TABLE flights2(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  origin TEXT NOT NULL,
  destination TEXT NOT NULL,
  duration INTEGER NOT NULL
);
insert into flights2(id, origin, destination, duration)values( 'New Jersey', 'chicago', 215);