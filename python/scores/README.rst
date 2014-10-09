Scores
======

Pour commencer le projet, il faut que vous le cloniez sur votre machine, puis,
une fois dans le bon repertoire, que vous installiez virtualenv puis les
dependences du projet::

   $ virtualenv .venv
   $ source .venv/bin/activate
   $ pip install -r dev-requirements.txt

Une fois que cela est fait, le projet devrais se lancer directement si vous
faites::

  $ pserver scores.ini

Aussi, pour lancer les tests, vous pouvez simplementer lancer::

  $ unit2 discover
