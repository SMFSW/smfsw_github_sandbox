
#define CPPCHECK_FAIL	0

int main(int argc, char *argv[])
{
#if !CPPCHECK_FAIL
    uint8_t array[32] = { 0 };
#else
    uint32_t array[32] = { 0 };   // cppcheck array sizeof outside boundaries
#endif


    for (int i = 0 ; i < sizeof(array) - 1 ; i++)
    {
        array[i+1] = array[i]++;
    }

#if !CPPCHECK_FAIL
    return 0;  // cppcheck no return
#endif
}