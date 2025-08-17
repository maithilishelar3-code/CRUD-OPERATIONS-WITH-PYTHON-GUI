from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hospitalDB"]
collection = db["patients"]

print("Connected to MongoDB!")
import tkinter as tk
from tkinter import messagebox

# GUI window
root = tk.Tk()
root.title("Hospital Management - CRUD App")
root.geometry("500x450")

# Labels & Entry boxes
tk.Label(root, text="Patient ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Disease").pack()
disease_entry = tk.Entry(root)
disease_entry.pack()

tk.Label(root, text="Admitted (true/false)").pack()
admitted_entry = tk.Entry(root)
admitted_entry.pack()
# CREATE
def add_patient():
    patient_id = id_entry.get()
    name = name_entry.get()
    age = int(age_entry.get())
    disease = disease_entry.get()
    admitted = True if admitted_entry.get().lower() == "yes" else False

    collection.insert_one({
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "disease": disease,
        "admitted": admitted
    })
    messagebox.showinfo("Success", "Patient Added!")

# READ
def view_patients():
    patients = collection.find()
    data = ""
    for p in patients:
        data += f"ID: {p['patient_id']} | {p['name']} | Age: {p['age']} | {p['disease']} | Admitted: {p['admitted']}\n"
    messagebox.showinfo("Patients", data if data else "No patients found")

# UPDATE
def update_patient():
    patient_id = id_entry.get()
    new_disease = disease_entry.get()
    collection.update_one({"patient_id": patient_id}, {"$set": {"disease": new_disease}})
    messagebox.showinfo("Updated", "Disease Updated!")

# DELETE
def delete_patient():
    patient_id = id_entry.get()
    collection.delete_one({"patient_id": patient_id})
    messagebox.showinfo("Deleted", "Patient Deleted!")
tk.Button(root, text="Add Patient", command=add_patient).pack(pady=5)
tk.Button(root, text="View Patients", command=view_patients).pack(pady=5)
tk.Button(root, text="Update Patient", command=update_patient).pack(pady=5)
tk.Button(root, text="Delete Patient", command=delete_patient).pack(pady=5)

root.mainloop()

