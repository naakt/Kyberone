#include <stdio.h>
#include <string.h> 
#include <stdlib.h>
#include <stdint.h>
#include <sys/ptrace.h>

#define flag_len 64

//char *flag= []

void setup(){
    srand(32321);
    printf("setup complete\n");

}

void decrypt(uint32_t *flag){
   //
    int xor_flag[32];
    uint32_t key[32];
    for(int i=0;i<32;i++){
      uint32_t val = rand();
      key[i] = val;
      xor_flag[i]= key[i]^(*(flag+i));   
//      printf("%c,",xor_flag[i]); 
     }
}


int main(int argc, char *argv[]){
    setup();
   uint32_t flag[32] = {1439652001,940131,1848338812,1483825720,476582451,529651862,1132729183,2051599359,1964951080,1559956736,1141754127,9286817,1988908659,1263243356,1521178339,1777602646,1815659325,1447257100,1199268268,1368483061,1761640406,100818642,1652868917,1588967656,1451284582,1342700928,1698689394,1832979814,784030843,366662571,1042481433,76199047};

//    int flag[32] = {67,84,70,123,99,111,110,115,116,97,110,116,95,115,101,101,100,115,95,97,114,101,95,110,116,95,115,101,99,117,114,125}; //cleartext 
printf("Can you guess my secret key?\n");
if (ptrace(PTRACE_TRACEME,0,1,0)<0) {
    printf("Slick move Rick, try again.");
    exit(57);
}

printf("almost there\n");
decrypt(flag);
return 0;}
