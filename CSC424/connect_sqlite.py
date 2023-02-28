import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('RedwoodUniversity.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# Assumption that '2021-12-05' is considered the current date

# DEPARTMENT Table
query = """
CREATE TABLE Department(
depName VARCHAR(100) NOT NULL,
chairName VARCHAR(100),
numFaculty INT,
PRIMARY KEY(depName),
CONSTRAINT beginDep CHECK (depName LIKE 'Department%')
);
"""


# Execute query, the result is stored in cursor
cursor.execute(query)




# STUDENT Table
query = """
CREATE TABLE Student(
studentID VARCHAR(100) NOT NULL,
studName VARCHAR(100),
studInitials VARCHAR(3),
PRIMARY KEY(studentID),
CONSTRAINT oneInit CHECK (studInitials LIKE  '__%')
);
"""

# Execute query, the result is stored in cursor
cursor.execute(query)



# Event Table
query = """
CREATE TABLE Event(
eventName VARCHAR(100) NOT NULL,
startDate DATE NOT NULL,
endDate DATE,
PRIMARY KEY (eventName, startDate),
CONSTRAINT validStart CHECK (startDate > '2021-12-05'),
CONSTRAINT validEnd CHECK (startDate < endDate)
);
"""

# Execute query, the result is stored in cursor
cursor.execute(query)




# MAJOR Table
query = """
CREATE TABLE Major(
majorName VARCHAR(100) NOT NULL,
Code INT,
depName VARCHAR(100),
PRIMARY KEY(majorName),
CONSTRAINT codeLen CHECK (Code < 1000 AND Code > 99),
FOREIGN KEY (depName) REFERENCES Department (depName) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

# Execute query, the result is stored in cursor
cursor.execute(query)




# DECLAREDMAJOR Table
query = """
CREATE TABLE DeclaredMajor(
studentID VARCHAR(100) NOT NULL,
majorName VARCHAR(100) NOT NULL DEFAULT 'Undeclared',
PRIMARY KEY(studentID, majorName),
FOREIGN KEY (studentID) REFERENCES Student (studentID) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (majorName) REFERENCES Major (majorName) ON DELETE SET DEFAULT ON UPDATE CASCADE
);
"""

# Execute query, the result is stored in cursor
cursor.execute(query)



# EVENTATTENDANCE Table
query = """
CREATE TABLE EventAttendance(
studentID VARCHAR(100) NOT NULL,
eventName VARCHAR(100) NOT NULL,
startDate DATE NOT NULL,
PRIMARY KEY(studentID, eventName, startDate),
FOREIGN KEY (studentID) REFERENCES Student (studentID) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (eventName) REFERENCES Event (eventName) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (startDate) REFERENCES Event (startDate) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

# Execute query, the result is stored in cursor
cursor.execute(query)




# UTILIZEDDEPARTMENT Table
query = """
CREATE TABLE UtilizedDepartment(
eventName VARCHAR(100) NOT NULL,
startDate DATE NOT NULL,
depName VARCHAR(100) NOT NULL,
PRIMARY KEY(eventName, startDate, depName),
FOREIGN KEY (eventName) REFERENCES Event (eventName) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (startDate) REFERENCES Event (startDate) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (depName) REFERENCES Department (depName) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

# Execute query, the result is stored in cursor
cursor.execute(query)





# Insert row into table
query = """
INSERT INTO Department
VALUES ("Department of Chemistry", "Mary", 7);
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Department
VALUES ("Department of Biology", "Megan", 9);
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Department
VALUES ("Department of Business", "Jacob", 23);
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Department
VALUES ("Department of Computer Science", "Jeffrey", 7);
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Department
VALUES ("Department of Mathematics", "Haley", 15);
"""
cursor.execute(query)




# Insert row into table
query = """
INSERT INTO Student
VALUES ("S0001", "Dean Osborne", "DEO");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Student
VALUES ("S0002", "Caleb Heathershaw", "CAH");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Student
VALUES ("S0003", "Patrick Denny", "PDD");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Student
VALUES ("S0004", "Julia Eisner", "JAE");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Student
VALUES ("S0005", "Maya Nambiar", "MIN");
"""
cursor.execute(query)




# Insert row into table
query = """
INSERT INTO Event
VALUES ("Miami vs WSU", '2021-12-31', '2022-01-01');
"""
cursor.execute(query)


# Insert row into table
query = """
INSERT INTO Event
VALUES ("Move-In", '2022-01-12', '2022-01-16');
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Event
VALUES ("Valentines Day", '2022-02-12', '2022-02-13');
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Event
VALUES ("Jeffs Birthday", '2022-03-31', '2022-04-01');
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Event
VALUES ("Spring Break", '2022-03-12', '2022-03-20');
"""
cursor.execute(query)



# Insert row into table
query = """
INSERT INTO EventAttendance
VALUES ("S0001", "Miami vs WSU", '2021-12-31');
"""
cursor.execute(query)


# Insert row into table
query = """
INSERT INTO EventAttendance
VALUES ("S0002", "Move-In", '2022-01-12');
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO EventAttendance
VALUES ("S0003", "Valentines Day", '2022-02-12');
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO EventAttendance
VALUES ("S0004", "Jeffs Birthday", '2022-03-31');
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO EventAttendance
VALUES ("S0005", "Spring Break", '2022-03-12');
"""
cursor.execute(query)




# Insert row into table
query = """
INSERT INTO UtilizedDepartment
VALUES ("Miami vs WSU", '2021-12-31', "Department of Chemistry");
"""
cursor.execute(query)


# Insert row into table
query = """
INSERT INTO UtilizedDepartment
VALUES ("Move-In", '2022-01-12', "Department of Biology");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO UtilizedDepartment
VALUES ("Valentines Day", '2022-02-12', "Department of Computer Science");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO UtilizedDepartment
VALUES ("Jeffs Birthday", '2022-03-31', "Department of Mathematics");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO UtilizedDepartment
VALUES ("Spring Break", '2022-03-12', "Department of Business");
"""
cursor.execute(query)


# Insert row into table
query = """
INSERT INTO Major
VALUES ("Investigative Chemistry", 101, "Department of Chemistry");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Major
VALUES ("Microbiology", 201, "Department of Biology");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Major
VALUES ("Marketing", 301, "Department of Business");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Major
VALUES ("Data Science", 401, "Department of Computer Science");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Major
VALUES ("Probability and Statistics", 501, "Department of Mathematics");
"""
cursor.execute(query)





# Insert row into table
query = """
INSERT INTO DeclaredMajor
VALUES ("S0005", "Investigative Chemistry");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO DeclaredMajor
VALUES ("S0002", "Microbiology");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO DeclaredMajor
VALUES ("S0003", "Marketing");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO DeclaredMajor
VALUES ("S0004", "Data Science");
"""
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO DeclaredMajor
VALUES ("S0001", "Probability and Statistics");
"""
cursor.execute(query)




# If the user wants to see all students that attened an event, they can search for all
# unique studentIDs in the EventAttendance table and use those IDs to find names in
# the Student table.

query = """
SELECT e.eventName, e.studentID, s.studName
FROM EventAttendance e, Student s
WHERE e.studentID == s.studentID AND e.eventName LIKE "Miami VS WSU"
"""
cursor.execute(query)


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
