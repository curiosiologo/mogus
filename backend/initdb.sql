CREATE TABLE ninja (
	id INTEGER PRIMARY KEY NOT NULL,
   	impostor INTEGER NOT NULL,
	name TEXT NOT NULL,
	killed_by INTEGER,
	cooldown INTEGER NOT NULL,
	
	--CHECK (impostor in (0, 1)),
	--CHECK (cooldown in (0, 1)),
	
	FOREIGN KEY(killed_by) REFERENCES ninja(id)
);

CREATE TABLE task (
	name TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE completed_task (
	ninja_id INTEGER NOT NULL,
	task TEXT NOT NULL,
	
	FOREIGN KEY(ninja_id) REFERENCES ninja(id),
	FOREIGN KEY(task) REFERENCES task(name),
	
	PRIMARY KEY(ninja_id, task)
);

CREATE TABLE log (
	id INTEGER PRIMARY KEY NOT NULL,
	msg TEXT NOT NULL
);

CREATE TABLE events (
	emergency_meeting INTEGER NOT NULL PRIMARY KEY
	
	--CHECK (impostor in (0, 1))
);

INSERT INTO events ( emergency_meeting ) VALUES ( 0 );