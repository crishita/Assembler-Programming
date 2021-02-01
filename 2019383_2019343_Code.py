"""COMPUTER ORGANISATION PROJECT 1
   NAME:Rishita chauhan(2019383);Vasu Kashyap(2019343)"""

def assembly(assemblycode):   #put the name of the file containing the assembly code in the form of string as parameter.File should be saved on the desktop.
    passone(assemblycode)
    passtwo()


class symtab():
	symtable=[]
	def __init__(self,symbol,typ,address=-1): 
		self.symbol=symbol
		self.typ=typ
		self.address=address
		if typ=="label":
			assert len(symbol)>1,"label should contain more than one character"
		else:
			assert len(symbol)==1,"variable should contain only one character"

	def insertelement(self):
		self.symtable.append([self.symbol,self.typ,self.address])

class littab():
	littable=[]
	def __init__(self,value,address=-1): 
		self.value=value
		self.address=address

	def insertelement(self):
		self.littable.append([self.value,self.address])

class registers():
	regtab=[["R1","11111100"],["R2","11111101"],["R3","11111110"],["R4","11111111"]]

class legalopcodes():
	legop=["START","END","DC","DS","CLA","LAC","SAC","ADD","SUB","MUL","DIV","BRP","BRZ","BRN","INP","DSP","STP"]

class operandopcodes():
	operandop=["LAC","SAC","ADD","SUB","MUL","DIV","BRP","BRZ","BRN","INP","DSP","DC","DS"]



