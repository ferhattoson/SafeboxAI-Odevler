
Select category.id, COUNT(*) AS count,
       LAG(COUNT(*)) over (order by COUNT(*) ) as previous_count
From film_category 
join category on film_category.category_id = category.category_id
group by category.id
order by count ;