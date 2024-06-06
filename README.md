YCSB to do performance test on MariaDB


LOAD Command : bin/ycsb load jdbc -P workloads/workloada -P jdbc-binding/conf/db.properties -cp mysql-connector- java-5.1.49


![load_operation](https://github.com/ashrith5355/network_flow_db/assets/162978232/cdafce09-d84f-498f-8860-e31e22f9ee89)


RUN Command : bin/ycsb run jdbc -P workloads/workloada -P jdbc-binding/conf/db.properties -cp mysql-connector- java-5.1.49


![run_operation](https://github.com/ashrith5355/network_flow_db/assets/162978232/44ccbfa2-ac68-40a6-869b-fbd167c8641f)



Batch Operations


<img width="715" alt="Screenshot 2024-06-06 at 11 05 04 AM" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/212a6a35-623d-4a6f-882b-3d62817f6c08">



Bulk Operations


<img width="812" alt="Bulk_result" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/6991c38d-6c76-4c0a-a98b-6e6788e29d43">


YCSB Bulk operations


<img width="836" alt="YCSB bulk Operations" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/94dc28b1-9c1c-426e-922f-9a334358b091">


Load Insertion Operations


100:
<img width="1710" alt="Load_insert_100" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/2b24e439-3125-4292-abde-e19df6cb509e">
1000:
<img width="1710" alt="Load_insert_1000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/4de50933-8e15-4339-8415-8ad0af498340">
10,000:
<img width="1710" alt="Load_insert_10000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/e420cc87-2df3-415e-b5e1-2066676c50a0">
1,00,000:
<img width="1710" alt="Load_insert_100000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/f2d9f24c-b854-4bad-aac7-8382e8944229">
10,00,000:
<img width="1710" alt="Load_insertion_1000000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/179b2aa1-91f2-4196-b8b7-45399e377939">


Run Updation Operations


100:
<img width="1710" alt="Run_update_100" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/3543e422-e383-4bf2-8032-acffbc98586a">
1000:
<img width="1710" alt="Run_update_1000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/c02ff630-fd3f-4487-9049-bded08b59be3">
10,000:
<img width="1710" alt="Run_update_10000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/cddee4e2-857d-4ac7-a6fe-f01fc094ff7f">
1,00,000:
<img width="1709" alt="Run_update_100000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/52b54e96-2339-4225-b245-4c2fc98b26db">
10,00,000:
<img width="1710" alt="Run_update_1000000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/efafdf0e-0cc5-4829-bf95-2c77ef35a13d">


