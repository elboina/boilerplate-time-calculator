def add_time(start, duration, start_day = ''):
    extra_days = 0
    extra_hours = 0

    start_data = start.split()
    starting_time = start_data[0]
    start_suffix = start_data[1]
    start_time_parts = starting_time.split(':')
    duration_parts = duration.split(':')
    start_hour = start_time_parts[0]
    start_min = start_time_parts[1]

    duration_hour = duration_parts[0]
    duration_minute = duration_parts[1]

    nb_new_minutes = int(start_min) + int(duration_minute)
    minutes_in_an_hour = 60
    if (nb_new_minutes > minutes_in_an_hour):
        extra_hours = nb_new_minutes // minutes_in_an_hour
        nb_new_minutes = nb_new_minutes % minutes_in_an_hour

    new_hour = int(start_hour) + int(duration_hour) + extra_hours
    new_suffix = start_suffix

    if new_hour >= 12:
        nb_clock_turns = new_hour // 12
        if nb_clock_turns > 1:
            extra_days = new_hour // 24
        if nb_clock_turns % 2 == 1:
            if start_suffix == 'PM':
                extra_days += 1
            new_suffix = toggle_time_suffix(start_suffix)
        new_hour = new_hour % 12 if new_hour % 12 > 0 else 12
    
    new_time = str(new_hour) + ':' + ('0' if nb_new_minutes < 10 else '') + str(nb_new_minutes) + ' ' + new_suffix


    if len(start_day) > 0: 
       new_day = add_days(start_day, extra_days)
       new_time += ', ' + new_day

    if extra_days == 1:
        new_time += ' (next day)'
    elif extra_days > 0:
        new_time += ' (' + str(extra_days) + ' days later)'
    return new_time

def add_days(starting_day: str, nb_added_days: int) -> str:
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index_starting_day = weekdays.index(starting_day.capitalize())
    num_day = index_starting_day + nb_added_days
    nb_weekdays = len(weekdays)
    index_result = num_day if num_day < nb_weekdays else num_day % nb_weekdays
    return weekdays[index_result]  

def toggle_time_suffix(suffix: 'AM' or 'PM') -> 'AM' or 'PM':
    if suffix == 'AM':
        return 'PM'
    return 'AM'