CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 467da026b324

INSERT INTO alembic_version (version_num) VALUES ('467da026b324');

-- Running upgrade 467da026b324 -> f7473311df2e

ALTER TABLE patients ADD COLUMN is_alive VARCHAR(50) NOT NULL;

UPDATE alembic_version SET version_num='f7473311df2e' WHERE alembic_version.version_num = '467da026b324';

