# 💻 Command Line on Terminal
**📘 Lecture Class 1**

---

## 📂 1. List – คำสั่งสำหรับแสดงแฟ้มข้อมูล
แสดง file / folder ที่อยู่ใน folder ปัจจุบัน

```
ls
```

```
ls -l
```
📝 แสดงรายละเอียดไฟล์ในรูปแบบ long format  
(Permission / จำนวน user / ขนาดไฟล์ / วันเวลา / ชื่อไฟล์)
> 🔐 Permission | 👤 Users | 📦 Size | 🕒 Date | 📄 File name

```
ls -lh
```
แสดงขนาดไฟล์แบบอ่านง่าย (human-readable)
> Permission | Users | Size (Readable) | Date | File name

```
ls -ltr
```
เรียงไฟล์ตามเวลาที่แก้ไขล่าสุด

ไฟล์ใหม่ที่สุดจะแสดงอยู่ด้านล่างสุด
> -t → เรียงตามเวลา

> -r → กลับลำดับ

Permission
> r → read

> w → write

> x → execute

## 📁 2. Change Directory
คำสั่งสำหรับเปลี่ยนตำแหน่งโฟลเดอร์

```
cd
```
กลับไปยัง Home directory (~)

```
cd ..
```
ย้อนกลับไปโฟลเดอร์ก่อนหน้า 1 ระดับ

```
cd ../..
```
ย้อนกลับ 2 ระดับ

```
cd <folder_name>/
```

> กด Tab เพื่อช่วยเติมชื่อโฟลเดอร์อัตโนมัติ

```
pwd
```

แสดงตำแหน่งที่อยู่ปัจจุบัน (current directory)

## 🗂️ 3. File / Folder Management
สร้างโฟลเดอร์

```
mkdir <folder_name>
```
สร้างและแก้ไขไฟล์

```
vi <file_name>
vi <file_name>.py
```
🛠️ ขั้นตอนการใช้งาน vi  
> ✏️ กด `i` → โหมดเขียน  
> ⎋ กด `Esc`  
> 💾 `:wq` → บันทึกและออก  
> ❌ `:q!` → ออกโดยไม่บันทึก  

🗑️ ลบไฟล์

```
rm <file_name>
```
ลบโฟลเดอร์ทั้งหมด

```
rm -r <folder_name>
```
เปิดดูเนื้อหาไฟล์

```
cat <file_name>
```
## 4. Move File
วิธีที่ 1 ระบุ path ต้นทางและปลายทาง

```
mv <source_path>/<file_name> <destination_path>/.
```
วิธีที่ 2 อยู่ในโฟลเดอร์ปลายทาง

```
mv ../<file_name> .
```
> . หมายถึงตำแหน่งปัจจุบัน

## 5. Copy File / Folder
Copy ไฟล์

```
cp <source_path>/<file_name> <destination_path>/.
```
📂 Copy โฟลเดอร์

```
cp -r <folder_source> .
```
## 6. Manual Page

```
man <command>
```
ใช้ดูคู่มือคำสั่ง

## 🖥️ 7. Check System Preference
```
htop
```
📊 ใช้ดูการใช้งาน RAM และ CPU  
> ⚠️ ต้องติดตั้งก่อนใช้งาน

## Notes เพิ่มเติม

```
drwxr-xr-x
```
* 📁 d → directory  
* 🔍 r → read  
* ⚙️ x → execute  
* 📏 ls -lh → แสดงขนาดไฟล์แบบอ่านง่าย  
* ⏱️ ls -ltr → ไฟล์ล่าสุดอยู่ด้านล่างสุด  

