class User(object):
  def __init__(self, user_id, site_version):
    self.user_id = user_id
    self.site_version = site_version
    self.coaches = []
    self.students = []

  def __repr__(self):
    return "{user_id=" + str(self.user_id) + ", coaches=" + str(self.coaches) + \
      ", students=" + str(self.students) + "}"

  def add_student(self, user):
    user.coaches.append(self)
    self.students.append(user)


