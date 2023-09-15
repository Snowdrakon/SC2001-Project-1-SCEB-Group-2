#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int** generateInput();

int main()
{
    //Generate input
    //Run algorithms
    int** input = generateInput();
    return 0;
}

int** generateInput(){
    const int MAX = 10000000;
    const int INITIALPOWER = 3;
    int** arrayOfInputArrays = (int **) malloc(5 * sizeof(int*));
    for (int i = 0; i<5; i++){
        int result = pow(10, INITIALPOWER + i);
        arrayOfInputArrays[i] = (int*) malloc(result * sizeof(int));
        for (int j = 0; j<result; j++){
            arrayOfInputArrays[i][j] = rand() % MAX;
        }
    }

    return arrayOfInputArrays;
}
