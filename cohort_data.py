"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    # TODO: 
    f = open(filename, "r").readlines()
    for line in f:
      newLine = line.strip()
      lineList = newLine.split('|')
      if lineList[2] != '<BLANKLINE>' and lineList[2] != '':
        houses.add(lineList[2])
    return list(houses)


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    # TODO: 
    f = open(filename, "r").readlines()
      
    for line in f:
      newLine = line.strip()
      lineList = newLine.split('|') 
      
      if lineList[4] != 'G' and lineList[4] != 'I':
        if cohort == 'All':
          student = f"{lineList[0]} {lineList[1]}"
          students.append(student)
          continue
        elif cohort in lineList:
          student = f"{lineList[0]} {lineList[1]}"
          students.append(student)
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: 
    f = open(filename, "r").readlines()
      
    list = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]

    for line in f:
      newLine = line.strip()
      lineList = newLine.split('|') 
      student = f"{lineList[0]} {lineList[1]}"

      if "Dumbledore's Army" in lineList:
        dumbledores_army.append(student)
        dumbledores_army.sort()
      elif "Gryffindor" in lineList:
        gryffindor.append(student)
        gryffindor.sort()
      elif "Hufflepuff" in lineList:
        hufflepuff.append(student)
        hufflepuff.sort()
      elif "Ravenclaw" in lineList:
        ravenclaw.append(student)
        ravenclaw.sort()
      elif "Slytherin" in lineList:
        slytherin.append(student)
        slytherin.sort()
      elif "G" == lineList[4]:
        ghosts.append(student)
        ghosts.sort()
      elif "I" == lineList[4]:
        instructors.append(student)
        instructors.sort()
      
    

    return list


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO:
    f = open(filename, "r").readlines()
      
    for line in f:
      newLine = line.strip()
      lineList = newLine.split('|') 
      person = f"{lineList[0]} {lineList[1]}"
      fmtd = (person, lineList[2], lineList[3], lineList[4])
      all_data.append(fmtd)
  

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO:
    f = open(filename, "r").readlines()
    

    for line in f:
      newLine = line.strip()
      lineList = newLine.split('|') 
      person = f"{lineList[0]} {lineList[1]}"

      if name == person:
        return lineList[4]

def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: 

    f = open(filename, "r").readlines()
    
    all_last_names = []

    for line in f:
      newLine = line.strip()
      lineList = newLine.split('|') 
      all_last_names.append(lineList[1])
    
    dupls = {x for x in all_last_names if all_last_names.count(x) >= 2}

    return dupls
    


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: 
    f = open(filename, "r").readlines()
    given_student = []
    housemates = set()
    given_house = None
    given_year = None
    for line in f:
      newLine = line.strip()
      lineList = newLine.split('|') 
      person = f"{lineList[0]} {lineList[1]}"
      
      if name == person:
        given_student.append(person)
        given_student.append(lineList[2])
        given_house = lineList[2]
        given_student.append(lineList[3])
        given_student.append(lineList[4])
        given_year = lineList[4]
      # print(given_house, given_year)
    for x in all_data(filename):
      if x[1] == given_house:
        if x[3] == given_year:
          if x[0] != given_student[0]:
            housemates.add(x[0])
    return housemates
    # return all_data(filename)
# print(get_housemates_for('cohort_data.txt', 'Hermione Granger'))

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
