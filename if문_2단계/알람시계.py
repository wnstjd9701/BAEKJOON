# 백준 2884번 문제 - 알람시계
hour, minute =map(int, input().split())

if minute<45:
    if hour==0:
        hour = 24
    hour = hour-1
    minute = minute + 15
else:
    minute = minute - 45
print(hour, minute) 