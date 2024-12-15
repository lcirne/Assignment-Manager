"""
Luke Cirne
Assignment Manager 1.2
"""
import array
import math

def add_assignment(course, assignment_name, due_date):
    if course_name in course_dict.keys():
        course_dict[course].append((assignment_name, due_date))
        return True
    return False

def remove_assignment(course, assignment_name):
    if course in course_dict:
        for assignment_package in course_dict[course]:
            if assignment_name in assignment_package:
                course_dict[course].pop(course_dict[course].index(assignment_package))
                

def write_new_file(file_name):
    with open(file_name + '.txt', 'w') as f:
        f.write(f"{'Courses:': <10}\t{'Assignments:'}\n")
        for i in range(len(course_lst)):
            f.write(f"\n{course_lst[i]: <10}")
            print('i', i)
            for courses in course_dict[course_lst[i]]:
                assignment, date = courses
                print(courses)
                if course_dict[course_lst[i]].index(courses) == 0:
                    f.write(f"\t{assignment + ' is due on ' + date}\n")
                else:
                        f.write(f"\t\t{assignment + ' is due on ' + date}\n")
                            

def add_to_file(file_name, course, assignment_name, due_date):
    course_dict[course].append((assignment_name, due_date))
    with open(file_name + '.txt', 'w') as f:
        f.write(f"{'Courses:': <10}\t{'Assignments:'}\n")
        for i in range(len(course_lst)):
            f.write(f"\n{course_lst[i]: <10}")
            print('i', i)
            for courses in course_dict[course_lst[i]]:
                assignment, date = courses
                print(courses)
                if course_dict[course_lst[i]].index(courses) == 0:
                    f.write(f"\t{assignment + ' is due on ' + date}\n")
                else:
                        f.write(f"\t\t{assignment + ' is due on ' + date}\n")
        
                    
if __name__ == '__main__':
    
    #Initialize a list of courses
    command = ''
    course_lst = []
    while command != 'd':
        command = input("\nEnter 'a' to add a class or enter 'd' when done: ")
        if len(course_lst) < 1 and command != 'a':
            command = input("Try pressing 'a' to add a class: ")
        else:
            if command == 'a':
                course_lst.append(input("Enter a course name: ").lower())
            elif command == 'd':
                break
    
    #Initialize an empty dictionary of courses
    course_dict = {}
    for new_course in course_lst:
        course_dict[new_course] = []
   
    #Start while loop that allows for creation of assignments to be added to course_dict
    running = True
    while running:
        
        command = input('\nWhat would you like to do?:\n+: add an assignment\n'
        '-: remove an assignment\nwnf: write a new file\nrf: read a file\natf: add to a file\nq: quit\ncommand: ')
        print('')
        
        if command == '+':
            attempting = True
            
            while attempting:
                try:
                    course_name = input(f'Choose a course:\n{course_lst}\n ').lower()
                    if course_name in course_lst:
                        assignment_name = input('Enter an assignment: ').lower()
                        due_date = input('Enter the due date: ')
                        added = add_assignment(course_name, assignment_name, due_date)
                    if added:
                        print('Assignment added')
                        break
                except NameError:
                    print('Course not found')
        
        if command == '-':
            course_name = input(f'Choose a course:\n{course_lst}\nInput: ').lower()
            assignment_name = input(f'Choose an assignment:\n{course_dict[course_name]}\nInput: ').lower()
            remove_assignment(course_name, assignment_name)
        
        if command == 'q':
            print(course_dict)
            break
            
        if command == 'p':
            print(course_dict)
        
        if command == 'wnf':
            write_new_file(input('Enter the file name: '))
            
        if command == 'rf':
            read_this_file = input('Enter the file name: ')
            with open(read_this_file + '.txt', 'r', newline = '') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        print(line)
        
        if command == 'atf':
            add_to_this_file = input('Enter the file name: ')
            add_to_course = input(f'Enter the course you would like to add to\n {course_lst}: ')
            add_assignment = input('Enter the assignment name: ')
            add_due_date = input('Enter the assignment due date: ')
            add_to_file(add_to_this_file, add_to_course, add_assignment, add_due_date)