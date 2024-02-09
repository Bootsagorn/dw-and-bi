Documentation Data Modeling 2
1. ทำการรัน pip install cqlsh ติดตั้งเครื่องมือ cqlsh ผ่าน pip เพื่อเชื่อมต่อการทำงานกับ Cassandra database
2. ทำการรัน docker compose up เพื่อเปิดการใช้งานแอพในไฟล์ docker-compose.yml
3. เปิดหน้า ports 9042 เพื่อดูการเชื่อมต่อบน browser 
4. เปิดหน้า terminal ใหม่ ทำการรัน python etl.py เพื่อดึงข้อมูลจากไฟล์ โดยจากการดู file ข้อมูลได้ทำการออกแบบความสัมพันธ์ของตารางใน model ได้มีการสร้าง table events มีข้อมูลในตาราง ประกอบด้วย 8 คอลัมน์
* 1)  id  (PK)  --> เก็บข้อมูลเป็น  text // เป็น id ของ events
* 2)  type (PK) --> เก็บข้อมูลเป็น text // การเก็บข้อมูล type สามารถเอามาดูได้ว่าผู้ใช้ทำ events type แบบใด 
* 3)  actor_id --> เก็บข้อมูลเป็น text // เป็น id ของชื่อผู้ใช้งาน
* 4)  actor_name --> เก็บข้อมูลเป็น text // การเก็บข้อมูลชื่อของผู้ใช้งานสามารถเอามาใช้ในหาจำนวนผู้ใช้งานได้
* 5)  repo_id --> เก็บข้อมูลเป็น text // เป็น id ของ repo
* 6)  repo_name --> เก็บข้อมูลเป็น text // เป็นชื่อที่เก็บใน repo
* 7)  create_at --> เก็บข้อมูลแบบ time stamp // สามารถนำข้อมูลวันที่เริ่มสร้างหาได้ว่าผู้ใช้ได้สร้าง events ไปแล้วกี่วัน
* 8)  public --> เก็บข้อมูลเป็น boolean // การเก็บข้อมูล public สามารถรู้ได้ว่า events นี้เปิดให้ดูเป็น public หรือไหม สามารถ query เรียกดูแค่ข้อมูล public = true ได้
 * ในการออกแบบให้ id , type เป็น primary key และ type เป็น clustering column เพื่อเรียงลำดับข้อมูลภายใน partition ของคอลัมน์ id
5. รัน $ cqlsh ทำการเชื่อมต่อกับ Cassandra database เพื่อ Test Cluster
6. รัน cqlsh> select * from github_events.events ; เพื่อดู insert_sample_data ที่ได้เพิ่มเข้าไป
7. เมื่อทดสอบเสร็จ cqlsh> exit 


Instruction Data Modeling 2 
1. open file in folder 02-data-modeling-2  --> cd 02-data-modeling-2
2. link to connect with Cassandra -- > $ pip install cqlsh
3. link to connect with file docker -->$  docker compose up 
4. open ports 9042 --> click ports --> open browser 9042 
5. load data in etl.py to Cassandra -->$  python etl.py 
6. Connected to Test Cluster -->$  cqlsh
7. run code to connect data --> cqlsh> select * from github_events.events ; 
8. exit from Test Cluster -- > cqlsh> exit
