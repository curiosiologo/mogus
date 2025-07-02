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

-- Estado global da Emergency Meeting
CREATE TABLE emeeting (
	active INTEGER NOT NULL,
	reporter INTEGER,
	
	-- Boolean: verdadeiro se reuinão foi chamada para reportar um cadaver
	report INTEGER NOT NULL,
	
	--CHECK (impostor in (0, 1))
	
	FOREIGN KEY(reporter) REFERENCES ninja(id)
);

INSERT INTO emeeting ( active, report ) VALUES ( 0, 0 );