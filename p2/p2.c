#include <stdio.h>
int main(void) {
	int first, second, third, sum;
	for(first=1,second=1,third=first+second,sum=0;third<4000000;sum+=third,first=second+third,second=first+third,third=first+second);
	printf("%d\n", sum);
	return 0;
}

