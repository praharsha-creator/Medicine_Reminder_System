import pandas as pd

import sqlite3

conn = sqlite3.connect("medicines.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS medicines(
               id INTEGER PRIMARY KEY,
               medicine_name TEXT,
               reminder_time TEXT,
               frequency TEXT)""")

conn.commit()

print("Database Connected Successfully")

class MedicineReminder:

    def __init__(self):

        self.conn = sqlite3.connect("medicines.db")

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicines(
            id INTEGER PRIMARY KEY,
            medicine_name TEXT,
            reminder_time TEXT,
            frequency TEXT
        )
        """)

        self.conn.commit()

    def add_medicine(self):

       medicine_name = input("Enter Medicine Name: ")

       reminder_time = input("Enter Reminder Time: ")

       frequency = input("Enter Frequency: ")

       self.cursor.execute("""
       INSERT INTO medicines
       (medicine_name, reminder_time, frequency)
       VALUES (?, ?, ?)
       """, (medicine_name, reminder_time, frequency))

       self.conn.commit()

       print("Medicine Added Successfully")


    def view_medicines(self):

       cursor.execute("SELECT * FROM medicines")

       medicines = cursor.fetchall()

       print("\n==== Medicine List ====")

       if len(medicines) == 0:
          print("No medicines found")
       else:
          for medicine in medicines:
            print(medicine)    


    def search_medicine(self):
       medicine_name = input("Enter Medicine Name to Search: ")

       self.cursor.execute(
        "SELECT * FROM medicines WHERE medicine_name = ?",
        (medicine_name,)
       )

       medicine = self.cursor.fetchone()

       if medicine:
        print("Medicine Found:")
        print(medicine)
       else:
        print("Medicine Not Found")

    def update_medicine(self):
       medicine_id = int(input("Enter Medicine ID to Update: "))
       new_time = input("Enter New Reminder Time: ")

       self.cursor.execute(
        "UPDATE medicines SET reminder_time = ? WHERE id = ?",
        (new_time, medicine_id)
       )

       conn.commit()

       print("Medicine Updated Successfully")

    def delete_medicine(self):
       medicine_id = int(input("Enter Medicine ID to Delete: "))

       self.cursor.execute(
        "DELETE FROM medicines WHERE id = ?",
        (medicine_id,)
       )

       conn.commit()

       print("Medicine Deleted Successfully")

    def export_medicines(self):

       self.cursor.execute("SELECT * FROM medicines")

       medicines = cursor.fetchall()

       df = pd.DataFrame(
        medicines,
        columns=[
            "ID",
            "Medicine Name",
            "Reminder Time",
            "Frequency"
        ]
       )

       df.to_csv("medicines_report.csv", index=False)

       print("Medicines Exported Successfully")

    def count_medicines(self):

       self.cursor.execute(
        "SELECT COUNT(*) FROM medicines"
       )

       total = self.cursor.fetchone()[0]

       print("Total Medicines =", total) 

app = MedicineReminder()   

while True:

    print("\n===== Medicine Reminder System =====")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Search Medicine")
    print("4. Update Medicine")
    print("5. Delete Medicine")
    print("6. Export Medicines")
    print("7. Count Medicines")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        app.add_medicine()

    elif choice == "2":
        app.view_medicines()

    elif choice == "3":
        app.search_medicine()

    elif choice == "4":
        app.update_medicine()

    elif choice == "5":
        app.delete_medicine()

    elif choice == "6":
        app.export_medicines() 

    elif choice == "7":
        app.count_medicines()       

    elif choice == "8":
        app.conn.close()
        print("Thank You!")
        break
    else:
        print("Invalid Choice")