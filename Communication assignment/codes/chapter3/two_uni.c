#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

//defining where to locate with a new .

#define U_1	"../data_center/u_1.dat"
#define U_2	"../data_center/u_2.dat"

int  main(void) 
{
 
//U_1 and U_2 uniform random variable.
uniform(U_1, 1000000);
uniform(U_2, 1000000);

return 0;
}
