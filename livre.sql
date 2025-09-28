create table Livre(ID : int primary key , Titre : TEXT,  Langue : TEXT, Publication : INT, Note : INTEGER, Auteur : INT, foreign key(Auteur) references Auteur(ID));
create table Auteur(ID : INT primary key, Nom : TEXT, Prenom : TEXT, Naissance : INT);
Insert into Livre vAlUes (1, '1984', 'anglais', 1949, 10), (2, 'Dune', 'anglais', 1965, 8), 
 (3, 'Fondation', 'anglais', 1951, 9), (4, 'Le meilleur des mondes', 'anglais', 1931, 7), (5, 'Farhenheit 451', 'anglais', 1953, 7), 
  (6, 'Ubik', 'anglais', 1969, 9), (7, 'Chroniques martiennes', 'anglais', 1950, 8),
  (8, 'La nuit des temps', 'français', 1968, 7), (9, 'Blade Runner', 'anglais', 1968, 8), 
  (10, 'Les Robots', 'anglais', 1950, 9), 
  (11, 'La Planète des singes', 'français', 1963, 8), (12, 'Ravage', 'français', 1943, 8),
  (13, 'Le Maitre du Haut Château', 'anglais', 1962, 8),
  (14, 'Le monde des Â', 'anglais', 1945, 7), (15, "La Fin de l'éternite", 'anglais', 1955, 8),
  (16, 'De la Terre à la Lune', 'français', 1865, 10);
insert into Auteur values (1, 'Orwell', "George", 1903), (2, 'Herbert', "frank", 1920),
  (3, 'Asimov', "Isaac", 1920),(4, 'Huxley', "Aldous", 1894),
  (5, 'Bradbury', "Ray", 1920),(6, 'K.Dick', "Phiip", 1928),
  (7, 'Bradbury', "Ray", 1920),(8, 'Barjavel', "René", 1911),
  (9, "K.Dick", "Philip", 1928),(10, 'Asimov', "Isaac", 1920),
  (11, 'Bonelle', "Pierre", 1912),(12, 'Barjavel', "René", 1911),
  (13, 'K.Dick', "Philip", 1928),(14, 'Van Vogt', "Alfred Elton", 1912),
  (15, 'Asimov', "Isaac", 1920),(16, 'Verne', "Jules", 1828);
select ID, Titre from Livre;
select Titre from Livre where Langue = 'français';
select ID, Titre from Livre where Publication > 1960;
select Nom from Auteur inner join Livre on Auteur.ID = Livre.Auteur where Langue = 'anglais';
select Nom, Prenom from Auteur inner join Livre on Auteur.ID = Livre.Auteur where Note >= 9;

