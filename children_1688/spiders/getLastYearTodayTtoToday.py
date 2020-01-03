# 返回　去年昨日到昨日　的所有日期　
import datetime
import time

from children_1688.spiders.date_All_Year import getAllDayPerYear


def getDataList():
    year = time.strftime('%y', time.localtime(time.time()))
    month = time.strftime('%m', time.localtime(time.time()))
    day = int(time.strftime('%d', time.localtime(time.time()))) - 1

    # 获取去年昨日的日期 添加20原因：结果会显示为18-1-1 没有20
    last_Year_Today = '20{}-{}-{}'.format(int(year) - 1, month, day)
    # 获取今日的日期
    today = '20{}-{}-{}'.format(year, month, int(day) + 1)

    # 获取今年
    year = '20{}'.format(year)

    lastYear = getAllDayPerYear(int(year) - 1)
    # 获取2019年全年的日期
    todayYear = getAllDayPerYear(year)

    list_2018 = []
    list_2019 = []

    # 在2018年全年list列表里匹配，当大于去年昨日日期，则添加进新数组
    for x in range(0, len(lastYear)):
        if datetime.datetime.strptime(lastYear[x], '%Y-%m-%d') >= datetime.datetime.strptime(last_Year_Today,
                                                                                             '%Y-%m-%d'):
            list_2018.append(lastYear[x])
    # 在2019年全年list列表里匹配，当今日日期大于列表元素时，添加进新数组
    for y in range(0, len(todayYear)):
        if datetime.datetime.strptime(today, '%Y-%m-%d') >= datetime.datetime.strptime(todayYear[y], '%Y-%m-%d'):
            list_2019.append(todayYear[y])
    # 去年昨日到今日的所有日期
    list_Count = list_2018 + list_2019
    return list_Count