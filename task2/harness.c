/*
 * CMSC 414
 * Spring 2021
 * Homework 2 | task2
 */

#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdint.h>

int passwd(char *data, size_t len);

int main() 
{
    // Insert code here
    char buffer[6]; //creating a buffer with length 6
   // scanf( "%s", &buffer);
   // fgets(buffer, 6, stdin); // get input from stander  input
    gets(buffer);
    passwd(buffer, 6); // calling passwd and passing buffer and 6 as arg
	return 0;
}
