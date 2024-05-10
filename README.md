YCSB to do performance test on MariaDB


LOAD Command : bin/ycsb load jdbc -P workloads/workloada -P jdbc-binding/conf/db.properties -cp mysql-connector- java-5.1.49


![load_operation](https://github.com/ashrith5355/network_flow_db/assets/162978232/cdafce09-d84f-498f-8860-e31e22f9ee89)


RUN Command : bin/ycsb run jdbc -P workloads/workloada -P jdbc-binding/conf/db.properties -cp mysql-connector- java-5.1.49


![run_operation](https://github.com/ashrith5355/network_flow_db/assets/162978232/44ccbfa2-ac68-40a6-869b-fbd167c8641f)



Batch Operations


<img width="690" alt="Batch insert,delete" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/33bca47d-e961-4d8c-b763-f315ee473d99">



Bulk Operations


<img width="812" alt="Bulk_result" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/6991c38d-6c76-4c0a-a98b-6e6788e29d43">


YCSB Bulk operations


<img width="853" alt="Screenshot 2024-05-10 at 2 26 23 PM" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/b5f5c315-3301-48c1-87e4-055a1bd789a4">


Load Insertion Operations

<img width="1710" alt="Load_insert_100" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/2b24e439-3125-4292-abde-e19df6cb509e">
<img width="1710" alt="Load_insert_1000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/4de50933-8e15-4339-8415-8ad0af498340">
<img width="1710" alt="Load_insert_10000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/e420cc87-2df3-415e-b5e1-2066676c50a0">
<img width="1710" alt="Load_insert_100000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/f2d9f24c-b854-4bad-aac7-8382e8944229">
<img width="1710" alt="Load_insertion_1000000" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/179b2aa1-91f2-4196-b8b7-45399e377939">

