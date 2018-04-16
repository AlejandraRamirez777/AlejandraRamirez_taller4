transformadas.txt : datos.txt fourier
	./fourier datos.txt > transformadas.txt

fourier : fourr.cpp
	g++ fourr.cpp -o ./fourier datos.txt > transformadas.txt
