from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql+pymysql://admin:password@localhost/student_details'
db_connection = create_engine(db_connection_str)


def insert_file(student_details):
    try:
        # Establish a connection
        
        name = student_details['name']
        english = student_details['english']
        maths = student_details['maths']
        science = student_details['science']
        social = student_details['social']
        second_language = student_details['second_language']
        # total = 123
        total = maths + science + social + second_language + english
        avg = total / 5
        print(total, avg)

        query = f"""
        INSERT INTO students (name, english, maths, science, second_language, social, total, avg) VALUES ('{name}', {english}, {maths}, {science}, {second_language}, {social}, '{total}', '{avg}')
        """
        print(query)
        # Execute the query
        db_connection.execute(query)
        print('File inserted successfully')
    except Exception as e:
        print("Failed to insert blob into the table", e)


username = input("Enter username:")
maths = input("Enter maths mark:")
science = input("Enter science mark:")
social = input("Enter social mark:")
second_language = input("Enter second language mark:")
english = input("Enter english mark:")

student = {
    "name": username,
    "english": int(english),
    "maths": int(maths),
    "science": int(science),
    "second_language": int(second_language),
    "social": int(social)
}
print(student)
insert_file(student)