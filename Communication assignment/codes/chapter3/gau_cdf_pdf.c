#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

#define data "../data_center/gau.dat"

int  main(void)
{
 

gaussian("gau.dat", 1000000);


printf("Gaussian Mean and Variance:\n");
printf("Mean is : %lf\n",mean("gau.dat"));
printf("Variance is : %lf\n",variance("gau.dat"));
return 0;
}
