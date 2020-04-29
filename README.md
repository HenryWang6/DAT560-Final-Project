# 处理第一列date time
* 只用python处理就好了，不用mapreduce。
* datetime_process_map.py
* 方法是：在自己的目录下: cat 2019-Oct.csv | python datetime_process_map.py > new2019-Oct.csv

# 建立HIVE数据库
* 浦哥 “/user/pudu/” 这个Hadoop文件夹的权限我们没有，建立不了table
* Hive_Code.sql

# 计算不同类别的转化率
* category_rate_map.py
* category_rate_red.py

# 计算不同类别产品中不同品牌购买成功率
* top_buy_brand_of_category_map.py
* top_buy_brand_of_category_red.py

# 购买成功发生的时间段 (画图，也许有规律)
* Hive：
* select event_time from estore where event_type = 'purchase'
* select event_time from estore where event_type = 'view'

# 没有经过 view -> cart -> purchase 链的产品。重复购买，日用型的商品？（洗衣液 etc。）
* no_hesitate_product_map.py
* no_hesitate_product_red.py

# 用户单次访问且成功购买，成功购买前浏览几个商品？
* views_before_purchase.sql
