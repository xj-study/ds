select w.name, a.count, a.date
from websites as w
right join access_log as a
on w.id = a.site_id
order by a.count desc;