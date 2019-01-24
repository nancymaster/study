# 将以数指定年、月、日的日期打印出来
months = [
    'Jan','Feb','Mar','Apr','May','June', \
    'July','Aug','Sep','Oct','Nov','Dec'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
    + ['st', 'nd', 'rd'] + 7 * ['th'] \
    + ['st']

year = input('year:')
month = input('month(1-12):')
day = input('day(1-31):')

month_num = int(month)
day_num = int(day)

month_name = months[month_num-1]
ordinal = day + endings[day_num-1]

print(month_name + ' ' + ordinal + ', ' +year)