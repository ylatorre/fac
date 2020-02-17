1)
CREATE InfoPays (
    Pays VARCHAR(255) PRIMARY KEY,
    Langue VARCHAR(255),
);
CREATE PaysConstructeur (
    Marque VARCHAR(255) PRIMARY KEY,
    Pays VARCHAR(255) REFERENCES InfoPays(Pays),
);
CREATE Auto (
    IdAuto INT PRIMARY KEY AUTO_INCREMENT,
    Marque VARCHAR(255) REFERENCES PaysConstructeur(Marque),
    Modele VARCHAR(255),
    Puissance INT,
);

2)
-- - Selection tous dans le tableau Auto
Tous afficher de Auto 

-- - Selection la colonne marque dans le tableau Auto
Afficher les Marques de Auto 
-- - Selection la colonne marque sans prendre les doublons dans le tableau Auto
Afficher les marques sans doublons de Auto
-- - Selection tous dans le tableau Auto a condition que dans la colonne Puissance la valeur soit egale a 4
Affiche tous les auto de puissance 4
-- - Selection Marque dans le tableau PaysConstructeur et Langue dans le tableau InfoPays
Afficher la marque et leur langue 

-- - Selection Marque dans le tableau PaysConstructeur et Langue dans le tableau InfoPays a conditions que
Afficher la marque qui on en commun leur pays et afficher leur langue 

-- --------
Afficher les marques dont la langues est le francais

SELECT  Marque 
FROM PaysConstructeur 
WHERE Pays IN (SELECT Pays FROM InfoPays WHERE Langue LIKE "Francais")

SELECT modele FROM Auto WHERE Puissance >= 6;

select Marque
  from PaysConstructeur
 where "France" = Pays;

 select pays
   from InfoPays
  where "Anglais" = langue; 

select puissance
  from Auto,PaysConstructeur
  where Auto.Marque = PaysConstructeur.Marque AND Pays LIKE "Francais";
OU 
select Puissance
  from Auto
 where Pays IN (select PaysConstructeur
   from PaysConstructeur
  where Pays LIKE "France");



select Puissance
  from Auto
 where Marque IN (select Marque
   from PaysConstructeur
  where Pays in (select Pays
    
    from InfoPays
   where Langue LIKE "Anglais")

