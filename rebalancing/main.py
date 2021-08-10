from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import date

# basedate = datetime.datetime.strptime(base_date, '%Y%m%d')



ret = date.fromisoformat('2021-06-29') + relativedelta(months=1) + timedelta(days=-1)

rebal = ret + timedelta(days=-2)

print(ret)
print(rebal)
