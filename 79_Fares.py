source={"Vancouver":1, "Toronto": 2, "Edmonton" : 3, "Calgary": 4, "Montreal" : 5, "Halifax" : 6, "Thunder Bay" : 7, "Winnipeg": 8, "St.John": 9, "Niagra": 10}
x= int(input("Please choose the source. Type 1 for Vancouver, 2 for Toronto, 3 for Edmonton, 4 for Calgary, 5 for Montreal, 6 for Halifax, 7 for Thunder Bay, 8 for Winnipeg, 9 for St.John, and 10 for Niagra: "))
fareflight=60
faretrain=45
farebus=20
def service():
	service= int(input("Please choose your method of travelling. Type 1 for Plane, 2 for train and 3 for bus: "))
	if service==1:
		price=u*fareflight
		name=input("Please enter your name: ")
		phone=input("Please enter your phone: ")
		print("Your total fare is: ", price)
		print("Thank you for booking with us!")
	elif service==2:
		price=u*faretrain
		name=input("Please enter your name: ")
		phone=input("Please enter your phone: ")
		print("Your total fare is: ", price)
		print("Thank you for booking with us!")
	elif service==3:
		price=u*farebus
		name=input("Please enter your name: ")
		phone=input("Please enter your phone: ")
		print("Your total fare is: ", price)
		print("Thank you for booking with us!")
