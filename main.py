import psycopg2

data: dict = {'database':'sql',
            'user':'postgres',
            'password':4444 ,
            'port':5432,
            'host':'localhost'}


class User:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(**data)

    def __enter__(self) -> str:
        self.cur = self.conn.cursor()
        return self.cur , self.conn
    
    @staticmethod
    def creat_table():
        create_table_query = '''CREATE TABLE IF NOT EXISTS users(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(100) NOT NULL,
                        last_name VARCHAR(100) NOT NULL,
                        username VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        age INT CHECK(age > 0),
                        is_active bool default false)
                        '''
        return create_table_query
    
    @staticmethod
    def find_id():
        get_all_id_query: str = '''SELECT id FROM users;'''
        cur = conn.cursor()
        cur.execute(get_all_id_query)
        data = cur.fetchall()
        return data

    @staticmethod
    def find_username():
        get_username_query: str = '''SELECT username FROM users;'''
        cur = conn.cursor()
        cur.execute(get_username_query)
        data = cur.fetchall
        return data

    @staticmethod
    def save_user() -> str | tuple:
        add_user_in_table = '''INSERT INTO users(first_name, last_name, username, email, age, is_active)
        VALUES(%s,%s,%s,%s,%s,%s);'''
        first_name: str = input('Enter your first name; ').capitalize()
        last_name: str = input('Enter your last name; ').capitalize()
        username: str = input('Enter your username; ')
        email: str = input('Enter your email; ')
        age: int = int(input('Enter your age; '))
        is_active: bool = bool(input('Do you active(must be bool)?; '))

        data: tuple = (first_name, last_name, username, email, age, is_active) 
        return add_user_in_table , data

    @staticmethod
    def get_all_users() -> str:
        get_all_users_query: str = '''SELECT id, username FROM users;'''
        return get_all_users_query
        

    @staticmethod
    def get_user() -> str | tuple:
        get_user_query: str = '''SELECT * FROM users WHERE id = %s;'''
        _id: int = int(input('Enter id ; '))
        data: tuple = (_id,)
        return get_user_query, data
    

    @staticmethod
    def update() -> str | tuple:
        update_user_query: str = '''UPDATE users SET username = %s, email = %s WHERE id = %s;'''
        _id: int = int(input('Enter user id you want to update; '))
        username: str = input('Enter new username; ')
        email: str = input('Enter new email; ')
        data: tuple = (username, email,_id)
        return update_user_query, data
    
    
    @staticmethod
    def rename() -> str | tuple:
        rename_user_query: str = '''UPDATE users SET first_name = %s, last_name= %s, username = %s, email = %s, age = %s, is_active = %s WHERE id = %s;'''
        _id: int = int(input('Enter user id you want to rename; '))
        first_name: str = input('Enter new first name; ').capitalize()
        last_name: str = input('Enter new last name; ').capitalize()
        username: str = input('Enter new username; ')
        email: str = input('Enter new email; ')
        age: int = int(input('Enter new age; '))
        is_active: bool = bool(input('The user is active(must be bool type); '))
        data: tuple = (first_name, last_name, username, email, age, is_active, _id)
        return rename_user_query, data
    

    @staticmethod
    def delete() -> str | tuple:
  
        delete_user_query: str = '''DELETE FROM users WHERE id = %s;'''
        _id: int = int(input('Enter user id you want to delete; '))
        data: tuple = (_id,)
        return delete_user_query, data
        

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print('Closing...')

user = User()
with user as (cur , conn):
    while True:
        choise: str = input('0 : creat table\n1 : add user\n2 : show users id and username\n3 : show user information\n4 : update user\n5 : rename user\n6 : delete user\nq : exit\nEnter your chooce: ').capitalize()
        if choise == '0':
            query = User.creat_table()
            cur.execute(query)
            conn.commit()
            print('Table successfully created')
        elif choise == '1':
            query, data = User.save_user()
            cur.execute(query,data)
            conn.commit()
            print('Successfully added')
        elif choise == '2':
            query = User.get_all_users()
            cur.execute(query)
            users = cur.fetchall()
            for user in users:
                print(user)
        elif choise == '3':
            query, data = User.get_user()
            cur.execute(query,data)
            user = cur.fetchone()
# if the id you entered id in the database, 
# it will show otherwise it will send a message that the id was not found
            if user:
                print(user)
            else:
                print('User not found')
        elif choise == '4':
            query, data = User.update()
            cur.execute(query, data)
            conn.commit()
            print('Successfully updated')
        elif choise == '5':
            query, data = User.rename()
            cur.execute(query,data)
            conn.commit()
            print('Successfully renamed')
        elif choise == '6':
            base = User.find_id()
            query,data = User.delete()
# If the id you entered is in the database,
#  it will be deleted, otherwise it will send a message that the id was not found 
            if data in base:               
                cur.execute(query,data)     
                conn.commit()              
                print('Successfully deleted')
            else:
                print('User not found')
        elif choise == 'Q':
            break
        else:
            print('Invalit choice')

