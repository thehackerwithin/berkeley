# basic.mk

graph.eps : 1.dat 2.dat 3.dat 
	gnuplot plot_data.gnu
