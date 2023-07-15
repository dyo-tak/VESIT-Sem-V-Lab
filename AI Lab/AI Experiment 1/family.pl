female(swara).
female(monisha).
female(aditi).
female(preesha).
female(nikhili).
female(kinari).
female(teena).
female(bhagyashri).
female(mrunal).
female(madhura).


male(nuren).
male(dyotak).
male(yash).
male(dhruv).
male(mandar).
male(mayur).
male(nishant).
male(pranav).
male(nandan).
male(mukund).


parent(mandar,dyotak).
parent(nikhili,dyotak).
parent(mandar,nuren).
parent(nikhili,nuren).

parent(kinari,yash).
parent(pranav,yash).
parent(kinari,swara).
parent(pranav,swara).

parent(nishant,monisha).
parent(tina,monisha).
parent(nishant,preesha).
parent(teena,preesha).

parent(mayur,dhruv).
parent(bhagyashri,dhruv).
parent(mayur,aditi).
parent(bhagyashri,aditi).

parent(mukund,mandar).
parent(madhura,mandar).
parent(mukund,mayur).
parent(madhura,mayur).

parent(nandan,nikhili).
parent(mrunal,nikhili).
parent(nandan,nishant).
parent(mrunal,nishant).
parent(nandan,kinari).
parent(mrunal,kinari).


mother(X,Y):- parent(X,Y),female(X).
daughter(Y,X):- parent(X,Y),female(Y).
father(X,Y):-parent(X,Y),male(X).
son(Y,X):-parent(X,Y),male(Y).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandparent(X,Y):-parent(X,Z),parent(Z,Y).
grandmother(X,Z):-mother(X,Y),parent(Y,Z).
grandfather(X,Z):-father(X,Y),parent(Y,Z).
wife(X,Y):-parent(X,Z),parent(Y,Z),female(X),male(Y).
kaka(X,Z):-brother(X,Y),father(Y,Z).
mama(X,Z):-brother(X,Y),mother(Y,Z).
kaki(X,Z):-wife(X,Y),kaka(Y,Z).
mami(X,Z):-wife(X,Y),mama(Y,Z).


