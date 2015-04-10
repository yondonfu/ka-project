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
