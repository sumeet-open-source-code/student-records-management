# import requests

# Coding Question: Given JSON object that have marks of students, create a json object that returns the average marks in each subject
class StudentRecords:
   'Student records management'

   def getAverageMarks(self, total_students_dict):

   		Total = {}
   		student_marks_list = []
   		total_students = len(total_students_dict)
   		#Defined lists dynamically - for total marks and average marks
   		for k, v in total_students_dict.items():
   			marks_List = list(v.values())
   			student_marks_list.append(marks_List)
   			# Dynamic lists using list comprehension for required design
   			total_marks_list = [0 for n in list(v)]
   			average_marks_list = [0 for n in list(v)]

   		for j in student_marks_list:
   			for i in range(0, len(student_marks_list[0])):
   				total_marks_list[i] = total_marks_list[i] + j[i] 

   		average_marks_counter = 0
   		for i in total_marks_list:
   			# round() method is used to store average marks - Added limit of 2 digits after decimal point
   			average_marks_list[average_marks_counter] = round(i/total_students, 2)
   			average_marks_counter += 1

   		update_records_counter = 0
   		for k,v in total_students_dict.items():
   			for i,j in v.items():
   				Total[i] = average_marks_list[update_records_counter]
   				update_records_counter += 1
   			break

   		return Total



# Input
total_students_dict = {
   'Student1' : {'english': 90,'maths': 50,'science': 80},
   'Student2' : {'english': 70,'maths': 70,'science': 70}
}

# Function call - get average marks in each subject
student_records = StudentRecords()
Total = student_records.getAverageMarks(total_students_dict)

# Output
print("Input - Total students :", total_students_dict)
print("Output - Average marks in each subject :", Total)



