import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog, font
from Crypto.Cipher import DES
import sqlite3
import base64
from PIL import Image, ImageTk

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self) -> str:
        return f'ID: {self.emp_id}, Họ và tên: {self.name}, Vị trí: {self.position}, Lương: {self.salary}'

class DESEncryption:
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, plaintext):
        des = DES.new(self.key, DES.MODE_EAX)
        nonce = des.nonce
        ciphertext, tag = des.encrypt_and_digest(plaintext.encode('utf-8'))
        return nonce, ciphertext, tag
    
    def decrypt(self, nonce, ciphertext, tag):
        des = DES.new(self.key, DES.MODE_EAX, nonce=nonce)
        plaintext = des.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')

def create_database():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        emp_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        position TEXT NOT NULL,
                        salary TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def save_to_database(employees):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.executemany('''INSERT OR REPLACE INTO employees (emp_id, name, position, salary) VALUES (?, ?, ?, ?)''',
                       [(emp.emp_id, emp.name, emp.position, emp.salary) for emp in employees])
    conn.commit()
    conn.close()

def load_from_database():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM employees''')
    rows = cursor.fetchall()
    conn.close()
    return [Employee(row[0], row[1], row[2], row[3]) for row in rows]

def add_employee_to_database(new_employee):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO employees (emp_id, name, position, salary) VALUES (?, ?, ?, ?)''',
                   (new_employee.emp_id, new_employee.name, new_employee.position, new_employee.salary))
    conn.commit()
    conn.close()

