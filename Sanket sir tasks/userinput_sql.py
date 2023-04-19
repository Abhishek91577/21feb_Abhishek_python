
import sqlite3
print("press 0 for create table")
print("press 1 for insert data in table")
print("press 2 for update record in table")
print("press 3 for  delete record in table")
print("press 4 for show data")
print("e for exit")

try:
    dbcon=sqlite3.connect('newdb')
    print("database connected")
except Exception as e:
    print(e)

c=int(input("enter your choice:"))
if c==0:
    print("__________here create table____")
    table=int(input("how many table created:"))
    for i in range(table):
        print(i)
    stnm=input("enter your tablename:")
    stcl1=input("enter your first column:")
    stcl2=input("enter second column name:")
    stcl3=input("enter third column name:")
    create_tbl=f"create table'{stnm}'('{stcl1}'integer primarykey ,'{stcl2}'text,'{stcl3}'text)"
    try:
        dbcon.execute(create_tbl)
        print("Table is created sucessfully")
    except Exception as e:
        print(e)
elif c==1:
    print("________insertdata in table______")
    n=int(input("Enter number of inserted record"))
    for i in range(n):
        stnm=input("Enter name:")
        stct=input("Enter your city")
        insert_data=f"insert into emp(name,city)values('{stnm}','{stct}')"
        try:
            dbcon.execute(insert_data)
            dbcon.commit()
            print("record inserted")
        except Exception as e:
            print(e)
elif c==2:
    print("____here update data in table____")
    sttnm=str(input("Enter your table name:"))
    stcy=str(input("Enter new city:"))
    stwh=str(input("Enter id:"))
    update_data=f"update'{sttnm}',city='{stcy}'where id ='{stwh}'"
    try:
        dbcon.execute(update_data)
        dbcon.commit()
        print("update new data")
    except Exception as e:
        print(e)

elif c==3:
    print("______________here delted data______________")
    stnm=str(input("enter delte name:"))
    delete_data=f"delete from emp where name='{stnm}'"
    try:
        dbcon.execute(delete_data)
        dbcon.commit()
        print("deletd data in table")
    except Exception as e:
        print(e)

elif c==4:
    cur=dbcon.cursor()
    show_data="select*from emp"
    cur.execute(show_data)
    data=cur.fetchall()
    print(data)

else:
    print("EXIT")