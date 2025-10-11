def add_time(start, duration, startDay = ''):
    sHour, sMinutePM = start.split(':')
    sMinute, AP = sMinutePM.split(' ')
    dHour,dMinute = duration.split(':')

    #convert to integers
    sHour = int(sHour)
    sMinute = int(sMinute)
    dHour = int(dHour)
    dMinute = int(dMinute)

    #convert to 24 hours
    if AP == 'PM':
        sHour += 12


    #add minutes
    new_min = sMinute + dMinute
    
    #case: next hour
    if new_min >= 60:
        new_min = new_min%60
        sHour += 1

    #add hour
    new_hour = sHour+dHour

    #new day
    n = 0
    if new_hour >= 24:
        n = new_hour//24
        new_hour = new_hour%24

    #AMPM 
    if new_hour <=11:
        newAP = 'AM'
        
    else:
        newAP = 'PM'
        new_hour -= 12


    #days later
    if n == 1:
        daysLater = '(next day)'
    elif n == 0:
        daysLater = None
    else:
        daysLater = f'({n} days later)'

#case:single digit minute
    if new_min <= 10:
        new_min = '0' +str(new_min)

#case: 12am
    if new_hour == 0:
        new_hour = 12


#convert back to strings
    new_hour = str(new_hour)
    new_min = str(new_min)
    if startDay == '':

        if daysLater == None:
            new_time = f'{new_hour}:{new_min} {newAP}'
        else:
            new_time = f'{new_hour}:{new_min} {newAP} '+ daysLater
        
        return new_time

    #non empty startDay variable
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    newDays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    newDay = newDays[(days.index(startDay.lower())+n)%7]
    
    if daysLater == None:
        new_time = f'{new_hour}:{new_min} {newAP}, {newDay}'
    else:
        new_time = f'{new_hour}:{new_min} {newAP}, {newDay} '+ daysLater
    print(new_time)
    return new_time
