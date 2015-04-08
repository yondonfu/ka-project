from models import User

"""
User attributes:
- Site version (i.e. A, B, C, D, etc.)
- Coaches (list of users that are this user's coaches)
- Students (list of users that are coached by this user)

Total infection
Given a starting user, infect the the coaching graph that
the user is contained in
Treat the coaching graph as a directed graph
First infect all users that have a directed edge pointed toward
them from the starting user
Second infect all users that have a directed edge pointed toward
them from any of the first wave of infectees
And so on...

Modified BFS?

Limited infection
Given a number of users that we would like to infect and a starting user
infect the coaching graph that the user is contained in
such that
number of users vs. coach and all students
"""
users = []

def limited_infection(start_user, num_users, new_site_version):
  pass

def total_infection(start_user, new_site_version):
  visited, queue = set(), []

  queue.append(start_user)

  while queue:
    user = queue.pop(0)
    if user not in visited:
      visited.add(user)
      user.site_version = new_site_version

      # All coach-student pairs should be on the same
      # site version
      for student in user.students:
        queue.append(student)

      for coach in user.coaches:
        queue.append(coach)


def init_users():
  user_1 = User(user_id=1, site_version='A')
  user_2 = User(user_id=2, site_version='A')
  user_3 = User(user_id=3, site_version='A')
  user_4 = User(user_id=4, site_version='A')
  user_5 = User(user_id=5, site_version='A')
  user_6 = User(user_id=6, site_version='A')
  user_7 = User(user_id=7, site_version='A')
  user_8 = User(user_id=8, site_version='A')

  user_1.add_student(user_2)
  user_1.add_student(user_3)
  user_1.add_student(user_4)
  user_2.add_student(user_5)
  user_6.add_student(user_7)
  user_8.add_student(user_3)

  users.append(user_1)
  users.append(user_2)
  users.append(user_3)
  users.append(user_4)
  users.append(user_5)
  users.append(user_6)
  users.append(user_7)
  users.append(user_8)

if __name__=="__main__":
  init_users()
  print "Before infection:"
  for user in users:
    print str(user.user_id) + " ---> " + str(user.site_version)

  total_infection(start_user=users[0], new_site_version='B')
  print "After infection:"
  for user in users:
    print str(user.user_id) + " ---> " + str(user.site_version)