def passone(inputfile):
    file1=open("C:\\Users\\satpal singh\\Desktop\\"+inputfile+".txt","r")
    file2=open("C:\\Users\\satpal singh\\Desktop\\intermediate.txt","w")
    file3=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
    file4=open("C:\\Users\\satpal singh\\Desktop\\ADtab.txt","r")
    file5=open("C:\\Users\\satpal singh\\Desktop\\DLtab.txt","r")
    LC=0
    firstline=file1.readline()
    list1=firstline.split()
    if "START" in list1:
    	if list1.index("START")==(len(list1)-1):
    		LC=0
    		file2.write("(AD,1)(LC,0)\n")
    	else:
    		LC=int(list1[list1.index("START")+1])
    		file2.write("(AD,1)(LC,"+list1[list1.index("START")+1]+")\n")
    else:
    	raise Exception("No START statement")
    line=file1.readline()
    while(line!=""):
    	list2=line.split()
    	if LC>=252:
    		raise Exception("Readjust the start value")
    	if len(list2)==3:
    		if list2[0] in legalopcodes.legop:
    			raise Exception("opcode is supplied with too many operands")
    		if not list2[1] in legalopcodes.legop:
    			raise Exception("opcode not supported by the assembler(illegal opcode)")
    		if not list2[1] in operandopcodes.operandop:
    			raise Exception("opcode is supplied with too many operands")
    		if(list2[1]!="DS" and list2[1]!="DC"):
    			a=symtab(list2[0],"label",LC)
    			if not [list2[0],"label",-1] in a.symtable:
    				a.insertelement()
    			else:
    				a.symtable[(a.symtable.index([list2[0],"label",-1]))][2]=LC
    			file3.close()
    			file3=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
    			x=file3.readline()
    			while(x!=""):
    				array=x.split()
    				if(len(array)!=0 and array[1]==list2[1]):
    					file2.write(str(LC)+")("+array[2]+","+array[0]+")")
    					LC+=1
    				x=file3.readline()
    			if len(list2[2])==1:
    				b=symtab(list2[2],"variable")
    				if not [list2[2],"variable",-1] in b.symtable:
    					b.insertelement()
    					file2.write("(S,"+str(len(b.symtable)-1)+")\n")
    				else:
    					eu=symtab.symtable.index([list2[2],"variable",-1])
    					file2.write("(S,"+str(eu)+")\n")
    			elif list2[2][0]=="=":
    				c=littab(list2[2])
    				c.insertelement()
    				file2.write("(L,"+str(len(c.littable)-1)+")\n")
    			elif list2[2] in ["R1","R2","R3","R4"]:
    				file2.write("("+list2[2]+")\n")
    			else:
    				d=symtab(list2[2],"label")
    				l=True
    				for z in symtab.symtable:
    					if(z[0]==list2[2]):
    						l=False
    						break
    				if l:
    					d.insertelement()
    					file2.write("(S,"+str(len(d.symtable)-1)+")\n")
    				else:
    					file2.write("(S,"+str(symtab.symtable.index(z))+")\n")


    		elif(list2[1]=="DS" or list2[1]=="DC"):
    			for e in symtab.symtable:
    				if LC>=252:
    					raise Exception("Readjust the start value")
    				if(e[0]==list2[0]  and e[1]=="variable"):
    					e[2]=LC
    					LC+=1
    	if len(list2)==2 and list2[0]!="START" and list2[1]!="START":
    		if ((not(list2[0] in legalopcodes.legop)) and (not(list2[1] in legalopcodes.legop))):
    			raise Exception("opcode not supported by the assembler(illegal opcode)")
    		elif (list2[1]=="DS" or list2[1]=="DC"):
    			raise Exception("Symbol value is missing")
    		elif list2[0] in legalopcodes.legop:
    			if not list2[0] in operandopcodes.operandop:
    				raise Exception("opcode supplied with too many operands")
    			file3.close()
    			file3=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
    			x=file3.readline()
    			while(x!=""):
    				array=x.split()
    				if(len(array)!=0 and array[1]==list2[0]):
    					file2.write(str(LC)+")("+array[2]+","+array[0]+")")
    					LC+=1
    				x=file3.readline()
    			if len(list2[1])==1:
    				b=symtab(list2[1],"variable")
    				if not [list2[1],"variable",-1] in b.symtable:
    					b.insertelement()
    					file2.write("(S,"+str(len(b.symtable)-1)+")\n")
    				else:
    					eu=symtab.symtable.index([list2[1],"variable",-1])
    					file2.write("(S,"+str(eu)+")\n")
    			elif list2[1][0]=="=":
    				c=littab(list2[1])
    				c.insertelement()
    				file2.write("(L,"+str(len(c.littable)-1)+")\n")
    			elif list2[1] in ["R1","R2","R3","R4"]:
    				file2.write("("+list2[1]+")\n")
    			else:
    				d=symtab(list2[1],"label")
    				l=True
    				for z in symtab.symtable:
    					if(z[0]==list2[1]):
    						l=False
    						break
    				if l:
    					d.insertelement()
    					file2.write("(S,"+str(len(d.symtable)-1)+")\n")
    				else:
    					file2.write("(S,"+str(symtab.symtable.index(z))+")\n")
    		elif list2[1] in legalopcodes.legop:
    			if list2[1] in operandopcodes.operandop:
    				raise Exception("not enough operands to support the operation")
    			else:
    				a=symtab(list2[0],"label",LC)
    				if not [list2[0],"label",-1] in a.symtable:
    					a.insertelement()
    				else:
    					a.symtable[(a.symtable.index([list2[0],"label",-1]))][2]=LC
    				file3.close()
    				file3=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
    				x=file3.readline()
    				while(x!=""):
    					array=x.split()
    					if(len(array)!=0 and array[1]==list2[1]):
    						file2.write(str(LC)+")("+array[2]+","+array[0]+")\n")
    						LC+=1
    					x=file3.readline()





    	if len(list2)==1 and list2[0]!="END" and list2[0]!="START":
    		if not list2[0] in legalopcodes.legop:
    			raise Exception("opcode not supported by the assembler(illegal opcode)")
    		else:
    			file3.close()
    			file3=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
    			x=file3.readline()
    			while(x!=""):
    				array=x.split()
    				if(len(array)!=0 and array[1]==list2[0]):
    					if(array[1] in operandopcodes.operandop):
    						raise Exception("not enough operands to support the operation")
    					else:
    						file2.write(str(LC)+")("+array[2]+","+array[0]+")\n")
    						LC+=1
    				x=file3.readline()
    	if len(list2)>3:
    		raise Exception("opcode is supplied with too many operands")
    	line=file1.readline()
    file1.close()
    file1=open("C:\\Users\\satpal singh\\Desktop\\"+inputfile+".txt","r")
    w=file1.readlines()
    q=w[-1].split()
    if(q[0]!="END"):
    	raise Exception("END statement not present")
    else:
    	file1.close()
    	file3.close()
    	file4.close()
    	file5.close()
    	file2.close()
    	file11=open("C:\\Users\\satpal singh\\Desktop\\Symboltable.txt","w")
    	file12=open("C:\\Users\\satpal singh\\Desktop\\Literaltable.txt","w")
    	for i in symtab.symtable:
    		if LC>=252:
    			raise Exception("Readjust the start value")
    		if i[2]==-1 and i[1]=="variable":
    			i[2]=LC
    			LC+=1
    		elif i[2]==-1 and i[1]=="label":
    			raise Exception("symbol used but not defined")
    		if i[1]=="variable":
    			file11.write(str(symtab.symtable.index(i))+"	"+i[0]+"	"+i[1]+"	"+str(i[2])+"\n")
    		else:
    			file11.write(str(symtab.symtable.index(i))+"	"+i[0]+"	"+i[1]+"		"+str(i[2])+"\n")
    	for j in littab.littable:
    		if LC>=252:
    			raise Exception("Readjust the start value")
    		if j[1]==-1:
    			j[1]=LC
    			LC+=1
    		file12.write(str(littab.littable.index(j))+"	"+j[0]+"	"+str(j[1])+"\n")
    	file11.close()
    	file12.close()










