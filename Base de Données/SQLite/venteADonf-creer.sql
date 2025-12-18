create table utilisateur(idUtil int primary key, nom varchar(50), prenom varchar(50), email text, rue text, cp int, ville text, tel int);
create table modele(idModele int primary key, nomModele text);
create table article(idArticle int primary key, nom text, descriptif text, idModele int, prix float, foreign key (idModele) references modele(idModele));
create table panier(idPanier int primary key, idUtil int, idArticle int, quantite int, total float, foreign key(idUtil) references utilisateur(idUtil), foreign key(idArticle) references article(idArticle));
