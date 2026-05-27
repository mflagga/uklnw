#include "dek.h"

int main(){

    // parametry
    int N=100;
    double a=1.0;
    double eps=2.0;
    double t=-1.0;

    // alokacje / inicjalizacje
    cmp *F=malloc(N*N*sizeof(cmp));

    // defniniowanie F
    double xl,km;
    for (int l=0;l<N;l++){
        xl = l*a;
        for (int m=0;m<N;m++){
            km = 2.0*M_PI*m/(N*a);
            F[l*N+m]=cexp(I*km*xl)/sqrt(N);
        }
    }

    // sprawdzenie
    cmp *Fdagger=malloc(N*N*sizeof(cmp));
    cmp *jeden=malloc(N*N*sizeof(cmp));
    dagger(F,Fdagger,N);
    matmul(Fdagger,F,jeden,N);

    // for (int i=0;i<N;i++){
    //     for (int j=0;j<N;j++){
    //         printf("%lf\t",creal(jeden[i*N+j]));
    //     }
    //     printf("\n");
    // }

    // printf("Diagonala F:\n");
    // for (int i=0;i<N;i++) printf("(%e,%e)\n",creal(jeden[i*N+i]),cimag(jeden[i*N+i]));

    // hamiltonian
    cmp *H=calloc(N*N,sizeof(cmp));
    initH(H,N,t,eps);

    // baza pedowa
    cmp *Hk=malloc(N*N*sizeof(cmp));
    matmul(Fdagger,H,jeden,N); // Fdagger * H -> temp
    matmul(jeden,F,Hk,N); // temp * F -> Hk

    // sprawdzenie diagonalnosci
    

    // czystki
    free(F);
    free(Fdagger);
    free(jeden);
    free(H);
    free(Hk);

    // return zero
    return 0;
}
