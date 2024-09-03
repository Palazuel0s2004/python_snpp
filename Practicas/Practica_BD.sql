--TABLA USUARIO
CREATE TABLE USUARIO(
    NICKNAME VARCHAR(20) NOT NULL,
    NOMBRE_APELLIDO VARCHAR(100) NOT NULL,
    EMAIL VARCHAR(50) NOT NULL,
    PASSWORD VARCHAR(10) NOT NULL,
    PRIMARY KEY(NICKNAME)
);

--TABLA GENERO
CREATE TABLE GENERO(
    ID INT AUTO_INCREMENT,
    DESCRIPCION VARCHAR(100) NOT NULL,
    PRIMARY KEY(ID)
);

--TABLA CANCION
CREATE TABLE CANCION(
    ID INT AUTO_INCREMENT,
    NOMBRE VARCHAR(100) NOT NULL,
    AUTOR VARCHAR(100) NOT NULL,
    NICKNAME VARCHAR(20) NOT NULL,
    GENERO_ID INT NOT NULL,
    PRIMARY KEY(ID)
);

ALTER TABLE CANCION ADD CONSTRAINT fk_cancion_usuario
FOREIGN KEY(NICKNAME) REFERENCES USUARIO(NICKNAME);

ALTER TABLE CANCION ADD CONSTRAINT fk_cancion_genero
FOREIGN KEY(GENERO_ID) REFERENCES GENERO(ID);

--TABLA LISTA_REPRODUCCION
CREATE TABLE LISTA_REPRODUCCION(
    ID INT AUTO_INCREMENT,
    DESCRIPCION VARCHAR(100) NOT NULL,
    NICKNAME VARCHAR(20) NOT NULL,
    PRIMARY KEY(ID)
);

ALTER TABLE LISTA_REPRODUCCION ADD CONSTRAINT fk_lista_usuario
FOREIGN KEY(NICKNAME) REFERENCES USUARIO(NICKNAME);

--TABLA LISTA_CANCION
CREATE TABLE LISTA_CANCION(
    LISTA_ID INT NOT NULL,
    CANCION_ID INT NOT NULL
);

ALTER TABLE LISTA_CANCION ADD CONSTRAINT fk_lista_cancion
PRIMARY KEY(LISTA_ID, CANCION_ID);

ALTER TABLE LISTA_CANCION ADD CONSTRAINT fk_lista_cancion
FOREIGN KEY(LISTA_ID) REFERENCES LISTA_REPRODUCCION(ID);

ALTER TABLE LISTA_CANCION ADD CONSTRAINT fk_lista_cancion
FOREIGN KEY(CANCION_ID) REFERENCES CANCION(ID);

--INSERT USUARIO
INSERT INTO USUARIO VALUES('messi', 'Roberto Carlos', 'rober300@gmail.com', '1357');
INSERT INTO USUARIO VALUES('javi85', 'Jose Ferreiro', 'javi96@gmail.com', 'qwerty2024');

UPDATE USUARIO SET NOMBRE_APELLIDO = 'Rodrigo Lezcano'
WHERE NICKNAME LIKE 'messi';

SELECT * FROM USUARIO;
SELECT email FROM USUARIO WHERE NICKNAME LIKE 'messi';

DELETE FROM USUARIO
WHERE NICKNAME = 'pepe';