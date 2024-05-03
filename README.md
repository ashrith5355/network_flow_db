YCSB to do performance test on MariaDB


LOAD Command : bin/ycsb load jdbc -P workloads/workloada -P jdbc-binding/conf/db.properties -cp mysql-connector- java-5.1.49


![load_operation](https://github.com/ashrith5355/network_flow_db/assets/162978232/cdafce09-d84f-498f-8860-e31e22f9ee89)


RUN Command : bin/ycsb run jdbc -P workloads/workloada -P jdbc-binding/conf/db.properties -cp mysql-connector- java-5.1.49


![run_operation](https://github.com/ashrith5355/network_flow_db/assets/162978232/44ccbfa2-ac68-40a6-869b-fbd167c8641f)



Batch Operations


<img width="690" alt="Batch insert,delete" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/33bca47d-e961-4d8c-b763-f315ee473d99">



Bulk Operations


<img width="812" alt="Bulk_result" src="https://github.com/ashrith5355/network_flow_db/assets/162978232/6991c38d-6c76-4c0a-a98b-6e6788e29d43">

