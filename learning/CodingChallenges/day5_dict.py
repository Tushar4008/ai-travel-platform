student_details={
    'name':"Tushar",
    'age':30,
    'course':"CS",
    'city':"Bangalore"
}

input_detail = input("Enter the field you want to see: ").strip().lower()

print(student_details.get(input_detail))