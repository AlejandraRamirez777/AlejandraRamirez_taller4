#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <complex>
#include <cmath>
#include <iomanip>
#include <vector>
#include <stdio.h>
#include <complex.h>
#include <tgmath.h>

using namespace std;

#define _USE_MATH_DEFINES
const complex<double> J(0.0, 1.0);

double lagrange(double x, int G, double *setX, double *setY);
vector<complex<double> > fou(double *unP, int N);
vector<double> ffreq(double n, double sp);
vector<double> rear(vector<double> inar);
vector<complex<double> > rearTT(vector<complex<double> > inarTT);

int main(int argc, char **argv){

    //info inputs
    //nombre del archivo ingresado
    string name = argv[1];

    //LEER EL TXT
    ifstream inl;

    //Contador de lineas
    int numL = 0;
    //info line
    string s;

    //Contador avance lineas
    int g = 0;

    //Abrir el archivo
    inl.open(name);

    //Si se produce algun error leyendolo se maneja
    if(inl.fail()){
        cout << "Error al leer datos.txt" << endl;
        return 0;
    }

    //Lee todo el archivo hasta el final
    while(!inl.eof()){
        getline(inl,s);
        //cuenta el numero de lineas que no esten vacias
        if(s != ""){
        ++numL;
      }
    }
    //Cierre archivo
    inl.close();

    //Inicializar arrays con sus pointers donde se guardara info
    //Primera columna --> tiempo
    double t[numL];
    double *tp;
    tp = t;

    //Segunda columna --> funcion del tiempo
    double ft[numL];
    double  *ftp;
    ftp = ft;

    //Abre archivo
    inl.open(name);

   //Lee todo el archivo hasta el final
    while(!inl.eof()){
        //Lee primera columna
        inl >> t[g];
        //Lee segunda columna
        inl >> ft[g];
        ++g;
    }
    //Cierre archivo
    inl.close();



/*
    for(int i = 0; i<numL; i++){
         cout << t[i] << " "<< endl;
         cout << ft[i] << " "<< endl;
    }
*/

//cout << numL<< endl;

    //Inicializar array con su pointer donde se guardara Lagrange
    double LL[numL];
    double *LLp;
    LLp = LL;
/*
    //EJECUTAR POLINOMIO DE LAGRANGE PARA CADA VALOR
    for(int i = 0; i<73; i++){
        //cout << "OK" << endl;
        //cout << i << endl;
        double ll = lagrange(i,numL,tp,ftp);
        //cout << ll << endl;
        LL[i] = ll;

        //cout << LL[i] << endl;
    }
*/
/*
    for(int i = 15; i<22; i++){
        double ll = lagrange(i,numL, tp,ftp);
        cout << ll << endl;

    }


    double ll = lagrange(754.8,numL,tp,ftp);
    cout << ll << endl;
*/

    //Fourier
    //fou(LLp,numL);

    double aa[10] = {0,1,2,3,4,5,6};
    //complex<double>ff[10] = fou(aa,10);
    vector<complex<double> > ff = fou(aa,7);

    for(int i = 0; i<7; i++){
        cout << ff[i]<<endl;
    }

    vector<complex<double> > rFt = rearTT(ff);

    cout << "Mariscos"<<endl;
    for(int i = 0; i<7; i++){
        cout << rFt[i]<<endl;
    }

    /*
    //Size de array de transformadas de fourier
    int size  = ff.size();
    cout << size<<endl;
    cout << "size"<<endl;
    vector<double> ffr = ffreq(10,0.1);
    //loop must be same size as n ffreq
    for(int i = 0; i<10; i++){
        cout << ffr[i]<<endl;
    }
    int size1  = ffr.size();
    cout << size1<<endl;

    cout << "rears"<<endl;
    vector<double> re = rear(ffr);
    for(int i = 0; i<10; i++){
        cout << re[i]<<endl;
    }
    */

return 0;
}

