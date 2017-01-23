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

paper.tex : 1.dat 2.dat 3.dat
	AV1 = python config_paper.py 1.dat
	sed -i 's/AV1/$(AV1)/g' $@
	AVALL = python config_paper.py $<
	sed -i 's/AVALL/$(AVALL)/g' $@

