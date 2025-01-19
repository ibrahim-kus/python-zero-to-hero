messageOriginal = "Hello There. My name is ibrahim Kuş"
message = " Hello There. My name is ibrahim Kuş"

message = message.upper() # lower # title # capitalize # 

print(message)

message2 = message.strip() # Boşluk sil. #split 
print(message2)

message2 = message2.split() # split('.')
print(message2)

message3 = ' '.join(message2)
print(message3)

index = messageOriginal.find('ibrahim')
print(index)

isStartWithH = messageOriginal.startswith('H')
print(isStartWithH)

message = message.replace(' ','*').replace('Ş','S')  #center #ljust #rjust
print(message)

course = "herotozero" 
result = course.isalpha()  # isdigit
print(result)
print(course.center(50))
print(course.center(50,'*'))
