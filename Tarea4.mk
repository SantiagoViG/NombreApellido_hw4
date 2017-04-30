Tc1a0.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
	python Plots_Temperatura.py
	pdflatex Resultados_hw4.tex
Tc1a100.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc1a2500.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc1f0.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc1f100.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc1f2500.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc1p0.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc1p100.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc1p2500.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2a0.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2a100.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2a2500.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2f0.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2f100.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2f2500.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2p0.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2p100.txt: DifusionTemperatura.py
	python DifusionTemperatura.py
Tc2p2500.txt: DifusionTemperatura.py
	python DifusionTemperatura.py

Plots_Temperatura.py: DifusionTemperatura.py
	python Plots_Temperatura.py

Caso1 Condiciones abiertas 0s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso1 Condiciones abiertas 100s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso1 Condiciones abiertas 2500.png: Plots_Temperatura.py
	python Plots_Temperatura.py

Caso1 Condiciones fijas 0s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso1 Condiciones fijas 100s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso1 Condiciones fijas 2500.png: Plots_Temperatura.py
	python Plots_Temperatura.py

Caso1 Condiciones periodicas 0s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso1 Condiciones periodicas 100s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso1 Condiciones periodicas 2500.png: Plots_Temperatura.py
	python Plots_Temperatura.py

Caso2 Condiciones abiertas 0s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso2 Condiciones abiertas 100s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso2 Condiciones abiertas 2500.png: Plots_Temperatura.py
	python Plots_Temperatura.py

Caso2 Condiciones fijas 0s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso2 Condiciones fijas 100s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso2 Condiciones fijas 2500.png: Plots_Temperatura.py
	python Plots_Temperatura.py

Caso2 Condiciones periodicas 0s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso2 Condiciones periodicas 100s.png: Plots_Temperatura.py
	python Plots_Temperatura.py
Caso2 Condiciones periodicas 2500.png: Plots_Temperatura.py
	python Plots_Temperatura.py

Resultados_hw4.pdf: Caso1 Condiciones abiertas 0s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso1 Condiciones abiertas 100s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso1 Condiciones abiertas 2500s.png
	pdflatex Resultados_hw4.tex

Resultados_hw4.pdf: Caso1 Condiciones fijas 0s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso1 Condiciones fijas 100s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso1 Condiciones fijas 2500s.png
	pdflatex Resultados_hw4.tex

Resultados_hw4.pdf: Caso1 Condiciones periodicas 0s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso1 Condiciones periodicas 100s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso1 Condiciones periodicas 2500s.png
	pdflatex Resultados_hw4.tex

Resultados_hw4.pdf: Caso2 Condiciones abiertas 0s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso2 Condiciones abiertas 100s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso2 Condiciones abiertas 2500s.png
	pdflatex Resultados_hw4.tex

Resultados_hw4.pdf: Caso2 Condiciones fijas 0s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso2 Condiciones fijas 100s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso2 Condiciones fijas 2500s.png
	pdflatex Resultados_hw4.tex

Resultados_hw4.pdf: Caso2 Condiciones periodicas 0s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso2 Condiciones periodicas 100s.png
	pdflatex Resultados_hw4.tex
Resultados_hw4.pdf: Caso2 Condiciones periodicas 2500s.png
	pdflatex Resultados_hw4.tex
