import time as t
print(t.localtime())
time_now = t.localtime()

print('transaction completed at ', str(time_now.tm_wday)+'h'+str(time_now.tm_min)+'m')

print('current time stamp',t.time())
print('current time stamp',t.time())
days=['Monday','Tuesday','Wednessday','Thursday','Friday','Sarturday','Sunday']
time_now=t.time()
delivery_time_in_7days = time_now + (86400 *7)
delivery_time = t.localtime(delivery_time_in_7days)
print('in seven day time',t.localtime(delivery_time_in_7days))
t.sleep(5)
print('delivery will be made at ', str(delivery_time.tm_hour)+'h'+str(delivery_time.tm_min)+'m','on',days[delivery_time.tm_wday], 'which is', str(delivery_time.tm_mday)+'days time from now')