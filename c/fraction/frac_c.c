#include <stdio.h>
#include <math.h>
 
int main() 
{
        double q;
	double y = 0.2;
	double z = modf(1.2, &q);
	
	unsigned long long *ly = &y;
	unsigned long long *lz = &z;

	printf("%llx\n", *ly);
	printf("%llx\n", *lz);
 
}          

