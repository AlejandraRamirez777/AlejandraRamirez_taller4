#include <iostream>
using namespace std;

double lagrange(double x, int G, double *setX, double *setY);

int main(){


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
              l *= a/b;
            }
        }
       sol[i] = l;
    }

    for (int i = 0; i<G; i++){
        ans = sol[i]*setY[i];
    }

return ans;
}
