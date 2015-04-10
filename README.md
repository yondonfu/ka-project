Khan Academy Project

Instructions to run:

git clone https://github.com/yondonfu/ka-project.git

pip install -r requirements.txt

To run total infection algorithm:
python infections.py total

To run limited infection algorithm:
python infections.py limited

Use the -u option to specify the desired number of users to infect for the limited infection algorithm

Ex.
python infections.py limited -u 7

Use the -v option to enable visualization

Ex.
python infections.py total -v
python infections.py limited -u 7 -v

Implementation Choices
Total Infection:
Used breadth-first search. Since we are dealing with "infection" I thought it would make sense to first infect all direct students of a coach before infecting the students of those students. All coach-student pairs should be on the same site version so we take into account all the coaches and all the students of each student

Limited Infection:
Also used breadth-first search, but also kept track of the current number of users to be infected. This algorithm tries to infect a number of users equal to the desired number of users passed into the algorithm. There is room for error as it is not always possible to infect the exact desired number of users. Thus, the number of infected users can exceed the desired number by a little bit.
