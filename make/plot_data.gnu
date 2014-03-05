set term postscript eps color  
set output 'graph.eps'
set key bmargin left horizontal Right noreverse enhanced autotitles box linetype -1 linewidth 1.000
set samples 800, 800
plot [-19:19] '1.dat'with impulses ,'2.dat' ,'3.dat' with lines
