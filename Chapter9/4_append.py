st = "Hii my name is anushka"
 
f = open("myfile.txt","a")   # appen() - Each time the program is executed, a line will be added to the myfile.txt

f.write(st)

f.close()