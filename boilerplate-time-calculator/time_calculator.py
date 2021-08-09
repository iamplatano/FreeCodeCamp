def add_time(start, duration,startingday = ""):
  starthour = int(start.split(" ")[0].split(":")[0])
  startminutes = int(start.split(" ")[0].split(":")[1])
  durationhour = int(duration.split(":")[0])
  durationminutes = int(duration.split(":")[1])
  ampm = start.split(" ")[1]
  days = 0
  weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  newday=""
  
  newhour = (starthour + durationhour) % 12
  if newhour == 0:
    newhour = 12

  newminutes = (startminutes + durationminutes) % 60
  newhour += (startminutes + durationminutes) // 60
  if((starthour + durationhour) >= 12 and durationhour % 24 != 0)or newhour>=12:
    if ampm == 'PM':
      ampm = 'AM'
      days += 1
    else:
      ampm = 'PM'
      
  days += durationhour // 24
  if(startingday != ""):
    for day in range(len(weekdays)):
      if weekdays[day].lower() == startingday.lower():
        newday=weekdays[(day+days)%len(weekdays)]
    
  if newminutes < 10:
    newminutes = '0'+str(newminutes)
  
  newhour = str(newhour)
  newminutes = str(newminutes)
  new_time = '{0}:{1} {2}'.format(newhour,newminutes,ampm)
  if newday != "":
    new_time += ', %s'%(newday)
  if days == 1:
    new_time += ' (next day)'
  elif days >1:
    new_time += ' (%d days later)'% (days)

  return new_time