if x==1:
	dest={"Toronto": 10, "Edmonton" : 11, "Calgary": 12, "Montreal" : 13, "Halifax" : 14, "Thunder Bay" : 15, "Winnipeg": 16, "St.John": 17, "Niagra": 18}
	dis={"Vancouver to Toronto":2000, "Vancouver to Edmonton":800, "Vancouver to Calgary":600, "Vancouver to Montreal": 2200,  "Vancouver to Halifax": 3000, "Vancouver to Thunder Bay": 1800, "Vancouver to Winnipeg": 1200, "Vancouver to St.John": 3200, "Vancouver to Niagra": 1943  }
	z= int(input("Please choose the destination.10 for Toronto, 11 for Edmonton, 12 for Calgary, 13 for Montreal, 14 for Halifax, 15 for Thunder Bay, 16 for Winnipeg, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis["Vancouver to Toronto"]
		service()
	elif z==11:
		u=dis["Vancouver to Edmonton"]
		service()
	elif z==12:
		u=dis["Vancouver to Calgary"]
		service()
	elif z==13:
		u=dis["Vancouver to Montreal"]
		service()
	elif z==14:
		u=dis["Vancouver to Halifax"]
		service()
	elif z==15:
		u=dis["Vancouver to Thunder Bay"]
		service()
	elif z==16:
		u=dis["Vancouver to Winnipeg"]
		service()
	elif z==17:
		u=dis["Vancouver to St.John"]
		service()
	elif z==18:
		u=dis["Vancouver to Niagra"]
		service()
elif x==2:
	dest={"Vancouver": 10, "Edmonton" : 11, "Calgary": 12, "Montreal" : 13, "Halifax" : 14, "Thunder Bay" : 15, "Winnipeg": 16, "St.John": 17, "Niagra": 18}
	dis2={"Toronto to Vancouver":2001, "Toronto to Edmonton":1802, "Toronto to Calgary":1620, "Toronto to Montreal": 650,  "Toronto to Halifax": 1234, "Toronto to Thunder Bay": 234, "Toronto to Winnipeg": 455, "Toronto to St.John": 1397, "Toronto to Niagra": 96  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Edmonton, 12 for Calgary, 13 for Montreal, 14 for Halifax, 15 for Thunder Bay, 16 for Winnipeg, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis2["Toronto to Vancouver"]
		service()
	elif z==11:
		u=dis2["Toronto to Edmonton"]
		service()
	elif z==12:
		u=dis2["Toronto to Calgary"]
		service()
	elif z==13:
		u=dis2["Toronto to Montreal"]
		service()
	elif z==14:
		u=dis2["Toronto to Halifax"]
		service()
	elif z==15:
		u=dis2["Toronto to Thunder Bay"]
		service()
	elif z==16:
		u=dis2["Toronto to Winnipeg"]
		service()
	elif z==17:
		u=dis2["Toronto to St.John"]
		service()
	elif z==18:
		u=dis2["Toronto to Niagra"]
		service()
elif x==3:
	dest={"Vancouver": 10, "Toronto" : 11, "Calgary": 12, "Montreal" : 13, "Halifax" : 14, "Thunder Bay" : 15, "Winnipeg": 16, "St.John": 17, "Niagra": 18}
	dis3={"Edmonton to Vancouver":245, "Edmonton to Toronto":1553, "Edmonton to Calgary":234, "Edmonton to Montreal": 1965,  "Edmonton to Halifax": 1234, "Edmonton to Thunder Bay": 1432, "Edmonton to Winnipeg": 800, "Edmonton to St.John": 2490, "Edmonton to Niagra": 1449  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Calgary, 13 for Montreal, 14 for Halifax, 15 for Thunder Bay, 16 for Winnipeg, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis3["Edmonton to Vancouver"]
		service()
	elif z==11:
		u=dis3["Edmonton to Toronto"]
		service()
	elif z==12:
		u=dis3["Edmonton to Calgary"]
		service()
	elif z==13:
		u=dis3["Edmonton to Montreal"]
		service()
	elif z==14:
		u=dis3["Edmonton to Halifax"]
		service()
	elif z==15:
		u=dis3["Edmonton to Thunder Bay"]
		service()
	elif z==16:
		u=dis3["Edmonton to Winnipeg"]
		service()
	elif z==17:
		u=dis3["Edmonton to St.John"]
		service()
	elif z==18:
		u=dis3["Edmonton to Niagra"]
		service()
elif x==4:
	dest={"Vancouver": 10, "Toronto" : 11, "Edmonton": 12, "Montreal" : 13, "Halifax" : 14, "Thunder Bay" : 15, "Winnipeg": 16, "St.John": 17, "Niagra": 18}
	dis4={"Calgary to Vancouver":245, "Calgary to Toronto":1668, "Calgary to Edmonton":234, "Calgary to Montreal": 1965,  "Calgary to Halifax": 2340, "Calgary to Thunder Bay": 2900, "Calgary to Winnipeg": 980, "Calgary to St.John": 3200, "Calgary to Niagra": 2400  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Edmonton, 13 for Montreal, 14 for Halifax, 15 for Thunder Bay, 16 for Winnipeg, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis4["Calgary to Vancouver"]
		service()
	elif z==11:
		u=dis4["Calgary to Toronto"]
		service()
	elif z==12:
		u=dis4["Calgary to Edmonton"]
		service()
	elif z==13:
		u=dis4["Calgary to Montreal"]
		service()
	elif z==14:
		u=dis4["Calgary to Halifax"]
		service()
	elif z==15:
		u=dis4["Calgary to Thunder Bay"]
		service()
	elif z==16:
		u=dis4["Calgary to Winnipeg"]
		service()
	elif z==17:
		u=dis4["Calgary to St.John"]
		service()
	elif z==18:
		u=dis4["Calgary to Niagra"]
		service()
elif x==5:
	dest={"Vancouver": 10, "Toronto" : 11, "Calgary": 12, "Edmonton" : 13, "Halifax" : 14, "Thunder Bay" : 15, "Winnipeg": 16, "St.John": 17, "Niagra": 18}
	dis5={"Montreal to Vancouver":3800, "Montreal to Toronto":800, "Montreal to Calgary":2400, "Montreal to Edmonton": 2600,  "Montreal to Halifax": 890, "Montreal to Thunder Bay": 900, "Montreal to Winnipeg": 1760, "Montreal to St.John": 500, "Montreal to Niagra": 800  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Calgary, 13 for Edmonton, 14 for Halifax, 15 for Thunder Bay, 16 for Winnipeg, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis5["Montreal to Vancouver"]
		service()
	elif z==11:
		u=dis5["Montreal to Toronto"]
		service()
	elif z==12:
		u=dis5["Montreal to Calgary"]
		service()
	elif z==13:
		u=dis5["Montreal to Edmonton"]
		service()
	elif z==14:
		u=dis5["Montreal to Halifax"]
		service()
	elif z==15:
		u=dis5["Montreal to Thunder Bay"]
		service()
	elif z==16:
		u=dis5["Montreal to Winnipeg"]
		service()
	elif z==17:
		u=dis5["Montreal to St.John"]
		service()
	elif z==18:
		u=dis5["Montreal to Niagra"]
		service()
elif x==6:
	dest={"Vancouver": 10, "Toronto" : 11, "Calgary": 12, "Edmonton" : 13, "Montreal" : 14, "Thunder Bay" : 15, "Winnipeg": 16, "St.John": 17, "Niagra": 18}
	dis6={"Halifax to Vancouver":4000, "Halifax to Toronto":1900, "Halifax to Calgary":2900, "Halifax to Edmonton": 2800,  "Halifax to Montreal": 890, "Halifax to Thunder Bay": 1882, "Halifax to Winnipeg": 1760, "Halifax to St.John": 500, "Halifax to Niagra": 1890  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Calgary, 13 for Edmonton, 14 for Montreal, 15 for Thunder Bay, 16 for Winnipeg, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis6["Halifax to Vancouver"]
		service()
	elif z==11:
		u=dis6["Halifax to Toronto"]
		service()
	elif z==12:
		u=dis6["Halifax to Calgary"]
		service()
	elif z==13:
		u=dis6["Halifax to Edmonton"]
		service()
	elif z==14:
		u=dis6["Halifax to Montreal"]
		service()
	elif z==15:
		u=dis6["Halifax to Thunder Bay"]
		service()
	elif z==16:
		u=dis6["Halifax to Winnipeg"]
		service()
	elif z==17:
		u=dis6["Halifax to St.John"]
		service()
	elif z==18:
		u=dis6["Halifax to Niagra"]
		service()
elif x==7:
	dest={"Vancouver": 10, "Toronto" : 11, "Calgary": 12, "Edmonton" : 13, "Montreal" : 14, "Halifax" : 15, "Winnipeg": 16, "St.John": 17, "Niagra": 18}
	dis7={"Thunder Bay to Vancouver":3200, "Thunder Bay to Toronto": 520, "Thunder Bay to Calgary":2100, "Thunder Bay to Edmonton": 2000,  "Thunder Bay to Montreal": 1000, "Thunder Bay to Halifax": 1400 , "Thunder Bay to Winnipeg": 400, "Thunder Bay to St.John": 1190, "Thunder Bay to Niagra": 560  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Calgary, 13 for Edmonton, 14 for Montreal, 15 for Halifax, 16 for Winnipeg, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis7["Thunder Bay to Vancouver"]
		service()
	elif z==11:
		u=dis7["Thunder Bay to Toronto"]
		service()
	elif z==12:
		u=dis7["Thunder Bay to Calgary"]
		service()
	elif z==13:
		u=dis7["Thunder Bay to Edmonton"]
		service()
	elif z==14:
		u=dis7["Thunder Bay to Montreal"]
		service()
	elif z==15:
		u=dis7["Thunder Bay to Thunder Bay"]
		service()
	elif z==16:
		u=dis7["Thunder Bay to Winnipeg"]
		service()
	elif z==17:
		u=dis7["Thunder Bay to St.John"]
		service()
	elif z==18:
		u=dis7["Thunder Bay to Niagra"]
		service()
elif x==8:
	dest={"Vancouver": 10, "Toronto" : 11, "Calgary": 12, "Edmonton" : 13, "Montreal" : 14, "Halifax" : 15, "Thunder Bay": 16, "St.John": 17, "Niagra": 18}
	dis8={"Winnipeg to Vancouver":800, "Winnipeg to Toronto": 1802, "Winnipeg to Calgary":200, "Winnipeg to Edmonton": 800,  "Winnipeg to Montreal": 1230, "Winnipeg to Halifax": 2100 , "Winnipeg to Thunder Bay": 400, "Winnipeg to St.John": 2000, "Winnipeg to Niagra": 1200  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Calgary, 13 for Edmonton, 14 for Montreal, 15 for Halifax, 16 for Thunder Bay, 17 for St.John, and 18 for Niagra: "))
	if z==10:
		u=dis8["Halifax to Vancouver"]
		service()
	elif z==11:
		u=dis8["Winnipeg to Edmonton"]
		service()
	elif z==12:
		u=dis8["Winnipeg to Calgary"]
		service()
	elif z==13:
		u=dis8["Winnipeg to Montreal"]
		service()
	elif z==14:
		u=dis8["Winnipeg to Montreal"]
		service()
	elif z==15:
		u=dis8["Winnipeg to Thunder Bay"]
		service()
	elif z==16:
		u=dis8["Winnipeg to Halifax"]
		service()
	elif z==17:
		u=dis8["Winnipeg to St.John"]
		service()
	elif z==18:
		u=dis8["Winnipeg to Niagra"]
		service()
elif x==9:
	dest={"Vancouver": 10, "Toronto" : 11, "Calgary": 12, "Edmonton" : 13, "Montreal" : 14, "Halifax" : 15, "Thunder Bay": 16, "Winnipeg": 17, "Niagra": 18}
	dis9={"St.John to Vancouver":3200, "St.John to Toronto": 1000, "St.John to Calgary":2400, "St.John to Edmonton": 2300,  "St.John to Montreal": 560, "St.John to Halifax": 250 , "St.John to Thunder Bay": 1650, "St.John to Winnipeg": 2000, "St.John to Niagra": 1200  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Calgary, 13 for Edmonton, 14 for Montreal, 15 for Halifax, 16 for Thunder Bay, 17 for Winnipeg, and 18 for Niagra: "))
	if z==10:
		u=dis9["St.John to Vancouver"]
		service()
	elif z==11:
		u=dis9["St.John to Toronto"]
		service()
	elif z==12:
		u=dis9["St.John to Calgary"]
		service()
	elif z==13:
		u=dis9["St.John to Edmonton"]
		service()
	elif z==14:
		u=dis9["St.John to Montreal"]
		service()
	elif z==15:
		u=dis9["St.John to Thunder Bay"]
		service()
	elif z==16:
		u=dis9["St.John to Halifax"]
		service()
	elif z==17:
		u=dis9["St.John to Winnipeg"]
		service()
	elif z==18:
		u=dis9["St.John to Niagra"]
		service()
elif x==10:
	dest={"Vancouver": 10, "Toronto" : 11, "Calgary": 12, "Edmonton" : 13, "Montreal" : 14, "Halifax" : 15, "Thunder Bay": 16, "Winnipeg": 17, "St.John": 18}
	dis10={"Niagra to Vancouver":3000, "Niagra to Toronto": 150, "Niagra to Calgary":2500, "Niagra to Edmonton": 2400,  "Niagra to Montreal": 600, "Niagra to Halifax": 1450 , "Niagra to Thunder Bay": 650, "Niagra to Winnipeg": 800, "Niagra to St.John": 1200  }
	z= int(input("Please choose the destination.10 for Vancouver, 11 for Toronto, 12 for Calgary, 13 for Edmonton, 14 for Montreal, 15 for Halifax, 16 for Thunder Bay, 17 for Winnipeg, and 18 for St.John: "))
	if z==10:
		u=dis10["Niagra to Vancouver"]
		service()
	elif z==11:
		u=dis10["Niagra to Toronto"]
		service()
	elif z==12:
		u=dis10["Niagra to Calgary"]
		service()
	elif z==13:
		u=dis10["Niagra to Edmonton"]
		service()
	elif z==14:
		u=dis10["Niagra to Montreal"]
		service()
	elif z==15:
		u=dis10["Niagra to Thunder Bay"]
		service()
	elif z==16:
		u=dis10["Niagra to Halifax"]
		service()
	elif z==17:
		u=dis10["Niagra to Winnipeg"]
		service()
	elif z==18:
		u=dis10["Niagra to St.John"]
		service()







