class assignment:

  def __init__(self, subject, difficulty, dueDate):
    self.subject = subject
    self.difficulty = difficulty
    self.dueDate = dueDate
    self.priority = difficulty - 4*dueDate
  
assignments = []
assignments.append(assignment("Science", 2, 1)) 
assignments.append(assignment("Math", 4, 2)) 
assignments.append(assignment("English", 4, 1)) 
assignments.append(assignment("socialStudies", 3, 2)) 
def insertion_sort():
  for i in range(1,len(assignments)):
    number = assignments[i].priority
    newthing = assignments[i]
    othernum = i
    shift_position = i - 1
    while shift_position >= 0:
      if number < assignments[shift_position].priority:
        assignments[othernum] = assignments[shift_position]
        assignments[shift_position] = newthing
        shift_position = shift_position - 1
        othernum = othernum - 1
      else:
        break


insertion_sort()
block1 = assignments[0].subject
block2 = assignments[1].subject
block3 = assignments[2].subject
block4 = assignments[3].subject
