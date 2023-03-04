import time

res = ''
timestamp = time.time()

year = timestamp / (365 * 24 * 60 * 60)
res += str(int(year) + 1970) + '-'
v = 0

for i in range(1970, int(year) + 1970):
    if i % 4 == 0:
        v += 1

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = (year - int(year)) * 365 - v + 1
month = '00'

for i in range(len(months)):
    if days < months[i]:
        month = str(i + 1)
        break
    days -= months[i]

m = len(month)
if m < 2:
    month = '0' + month
res += month + '-'
dl = len(str(int(days)))
d = str(int(days))

if dl < 2:
    res += '0' + d + ' '
else:
    res += d + ' '

hours = (days - int(days)) * 24
hl = len(str(int(hours + 4)))
h = str(int(hours + 4))
if hl < 2:
    res += '0' + h + ':'
else:
    res += h + ':'

minutes = (hours - int(hours)) * 60
ml = len(str(int(minutes)))
m = str(int(minutes))
if ml < 2:
    res += '0' + m + ':'
else:
    res += m + ':'

seconds = (minutes - int(minutes)) * 60
sl = len(str(int(seconds)))
s = str(int(seconds))
if sl < 2:
    res += '0' + s
else:
    res += s

print(res)
#print(time.time())
