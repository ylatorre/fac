2.1)
select count(N~Etudiant)
  
  from Etudiant

2.2) 
select MAX(Note),MIN(Note) 
    from Evaluer
2.3)
create table MoyenneEtudoantMatiere AS (
    select Etudiant, Nom, Prenom, LibelleMatiere, CoefficientMatiere, AVG(Note) AS MoyEtuMat
      from Evaluer, Etudiant, Matiere
     where Etudiant.N~Etudiant = Evaluer.N~Etudiant and Matiere.CodeMatiere = Evaluer.CodeMatiere
     group by Etudiant.N~Etudiant, Matiere.CodeMatiere
)

2.4)
select LibelleMatiere, AVG(MoyEtuMat)   
  from MoyenneEtudoantMatiere
  group by LibelleMatiere

2.5) 
select N~Etudiant,Nom,Prenom,SUN(CoefficientMatiere * MoyEtuMat)/SUN(CoefficientMatiere)
  from MoyenneEtudiant Matiere
 group by N~Etudiant


3.1)
select NumeroCoureur,NomCoureur,NomPays
  from Coureur,Equipe,Pays
 where Coureur.CodeEquipe = Equipe.CodeEquipe and Coureur.CodePays = Pays.CodePays and NomEquipe = "Quickslep";

3.2)
select SUN(NbKm)
  from Etage

3.3) 
select SUN(NbKm)
  from Etage,TypeEtage
 where TypeEtage.CodeType=Etage.CodeType AND Libelle.Type="Haute Montage";

3.4)
select NomCoureur
  from Coureur
 where NumeroCoureur not in (select NumeroCoureur from AttribuerBonification);

3.5)
select NomCoureur
  from Coureur,Equipe,Etage,Participe
 where Coureur.CodeEquipe =Equipe.CodeEquipe and Coureur.NumeroCoureur = Participe.NumeroCoureur and Participe.NumeroEtage =Etage.NumeroEtage and NomDirection.Sportif = VilleArriver and TempsRealise < "05:00:00"

3.6)
select NomCoureur
  from Coureur,Participer  
 where Coureur.NumeroCoureur:Participer.

 3.9) 
 select NumeroCoureur, NomCoureur, SUN(NbKm), AVG(NbKm)
 from Coureur, Participe, Etape
 where Coureur.NumeroCoureur = Participer.NumeroCoureur and Participer.NumeroEtage = Etape.NumeroEtage

3.10)
 select NumeroCoureur, SUN(NbSecondes)
   from Atribuer.bonfienten
  group by NumeroCoureur:

4.1)
select NumeroEtudiant, NumEtudiant
  from Etudiant
 where NumeroEtudiant NOT IN (select NumeroEtudiant from Notes,Matiere)

 4.2)
Select NomEnseignant, Grade, Anciente
From Enseignant, Matiere
where Enseignant.NumeroEtudiant = Matiere.NumeroEnseignant
group by NomEnseignant
having count(NumeroMatiere) > 1;

4.3)
select NomEnseignant, NomMatiere, AVG(Note)
  from Enseignant, Matiere, Note
 where Enseignant.NomEnseignant = Matiere>NumeroEnseignant and Matiere.NumeroMatiere = Note.NumeroMatiere and Matiere>NumeroMatiere = Note.NumeroMatiere
 group by NomMatiere having AVG(Note)<10;

4.4)
select NomMatiere
  from Matiere,Notes,Etudiant
 where Matiere.Numero = Notes.NumeroMatiere and Etudiant.

4.5)
SELECT Sexe, SUM(Note)/COUNT(Note)
FROM Etudiant, Notes, Matieres, NomEnseignant
WHERE Etudiant.NumeroEtudiant = Note.NumeroEtudiant
AND Notes.NumeroMatiere = Matiere.NumeroMatiere
AND Matiere.NumeroEnseignant = Enseignant.NumeroEnseignant
AND NomEnseignant= "Jean Bonnot"
GROUP BY Sexe;

4.6)
select NomEtudiant
  from Etudiant,Notes,Matiere
 where Etudiant.