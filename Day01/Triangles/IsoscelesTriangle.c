#include <stdio.h>

int main() {
	int input = 5;
	for(int i = 0; i < input; i++) {
		for(int j = 0; j <= i; j++) {
			printf("*");
		} 
		printf("\n");
	}

}
