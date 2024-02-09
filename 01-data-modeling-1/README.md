## Data modeling 1 ##
1. จากไฟล์ข้อมูล json จะความสัมพันธ์เพิ่มเติมระหว่าง table repo , table actors กับ table events  โดยเป็นความสัมพันธ์แบบ one to many โดยตาราง repo , actors เป็น one ส่วนทาง events เป็น many 
* 1) table events
    id (PK)  , type , actor_id (FK) , repo-id (FK)
* 2) table actors
    id (FK) , login
* 3) table repo
    id (FK) , name 
2. ทำการเพิ่ม code ในส่วน repo table ใน file etl.py และ create_tables.py  ใน folder 01-data-modeling-1
3.ทำการใช้งาน database 
	* กด terminal พิมพ์ cd 01-data-modeling-1/ 
	* ทำการเปิดใช้งาน teminal  pip install psycopg2 
	* terminal docker compose up 
	* click port 8080 เพื่อเปิด หน้า browser จะเข้าสู่หน้า database ให้ใส่รหัส postgres ทั้งหมด เข้าไปแล้วจะยังไม่ show table 
	* เปิด teminal ใหม่ python create_tables.py เพื่อทำการเชื่อมต่อสร้างตาราง
	* หน้า brower 8080 จะ มีตาราง table ขึ้นมา 3 tables คือ events , actors , repo

## Instruction ##
1. open file in folder 01-data-modeling-1  --> cd 01-data-modeling-1
2. link to connect with Postgres -- > $ pip install psycopg2
3. link to connect with file docker -->$  docker compose up 
4. open ports 8080 --> click ports --> open browser 8080 
5. load data in create_tables.py to postgres -->$  python create_tables.py
