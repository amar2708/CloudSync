'''import psycopg2

try:
    conn = psycopg2.connect("dbname=amardeep user=amardeep password='yourdbpassword'")
except Exception,e:
    print(e)
    print("I am unable to connect to the database.")


cur = conn.cursor()
def display():
    cur.execute('SELECT * from "user"') 
    rows = cur.fetchall()
    print("the values of databases are:") 
    for row in rows:
        print(row)


def insert():
    uid = (input("enter the id of the employee"))
    name = input("enter the name of the employee")
    email = input("enter the email of the employee")
    phone = (input("enter the phone number of the employee"))
    with conn:
        cur.execute('INSERT INTO "user" (id,name,email,phone) VALUES(%s, %s, %s, %s)',
                    (uid,name,email,phone))
    conn.commit()

    
def delete():
    uid = (input("enter the id of the employee to be deleted\n"))
    cur.execute('DELETE FROM "user" WHERE id=(%s)',(uid))
    conn.commit()


def update():
    uid = input("enter the id of the employee to be updated\n")
    name = input("enter the new name of the employee")
    email = input("enter the new email of the employee")
    phone = input("enter the new phone of the employee")
    cur.execute('UPDATE "user" SET name=(%s), email=(%s), phone=(%s) WHERE id=(%s)',
                (name,email,phone,uid))
    conn.commit()

    
if __name__ == "__main__":
    while(1):
        choice = (int)(input("enter your choice:\n1.insert\t2.display\t3.delete\t4.update\t5.exit\n"))
        if choice == 1:
            insert()
        elif choice == 2:
            display()
        elif choice == 3:
            delete()
        elif choice == 4:
            update()
        else:
            break'''




import psycopg2


class Crud:
    def display(self):
        cur.execute('SELECT * from "user"') 
        rows = cur.fetchall()
        print("the values of datavases are:") 
        for row in rows:
            print(row)


    def insert_row(self):
        uid = (input("enter the id of the employee"))
        name = input("enter the name of the employee")
        email = input("enter the email of the employee")
        phone = (input("enter the phone number of the employee"))
        with conn:
            cur.execute('INSERT INTO "user" (id,name,email,phone) VALUES(%s,%s,%s,%s)',(uid,name,email,phone))
    
        conn.commit()

    def delete_row(self):
        uid = (input("enter the id of the employee to be deleted\n"))
        cur.execute('DELETE FROM "user" WHERE id=(%s)',(uid))
        conn.commit()


    def update_row(self):
        uid = input("enter the id of the employee to be updated\n")
        name = input("enter the new name of the employee")
        email = input("enter the new email of the employee")
        phone = input("enter the new phone of the employee")
        cur.execute('UPDATE "user" SET name=(%s), email=(%s), phone=(%s) WHERE id=(%s)',(name,email,phone,uid))
        conn.commit()

if __name__ == "__main__":
    obj = Crud()
    try:
        conn = psycopg2.connect("dbname=amardeep user=amardeep password='Amar!@#'")
    except:
        print("I am unable to connect to the database.")
    
    cur = conn.cursor()

    while(1):
        choice = (int)(input("enter your choice:\n1.insert\t2.display\t3.delete\t4.update\t5.exit\n"))
        if choice == 1:
            obj.insert_row()
        elif choice == 2:
            obj.display()
        elif choice == 3:
            obj.delete_row()
        elif choice == 4:
            obj.update_row()
        else:
            break
