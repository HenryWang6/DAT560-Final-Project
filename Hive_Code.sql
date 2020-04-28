# 问题！！！event_time 需要把数据里面的utc这三个字去掉，不然应该会建表之后变null
-- Create Table
create table eshop (event_time timestamp, event_type string, product_id bigint, category_id bigint, category_code string,
	brand string, price float, user_id bigint, user_session string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
tblproperties("skip.header.line.count" = '1');

-- Load data
LOAD DATA INPATH '/user/pudu/2019-Oct.csv' INTO TABLE `eshop`;