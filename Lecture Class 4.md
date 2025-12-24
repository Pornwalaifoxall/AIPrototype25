# 🐍 Managing Conda Environment
**Lecture: Environment & Version Control**

---

## 📦 Installing Conda
Conda สามารถติดตั้งได้จาก 2 แหล่งหลัก

- **Miniconda** (เบา เหมาะกับ Server)  
  👉 https://docs.conda.io/en/latest/miniconda.html

- **Anaconda** (ครบ พร้อม GUI)  
  👉 https://www.anaconda.com/products/distribution

ตรวจสอบว่าติดตั้งสำเร็จหรือไม่
```
conda --version
```
---

## 🌱 Create Conda Environment
เมื่อเปิด Terminal ใหม่ จะอยู่ที่ `(base)`

### 🌈 Create Environment
สร้าง Environment ใหม่
```
conda create --name <env_name> python=<version>
```
📌 ตัวอย่าง
```
conda create --name testpy38 python=3.8
```
ใช้งาน Environment
```
conda activate <env_name>
```
ออกจาก Environment
```
conda deactivate
```
ลบ Environment
```
conda remove --name <env_name> --all
```
ดูรายการ Environment ทั้งหมด
```
conda env list
```
### 📦  Install Packages

⚠️ ต้อง Activate Environment ก่อนติดตั้ง Package

ติดตั้ง Package
```
conda install <package_name>
```
ตัวอย่าง
```
conda install pandas
```
ดู Package ทั้งหมดที่ติดตั้งอยู่
```
conda list
```
### 🐙 GitHub Command Line
#### ⚙️ Git Configuration (ทำครั้งเดียว)

ตั้งค่า Username และ Email
```
git config --global user.name "username"
git config --global user.email "email@example.com"
```
🔐 เวลา push จะใช้ Personal Access Token แทน password

##### 📥 Clone Repository

โคลน Repository จาก GitHub
```
git clone <repository_url>
```
##### 🚀 Save Code to GitHub

เมื่อมีการแก้ไขไฟล์ ให้ทำตามขั้นตอนนี้

1️⃣ ดึงเวอร์ชันล่าสุด
```
git pull
```
2️⃣ เพิ่มไฟล์เข้า staging
```
git add <file_name>
```
3️⃣ Commit การเปลี่ยนแปลง
```
git commit -m "commit message"
```
4️⃣ Push ขึ้น GitHub
```
git push
```
✨ ลำดับที่ต้องจำให้ได้
add → commit → push

##### 🔍 Check Status

ตรวจสอบสถานะไฟล์
```
git status
```
ความหมายของสถานะ

- 🔴 สีแดง → ยังไม่ถูก track

- 🟢 สีเขียว → อยู่ใน staging

- ⚪ ไม่ขึ้นอะไร → ทุกอย่างเรียบร้อยแล้ว

##### 🔑 GitHub Token

สร้าง Token ได้ที่
GitHub → Settings → Developer Settings → Personal Access Tokens
> 💾 Token จะแสดงเพียงครั้งเดียว อย่าลืมเก็บไว้ให้ดีนะคะ

##### 💡 Useful Command Line Tips

ค้นหาคำสั่งที่เคยใช้ใน Terminal
```
Ctrl + R
```
พิมพ์ keyword เพื่อค้นหาคำสั่งย้อนหลังได้เลย ✨

