from src.database.config import supabase
import bcrypt

# To check teacher already exist inside database or not 
def check_teacher_exists(username):
    
    # same as : SELECT username FROM teachers WHERE username = unsername;
    response = supabase.table("teachers").select("username").eq("username", username).execute()

    return len(response.data) > 0


def hash_pass(password: str): 
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


# Create teacher - insert teacher data inside the database 
def create_teacher(username, password, name):
    
    data = {
        "username": username,
        "password": hash_pass(password),
        "name": name
    }

    # insert data inside the database 
    '''
    Same as : 
    INSERT INTO teachers (username, password, name)
    VALUES ('teacher_username', 'hashed_password_here', 'Teacher Name');
    '''
    response = supabase.table("teachers").insert(data).execute()
    
    # Note : response.data always in list of dictionary means [{record1}, {record2} ... {recordN}]
    return response.data


# Note : here this hash_password have its salt and algorithm version value also so that case it internally easily compare to password 
def check_password(enter_password, hash_password): 
    return bcrypt.checkpw(enter_password.encode(), hash_password.encode())


# Authenticate the teacher 
def teacher_login(username, password):

    # search in database 
    # same as : SELECT * FROM teacher WHERE username = username
    response = supabase.table("teachers").select("*").eq("username", username).execute()

    if response.data:
        teacher = response.data[0]
        if check_password(password, teacher["password"]):
            return teacher 
        
    return None 


def get_all_students():
    
    # Access all students form the database
    # Same as : SELECT * FROM students;
    response = supabase.table("students").select("*").execute()

    return response.data or None
    

# insert all students inside the database 
def create_student(name, face_embedding = None, voice_embedding = None):
    
    # create dictionary of data to better insertion 
    data = {
        "name": name,
        "face_embedding": face_embedding,
        "voice_embedding": voice_embedding
    }

    response = supabase.table("students").insert(data).execute()
    return response.data


def create_subject(sub_id, sub_name, sub_section, teacher_id):
    data = {
        "subject_code": sub_id,
        "name": sub_name,
        "section": sub_section,
        "teacher_id": teacher_id
    }

    # insert data inside the database 
    '''
    Same as : 
    INSERT INTO subjects(subject_code, name, section, teacher_id)
    VALUES (sub_id, sub_name, sub_section, teacher_id)
    '''

    response = supabase.table("subjects").insert(data).execute()

    return response.data


# Fetch the subjects table all data and along with that find total students per each subjects and attendece_timestamps per each subjects 
def get_teacher_subjects(teacher_id):
    
    '''
    Same as : 
    SELECT
        s.subject_id,
        s.subject_code,
        s.name,
        s.section,
        s.teacher_id,
        COUNT(DISTINCT ss.student_id) AS total_students,
        ARRAY_AGG(a.timestamp) AS attendance_timestamps
    FROM subjects AS s

    LEFT JOIN subject_students AS ss
        ON s.subject_id = ss.subject_id

    LEFT JOIN attendance_logs AS a
        ON s.subject_id = a.subject_id

    WHERE s.teacher_id = given_teacher_id

    GROUP BY
        s.subject_id,
        s.subject_code,
        s.name,
        s.section,
        s.teacher_id;

    Understanding the .select() syntax:
    
    "*"                           -> Fetch all columns from the main table
                                     (subjects).
    
    "subject_students(count)"     -> Follow the foreign-key relationship from
                                     subjects -> subject_students and return
                                     only the total number of enrolled students
                                     for each subject.
    
    "attendance_logs(timestamp)"  -> Follow the foreign-key relationship from
                                     subjects -> attendance_logs and return only
                                     the timestamp column for each attendance
                                     record.
    
    Relationship Rules:
    
    • Tables inside .select() must have a valid foreign-key relationship with
      the table specified in .table().
    
    • Supabase automatically discovers these relationships from the database
      schema, so no explicit JOIN condition is required.
    
    • By default, nested relationship fetching behaves like a LEFT JOIN.
      This means every subject is returned even if it has:
          - no enrolled students
          - no attendance records
    
    • To perform an INNER JOIN instead, use:
    
          attendance_logs!inner(...)
    
      Example:
    
          .select("*, attendance_logs!inner(*)")
    
      This returns only subjects that have matching attendance records.
    
    Returned Response Example:
    
    [
        {
            "subject_id": 1,
            "subject_code": "IT601",
            "name": "Machine Learning",
            "section": "A",
            "teacher_id": 10,
    
            "subject_students": [
                {
                    "count": 52
                }
            ],
    
            "attendance_logs": [
                {
                    "timestamp": "2026-07-01T09:00:00"
                },
                {
                    "timestamp": "2026-07-03T09:00:00"
                },
                {
                    "timestamp": "2026-07-05T09:00:00"
                }
            ]
        }
    ]
    
    Notice:
    
    The returned object is NOT a flat SQL table.
    Supabase returns nested JSON where each subject contains its related
    records (students and attendance) as child objects.
    '''


    response = supabase.table("subjects").select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()

    # Extract the subjects from the response 
    subjects = response.data

    # Parse the response data subjects 
    for sub in subjects:
        
        sub['total_students'] = sub.get("subject_students", [{}])[0].get("count", 0) if sub.get("subject_students") else 0
        
        # find the tatal_classes and total_classes == no of unique timestamps of this subject
        attendence = sub.get("attendance_logs", [])
        unique_sessions = len(set(log['timestamp'] for log in attendence))
        sub['total_classes'] = unique_sessions

        # Remove unncessary data 
        sub.pop("subject_students", None)
        sub.pop("attendance_logs", None)

    return subjects


def enroll_student_to_subject(student_id, subject_id):
    data = {
        'student_id': student_id,
        'subject_id': subject_id
    }
    
    # INSERT INTO subject_students (student_id, subject_id) VALUES ('student_id_value', 'subject_id_value');
    response = supabase.table("subject_students").insert(data).execute()

    return response.data

def unenroll_student_to_subject(student_id, subject_id):
    data = {
        'student_id': student_id,
        'subject_id': subject_id
    }
    
    # DELETE FROM subject_students WHERE student_id = 'student_id_value' AND subject_id = 'subject_id_value';
    response = supabase.table("subject_students").delete().eq("student_id", student_id).eq("subject_id", subject_id).select().execute()

    return response.data


def get_student_subjects(student_id):
    
    '''
    Same as : 
    SELECT
        subject_students.*,
        subjects.*
    FROM subject_students
    LEFT JOIN subjects
    ON subject_students.subject_id = subjects.subject_id
    WHERE student_id = given_student_id;
    
    '''
    response = supabase.table("subject_students").select("*, subjects(*)").eq("student_id", student_id).execute()

    return response.data


def get_student_attendance(student_id):

    # same as : SELECT * FROM attendance_logs WHERE student_id = given_student_id;
    response = supabase.table('attendance_logs').select('*').eq('student_id', student_id).execute()
    
    return response.data


def insert_attendance_logs(attendance_logs):
    response = supabase.table("attendance_logs").insert(attendance_logs).execute()
    return response.data


def get_studetns_voice_embeddings():
    response = supabase.table("students").select("student_id, voice_embedding").execute()
    return response.data

def get_teacher_subject_attendance(teacher_id):

    response = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data

# DELETE FROM subjects WHERE subject_id = given_subject_id;
def delete_subject(subject_id):

    response = supabase.table("subjects").delete().eq("subject_id", subject_id).select().execute()

    return response 
