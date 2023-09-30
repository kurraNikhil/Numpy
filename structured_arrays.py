import numpy as np

# Create a custom data type to represent a student record
student_record_dtype = np.dtype([('name', np.str_), ('age', np.int_), ('gpa', np.float64)])

# Create a structured array of student records
student_records = np.array([('Alice', 18, 3.8), ('Bob', 19, 3.5)], dtype=student_record_dtype)

# Access the fields of the structured array
student_records['name']
student
