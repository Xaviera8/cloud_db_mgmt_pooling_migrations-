CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 7aeb93509bfb

INSERT INTO alembic_version (version_num) VALUES ('7aeb93509bfb');

