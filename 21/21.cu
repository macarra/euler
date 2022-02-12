#include <iostream>
#include <math.h>
#include <vector>
#include <map>
#include <string>
#include <stdio.h>

using namespace std;
__global__
void divide(int N, int* m){
    int index = blockIdx.x * blockDim.x + threadIdx.x;
    int stride = blockDim.x*gridDim.x;
    for(int z = index; z < N; z += stride)
    {
	    m[z] = 0;
	    for(int id = 1; id < z; id++){
		if(z%id == 0){
		    m[z] +=id;
		}
	    }
    }
}

int main(int argc, char** argv){
    const int k = 1000000;
    int *m;
    cudaMallocManaged(&m, k*sizeof(int));
    int blockSize=  256;
    int numBlocks = (k + blockSize - 1) / blockSize;
    divide<<< numBlocks, blockSize>>> (k, m);

    cudaDeviceSynchronize();

    cout <<"\n";
    int res = 0;
    for(int i = 1; i < k; i++){
        int val = m[i];
        if(val < k && val != i && m[val] == i){
            res += i;
            res += val;
	    m[i]=0;
	    m[val]=0;
        }
    }
    cout << "res: "<< res << "\n";
    cudaFree(m);
    return 0;
}
