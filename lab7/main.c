#include "header.h"

int main(){
    
    // parametry jednostkowe
    double m=1.0;
    double hbar=1.0;

    // parametry układu
    double a=1.0;
    double V0=100.0;
    int M=4;
    int N=100;

    // parametry wtórne
    double w=a/2;
    double xa=-2*a;
    double xb=3*a;
    double dx=(xb-xa)/N;

    // alokacje inicjalizacje
    double *x=malloc((N+1)*sizeof(double));
    for (int i=0;i<=N;i++) x[i]=i*dx;
    double *V=calloc(N+1,sizeof(double));

    // czystki
    free(x);
    free(V);

    // return zero
    return 0;
}
