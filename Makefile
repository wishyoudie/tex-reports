target:
	pdflatex -halt-on-error -output-directory=out $(SRC)
	pdflatex -halt-on-error -output-directory=out $(SRC)
	rm out/*.aux out/*.log out/*.toc out/*.out