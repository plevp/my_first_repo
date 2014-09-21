#include <stdio.h>
#include <math.h>
 
#define fp double
 
fp frac(fp x)
{
        double q;
        return modf(x, &q);
}
 
main()
{
        fp x = 0.6;
        int i;
 
        for (i = 0; i < 100; i++) {
	       printf("%.17f\n", x);
               x = frac(2.0 * x);
        }
 
 
}          

