#include <iostream>
#include <fstream>
#include <string>
using namespace std;

double lagrange(double x, int G, double *setX, double *setY);

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

cout << numL<< endl;
/*
    //EJECUTAR POLINOMIO DE LAGRANGE PARA CADA VALOR
    for(int i = 0; i<numL; i++){
        double ll = lagrange(t[i],numL, tp,ftp);
        cout << ll << endl;

    }
*/
/*
    for(int i = 15; i<22; i++){
        double ll = lagrange(i,numL, tp,ftp);
        cout << ll << endl;

    }
*/

    double ll = lagrange(754.8,numL,tp,ftp);
    cout << ll << endl;

return 0;
}


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
