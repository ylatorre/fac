
CREATE TABLE Usine(
    NU INT PIRMARY KEY Auto_incremente,
    NomU VARCHAR(255),
    Ville VARCHAR(255)
);
CREATE TABLE Produit(
    ND INT PIRMARY KEY Auto_incremente,
    NomP VARCHAR(255),
    Couleur VARCHAR(255),
    Poids INT
);
CREATE TABLE Fournisseur(
    NF INT PIRMARY KEY Auto_incremente,
    NomF VARCHAR(255),
    Statut VARCHAR(255),
    Ville VARCHAR(255),
);
CREATE TABLE Livraison (
    NP reference Produit(NP),
    NU reference Usine(NU),
    NF reference Fournisseur(NF),
    Quantite INT
) PIRMARY KEY (NP,NF,NU);

1)
select * form Usine
2)
select NU, NomU
  from Usine
 where 'Sochaux' = Usine.Ville;

3)
select NF
  from Livraison
 where NU = 1 and Produit.NP = 3;


4)
select NomF
  from Fournisseur, livraison
 where Fournisseur.NF = Livraison,NF and NU = 1 and and NP = 3;

5)
select NomP,Couleur
  from Produit,Livraison
 where NF = 12 and Livraison.NP = Produit.NP ;

6)
select NF
  from Livraison 
 where NU = 1 and NP in (select NP
   from Produit
  where Couleur LIKE "Rouge")

7) select NomF  
  from Fournisseur
 where NU in (select NF
   from Livraison
  where NU in (select NU from Usine where Ville LIKE "Sochaux" or "Paris") and NP in (select NP from Produit where couleur LIKE "Rouge"));

select NomF
  from Fourniseur, Usine Produit, Livraison 
 where Fournisseur.NF = Livraison.NF and Produit.NP = livraison.NP AND Usine.NU = livraison.NU And couleur = 'rouge' and (Usine.ville = "Paris" or Usine.ville="Sochaux")

8)
select NP
  from Usine, Fournisseur, Livraison
 where Livraison.NU = Usine.NU and Livraison.NF = Fournisseur.NF and Usine.ville = Fournisseur.ville
 
 9)
 select NP
  from Usine, Fournisseur, Livraison
 where Livraison.NU = Usine.NU and Livraison.NF = Fournisseur.NF and Usine.ville = Fournisseur.ville and Usine.ville = "Paris"

 select NP
   from Livraison
  where NU in(select NU
    from Usine
    where ville = "Paris"), and NF in (select NF
      from Fourniseur
      where ville="Paris")

10)
select NU 
  from Usine,Fournisseur,Livraison
 where Livraison.NU = Usine.NU and Livraison.NF = Fournisseur.NF and Usine.ville != Fournisseur.ville

 11)
 (select NF
   from Livraison
  where NU = 1)
  intersect
  (select NF
    from Livraison 
   where NU=2)

12)
select NU
  
  from Livraison
 where NO in (select NP
   
   from Livraison
  where NF = 3)

13)
select NP
  
  from Produit
 where Poids (select MIN(Poids)
   
   from Produit);

14)
select NJ
  
  from Usine
 where NU not in (select NU
   
   from Livraison,Produit,Fournisseur
  where Livraison.NP = Produit.NP and Livraison.NF = Fournisseur.NF and couleur = "rouge" and ville="Paris")

15)
select NF
  
  from Livraison
 where NP in (select NP
              from Livraison
            where NP in (select NF
              from Livraison
              where NP in(select NP
                from Produit
              where couleur="rouge")))

16)
select Fourniseur.ville AS villeF, NP,Usine.ville AS VilleU
  from Livraison,Fournisseur,Usine  
 where Livraison.NF = Fournisseur.NF and Livraison.NU = Usine.NU
 
 17)
 select Fourniseur.ville AS villeF, NP,Usine.ville AS VilleU
  from Livraison,Fournisseur,Usine  
 where Livraison.NF = Fournisseur.NF and Livraison.NU = Usine.NU

 18) select NP
   from Livraison,Usine
  where Livraison.NU =Usine.NU and ville = "Paris"
  GROUP BY NP HAVING COUNT(DISTINCT NU) = (select COUNT 
    from Usine  
   where ville="Paris")

19)
select NF
  
  from Livraison
 GROUP BY NF, NP HAVING COUNT(DISTINCT)=(select COUNT(NU) from Usine)

20)
select NU
  from Livraison
 where NF=4

 21) 
 select NU
   from Livraison
  where NU NOT IN (select NU
    from Livraison  
   where NF != 3)

22)insert into Fourniseur 
values (45,"Dupont","sous-traitant")