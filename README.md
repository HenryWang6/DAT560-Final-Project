# 计算不同类别的转化率
category_rate_map.py
category_rate_red.py

# 计算不同类别产品中不同品牌购买成功率
top_buy_brand_of_category_map.py
top_buy_brand_of_category_red.py

# 购买成功发生的时间段 (画图，也许有规律)
Hive：
select event_time from estore where event_type = 'purchase'
select event_time from estore where event_type = 'view'

# 没有经过 view -> cart -> purchase 链的产品。重复购买，日用型的商品？（洗衣液 etc。）
no_hesitate_product_map.py
no_hesitate_product_red.py

# 