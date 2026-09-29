#include <errno.h>
#include <stdlib.h>
#include <sys/stat.h>

void _exit(int status) {
    while (1) {
    }
}

extern char _end;  // defined by linker
static char* heap_end;

void* _sbrk(ptrdiff_t incr) {
    char* prev_heap_end;

    if (heap_end == 0)
        heap_end = &_end;

    prev_heap_end = heap_end;

    heap_end += incr;

    return (void*)prev_heap_end;
}

int _getpid(void) {
    return 1;
}

int _kill(int pid, int sig) {
    errno = EINVAL;
    return -1;
}
