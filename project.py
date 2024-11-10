import csv
import datetime

class EmployeeAttendanceSystem:
    def __init__(self, employee_file='employees.csv', attendance_file='attendance.csv'):
        self.employee_file = employee_file
        self.attendance_file = attendance_file
        
        # Initialize employee data and attendance data
        self.employees = self.load_employees()
        self.attendance = self.load_attendance()

    def load_employees(self):
        employees = {}
        try:
            with open(self.employee_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # skip empty rows
                        emp_id, emp_name = row
                        employees[emp_id] = emp_name
        except FileNotFoundError:
            print("Employee file not found. Creating a new one.")
        return employees

    def load_attendance(self):
        attendance = {}
        try:
            with open(self.attendance_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # skip empty rows
                        emp_id, date, status = row
                        if emp_id not in attendance:
                            attendance[emp_id] = {}
                        attendance[emp_id][date] = status
        except FileNotFoundError:
            print("Attendance file not found. Creating a new one.")
        return attendance

    def add_employee(self, emp_id, emp_name):
        if emp_id in self.employees:
            print(f"Employee ID {emp_id} already exists.")
        else:
            self.employees[emp_id] = emp_name
            # Save the employee to the CSV file
            with open(self.employee_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([emp_id, emp_name])
            print(f"Employee {emp_name} added successfully.")

    def mark_attendance(self, emp_id, status):
        date_today = datetime.datetime.now().strftime('%Y-%m-%d')
        if emp_id not in self.employees:
            print(f"Employee ID {emp_id} not found.")
            return
        
        if emp_id not in self.attendance:
            self.attendance[emp_id] = {}

        self.attendance[emp_id][date_today] = status
        # Save the attendance to the CSV file
        with open(self.attendance_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, date_today, status])
        print(f"Attendance for {self.employees[emp_id]} on {date_today} marked as {status}.")

    def view_attendance(self, emp_id):
        if emp_id not in self.employees:
            print(f"Employee ID {emp_id} not found.")
            return
        if emp_id not in self.attendance:
            print(f"No attendance records found for {self.employees[emp_id]}.")
            return

        print(f"Attendance records for {self.employees[emp_id]}:")
        for date, status in self.attendance[emp_id].items():
            print(f"{date}: {status}")

    def show_all_attendance(self):
        print("All Attendance Records:")
        for emp_id, records in self.attendance.items():
            employee_name = self.employees.get(emp_id, "Unknown Employee")
            print(f"\nAttendance for {employee_name} (ID: {emp_id}):")
            for date, status in records.items():
                print(f"{date}: {status}")

def main():
    system = EmployeeAttendanceSystem()

    while True:
        print("\nEmployee Attendance System")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. View Attendance for Employee")
        print("4. View All Attendance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            emp_name = input("Enter Employee Name: ")
            system.add_employee(emp_id, emp_name)

        elif choice == '2':
            emp_id = input("Enter Employee ID: ")
            status = input("Enter Attendance Status (Present/Absent): ")
            system.mark_attendance(emp_id, status)

        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            system.view_attendance(emp_id)

        elif choice == '4':
            system.show_all_attendance()

        elif choice == '5':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