def delete_employee_from_database(emp_id):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM employees WHERE emp_id = ?''', (emp_id,))
    conn.commit()
    conn.close()

def update_employee_in_database(emp_id, field, new_value):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute(f'''UPDATE employees SET {field} = ? WHERE emp_id = ?''', (new_value, emp_id))
    conn.commit()
    conn.close()

def load_data():
    global employees
    try:
        employees = load_from_database()
        return [{'emp_id': emp.emp_id, 'name': emp.name, 'position': emp.position, 'salary': emp.salary} for emp in employees]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data: {str(e)}")
        return None

def show_data(data):
    global tree
    for item in tree.get_children():
        tree.delete(item)
    if data:
        for idx, item in enumerate(data, start=1):
            tree.insert("", tk.END, values=(idx, item['emp_id'], item['name'], item['position'], item['salary']))
        tree.column('STT', width=30, anchor=tk.CENTER)
        tree.column('ID', width=30, anchor=tk.CENTER)
        tree.column('Họ và tên', width=200)
        tree.column('Vị trí', width=150)
        tree.column('Lương', width=100)

def encrypt_data():
    global employees, en_key
    if employees:
        en_key = prompt_for_key()
        if not en_key:
            return
        des_encryption = DESEncryption(en_key)
        encrypted_data = []
        for emp in employees:
            emp_data = f'{emp.emp_id}, {emp.name}, {emp.position}, {emp.salary}'
            nonce, ciphertext, tag = des_encryption.encrypt(emp_data)
            encrypted_data.append((nonce, ciphertext, tag))
        save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if save_path:
            save_to_file(save_path, encrypted_data)
            messagebox.showinfo("Thông báo", "Dữ liệu đã được mã hóa và lưu vào file.")

def match():
    global en_key
    while True:
        key = prompt_for_key()
        if key != en_key:
            messagebox.showerror("Error", "Key khi giải mã phải giống với key dùng khi mã hóa.")
        elif key is None:
            return None
        else:
            return key

def decrypt_data():
    global de_key
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        de_key = match()
        if not de_key:
            return
        des_encryption = DESEncryption(de_key)
        try:
            loaded_data = load_from_file_encrypted(file_path)
            decrypted_data = []
            for nonce, ciphertext, tag in loaded_data:
                plaintext = des_encryption.decrypt(nonce, ciphertext, tag)
                decrypted_data.append(plaintext)
            save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if save_path:
                save_decrypted_to_file(save_path, decrypted_data)
                messagebox.showinfo("Thông báo", "Dữ liệu đã được giải mã và lưu vào file.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt data: {str(e)}")

def add_employee():
    def submit():
        emp_id = entry_id.get()
        name = entry_name.get()
        position = entry_position.get()
        salary = entry_salary.get()

        new_employee = Employee(emp_id, name, position, salary)
        employees.append(new_employee)

        show_data([{
            'emp_id': emp.emp_id,
            'name': emp.name,
            'position': emp.position,
            'salary': emp.salary
        } for emp in employees])
        add_employee_to_database(new_employee)
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title('Thêm nhân viên.')

    tk.Label(add_window, text='ID').grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(add_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text='Họ và tên: ').grid(row=1, column=0, padx=10, pady=5)
    entry_name = tk.Entry(add_window)
    entry_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_window, text='Vị trí: ').grid(row=2, column=0, padx=10, pady=5)
    entry_position = tk.Entry(add_window)
    entry_position.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_window, text='Lương: ').grid(row=3, column=0, padx=10, pady=5)
    entry_salary = tk.Entry(add_window)
    entry_salary.grid(row=3, column=1, padx=10, pady=5)

    submit_button = tk.Button(add_window, text='Gửi', command=submit)
    submit_button.grid(row=4, columnspan=2, pady=20, ipadx=20)

def update_idx():
    for idx, item in enumerate(tree.get_children(), start=1):
        tree.set(item, 'STT', idx)

def delete_employee():
    global employees
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Chú ý", "Chọn ít nhất một nhân viên để xóa.")
        return
    
    confirm = messagebox.askyesno("Xác nhận xóa", "Bạn chắc chắn xóa chứ?")
    if not confirm:
        return

    for selected_item in selected_items:
        emp_id = tree.item(selected_item, 'values')[1]
        for employee in employees:
            if str(employee.emp_id) == emp_id:
                employees.remove(employee)
                break
        tree.delete(selected_item)

    update_idx()
    show_data([{
        'emp_id': emp.emp_id,
        'name': emp.name,
        'position': emp.position,
        'salary': emp.salary
    } for emp in employees])
    delete_employee_from_database(emp_id)

def edit_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Chú ý", "Chọn một nhân viên để chỉnh sửa.")
        return

    def submit():
        field = combo_field.get()
        new_value = entry_new_value.get()
        emp_id = tree.item(selected_item, 'values')[1]
        for emp in employees:
            if str(emp.emp_id) == emp_id:
                if field == 'Họ và tên':
                    emp.name = new_value
                elif field == 'Vị trí':
                    emp.position = new_value
                elif field == 'Lương':
                    emp.salary = new_value
                break

        show_data([{
            'emp_id': emp.emp_id,
            'name': emp.name,
            'position': emp.position,
            'salary': emp.salary
        } for emp in employees])
        update_employee_in_database(emp_id, field, new_value)
        edit_window.destroy()

    edit_window = tk.Toplevel(root)
    edit_window.title('Chỉnh sửa thông tin nhân viên.')

    tk.Label(edit_window, text='Chọn trường thông tin cần chỉnh sửa:').grid(row=0, column=0, padx=10, pady=5)
    combo_field = ttk.Combobox(edit_window, values=['Họ và tên', 'Vị trí', 'Lương'])
    combo_field.grid(row=0, column=1, padx=10, pady=5)
    combo_field.current(0)

    tk.Label(edit_window, text='Nhập giá trị mới:').grid(row=1, column=0, padx=10, pady=5)
    entry_new_value = tk.Entry(edit_window)
    entry_new_value.grid(row=1, column=1, padx=10, pady=5)

    submit_button = tk.Button(edit_window, text='Gửi', command=submit)
    submit_button.grid(row=2, columnspan=2, pady=20, ipadx=20)

def prompt_for_key():
    return simpledialog.askstring("Mật khẩu", "Nhập key (8 ký tự):", show="*")

# GUI Setup
root = tk.Tk()
root.title("Quản lý nhân viên.")
root.geometry("1000x500")

# Set the icon for the Tkinter window
# icon_image = Image.open("user_login.jpg")
# icon_photo = ImageTk.PhotoImage(icon_image)
# root.iconphoto(True, icon_photo)

employees = []

title_font = font.Font(family="Helvetica", size=24, weight="bold")
title_label = tk.Label(root, text="QUẢN LÝ NHÂN VIÊN", font=title_font)
title_label.pack(pady=10)

tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, columns=('STT', 'ID', 'Họ và tên', 'Vị trí', 'Lương'), show='headings')
tree.pack()

tree_scroll.config(command=tree.yview)

tree.heading('STT', text='STT')
tree.heading('ID', text='ID')
tree.heading('Họ và tên', text='Họ và tên')
tree.heading('Vị trí', text='Vị trí')
tree.heading('Lương', text='Lương')

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="Thêm nhân viên", command=add_employee)
add_button.grid(row=0, column=0, padx=10)

edit_button = tk.Button(button_frame, text="Sửa thông tin", command=edit_employee)
edit_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(button_frame, text="Xóa nhân viên", command=delete_employee)
delete_button.grid(row=0, column=2, padx=10)

encrypt_button = tk.Button(button_frame, text="Mã hóa dữ liệu", command=encrypt_data)
encrypt_button.grid(row=0, column=3, padx=10)

decrypt_button = tk.Button(button_frame, text="Giải mã dữ liệu", command=decrypt_data)
decrypt_button.grid(row=0, column=4, padx=10)

load_button = tk.Button(root, text="Tải dữ liệu", command=lambda: show_data(load_data()))
load_button.pack(pady=10)

create_database()
load_button.invoke()

root.mainloop()
