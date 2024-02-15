#/usr/bin/python3
"""
progress bar
"""
data_set = range(1, 30)         #29
data_set_length = len(data_set) #29
bar_length = 10                 #10
for loop_index, _ in enumerate(data_set): 
    #print(f'{loop_index} ===> {_}')   #0 ===> 1 to 28 ==> 29
    percent_completed = (loop_index / data_set_length) * 100  # 4/29*100 = 13.793103448275861
    percent_completed = round(percent_completed, 2) #13.73
    progress_chars = int(percent_completed / (100 / bar_length)) # 13.73/ 100/10 = 13.73/10 =1.37 = 1
    bar = '[' + '*' * progress_chars + ' ' * (bar_length - progress_chars) + ']'  #* + '   '
    print(f"\r{bar} {percent_completed:3}% completed", end="")