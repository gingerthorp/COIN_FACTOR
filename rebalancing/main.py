from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import date

# basedate = datetime.datetime.strptime(base_date, '%Y%m%d')


ret = date.fromisoformat('2021-01-29')
ret_for = ret + relativedelta(months=1)
ret_back = ret_for - relativedelta(months=1)

print(ret)
print(ret_back)
