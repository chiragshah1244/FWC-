#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

/*
int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

//Mean and variance of Uniform 
printf("Uniform stats:\n");
printf("Mean: %lf\n",mean("uni.dat"));
printf("Variance: %lf\n",variance("uni.dat"));
return 0;
}
*/


#define uni_data 	"../data_center/uni.dat"

int  main(void) 
{
 
uniform(uni_data, 1000000);

printf("Mean is : %lf\n",mean(uni_data));
printf("Variance is : %lf\n",variance(uni_data));
return 0;
}


