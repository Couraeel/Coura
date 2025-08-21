%Questao 1
%Base de Fatos

cachorro(doky).
gato(garfield).
peixe(nemo).
passaro(dudu).
pessoa(joao).
pessoa(maria).
magro(doky).
gordo(garfield).

%Regras

gosta(X,Y) :- gato(X), peixe(Y).
gosta(X,Y) :- gato(X), passaro(Y).
gosta(X,Y) :- cachorro(X), pessoa(Y).
gosta(X,Y) :- gato(X), pessoa(Y).

come(X,Y) :- gosta(X,Y), \+ pessoa(Y).


%Questao 2
%Base de Fatos

homem(marcos).
homem(rodrigo).
homem(silvio).
mulher(ana).
mulher(maria).

bonito(ana).
bonito(marcos).
rico(marcos).
rico(maria).
forte(maria).
forte(rodrigo).
bonito(rodrigo).
amavel(silvio).
forte(silvio).

%Regras

gosta(Homem,Mulher) :- homem(Homem), mulher(Mulher), bonito(Mulher).

feliz(Homem) :- homem(Homem), rico(Homem).
feliz(Homem) :- gosta(Homem,Mulher), gosta(Mulher,Homem).
feliz(Mulher) :- gosta(Mulher,Homem), gosta(Homem,Mulher).

gosta(Maria,Homem) :- homem(Homem), gosta(Homem,Maria).
gosta(ana,Homem) :- homem(Homem), gosta(Homem,ana), rico(Homem), amavel(Homem).
gosta(ana,Homem) :- homem(Homem), gosta(Homem,ana), bonito(Homem), forte(Homem).


