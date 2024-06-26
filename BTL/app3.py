import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog, font
from Crypto.Cipher import DES
import json
import base64
import sqlite3
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
    
def save_to_file(filepath, ciphertext):
    with open(filepath, 'w', encoding='utf-8') as file:
        json_data = [[base64.b64encode(nonce).decode('utf-8'),
                      base64.b64encode(ciphertext).decode('utf-8'),
                      base64.b64encode(tag).decode('utf-8')] for nonce, ciphertext, tag in ciphertext]
        json.dump(json_data, file, ensure_ascii=False, indent=4)

# def create_database():
#     conn = sqlite3.connect('employees.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
#                         emp_id TEXT PRIMARY KEY,
#                         name TEXT NOT NULL,
#                         position TEXT NOT NULL,
#                         salary TEXT NOT NULL
#                     )''')
#     conn.commit()
#     conn.close()

# def save_to_database(employees):
#     conn = sqlite3.connect('employees.db')
#     cursor = conn.cursor()
#     cursor.executemany('''INSERT OR REPLACE INTO employees (emp_id, name, position, salary) VALUES (?, ?, ?, ?)''',
#                        [(emp.emp_id, emp.name, emp.position, emp.salary) for emp in employees])
#     conn.commit()
#     conn.close()

# def load_from_database():
#     conn = sqlite3.connect('employees.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT * FROM employees''')
#     rows = cursor.fetchall()
#     conn.close()
#     return [Employee(row[0], row[1], row[2], row[3]) for row in rows]

