select article.*, user.email 
from article
join user
on article.author = user.id;

select * from article
where id between 7 and 12
order by id;