from erpnext.setup.doctype.employee.employee import Employee
import frappe

class WashingEmployee(Employee):
    def validate(self):
        frappe.msgprint("🔥 WashingEmployee override method WORKING! Save blocked for test")
        print("🔥 WashingEmployee override method WORKING! Save blocked for test")
        return   # stops save for testing
