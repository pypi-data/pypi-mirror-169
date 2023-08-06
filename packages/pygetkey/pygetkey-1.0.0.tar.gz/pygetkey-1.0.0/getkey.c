#ifndef GETKEY
#define GETKEY
#ifdef __cplusplus
extern "C" {
#endif
#include "Python.h"
#define __prototype(name) static PyObject * name(PyObject * self, PyObject * args)
#define add_name(func) #func, func
char u;
#ifdef _WIN32
#include <conio.h>
// #define UP 72
// #define DOWN 80
// #define RIGHT 77
// #define LEFT 75
#define Read() u = kbhit() ? getch() : u
#define init()
#else
#include <unistd.h>
#include <termios.h>
// #define UP 65
// #define DOWN 66
// #define RIGHT 67
// #define LEFT 68
#define Read() read(0, &u, 1)
#define init() \
    struct termios z; \
    tcgetattr(0, &z); \
    z.c_lflag &= ~ICANON; \
    z.c_cc[VMIN] = 0; \
    tcsetattr(0, TCSANOW, &z)
#endif
char SRead() {
    u = 0;
    while(!u) Read();
    return u;
}
__prototype(get_key);
__prototype(get_last_key);
static PyMethodDef getkey_methods[] = {
    {add_name(get_key), METH_NOARGS, "Wait for a key to be pressed and return it"},
    {add_name(get_last_key), METH_NOARGS, "Don't wait for a key to be pressed and return the last pressed key"},
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef getkey_module = {PyModuleDef_HEAD_INIT, "getkey", NULL, -1, getkey_methods};
PyMODINIT_FUNC PyInit_getkey(void) {
    init();
    PyObject *m = NULL;
    m = PyModule_Create(&getkey_module);
    // PyModule_AddIntConstant(m, add_name(UP));
    // PyModule_AddIntConstant(m, add_name(DOWN));
    // PyModule_AddIntConstant(m, add_name(RIGHT));
    // PyModule_AddIntConstant(m, add_name(LEFT));
    return m;
}
__prototype(get_last_key) {
    Read();
    return PyUnicode_FromStringAndSize(&u, 1);
}
__prototype(get_key) {
    SRead();
    return PyUnicode_FromStringAndSize(&u, 1);
}
#ifdef __cplusplus
}
#endif
#endif
