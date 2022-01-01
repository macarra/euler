## Make file for superprime

INCLUDES=--allow-unsupported-compiler

all: 21 

force: 
	touch *.cu
	make all

21:
	g++ 21.cpp -std=c++11 -o 21_cpu
	nvcc 21.cu -o 21_gpu $(INCLUDES)
