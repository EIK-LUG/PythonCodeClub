#!/usr/bin/env python3

fast_code = r"""
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//#define MAX 10000

/*
 * Prints all primes less than MAX using the Sieve of Eratosthenes.
 */
int main(int argc, char *argv[]) {
    
    uint64_t MAX;
    if ( argc != 2 ) {
        MAX = 1000;
    } else {
        MAX = atol(argv[1]);
    }
	bool sieve[MAX];
	uint64_t i, j, primecount = 0, prime[MAX];
	uint64_t last_prime;

	for (i = 0; i < MAX; i++)
		sieve[i] = true;
	sieve[0] = sieve[1] = false;
	for (i = 2; i < MAX; i++) {
		if (!sieve[i])
			continue;
		//prime[primecount++] = i;
		last_prime = i;
		for (j = i * i; j < MAX; j += i)
			sieve[j] = false;
	}
	//for (i = 0; i < primecount; i++)
	//	printf("%d\n", prime[i]);
	printf("%d\n", last_prime);
}

"""

def primes(max_prime):
    for x in range(2, max_prime+1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            #print(x)
            pass

def faster(max_prime):
    with open("/tmp/code.c", "w") as f:
        f.write(fast_code)
    from subprocess import check_output, check_call
    check_call(("gcc", "/tmp/code.c", "-o", "/tmp/code"))
    last_prime = check_output(("/tmp/code", str(max_prime)))
    print(last_prime.decode().strip())

if __name__ == "__main__":
    import sys
    import time
    max_prime = 100000
    if len(sys.argv) == 3:
        max_prime = sys.argv[2]
    start_time = time.time()
    #primes(max_prime)
    faster(max_prime)
    end_time = time.time()
    print("time:", end_time - start_time)
