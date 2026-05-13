#define M_PI 3.141592653589793115997963468544185161590576171875
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_complex.h>
#include <gsl/gsl_complex_math.h>
#include <gsl/gsl_eigen.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_sort_vector.h>

void initV(double *V, int N, double V0, double w, double *x){
    for (int i=0;i<N;i++){
        if (x[i]>=-w/2 && x[i]<=w/2) V[i]=-fabs(V0);
    }
}

void diagHdlaK(double k, size_t N, double dx, double t, double *V, double *ev){
    double phi = k*dx;
    // definiowanie macierzy
    gsl_matrix_complex *H=gsl_matrix_complex_calloc(N,N);
    gsl_complex L,D,U;
    GSL_SET_COMPLEX(&L,-t,t*phi);
    U = gsl_complex_conjugate(L);
    for (size_t j=0;j<N;j++){
        GSL_SET_COMPLEX(&D,t*(2.0+phi*phi)+V[j],0.0);
        gsl_matrix_complex_set(H,j,j,D);
    }
    for (size_t j=1;j<N;j++){
        gsl_matrix_complex_set(H,j,j-1,U);
        gsl_matrix_complex_set(H,j-1,j,L);
    }
    gsl_matrix_complex_set(H,0,N-1,L);
    gsl_matrix_complex_set(H,N-1,0,U);
    // wektor własny
    gsl_vector *eval = gsl_vector_alloc(N);
    // rozwiazanie
    gsl_eigen_herm_workspace *w = gsl_eigen_herm_alloc(N);
    gsl_eigen_herm(H,eval,w);
    gsl_eigen_herm_free(w);
    gsl_sort_vector(eval);
    // zapisanie 
    for (size_t j=0;j<N;j++){
        ev[j]=gsl_vector_get(eval,j);
    }
    gsl_vector_free(eval);
    gsl_matrix_complex_free(H);
}

// wektor x dlugosci tylko n bo punkt n+1 == punkt 0 - to jest zawarte w macierzy
// u mnie macierz pasmowa dla metody RS wyglada jak:
// [e1, e2, e3, ...] dla k=k_min
// [e1, e2, e3, ...] dla k=k_min+dk
// ...
// [e1, e2, e3, ...] dla k=k_max
// czyli jest (Nk+1)x(N)
