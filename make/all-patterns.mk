# all-patterns.mk

paper.pdf : paper.dvi
	dvipdf $<

paper.dvi : paper.tex thw_icon.eps graph.eps
	latex paper.tex

graph.eps : *.dat
	gnuplot plot_data.gnu

1.dat : data_analysis.py
	python data_analysis.py

2.dat : data_analysis.py
	python data_analysis.py

3.dat : data_analysis.py
	python data_analysis.py
