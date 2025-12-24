# ☁️ Cloud Virtual Machines
**Lecture Class : Azure Virtual Machine**

---

## 🌐 Cloud Service Models
รูปแบบการให้บริการคลาวด์หลัก ๆ มี 3 แบบ

- 🧱 **Infrastructure as a Service (IaaS)**
- 🧩 **Platform as a Service (PaaS)**
- 🖥️ **Software as a Service (SaaS)**
  

  🔗 สมัครใช้งานผ่าน      [Microsoft Azure for Students](https://azure.microsoft.com/en-us/free/students)

  🔗 เข้าใช้งาน Portal    [Azure Portal – ai_prototype_25](https://portal.azure.com)

---
## 💻 Virtual Machine (VM)
การสร้าง Virtual Machine บน Azure

📌 ขั้นตอน  
`Azure Portal → Education → Virtual Machines → Create a virtual machine`

---

### 🔐 1. เข้า Server ด้วย SSH
**SSH = Secure Shell** 

```
ssh username@IPaddress
```
### 👥 2. เพิ่ม User ให้เพื่อนเข้า Server ได้

```
sudo adduser friendusername
```
---

### 📊 3. ตรวจสอบการทำงานของ Server
ดูการใช้ CPU และ RAM

```
htop
```
### 🗂️ 4. จัดการ Group
ย้าย user ไปอยู่ group เดียวกัน

```
sudo usermod friendusername yourusername 
```
ตรวจสอบ group ทั้งหมดใน server

```
sudo groups yourusername
```
---

### 🛡️ 5. เพิ่มสิทธิ์ SuperUser (sudo)
ให้เพื่อนใช้คำสั่ง `sudo` ได้

```
sudo adduser friendusername sudo
```
### 📦 6. SCP – Secure Copy
ใช้ส่งไฟล์ระหว่างเครื่องเรา ↔ Cloud  
⚠️ **ต้องรันบนเครื่องของเรา ไม่ใช่ใน VM**

#### รูปแบบพื้นฐาน

```
scp <source_path> <destination_path>
```
#### 📤 คัดลอกจากเครื่อง → Cloud

```
scp <path_file>/<filename> username@IP:~<folder>/.
```
#### 📥 คัดจาก Cloud → เครื่อง

```
scp username@IP:<path_file>/<filename> <destination_path>/.
```
#### 📁 คัดลอกโฟลเดอร์

```
scp -r <folder_source> username@IP:~<folder>/.
```
---

### 🚪 7. ออกจาก Program (เช่น Python)

```
exit()
```
---

### 🔚 8. Log out จาก VM

```
exit
```

---

## 📝 Example Workflow

### 🔹 ส่งไฟล์จากเครื่อง → VM
- ใช้คำสั่ง `scp` บนเครื่องเรา
- ตรวจสอบบน VM ด้วย `ls`

### 🔹 ส่งไฟล์จาก VM → เครื่อง
- ออกจาก VM ก่อน
- ใช้ `scp` บนเครื่องเรา

---

## 🐍 Python Environment
### ติดตั้ง Miniconda
ใช้สำหรับจัดการ environment ของ Python

📌 เพื่อให้ `(base)` แสดงตลอด  
ให้รันคำสั่งตั้งค่า environment ตามลำดับ

---

## 🧠 Notes เพิ่มเติม
- `exit()` → ต้องมีวงเล็บ
- `scp` → ต้องรันจากเครื่องเรา
- `ssh` → ใช้ username ที่ตั้งตอนสร้าง VM
- ตรวจสอบไฟล์บน VM เสมอด้วย `ls`

---

✨ **End of Lecture**



