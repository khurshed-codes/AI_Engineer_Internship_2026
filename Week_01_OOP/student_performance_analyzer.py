def st_average(students):
	max11=0
	ctr=0
	sum1=0
	for name,marks in students.items():
		avg=sum(marks)/len(marks)
		if avg>=90:
			grade="A"
		elif avg>=75:
			grade="B"
		elif avg>=60:
			grade="C"
		else:
			grade="D"
		if avg>=60:
			status="PASS"
			ctr+=1
		else:
			status="FAIL"
		sum1+=avg
		if avg>max11:
			max11=avg
			top_st=name
		print(f"{name} \nAverage: {avg}\nGrade: {grade}\nStatus:{status}")
	print("-----------")
	cl_avg=sum1/len(students)
	print(f"Class Average: {cl_avg}\nTop Student: {top_st}\n Students 		Passed: {ctr}")
		
students = {
    "Rahul": [78, 85, 92, 67, 74],
    "Aman": [55, 62, 58, 71, 60],
    "Priya": [91, 88, 95, 90, 93],
    "Arjun": [45, 52, 48, 60, 55]
}
print("STUDENT PERFORMANCE")
print("_______")
st_average(students)	

