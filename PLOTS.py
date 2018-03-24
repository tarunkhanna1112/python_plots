# SIMPLE PYTHON SCRIPT FOR LINE PLOTS

import matplotlib.pyplot as plt
import sys
import numpy as np

# color pallet

black = (0.0,0.0,0.0)
light_red = (0.984,0.356,0.521)
cyanish = (0.470,0.8,0.807)
warm_yellow = (0.949,0.784,0.027)

pt = sys.argv[(len(sys.argv)-2)]
if pt == "M" or pt == "m":
	nplots = int(sys.argv[(len(sys.argv)-1)])
	if len(sys.argv) == (7+nplots) and sys.argv[3+nplots] != "BAR":

		# XYY PLOT

		min1 = 1000.0
		max1 = -1000.0
		d = dict()
		d1 = dict()
		for kk in range(0,nplots):

			f = open("{}".format(sys.argv[1+kk]),"r")
			ft = f.readlines()
			f.close()
			col1 = int(sys.argv[1+nplots]) - 1
			col2 = int(sys.argv[2+nplots]) - 1
			col3 = int(sys.argv[3+nplots]) - 1

			k = 0
			if sys.argv[(len(sys.argv)-3)] == "CSV":
				ft1 = ft[0].split(",")
			else:
				ft1 = ft[0].split()
			if ft1[0][0:1] == "#":
				k = k + 1

			list1 = []
			list2 = []
			list3 = []
			while k < len(ft):
				if sys.argv[(len(sys.argv)-3)] == "CSV":
					ft1 = ft[k].split(",")
				else:
					ft1 = ft[k].split()
				t1 = float(ft1[col1].strip("\n"))
				t1 = round(t1,2)
				t2 = float(ft1[col2].strip("\n"))
				t2 = round(t2,2)
				t3 = float(ft1[col3].strip("\n"))
				t3 = round(t3,2)
				list1.append(t1)
				list2.append(t2)
				list3.append(t3)
				k = k + 1

			x = np.array(list1)
			y1 = np.array(list2)
			y1max = np.amax(y1)
			y1min = np.amin(y1)
			y2 = np.array(list3)
			y2max = np.amax(y2)
			y2min = np.amin(y2)

			if y1min < y2min and y1min < min1:
				min1 = y1min - 2.0
			elif y2min < min1:
				min1 = y2min - 2.0

			if y1max > y2max and y1max > max1:
				max1 = y1max + 2.0
			elif y2max > max1:
				max1 = y2max + 2.0

			d[kk] = y1
			d1[kk] = y2


		print("ENTER THE X LABEL")
		xl = input()
					
		print("ENTER THE FIRST Y LABEL")
		yl = input()

		print("ENTER THE SECOND Y LABEL")
		yl1 = input()

		print("ENTER THE GRAPH LABEL FOR GRAPH 1")
		gl = input()

		print("ENTER THE GRAPH LABEL FOR GRAPH 2")
		gl = input()

		fig, ax1 = plt.subplots()

		color = cyanish
		ax1.set_ylabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.set_xlabel('{}'.format(yl), color=color, fontsize=10, fontweight='bold')
		ax1.plot(x, d[0], color=color)
		ax1.plot(x, d[1], color=color)
		ax1.set_ylim([min1,max1])
		ax1.tick_params(axis='x', labelcolor=color)

		ax2 = ax1.twiny()  

		color = light_red
		ax2.set_xlabel('{}'.format(yl1), color=color, fontsize=10, fontweight='bold')  
		ax2.plot(x, d1[0], color=color)
		ax2.plot(x, d1[2], color=color)
		ax2.tick_params(axis='x', labelcolor=color)
		ax2.set_ylim([min1,max1])
		fig.tight_layout() 

		plt.show()

	elif len(sys.argv) == (7+nplots) and sys.argv[3+nplots] == "BAR":

		# VERTICAL BAR
		d = dict()
		W = 0.3
		for kk in range(0,nplots):

			f = open("{}".format(sys.argv[1+kk]),"r")
			ft = f.readlines()
			f.close()

			col1 = int(sys.argv[1+nplots]) - 1
			col2 = int(sys.argv[2+nplots]) - 1

			k = 0
			if sys.argv[(len(sys.argv)-3)] == "CSV":
				ft1 = ft[0].split(",")
			else:
				ft1 = ft[0].split()
			if ft1[0][0:1] == "#":
				k = k + 1

			list1 = []
			list2 = []
			list3 = []
			while k < len(ft):
				if sys.argv[(len(sys.argv)-3)] == "CSV":
					ft1 = ft[k].split(",")
				else:
					ft1 = ft[k].split()

				try:
					t1 = float(ft1[col1].strip("\n"))
					t1 = round(t1,1)
				except:
					t1 = ft1[col1].strip("\n")

				t2 = float(ft1[col2].strip("\n"))
				t2 = round(t2,2)
				list1.append(t1)
				list2.append(t2)
				list3.append(k)
				k = k + 1

			x = np.array(list3)
			y = np.array(list2)
			xtics = np.array(list1)

			d[kk] = y
		

		# PLOTTING

		print("ENTER THE X LABEL")
		xl = input()
				
		print("ENTER THE Y LABEL")
		yl = input()

		print("ENTER THE GRAPH LABEL FOR PLOT1")
		gl = input()

		print("ENTER THE GRAPH LABEL PLOT2")
		gl1 = input()
			
		fig, ax1 = plt.subplots()

		plt.ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		plt.xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		plt.bar(x-(W/2.0), d[0], width=W, color=light_red, label="{}".format(gl))
		plt.bar(x+(W/2.0), d[1], width=W, color=warm_yellow, label="{}".format(gl1))
		plt.xticks(x, xtics)
		#plt.legend(loc='upper right')
		plt.legend(loc='best', fontsize=12)

		fig.tight_layout() 
		
		plt.show()

	elif len(sys.argv) == (6+nplots):

		# XY PLOT
		d = dict()
		kk = 0
		for kk in range(0,nplots):

			f = open("{}".format(sys.argv[1+kk]),"r")
			ft = f.readlines()
			f.close()

			col1 = int(sys.argv[1+nplots]) - 1
			col2 = int(sys.argv[2+nplots]) - 1

			k = 0
			if sys.argv[(len(sys.argv)-3)] == "CSV":
				ft1 = ft[k].split(",")
			else:
				ft1 = ft[k].split()

			if ft1[0][0:1] == "#":
				k = k + 1

			list1 = []
			list2 = []
			while k < len(ft):
				if sys.argv[(len(sys.argv)-3)] == "CSV":
					ft1 = ft[k].split(",")
				else:
					ft1 = ft[k].split()
				t1 = float(ft1[col1].strip("\n"))
				t1 = round(t1,2)
				t2 = float(ft1[col2].strip("\n"))
				t2 = round(t2,2)
				list1.append(t1)
				list2.append(t2)
				k = k + 1

			x = np.array(list1)
			y = np.array(list2)

			d[kk] = y

		fig, ax1 = plt.subplots()

		print("ENTER THE X LABEL")
		xl = input()
				
		print("ENTER THE Y LABEL")
		yl = input()

		print("ENTER THE GRAPH LABEL FOR GRAPH1")
		gl = input()

		print("ENTER THE GRAPH LABEL FOR GRAPH2")
		gl1 = input()

		ax1.set_ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		ax1.set_xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.scatter(x, d[0], color=light_red, label="{}".format(gl))
		ax1.scatter(x, d[1], color=warm_yellow, label="{}".format(gl1) )
		#ax1.plot(x, y1, color=light_red)

		plt.legend(loc='best', fontsize=12)
			
		fig.tight_layout() 
		plt.show()

	elif len(sys.argv) == (5+nplots):

		kk = 0
		d = dict()
		for kk in range(0,nplots):

			f = open("{}".format(sys.argv[1+kk]),"r")
			ft = f.readlines()
			f.close()

			col1 = int(sys.argv[1+nplots]) - 1

			k = 0
			if sys.argv[(len(sys.argv)-3)] == "CSV":
				ft1 = ft[k].split(",")
			else:
				ft1 = ft[k].split()

			if ft1[0][0:1] == "#":
				k = k + 1

			list1 = []
			list2 = []
			while k < len(ft):
				if sys.argv[(len(sys.argv)-3)] == "CSV":
					ft1 = ft[k].split(",")
				else:
					ft1 = ft[k].split()
				t1 = float(ft1[col1].strip("\n"))
				t1 = round(t1,2)
				list2.append(k)
				list1.append(t1)
				k = k + 1

			x = np.array(list2)
			y = np.array(list1)
			d[kk] = y


		# PLOTIING
		print("ENTER THE X LABEL")
		xl = input()
				
		print("ENTER THE Y LABEL")
		yl = input()

		print("ENTER THE GRAPH LABEL FOR GRAPH1")
		gl = input()
	
		print("ENTER THE GRAPH LABEL FOR GRAPH2")
		gl1 = input()

		fig, ax1 = plt.subplots()

		ax1.set_ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		ax1.set_xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.scatter(x, d[0], color=light_red, linewidth=2.5)
		ax1.plot(x, d[0],  color=light_red, linewidth=2.5,label="{}".format(gl))
		ax1.scatter(x, d[1], color=warm_yellow, linewidth=2.5)
		ax1.plot(x, d[1],  color=warm_yellow, linewidth=2.5,label="{}".format(gl1))
		
		plt.legend(loc='best', fontsize=12)
		fig.tight_layout() 
		plt.show()

	elif len(sys.argv) == (8+nplots) and sys.argv[4+nplots] == "ERR":

		kk = 0
		d = dict()
		d1 = dict()
		for kk in range(0,nplots):

			f = open("{}".format(sys.argv[1+kk]),"r")
			ft = f.readlines()
			f.close()

			col1 = int(sys.argv[1+nplots]) - 1
			col2 = int(sys.argv[2+nplots]) - 1
			col3 = int(sys.argv[3+nplots]) - 1

			k = 0
			if sys.argv[(len(sys.argv)-3)] == "CSV":
				ft1 = ft[0].split(",")
			else:
				ft1 = ft[0].split()
			if ft1[0][0:1] == "#":
				k = k + 1

			list1 = []
			list2 = []
			list3 = []
			while k < len(ft):
				if sys.argv[(len(sys.argv)-3)] == "CSV":
					ft1 = ft[k].split(",")
				else:
					ft1 = ft[k].split()
				t1 = float(ft1[col1].strip("\n"))
				t1 = round(t1,2)
				t2 = float(ft1[col2].strip("\n"))
				t2 = round(t2,2)
				t3 = float(ft1[col3].strip("\n"))
				t3 = round(t3,2)
				list1.append(t1)
				list2.append(t2)
				list3.append(t3)
				k = k + 1

			x = np.array(list1)
			y = np.array(list2)
			yerr = np.array(list3)
			d[kk] = y
			d1[kk] = yerr
		

		# PLOTIING
		fig, ax1 = plt.subplots()

		print("ENTER THE X LABEL")
		xl = input()
		
		print("ENTER THE Y LABEL")
		yl = input()

		print("ENTER THE GRAPH LABEL FOR GRAPH 1")
		gl = input()

		print("ENTER THE GRAPH LABEL FOR GRAPH 2")
		gl1 = input()

		ax1.set_ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		ax1.set_xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.errorbar(x, d[0], d1[0], color=light_red, fmt='--o', capsize=4)
		ax1.scatter(x, d[0], color=light_red, label="{}".format(gl))
		ax1.errorbar(x, d[1], d1[1], color=warm_yellow, fmt='--o', capsize=4)
		ax1.scatter(x, d[1], color=warm_yellow, label="{}".format(gl1))
		#ax1.plot(x, y1, color=light_red)
		plt.legend(loc='best', fontsize=12)
		fig.tight_layout() 
		plt.show()