def passtwo():
	file=open("C:\\Users\\satpal singh\\Desktop\\intermediate.txt","r")
	file6=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
	file10=open("C:\\Users\\satpal singh\\Desktop\\output.txt","w")
	firstline=file.readline()
	line=file.readline()
	while(line!=""):
		o=line.strip()
		w=o.split(")")
		if len(w)==3:
			a=w[0]
			d=bin(int(a))
			d=d[2:]
			g=len(d)
			while(g<8):
				d="0"+d
				g=g+1
			file10.write(d+" ")
			b=w[1]
			l=b.find(",")
			n=b[l+1:]
			file6.close()
			file6=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
			line1=file6.readline()
			while(line1!=""):
				array=line1.split()
				if len(array)!=0 and array[0]==n:
					file10.write(array[3]+"\n")
				line1=file6.readline()
		elif len(w)==4:
			a=w[0]
			d=bin(int(a))
			d=d[2:]
			g=len(d)
			while(g<8):
				d="0"+d
				g=g+1
			file10.write(d+" ")
			b=w[1]
			l=b.find(",")
			n=b[l+1:]
			file6.close()
			file6=open("C:\\Users\\satpal singh\\Desktop\\optab.txt","r")
			line1=file6.readline()
			while( line1!=""):
				array=line1.split()
				if len(array)!=0 and array[0]==n:
					file10.write(array[3]+" ")
				line1=file6.readline()
			c=w[2]
			if c[1]=="S":
				p=int(c[3])
				u=symtab.symtable[p][2]
				d=bin(u)
				d=d[2:]
				g=len(d)
				while(g<8):
					d="0"+d
					g=g+1
				file10.write(d+"\n")
			elif c[1]=="L":
				p=int(c[3])
				u=littab.littable[p][1]
				d=bin(u)
				d=d[2:]
				g=len(d)
				while(g<8):
					d="0"+d
					g=g+1
				file10.write(d+"\n")
			else:
				p=c[1:]
				for e in registers.regtab:
					if e[0]==p:
						file10.write(e[1]+"\n")
		line=file.readline()
	file.close()
	file6.close()
	file10.close()











def main():
	a=input("Enter the name of input text file:")
	assembly(a)




if __name__ == '__main__':
	main()

