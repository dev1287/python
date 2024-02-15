data_set = range(1, 30)         
data_set_length = len(data_set) 
bar_length = 10                 
for loop_index, _ in enumerate(data_set):    
    percent_completed = (loop_index / data_set_length) * 100  
    percent_completed = round(percent_completed, 2) 
    progress_chars = int(percent_completed / (100 / bar_length)) 
    bar = '[' + '*' * progress_chars + ' ' * (bar_length - progress_chars) + ']'  
    print(f"\r{bar} {percent_completed:3}% completed", end="")