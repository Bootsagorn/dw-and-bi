Instruction Data Modeling 2 
1. open file in folder 02-data-modeling-2  --> cd 02-data-modeling-2
2. link to connect with Cassandra -- > $ pip install cqlsh
3. link to connect with file docker -->$  docker compose up 
4. open ports 9042 --> click ports --> open browser 9042 
5. load data in etl.py to Cassandra -->$  python etl.py 
6. Connected to Test Cluster -->$  cqlsh
7. run code to connect data --> cqlsh> select * from github_events.events ; 
8. exit from Test Cluster -- > cqlsh> exit
