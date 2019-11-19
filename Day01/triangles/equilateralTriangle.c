#include <stdio.h>

int main() {
	int input = 5;
	int noOfStars = 1;
	for(int rowInverse = input; rowInverse >= 0; rowInverse--) {
		for(int spaces = 0; spaces < rowInverse; spaces++) {
			printf(" ");
		} 
		for(int stars = 0; stars < noOfStars; stars++) {
			printf("*");
		}
		noOfStars += 2;
		printf("\n");
	}

}
