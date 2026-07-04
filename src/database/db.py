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

    if response.data:
        return response.data
    else:
        return None
    

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