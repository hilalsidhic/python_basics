import datetime
now=datetime.datetime.now()
# print(now.strftime("%d/%m/%y"))
print(("now:"+str(now)))
print(datetime.date.today().month)

x=datetime.datetime(2021,10,28)
y=datetime.datetime(2020,8,29)
print(x-y)
print(x)

end=datetime.datetime.now()
diff=end-now

print(diff)