
students = []


while True:
   menu = ["Add a new student", "Add a grades for a student", "Show report (all students)", "Find top performer", "Exit"]
   print ("--- Student Grade Analyzer ---")
   for i, option in enumerate(menu, start=1):
      print(i, option)

   choice = input("Enter your choice: ")

   if choice == "1":
      name = input("Enter student name: ")
      grades = []
      if any (student["name"].lower() == name.lower() for student in students) is True:      
         print (f"{name} already added!")
      else:
         students.append({"name": name, "grade": grades})
      
         

   elif choice == "2":
      gr_name = input("Enter student name: ")
      gr_student = None
      for student in students:
         if student["name"].lower() == gr_name.lower():
            gr_student = student
            break
      if gr_student is None:
         print (f"Student {gr_name} not found!")
      else:
         
         while True:
            try:
               str_grade = input("Enter a grade (or 'done' to finish): ")
               if str_grade.lower() == "done":
                  break
               grade = int(str_grade)
               if not 0 <= grade <= 100:
                  print ("Please enter a grade between 0 and 100")
               
               else:
                  gr_student["grade"].append(grade)
                  print (students)
            except ValueError:
               print ("ValueError! Please enter a grade in digits")

   elif choice == "3":
      if not students:
         print ("No students added yet")
      else:

         all_averages = []

         for student in students:
            av_name = [student["name"]]
            average_grades = []
            try:
               av_gr = sum(student["grade"])/len(student["grade"])
               average_grades.append(av_gr)
               all_averages.append(av_gr)
               
               for n, a in zip(av_name, average_grades):
                  print (f"{n}'s average grade is {a}")

             
            except ZeroDivisionError:
               print (f"{av_name[0]}'s average grade is N/A")
 
         if all_averages:
            print (f"Max average is {max(all_averages)}")
            print(f"Min average is {min(all_averages)}")
            overal_average = sum(all_averages)/len(all_averages)
            print(f"Overall average is {overal_average}")
         else:
            print ("No grades added yet!")
         
   elif choice == "4":
      if not students:
         print ("No students added yet")
      else:
         try:
            top_performer = max(students, key=lambda x: sum(x["grade"])/len(x["grade"]) if x["grade"] else 0)
            top_av = sum(top_performer["grade"])/len(top_performer["grade"])
            print (f"Top performer is {top_performer["name"]} ({top_av})")
         except ZeroDivisionError:
               print ("No grades added yet!")


   elif choice == "5":
      break
   else:
      print ("Please, choose option 1 - 5")
   