#Convert the time entered in hr,min and sec into seconds.
sec = int(input('Enter the sec : '))

# 1 min = 60sec
# 1hr = 60 min
# 1 hr = ? sec
hrs= sec // 3600 # To find the quoient. "/" for finding with points also
sec = sec % 3600 # To find the remainder
min = sec // 60
sec = sec % 60
print(f'Hrs = {hrs},Min = {min},Sec = {sec}')


