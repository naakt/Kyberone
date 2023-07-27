import datetime


now = datetime.datetime.now()
first = (now.minute + 1) * 20
second = (round(now.second / 10) + 1)* 10
print(second)

print(f'{first} ** {second}')
expression = first ** second
print(expression)