def ver_hist():

	import matplotlib.pylab as plt
	import numpy as np

	x = [1,2,3,4,5,6,7,8,9]
	xlabels = ["H","B","E","G","I","T","S","U","NF"]
	y = [4265,536,3632,587,3,1765,1478,4694,196]

	plt.bar(x,y)
	plt.xticks(x,xlabels)
	plt.show()

def hor_hist():

	import matplotlib.pylab as plt
	import numpy as np

	from matplotlib import rc

	import sys

	plt.rcdefaults()
	fig, ax = plt.subplots()

	f = open("{}".format(sys.argv[1]),"r")
	ft = f.readlines()
	f.close()

	if len(ft) == 0:
		print("ERROR IN THE INPUT FILE {}".format(sys.argv[1]))
		quit()
	
	ft1 = ft[0].split()

	print(ft1)

	print("ENTER THE COLUMN FOR X AXIS")
	xcol = input()
	xcol = xcol - 1

	xtest = "{}".format(ft1[int(xcol)]).isdigit()
	if xtest != "True":
		cc = "x"

	print("ENTER THE COLUMN FOR Y AXIS")
	ycol = input()
	ycol = ycol - 1

	ytest = "{}".format(ft1[int(ycol)]).isdigit()
	if ytest != "True":
		cc = "y"

	if "{}".format(xtest) != "True" and "{}".format(ytest) != "True":
		print("ERROR: BOTH COLUMNS ARE CHARACTER TYPES")
		quit()

	print(cc)
	k=0
	x = []
	y = []	
	xlabel = []
	ylabel = []
	while k < len(ft):
		ft1 = ft[k].split()
		t1 = ft1[int(xcol)]
		t2 = ft1[int(ycol)]	
		if cc == "x":
			xlabel.append(t1)
			x.append((k+1))
			y.append(int(t2))
		if cc == "y":
			x.append(int(t1))
			ylabel.append(t2)
			y.append((k+1))
		k = k + 1
	
	ax.barh(y, x, align='center')
	if cc == "x":
		ax.set_xticks(x)
		ax.set_xticklabels(xlabel)
	if cc == "y":
		ax.set_yticks(y)
		ax.set_yticklabels(ylabel, fontweight='bold')

	ax.set_xlabel('MUTANTS', fontweight='bold')

	rc('font', weight='bold')

	ax.set_title('Distribution of mutants across the taxonomy', fontweight='bold')

	plt.show()

hor_hist()





		
