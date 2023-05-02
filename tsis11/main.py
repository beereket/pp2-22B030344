import psycopg2, csv
from config import host, password, user, database, port

def main():

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
        1 - Get records by pattern
        2 - Insert new user
        3 - Insert new users
        4 - Querying data from the tables with pagination (by limit and offset)
        5 - Deleting data from tables by username or phone
        ''')

        chosenone = int(input())
        if chosenone == 1:
            pattern = input()

            cur.execute('''
            CREATE OR REPLACE FUNCTION getting_records(pattern VARCHAR)
            RETURNS table(id INTEGER, first_name VARCHAR, last_name VARCHAR, phone_num VARCHAR)
            AS $$
            BEGIN 
              RETURN QUERY
              SELECT * FROM phonebook_table WHERE phonebook_table.first_name LIKE '%' || pattern || '%' OR phonebook_table.last_name LIKE '%' || pattern || '%' OR phonebook_table.phone_num LIKE '%' || pattern || '%';
            END
            $$ language plpgsql
            ''')
            conn.commit()

            cur.execute(f'''SELECT * FROM getting_records('{pattern}')''')
            res = cur.fetchall()

            for row in res: print(row)

        if chosenone == 2:
            cur.execute('''
            CREATE PROCEDURE insert_user(name VARCHAR, lastname VARCHAR, phone VARCHAR)
            LANGUAGE plpgsql
            AS $$
            BEGIN
              IF EXISTS(SELECT 1 FROM phonebook_table WHERE first_name = name AND last_name = lastname) THEN
                UPDATE phonebook_table SET phone_num = phone WHERE first_name = name AND last_name = lastname;
              ELSE
                INSERT INTO phonebook_table(first_name, last_name, phone_num) VALUES (name, lastname, phone);
              END IF;
            END;
            $$;''')
            conn.commit()

            name = input('Enter name:')
            lastname = input('Enter lastname:')
            phone = input('Enter phone number:')
            cur.execute(f'''CALL insert_user('{name}', '{lastname}','{phone}')''')

        if chosenone == 3:
            cur.execute('''
            CREATE OR REPLACE FUNCTION insert_users(names_and_phones text[])
            RETURNS TABLE (name text, phone text, error text) AS $$
            DECLARE
              name_and_phone text;
              name_parts text[];
              first_name text;
              last_name text;
              phone_num text;
            BEGIN
              FOREACH name_and_phone IN ARRAY names_and_phones LOOP
                name_parts := string_to_array(name_and_phone, ':');
                first_name := trim(name_parts[1]);
                last_name := trim(name_parts[2]);
                phone_num := trim(name_parts[3]);
    
                IF length(phone_num) != 10 OR phone_num !~ '^[0-9]+$' THEN
                  error := 'Incorrect phone number';
                ELSE
                  INSERT INTO phonebook_table (first_name, last_name, phone_num) VALUES (first_name, last_name, phone_num);
                END IF;
    
                RETURN NEXT first_name || ' ' || last_name, phone_num, error;
              END LOOP;
            END;
            $$ LANGUAGE plpgsql;''')
            conn.commit()

            names_and_phone = input().split()
            cur.execute(f'''CALL insert_user('{names_and_phone}')''')

        if chosenone == 4:
            cur.execute('''
            CREATE OR REPLACE FUNCTION get_phonebook(limit integer, offset integer)
            RETURNS TABLE (first_name text, last_name text, phone_num text) AS $$
            BEGIN
              RETURN QUERY SELECT first_name, last_name, phone_num FROM phonebook_table
                ORDER BY last_name, first_name
                LIMIT limit
                OFFSET offset;
            END;
            $$ LANGUAGE plpgsql;''')
            conn.commit()

            Limit = input('Enter limit:')
            Offset = input('Enter offset:')

            cur.execute(f'''SELECT * FROM get_phonebook('{Limit}', '{Offset}');''')
            res = cur.fetchall()

            for row in res:
                print(row)

        if chosenone == 5:
            cur.execute('''
            CREATE OR REPLACE PROCEDURE delete_from_phonebook(IN search_text TEXT)
            LANGUAGE plpgsql
            AS $$
            BEGIN
              DELETE FROM phonebook_table
              WHERE first_name ILIKE '%' || search_text || '%'
              OR last_name ILIKE '%' || search_text || '%'
              OR phone_num ILIKE '%' || search_text || '%';
            END;
            $$;''')
            conn.commit()

            pattern = input()
            cur.execute(f'''Call delete_from_phonebook('{pattern}')''')
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