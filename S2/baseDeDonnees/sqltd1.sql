ALTER TABLE Joueur ADD
(age INT),

5)
ALTER TABLE Joueur
MODIFY (age TINYINT)

6)
ALTER TABLE Spectateur
ADD(CHECK(age BETWEEN 5 AND 100))
ALTER TABLE Spectateur
MODIFY (age CHECK(age BETWEEN 5 AND 100))

7) ALTER TABLE Stade DROP COLUMN etat,

8) ALTER TABLE Joueur ADD (dateDeNaissance DATE),

9)INSERT INTO TABLE Stade VALUES (1, 'Geoffray Guichard','Saint-Etienne',35616,'bon')

10)insert into Stade (nom,ville)
values ('Stadium des champions','Trifouillis les oies')

11) update Stade
    set Etat='moyen'
    where nom="Parc des Princes"

12) delete from Match
 where date >= '01/01/2011 00:00:00' AND date <= '31/12/2011 23:59:59',
 delete from Match
  where year(date)=2011

Ex2:
1)c)
CREATE TABLE Etudiant (
    nomE VARCHAR (255)
    PrenomE VARCHAR (255)
    DateNaissanceE DATE,
    AnneePremindcE YEAR,
    AnneeEtude TINYINT
    ),
CREATE TABLE Cours (
    NomC VARCHAR(255),
    AnneeC TINYINT,
    JourC TINYINT,
    SalleC VARCHAR(5)
),

1)b)
ALTER TABLE Etudiant ADD adresse VARCHAR(255)
ALTER TABLE Etudiant ADD (
    NumRue INT,
    NomRue VARCHAR(255),
    CodePastal INT(5),
    NomVille VARCHAR(255)
),
1)c) 
ALTER TABLE Etudiant
ADD CHECK AnneePremindcE > 2000,

d) ALTER TABLE Etudiant
DROP COLUMN AnneePremindcE,

e) ALTER TABLE Etudiant 
RENAME TO Etudiant

2)ALTER TABLE Etudiant
 ADD PRIMARY KEY (NomE, PrenomE);

3)ALTER TABLE Etudiant ADD (
    IdE INT PRIMARY KEY AUTO_INCREMENT 
);

4)ALTER TABLE Cours ADD (
    IdC INT PRIMARY KEY d
);

5)CREATE TABLE PrenomsEtudiant (
    IdE INT REFERENCIES Etudiant(IdE)
    Prenom VARCHAR(255)
);

6) ALTER TABLE PrenomsEtudiant ADD (
    rang TINYINT
);

7) CREATE TABLE EtudiantSuitCours (
    IdE INT REFERENCES Etudiant(IdE)
    IdC INT REFERENCES Cours(IdC)
);

8) 
INSERT INTO Etudiant VALUES ("Dupont","Jean","23/12/11994",2012,3),
INSERT INTO Cours VALUES ("Bases de Donnees",1,5,"F101"),
INSERT INTO EtudiantSuitCours VALUES (1,1),
