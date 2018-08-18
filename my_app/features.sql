PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE area (
	id INTEGER NOT NULL, 
	name VARCHAR(50), 
	PRIMARY KEY (id)
);
INSERT INTO "area" VALUES(1,'Policies');
INSERT INTO "area" VALUES(2,'Billing');
INSERT INTO "area" VALUES(3,'Claims');
INSERT INTO "area" VALUES(4,'Reports');
CREATE TABLE client (
	id INTEGER NOT NULL, 
	name VARCHAR(100), 
	PRIMARY KEY (id)
);
INSERT INTO "client" VALUES(1,'Client A');
INSERT INTO "client" VALUES(2,'Client B');
INSERT INTO "client" VALUES(3,'Client C');
CREATE TABLE feature (
	id INTEGER NOT NULL, 
	title VARCHAR(255), 
	description VARCHAR(2048), 
	client_priority INTEGER, 
	target_date DATE, 
	area_id INTEGER, 
	client_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(area_id) REFERENCES area (id), 
	FOREIGN KEY(client_id) REFERENCES client (id)
);
COMMIT;
