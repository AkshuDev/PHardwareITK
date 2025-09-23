#define HI

#ifdef HI
int myfunc(int a, int b);
#else
void greet(char* str);
#endif

extern void test(int i);

//enum Hi {
//    Start,
//    End
//};

typedef enum {
    TEST
} test_;

typedef int bool_;

#include <CSpectreTest2.h>