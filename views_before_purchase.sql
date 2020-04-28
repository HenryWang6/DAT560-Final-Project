--不同用户访问，购买前浏览数量
select count(distinct(product_id)) as views_before_purchase
from estore
where user_session in (
	select user_session
	from estore
	where event_type = 'purchase'
)
group by user_session
order by desc;

--平均用户购买前浏览数量
上面的结果再求avg