# def add_employee_to_database(new_employee):
#     conn = sqlite3.connect('employees.db')
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO employees (emp_id, name, position, salary) VALUES (?, ?, ?, ?)''',
#                    (new_employee.emp_id, new_employee.name, new_employee.position, new_employee.salary))
#     conn.commit()
#     conn.close()

# def delete_employee_from_database(emp_id):
#     conn = sqlite3.connect('employees.db')
#     cursor = conn.cursor()
#     cursor.execute('''DELETE FROM employees WHERE emp_id = ?''', (emp_id,))
#     conn.commit()
#     conn.close()

# def update_employee_in_database(emp_id, field, new_value):
#     conn = sqlite3.connect('employees.db')
#     cursor = conn.cursor()
#     cursor.execute(f'''UPDATE employees SET {field} = ? WHERE emp_id = ?''', (new_value, emp_id))
#     conn.commit()
#     conn.close()

def save_decrypted_to_file(filename, decrypted_data):
    data = []
    for item in decrypted_data:
        emp_id, name, position, salary = item.split(', ')
        data.append({
            "emp_id": emp_id,
            "name": name,
            "position": position,
            "salary": salary
        })
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_after_delete(filename, employees):
    data = []
    for emp in employees:
        data.append({
            "emp_id": emp.emp_id,
            "name": emp.name,
            "position": emp.position,
            "salary": emp.salary
        })
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_employee_to_file(filename, new_employee):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data.append({
        "emp_id": new_employee.emp_id,
        "name": new_employee.name,
        "position": new_employee.position,
        "salary": new_employee.salary
    })

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_from_file_encrypted(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        return [(base64.b64decode(nonce),
                 base64.b64decode(ciphertext),
                 base64.b64decode(tag)) for nonce, ciphertext, tag in json_data]

def load_data():
    global employees, dataa
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                employees = [Employee(item['emp_id'], item['name'], item['position'], item['salary']) for item in data]
                dataa = data
            return data
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
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
    global dataa, en_key
    # data = load_data()
    if dataa:
        en_key = prompt_for_key()
        if not en_key:
            return
        des_encryption = DESEncryption(en_key)
        employees = [Employee(item['emp_id'], item['name'], item['position'], item['salary']) for item in dataa]
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
        emp_id = (entry_id.get())
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
        # save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        add_employee_to_file('D:\An toan va bao mat thong tin\BTL\employees.json', new_employee)
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

    summit_button = tk.Button(add_window, text='Gửi', command=submit)
    summit_button.grid(row=4, columnspan=2, pady=20, ipadx=20)

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
    save_after_delete('D:\An toan va bao mat thong tin\BTL\employees.json', employees)

def edit_employee():
    global employees
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Chú ý", "Chọn một nhân viên để sửa")
        return
    
    if len(selected_item) != 1:
        messagebox.showwarning("Chú ý", "Chỉ được chọn một nhân viên trong một lần chỉnh sửa")
        return
    
    selected_emp_id = tree.item(selected_item, 'values')[1]

    def submit():
        field_to_edit = field_var.get()
        new_value = entry_value.get()

        for employee in employees:
            if str(employee.emp_id) == selected_emp_id:
                if field_to_edit == 'ID':
                    employee.emp_id = new_value
                elif field_to_edit == "Họ và tên":
                    employee.name = new_value
                elif field_to_edit == "Vị trí":
                    employee.position = new_value
                elif field_to_edit == "Lương":
                    employee.salary = new_value
                break
    
        show_data([{
            'emp_id': emp.emp_id,
            'name': emp.name,
            'position': emp.position,
            'salary': emp.salary
        } for emp in employees])
        edit_window.destroy()
        save_after_delete('D:\An toan va bao mat thong tin\BTL\employees.json', employees)
    
    selected_employee = None
    for employee in employees:
        if str(employee.emp_id) == selected_emp_id:
            selected_employee = employee
            break
    
    if not selected_employee:
        messagebox.showerror("Lỗi", "Không tìm thấy nhân viên được chọn.")
        return
    
    edit_window = tk.Toplevel(root)
    edit_window.title("Sửa thông tin nhân viên.")

    tk.Label(edit_window, text='ID:').grid(row=0, column=0, padx=10, pady=5)
    tk.Label(edit_window, text=selected_employee.emp_id).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(edit_window, text='Chọn thông tin cần sửa:').grid(row=1, column=0, padx=10, pady=5)
    field_var = tk.StringVar()
    field_dropdown = tk.OptionMenu(edit_window, field_var, "ID", "Họ và tên", "Vị trí", "Lương")
    field_dropdown.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(edit_window, text='Nhập giá trị mới:').grid(row=2, column=0, padx=10, pady=5)
    entry_value = tk.Entry(edit_window)
    entry_value.grid(row=2, column=1, padx=10, pady=5)

    submit_button = tk.Button(edit_window, text='Gửi', command=submit)
    submit_button.grid(row=3, columnspan=2, pady=20, ipadx=20)

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Key")
        tk.Label(master, text="Nhập key:").grid(row=0)
        self.entry = tk.Entry(master, show="*")
        self.entry.grid(row=0, column=1)
        
        self.show_password = tk.BooleanVar()
        tk.Checkbutton(master, text="Hiển thị mật khẩu", variable=self.show_password, command=self.toggle_password, onvalue=1, offvalue=0).grid(row=1, columnspan=2)
        return self.entry

    def toggle_password(self):
        if self.show_password.get() == 0:
            self.entry.config(show="")
        elif self.show_password.get() == 1:
            self.entry.config(show="*")

    def apply(self):
        self.result = self.entry.get()

def prompt_for_key():
    root = tk.Tk()
    root.withdraw()

    while True:
        key = CustomDialog(root)
        key = key.result
        if key is None:
            return None
        elif len(key) != 8:
            messagebox.showerror("Error", "Key phải có đúng 8 ký tự.")
        else:
            return key.encode('utf-8')

def load_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

def main():
    global tree, root, employees
    employees = []

    root = tk.Tk()
    root.title('Quản lý nhân viên')

    load_icon = load_image("D:\An toan va bao mat thong tin\BTL\img and ico\loading.png", 20, 20)
    add_icon = load_image("D:\An toan va bao mat thong tin\BTL\img and ico\Add-user.png", 20, 20)
    edit_icon = load_image("D:\An toan va bao mat thong tin\BTL\img and ico\editing.png", 20, 20)
    delete_icon = load_image("D:\An toan va bao mat thong tin\BTL\img and ico\delete.png", 20, 20)
    encrypt_icon = load_image("D:\An toan va bao mat thong tin\BTL\img and ico\data-encryption.png", 20, 20)
    decrypt_icon = load_image("D:\An toan va bao mat thong tin\BTL\img and ico\decryption.png", 20, 20)


    frame = tk.Frame(root, bg='light gray')
    frame.pack(pady=100, fill=tk.BOTH, expand=True)

    root.geometry("1200x600")
    root.iconbitmap("D:\An toan va bao mat thong tin\BTL\img and ico\manager.ico")
    root.config(bg='light blue')

    custom_font = font.Font(family="Helvetica", size=12, weight="bold")

    tree = ttk.Treeview(frame, columns=('STT', 'ID', 'Họ và tên', 'Vị trí', 'Lương'), show='headings')
    tree.heading('STT', text='STT', )
    tree.heading('ID', text='ID')
    tree.heading('Họ và tên', text='Họ và tên')
    tree.heading('Vị trí', text='Vị trí')
    tree.heading('Lương', text='Lương')
    tree.pack(fill=tk.BOTH, expand=True)

    btn_load = tk.Button(
    root, image=load_icon, compound=tk.LEFT, text='Tải dữ liệu', 
    command=lambda: show_data(load_data()), font=custom_font,
    bg='deep sky blue', fg='white', activebackground='sky blue', activeforeground='white', 
    relief='raised', bd=5, padx=10, pady=5)
    btn_load.pack(side=tk.LEFT, padx=10, pady=10)

    btn_add = tk.Button(
    root, text='Thêm nhân viên', command=add_employee, image=add_icon, compound=tk.LEFT, 
    font=custom_font, bg='deep sky blue', fg='white', activebackground='sky blue', activeforeground='white',
    relief='raised', bd=5, padx=10, pady=5)
    btn_add.pack(side=tk.LEFT, padx=10, pady=10)

    btn_edit = tk.Button(
    root, text="Sửa thông tin nhân viên", command=edit_employee, image=edit_icon, compound=tk.LEFT, 
    font=custom_font, bg='deep sky blue', fg='white', activebackground='sky blue', activeforeground='white',
    relief='raised', bd=5, padx=10, pady=5)
    btn_edit.pack(side=tk.LEFT, padx=10, pady=10)

    btn_delete = tk.Button(
    root, text='Xóa nhân viên', command=delete_employee, image=delete_icon, compound=tk.LEFT, 
    font=custom_font, bg='deep sky blue', fg='white', activebackground='sky blue', activeforeground='white',
    relief='raised', bd=5, padx=10, pady=5)
    btn_delete.pack(side=tk.LEFT, padx=10, pady=10)

    btn_encrypt = tk.Button(
    root, text="Mã hóa dữ liệu", command=encrypt_data, image=encrypt_icon, compound=tk.LEFT, 
    font=custom_font, bg='red', fg='white', activebackground='dark red', activeforeground='white',
    relief='raised', bd=5, padx=10, pady=5)
    btn_encrypt.pack(side=tk.LEFT, padx=10, pady=10)


    btn_decrypt = tk.Button(
    root, text="Giải mã dữ liệu", command=decrypt_data, image=decrypt_icon, compound=tk.LEFT, 
    font=custom_font, bg='red', fg='white', activebackground='dark red', activeforeground='white',
    relief='raised', bd=5, padx=10, pady=5)
    btn_decrypt.pack(side=tk.LEFT, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
