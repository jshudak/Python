import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('RedwoodUniversity.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# Assumption that '2021-12-05' is considered the current date

# If the user wants to see all students that attened an event, they can search for all
# unique studentIDs in the EventAttendance table and use those IDs to find names in
# the Student table.

query = """
SELECT e.eventName, e.studentID, s.studName
FROM EventAttendance e, Student s
WHERE e.studentID == s.studentID AND e.eventName LIKE "Miami VS WSU"
"""
cursor.execute(query)

"""
# If the user wants to count how many students are in each major they can figure that
# out just counting how many times a major shows up in the DeclaredMajor table.

query = """
SELECT majorName, COUNT(majorName)
FROM DeclaredMajor
GROUP BY majorName
"""
cursor.execute(query)



# If the user wants to find each event the chemistry department helped plan they can
# find all events in the UtilizedDepartment table that matches that a depName of
# “%Chemistry”.

query = """
SELECT eventName, depName
FROM UtilizedDepartment u
WHERE depName LIKE "%Chemistry"
"""
cursor.execute(query)


# If the user wants to find which events data science majors attended, and how many
# people in that major attended each event, they can match student IDs from 
# EventAttendance and DeclaredMajor and find where majorName is “Data Science”
# major, and count the number of student IDs. 

query = """
SELECT eventName, d.majorName, COUNT(e.studentID)
FROM DeclaredMajor d, EventAttendance e
WHERE (d.studentID == e.studentID) AND (d.majorName LIKE "Data Science")
GROUP BY d.majorName, eventName
"""
cursor.execute(query)


# If the user wants to find all events that are after Feb. 1st they can just look in the
# Event table and find all events where the startDate is greater than ‘2022-02-01’.
query = """
SELECT eventName, startDate
FROM Event
WHERE startDate > "2022-02-01"
"""
cursor.execute(query)



query = """
SELECT *
FROM Student
"""
cursor.execute(query)

query = """
SELECT *
FROM Major
"""
cursor.execute(query)

query = """
SELECT *
FROM Department
"""
cursor.execute(query)

query = """
SELECT *
FROM Event
"""
cursor.execute(query)

query = """
SELECT *
FROM DeclaredMajor
"""
cursor.execute(query)

query = """
SELECT *
FROM UtilizedDepartment
"""
cursor.execute(query)

query = """
SELECT *
FROM EventAttendance
"""
cursor.execute(query)
"""


# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print("EventAttendance Table:")
print(df)
print(df.columns)

# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