else:
	f = open("{}".format(sys.argv[1]),"r")
	ft = f.readlines()
	f.close()

	# color pallet

	black = (0.0,0.0,0.0)
	light_red = (0.984,0.356,0.521)
	cyanish = (0.470,0.8,0.807)
	warm_yellow = (0.949,0.784,0.027)

	if len(sys.argv) == 6 and sys.argv[4] != "BAR":
		# XYY PLOT
		col1 = int(sys.argv[2]) - 1
		col2 = int(sys.argv[3]) - 1
		col3 = int(sys.argv[4]) - 1

		k = 0
		if sys.argv[(len(sys.argv)-1)] == "CSV":
			ft1 = ft[0].split(",")
		else:
			ft1 = ft[0].split()
		if ft1[0][0:1] == "#":
			k = k + 1

		list1 = []
		list2 = []
		list3 = []
		while k < len(ft):
			if sys.argv[(len(sys.argv)-1)] == "CSV":
				ft1 = ft[k].split(",")
			else:
				ft1 = ft[k].split()
			t1 = float(ft1[col1].strip("\n"))
			t1 = round(t1,2)
			t2 = float(ft1[col2].strip("\n"))
			t2 = round(t2,2)
			t3 = float(ft1[col3].strip("\n"))
			t3 = round(t3,2)
			list1.append(t1)
			list2.append(t2)
			list3.append(t3)
			k = k + 1

		x = np.array(list1)
		y1 = np.array(list2)
		y1max = np.amax(y1)
		y1min = np.amin(y1)
		y2 = np.array(list3)
		y2max = np.amax(y2)
		y2min = np.amin(y2)

		if y1min < y2min:
			min1 = y1min - 2.0
		else:
			min1 = y2min - 2.0

		if y1max > y2max:
			max1 = y1max + 2.0
		else:
			max1 = y2max + 2.0

		print("ENTER THE X LABEL")
		xl = input()
		
		print("ENTER THE FIRST Y LABEL")
		yl = input()

		print("ENTER THE SECOND Y LABEL")
		yl1 = input()

		#print("ENTER THE GRAPH LABEL")
		#gl = input()

		fig, ax1 = plt.subplots()

		color = cyanish
		ax1.set_xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.set_ylabel('{}'.format(yl), color=color, fontsize=10, fontweight='bold')
		ax1.scatter(x, y1, color=color)
		ax1.set_ylim([min1,max1])
		ax1.tick_params(axis='y', labelcolor=color)

		ax2 = ax1.twinx()  

		color = light_red
		ax2.set_ylabel('{}'.format(yl1), color=color, fontsize=10, fontweight='bold')  
		ax2.scatter(x, y2, color=color)
		ax2.tick_params(axis='y', labelcolor=color)
		ax2.set_ylim([min1,max1])
		fig.tight_layout() 
		plt.show()

	elif len(sys.argv) == 6 and sys.argv[4] == "BAR":

		# VERTICAL BAR
		col1 = int(sys.argv[2]) - 1
		col2 = int(sys.argv[3]) - 1

		k = 0
		if sys.argv[(len(sys.argv)-1)] == "CSV":
			ft1 = ft[0].split(",")
		else:
			ft1 = ft[0].split()
		if ft1[0][0:1] == "#":
			k = k + 1

		list1 = []
		list2 = []
		list3 = []
		while k < len(ft):
			if sys.argv[(len(sys.argv)-1)] == "CSV":
				ft1 = ft[k].split(",")
			else:
				ft1 = ft[k].split()

			try:
				t1 = float(ft1[col1].strip("\n"))
				t1 = round(t1,1)
			except:
				t1 = ft1[col1].strip("\n")

			t2 = float(ft1[col2].strip("\n"))
			t2 = round(t2,2)
			list1.append(t1)
			list2.append(t2)
			list3.append(k)
			k = k + 1

		x = np.array(list3)
		y = np.array(list2)
		xtics = np.array(list1)


		print("ENTER THE X LABEL")
		xl = input()
		
		print("ENTER THE Y LABEL")
		yl = input()

		print("ENTER THE GRAPH LABEL")
		gl = input()
		

		fig, ax1 = plt.subplots()

		plt.ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		plt.xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		plt.bar(x, y, color=light_red, label="{}".format(gl))
		plt.xticks(x, xtics)
		#plt.legend(loc='upper right')
		plt.legend(loc='best', fontsize=12)

		fig.tight_layout() 
		plt.show()

	elif len(sys.argv) == 5:

		col1 = int(sys.argv[2]) - 1
		col2 = int(sys.argv[3]) - 1

		k = 0
		if sys.argv[(len(sys.argv)-1)] == "CSV":
			ft1 = ft[k].split(",")
		else:
			ft1 = ft[k].split()

		if ft1[0][0:1] == "#":
			k = k + 1

		list1 = []
		list2 = []
		while k < len(ft):
			if sys.argv[(len(sys.argv)-1)] == "CSV":
				ft1 = ft[k].split(",")
			else:
				ft1 = ft[k].split()
			t1 = float(ft1[col1].strip("\n"))
			t1 = round(t1,2)
			t2 = float(ft1[col2].strip("\n"))
			t2 = round(t2,2)
			list1.append(t1)
			list2.append(t2)
			k = k + 1

		x = np.array(list1)
		y = np.array(list2)

		fig, ax1 = plt.subplots()

		print("ENTER THE X LABEL")
		xl = input()
		
		print("ENTER THE Y LABEL")
		yl = input()

		print("ENTER THE GRAPH LABEL")
		gl = input()

		ax1.set_ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		ax1.set_xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.scatter(x, y, color=light_red, label="{}".format(gl))
		#ax1.plot(x, y1, color=light_red)
		plt.legend(loc='best', fontsize=12)
		fig.tight_layout() 
		plt.show()

	elif len(sys.argv) == 4:
		col1 = int(sys.argv[2]) - 1

		k = 0
		if sys.argv[(len(sys.argv)-1)] == "CSV":
			ft1 = ft[k].split(",")
		else:
			ft1 = ft[k].split()

		if ft1[0][0:1] == "#":
			k = k + 1

		list1 = []
		list2 = []
		while k < len(ft):
			if sys.argv[(len(sys.argv)-1)] == "CSV":
				ft1 = ft[k].split(",")
			else:
				ft1 = ft[k].split()
			t1 = float(ft1[col1].strip("\n"))
			t1 = round(t1,2)
			list2.append(k)
			list1.append(t1)
			k = k + 1

		x = np.array(list2)
		y = np.array(list1)

		print("ENTER THE X LABEL")
		xl = input()
		
		print("ENTER THE Y LABEL")
		yl = input()

		fig, ax1 = plt.subplots()

		ax1.set_ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		ax1.set_xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.scatter(x, y, color=(0.984,0.356,0.521), linewidth=2.5, label="{}".format(gl))
		ax1.plot(x, y,  color=(0.984,0.356,0.521), linewidth=2.5, )
		# (0.984,0.356,0.521)
		# (0.470,0.8,0.807)
		# (0.949,0.784,0.027)
		plt.legend(loc='best', fontsize=12)
		fig.tight_layout() 
		plt.show()

	elif len(sys.argv) == 7 and sys.argv[5] == "ERR":

		col1 = int(sys.argv[2]) - 1
		col2 = int(sys.argv[3]) - 1
		col3 = int(sys.argv[4]) - 1

		k = 0
		if sys.argv[(len(sys.argv)-1)] == "CSV":
			ft1 = ft[k].split(",")
		else:
			ft1 = ft[k].split()

		if ft1[0][0:1] == "#":
			k = k + 1

		list1 = []
		list2 = []
		list3 = []
		while k < len(ft):
			if sys.argv[(len(sys.argv)-1)] == "CSV":
				ft1 = ft[k].split(",")
			else:
				ft1 = ft[k].split()
			t1 = float(ft1[col1].strip("\n"))
			t1 = round(t1,2)
			t2 = float(ft1[col2].strip("\n"))
			t2 = round(t2,2)
			t3 = float(ft1[col3].strip("\n"))
			t3 = round(t3,2)
			list1.append(t1)
			list2.append(t2)
			list3.append(t3)
			k = k + 1

		x = np.array(list1)
		y = np.array(list2)
		yerr = np.array(list3)

		fig, ax1 = plt.subplots()

		print("ENTER THE X LABEL")
		xl = input()
		
		print("ENTER THE Y LABEL")
		yl = input()

		print("ENTER THE GRAPH LABEL")
		gl = input()

		ax1.set_ylabel('{}'.format(yl), fontsize=10, fontweight='bold')
		ax1.set_xlabel('{}'.format(xl), fontsize=10, fontweight='bold')
		ax1.errorbar(x, y, yerr, color=light_red, fmt='--o', capsize=4)
		ax1.scatter(x, y, color=light_red, label="{}".format(gl))
		#ax1.plot(x, y1, color=light_red)
		plt.legend(loc='best', fontsize=12)
		fig.tight_layout() 
		plt.show()


	
		
