set table "thesis.pgf-plot.table"; set format "%.5f"
set samples 100; set parametric; plot [t=0.0:20.0] t,1.5*sin((t/2)*180/pi)+2
