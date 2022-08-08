With 
OrderDate as (
              SELECT distinct  "Order Date" as OrderDate
             FROM "sample superstore"
             order by "Order Date"
        )

select count(*),min(OrderDate)
from
  (select *,
        -- Substract the row_Number from the date will give you a consecutive date
        date_sub(OrderDate,row_number() over (order by OrderDate) )as condate
        from OrderDate
        )
    group by condate
    order by min(OrderDate)