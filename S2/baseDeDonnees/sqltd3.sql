
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
