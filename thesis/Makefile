all: dissertation clean

dissertation:
	pdflatex main.tex
	bibtex main
	makeindex main.tex
	pdflatex main.tex
	pdflatex main.tex

clean:
	rm -rf main.{4ct,4tc,acn,acr,alg,aux,bbl,bcf,blg,dvi,fdb_latexmk,fls,glg,glo,gls,ilg,ind,ist,idv,lg,loa,loe,lof,log,lot,out,run.xml,synctex.gz,toc,xref}
	rm -rf figures/*.{log,aux}
