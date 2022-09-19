#Lists : A list is an immutable one.it is denoted as[].it is similar array in a java and c..
numbers=[1,2,3,5,7]
print(numbers)
alphabets.insert(6,9)
print(numbers)
numbers.append(3)
print(numbers)
numbers.remove(2)
print(numbers)
#slicing : it is simply nothing but giving the values or alphabets are from a certain range...
numbers=[1,2,3,5,7]
print(numbers)
print(numbers[0:3])
print(numbers[-3:-1])
print(numbers[9:90])
print(numbers[-4:-3])
#tuples : these are muttable ones,In which we cannot insert or update the values of the data..
#these are denoted as ().
Mobiles=['Oppo','Vivo','Mi','Iqoo','Samsung','Apple','Realme']
print(Mobiles) 
#Slicing in tuples..
print(Mobiles[0:3])
print(Mobiles[4:6])
print(Mobiles[-5:-1])
print(Mobiles[-90:-4])
print(Mobiles[-1:0])
#Dictionary:These are immutable ones for some cases and these can be represented as {}...
#these also consists of some values for each data in it
#example:Tesla:100k..
Bikes={'Kawasaki':'10 lakhs','Dugati':'12 lakhs','RE':'5 lakhs','Suzuki':'15 lakhs'}
print(Bikes)
Bikes.update({'Kawasaki':'16 lakhs'})
print(Bikes)
Bikes.update({'Dugati':'14 lakhs'})
print(Bikes)
Bikes.clear()
print(Bikes)
#del Bikes['Kawasaki']
print(Bikes)
#Bikes.pop('Dugati')
print(Bikes)
#slicing in an Dictionary..
Bikes={'Kawasaki':'10 lakhs','Dugati':'12 lakhs','RE':'5 lakhs','Suzuki':'15 lakhs'}
print(Bikes)
keys_for_slicing=["Dugati","Suzuki"]
sliced_Bikes = {key:Bikes[key] for key in keys_for_slicing}
print(Bikes)
keys_for_slicing=["Suzuki"]
sliced_Bikes = {key:Bikes[key] for key in keys_for_slicing} 
print(Bikes)
