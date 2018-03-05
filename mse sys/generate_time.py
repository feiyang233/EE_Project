def getime(date):
	list1=[]
	for hour in range(8):
		for minute in range(0,56,5):
			if minute<10:
				time=str(date)+' 0'+str(hour)+':0'+str(minute)+':01'
			else:
				time=str(date)+' 0'+str(hour)+':'+str(minute)+':01'
			list1.append(time)

	for hour in range(8,24):
		if hour<10:
			for minute in range(0,60):
				if minute<10:
					time=str(date)+' 0'+str(hour)+':0'+str(minute)+':01'
				else:
					time=str(date)+' 0'+str(hour)+':'+str(minute)+':01'
				list1.append(time)
		else:
			for minute in range(0,60):
				if minute<10:
					time=str(date)+' '+str(hour)+':0'+str(minute)+':01'
				else:
					time=str(date)+' '+str(hour)+':'+str(minute)+':01'
				list1.append(time)
	return list1
