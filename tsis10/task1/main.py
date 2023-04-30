import psycopg2, csv
from config import host, password, user, database, port

def main():
    def CREATE():
        f_name = input()
        s_name = input()
        p_num = input()
        reg = input()

        # Create a cursor object
        cur = conn.cursor()

        # Define the SQL query to insert a new row into the phonebook_table table
        insert_query = "INSERT INTO phonebook_table (first_name, last_name, phone_num, region) VALUES (%s, %s, %s, %s)"

        # Define the values to insert into the new row
        values = (f_name, s_name, p_num, reg)

        # Execute the SQL query with the values
        cur.execute(insert_query, values)

    def READ_CSV():
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for item in reader:
                cur.execute('''INSERT INTO phonebook_table (
                            first_name,
                            last_name, 
                            phone_num, 
                            region)
                            VALUES (%s, %s, %s, %s)
                            ''', (item[0], item[1], item[2], item[3]))

    def CHANGE():

        print('''
        1 - by name
        2 - by phone number
        ''')

        num = int(input())
        if num == 1:
            name = input()
            id = input()
            cur.execute(
                '''UPDATE phonebook_table SET first_name = %s WHERE id = %s''', (name, id)
            )

        if num == 2:
            phone = input()
            id = input()
            cur.execute(
                '''UPDATE phonebook_table SET phone_num = %s WHERE id = %s''', (phone, id)
            )
    def QUERY():

        print('''
        1 - by name
        2 - by phone number
        ''')

        num = int(input())
        if num == 1:
            name = input()
            cur.execute(
                "SELECT * FROM phonebook_table WHERE first_name = '{}'".format(name)
            )
            data = cur.fetchall()
            for item in data:
                print(item)
        if num == 2:
            phone = input()
            cur.execute(
                "SELECT * FROM phonebook_table WHERE phone = '{}'".format(phone)
            )
            data = cur.fetchall()
            for item in data:
                print(item)

    def DELETE():

        print('''
        1 - by name
        2 - by phone number
        ''')

        num = int(input())
        if num == 1:
            name = input()
            cur.execute(
                "DELETE FROM phonebook_table WHERE first_name = '{}'".format(name)
            )
        if num == 2:
            phone = input()
            cur.execute(
                "DELETE FROM phonebook_table WHERE phone_num = '{}'".format(phone)
            )

    try:
        conn = psycopg2.connect(
            host=host,
            dbname=database,
            user=user,
            password=password,
            port=port
        )
        cur = conn.cursor()
        command = '''
        CREATE TABLE IF NOT EXISTS phonebook_table(
                    id  SERIAL PRIMARY KEY,
                    first_name VARCHAR(30) NOT NULL,
                    last_name VARCHAR(30) NOT NULL,
                    phone_num VARCHAR(30) NOT NULL,
                    region VARCHAR(30) NOT NULL
        )'''
        cur.execute(command)
        conn.commit()

        print(
        '''
        1 - Create a new contact
        2 - Read from csv
        3 - Change 
        4 - Delete
        5 - Querying data from the tables
        ''')

        chosenone = int(input())

        if chosenone == 1:
            CREATE()
        if chosenone == 2:
            READ_CSV()
        if chosenone == 3:
            CHANGE()
        if chosenone == 4:
            DELETE()
        if chosenone == 5:
            QUERY()

        conn.commit()

        cur.close()
        conn.close()

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    main()