input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
c1 = int(data[0])
c2 = int(data[1]) 
c3 = int(data[2])
sum = int(c1*(c2**c3-1)/(c2-1))
output_data = open("output.txt","w")
data = output_data.write(str(sum))
input_data.close()
output_data.close()
