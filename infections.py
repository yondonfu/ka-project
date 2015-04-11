import argparse
from models import User
import networkx as nx
import matplotlib
# Need to use TkAgg backend instead of MacOSX backend or else
# the matplotlib window will not be able to be a top-level window
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

users = []
infection_path = []
colorlist = []
edge_list = []
TOTAL_USERS = 12

# Get index in a subset list of users such that
# the index corresponds with the user with the most
# students
def user_index_most_students(users):
  user_students = [len(user.students) for user in users]
  return user_students.index(max(user_students))
 
def limited_infection(num_users, new_site_version):
  curr_infected = 0
  visited, queue = set(), []
  infect = set()

  # Set of total users - set of users that have been visited = set of
  # univisted u sers
  while set(users) - visited:
    unvisited = list(set(users) - visited)
    queue.append(unvisited.pop(user_index_most_students(unvisited)))

    while queue:
      user = queue.pop(0)

      if user not in visited:
        visited.add(user)

        should_infect_students_coaches = False

        if user in infect:
          user.site_version = new_site_version
          infection_path.append(user.user_id)
          infect.remove(user)

          proj_infect = curr_infected + len(set(user.students) - visited) + \
            len(set(user.coaches) - visited)

          if num_users - proj_infect >= 0 or proj_infect - num_users <= 2:
            curr_infected += len(set(user.students) - visited) + len(set(user.coaches) - visited)
            should_infect_students_coaches = True

        else:
          proj_infect = curr_infected + len(set(user.students) - visited) + \
            len(set(user.coaches) - visited) + 1

          if num_users - proj_infect >= 0 or proj_infect - num_users <= 2:
            user.site_version = new_site_version
            infection_path.append(user.user_id)
            curr_infected += len(set(user.students) - visited) + len(set(user.coaches) - visited) + 1
            should_infect_students_coaches = True
          else:
            # This user and all its students will not be affected
            # so we can just mark all of its students as visited
            # because the infection will not spread anymore from this user
            for student in user.students:
              visited.add(student)
            break

        for student in user.students:
          queue.append(student)

          if should_infect_students_coaches:
            infect.add(student)

        for coach in user.coaches:
          queue.append(coach)

          if should_infect_students_coaches:
            infect.add(coach)


def total_infection(start_user, new_site_version):
  visited, queue = set(), []

  queue.append(start_user)

  while queue:
    user = queue.pop(0)
    if user not in visited:
      visited.add(user)
      user.site_version = new_site_version
      infection_path.append(user.user_id)

      # All coach-student pairs should be on the same
      # site version
      for student in user.students:
        queue.append(student)

      for coach in user.coaches:
        queue.append(coach)

def add_user():
  user = User(user_id=len(users)+1, site_version='A')
  users.append(user)

def add_coach_and_student(user_1, user_2):
  user_1.add_student(user_2)
  edge_list.append((user_1, user_2))

def init_users():
  for i in range(0, TOTAL_USERS):
    add_user()

  add_coach_and_student(users[0], users[1])
  add_coach_and_student(users[0], users[2])
  add_coach_and_student(users[0], users[3])
  add_coach_and_student(users[1], users[4])
  add_coach_and_student(users[5], users[6])
  add_coach_and_student(users[7], users[3])
  add_coach_and_student(users[8], users[9])
  add_coach_and_student(users[8], users[10])
  add_coach_and_student(users[8], users[11])

  for i in range(0, TOTAL_USERS):
    colorlist.append('r')

def visualize():
  G = nx.Graph()

  for user in users:
    G.add_node(user)

  fig = plt.figure(figsize=(8,8))
  pos = nx.spring_layout(G)

  nodes = nx.draw_networkx_nodes(G, pos, nodelist=users,
    node_color=colorlist, node_size=500, alpha=0.8)

  edges = nx.draw_networkx_edges(G, pos, edgelist=edge_list, width=2, alpha=0.5, edge_color='r')

  nx.draw_networkx_labels(G, pos, dict(zip(users, [user.user_id for user in users])), font_size=10)

  def update(n):
    print n
    if n < len(infection_path):
      colorlist[infection_path[n] - 1] = 'b'

    nodes = nx.draw_networkx_nodes(G, pos, nodelist=users, node_color=colorlist, node_size=500, alpha=0.8)
    return nodes,

  anim = FuncAnimation(fig, update, frames=len(infection_path), interval=1500, blit=False, repeat=False)

  plt.axis('off')
  plt.show()


if __name__=="__main__":
  parser = argparse.ArgumentParser(description="Test infection algorithms.")
  parser.add_argument("test", help="the test to run. \"total\" for total infection. \
    \"limited\" for limited infection", type=str)

  parser.add_argument("-u", "--numusers", help="the number of users to infect for \
    limited infection.", type=int, default=3)

  parser.add_argument("-v", "--visualize", help="flag for visualization", action="store_true")
  args = parser.parse_args()

  if args.test.lower() == "total":
    init_users()
    print "Before infection:"
    for user in users:
      print str(user.user_id) + " ---> " + str(user.site_version)

    # Can change the start_user here
    total_infection(start_user=users[0], new_site_version='B')
    print "After total infection:"
    for user in users:
      print str(user.user_id) + " ---> " + str(user.site_version)

    print "Number infected: " + str(len(infection_path))

    if args.visualize:
      visualize()


  elif args.test.lower() == "limited":
    init_users()
    print "Before infection:"
    for user in users:
      print str(user.user_id) + " ---> " + str(user.site_version)

    limited_infection(num_users=args.numusers, new_site_version='B')
    print "After limited infection:"
    for user in users:
      print str(user.user_id) + " ---> " + str(user.site_version)

    print "Number infected: " + str(len(infection_path))

    if args.visualize:
      visualize()
    
    print infection_path
  else:
    parser.print_help()