//Aplica el polinomio de LAGRANGE
//Param: x valor a evaluar, G grado del polinomio,
//*setX pointer para array de x que construiran el polinomio,
//*setY pointer para array de y = f(x) que construiran el polinomio.
//Return: correspondiente y al x ingresado despues de interpolacion
double lagrange(double x, int G, double *setX, double *setY){
    double sol[G];
    double ans;

    for(int i = 0; i<G; i++){
        double l = 1.0;

        for(int p = 0; p<G; p++){
            double a = x - setX[p];
            double b = setX[i] - setX[p];

            if(i != p){
              if(b == 0){
                cout << "Error division entre 0" << endl;
              }
              l *= a/b;
            }
        }
      sol[i] = l;
    }

    for (int i = 0; i<G; i++){
        ans += sol[i]*setY[i];
    }
    //Aproximacion al cero
    if(ans<0.00000000000000001){
      ans = 0;
    }

    return ans;
}

//Aplica transformada de fourier a un array
//Param: *unP pointer de array evenly spaced que se fourierizara,
//N longitud del array a fourierizar
//Return: array de longitud variable con transformada de fourier
vector<complex<double> > fou(double *unP, int N){
      vector<complex<double> > sol;

      for (int n = 0; n<N; n++){
          complex<double> g = 0;

          for (int k = 0; k<N; k++){
              double w = (n/float(N));
              double kk = double(k);
              complex<double> y =-J*2.0*M_PI*kk*w;
              complex<double> m = exp(y);
              g += unP[k]*m;
          }
         sol.push_back(g);
      }

      return sol;
}

//Metodo analogo a ffreq de numpy para obtener Frecuencias
//Param:n size del array con la transformada de fourier,
//sp sample spacing
//Return: array de longitud variable con frecuencias
vector<double> ffreq(double n, double sp){
    vector<double> sol;
    double cen = int(n/2.0);
    //Para N par
    if(fmod(n, 2.0) == 0.0){
        for (int k = 0; k<cen+1; k++){
            double a;
            if(k != n){
                a = k/(n*sp);
            }
            if(k == cen){
                a = (-1*k)/(n*sp);
            }
            sol.push_back(a);
        }
        for (int k = cen; k --> 0;){
            double a = -k/(n*sp);
            sol.push_back(a);
        }
    }
    //Para N impar
    else{
      for (int k = 0; k<cen+1; k++){
          double a;
          if(k != n){
              a = k/(n*sp);
          }
          sol.push_back(a);
      }
      for (int k = cen+1; k --> 0;){

          double a = -k/(n*sp);
          sol.push_back(a);
      }
    }
    return sol;
}

//Reorganiza las frecuencias obtenidas por ffreq ascendentemente
//Param: array de size variable de frecuencias dadas por fftfreq
//Return: array de input organizado
vector<double> rear(vector<double> inar){
    vector<double> sol;
    int n = inar.size();
    //Redondea hacia abajo
    double cenP = int(n/2.0);
    double cenI = int((n+1)/2.0);

    if(fmod(n, 2.0) != 0.0){
        for (int k = cenI-1; k<(cenI-1)*2; k++){
            double a = inar[k];
            sol.push_back(a);
        }
        for (int k = 0; k<cenI; k++){
            double a = inar[k];
            sol.push_back(a);
        }
    }
    //Par
    else{
      for (int k = cenP; k<cenP*2; k++){
          double a = inar[k];
          sol.push_back(a);
      }
      for (int k = 1; k<cenP; k++){
          double a = inar[k];
          sol.push_back(a);
      }
    }
    return sol;
}

//Reorganiza la transformada obtenidas como rear
//Param: array de size variable de transformada
//Return: array de input organizado
vector<complex<double> > rearTT(vector<complex<double> > inarTT){
    vector<complex<double> > sol;
    int n = inarTT.size();
    //Redondea hacia abajo
    double cenP = int(n/2.0);
    double cenI = int((n+1)/2.0);
    //Impar
    if(fmod(n, 2.0) != 0.0){

        for (int k = cenI; k<(cenI*2)-1; k++){
            complex<double> a = inarTT[k];
            sol.push_back(a);
        }
        for (int k = 0; k<cenI; k++){
            complex<double> a = inarTT[k];
            sol.push_back(a);
        }
    }
    else{

      for (int k = cenP; k<cenP*2; k++){
          complex<double> a = inarTT[k];
          sol.push_back(a);
      }
      for (int k = 0; k<cenP; k++){
          complex<double> a = inarTT[k];
          sol.push_back(a);
      }
    }
    return sol;
}
