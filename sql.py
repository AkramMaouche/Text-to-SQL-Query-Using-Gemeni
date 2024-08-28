import sqllite3 

#Define connection 
connection = sqllite3.connect("")
#Cursor
curr = connection.cursor("Student.db") 

#Create Table 
table_info = ''' 
CREATE TABLE  IF NOT EXISTS STUDENT(
    ID INTGER NOT NULL PRIMARY KEY , 
    NAME VARCHAR(255) NOT NULL,
    Class VARCHAR(255),
    Section VARCHAR(255),
    Marks INTGER
    );
'''

curr.execute(table_info)


#Insert Some Records 
curr.execute(''' INSERT INTO STUDENT VALUES 
            (1,'Aymen','Math','A', 50),
            (2, 'Isabella', 'Chemistry', 'A', 90),
            (3, 'Benjamin', 'Physics', 'C', 70),
            (4, 'Mia', 'Computer Science', 'B', 82),
            (5, 'Lucas', 'Economics', 'A', 94),
            (6, 'Charlotte', 'Psychology', 'B', 80),
            (7, 'Ethan', 'Sociology', 'A', 89),
            (8, 'Amelia', 'Music', 'C', 72),
            (9, 'Oliver', 'Theater', 'B', 77),
            (10, 'Ava', 'Philosophy', 'A', 91),
            (11, 'Mason', 'Engineering', 'B', 84),
            (12, 'Harper', 'Literature', 'A', 87),
            (13, 'Elijah', 'Statistics', 'C', 65),
            (14, 'Ella', 'Astronomy', 'B', 79),
            (15, 'Alexander', 'Geology', 'A', 95),
            (16, 'Grace', 'Anthropology', 'B', 81),
            (17, 'Jackson', 'Political Science', 'C', 68),
            (18, 'Lily', 'Religious Studies', 'A', 88),
            (19, 'Aiden', 'Law', 'B', 76),
            (20, 'Zoe', 'Art History', 'A', 92),
            (21, 'Daniel', 'Public Health', 'C', 71),
            (22, 'Megan', 'Sociology', 'B', 83),
            (23, 'Henry', 'Finance', 'A', 96),
            (24, 'Natalie', 'Education', 'B', 78),
            (25, 'Matthew', 'Environmental Science', 'C', 66),
            (26, 'Sofia', 'Journalism', 'B', 82),
            (27, 'Ryan', 'Statistics', 'A', 90),
            (28, 'Evelyn', 'Engineering', 'B', 80),
            (29, 'Jack', 'Medicine', 'C', 72),
            (30, 'Chloe', 'Architecture', 'A', 89),
            (31, 'Logan', 'Music Theory', 'B', 75),
            (32, 'Luna', 'Urban Studies', 'A', 93),
            (33, 'Sebastian', 'French', 'B', 74),
            (34, 'Aria', 'Spanish', 'A', 91),
            (35, 'Wyatt', 'German', 'C', 69),
            (36, 'Mila', 'Italian', 'B', 77),
            (37, 'Owen', 'Chinese', 'A', 85),
            (38, 'Layla', 'Japanese', 'C', 70),
            (39, 'Jameson', 'Latin', 'B', 82),
            (40, 'Samantha', 'Russian', 'A', 88),
            (41, 'Gabriel', 'Arabic', 'B', 79),
            (42, 'Harper', 'Korean', 'A', 87),
            (43, 'Ella', 'Portuguese', 'B', 76),
            (44, 'William', 'Swahili', 'C', 67),
            (45, 'Avery', 'History of Art', 'B', 80),
            (46, 'Jaxon', 'Public Administration', 'A', 93),
            (47, 'Madison', 'Marine Biology', 'B', 84),
            (48, 'Oliver', 'Neuroscience', 'C', 73),
            (49, 'Sophia', 'Gender Studies', 'A', 90),
            (50, 'Mason', 'Veterinary Science', 'B', 79) 
             
              ''')


