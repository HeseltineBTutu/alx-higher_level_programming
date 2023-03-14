#include <Python.h>

void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    PyObject *item;
    Py_ssize_t i;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyLong_Check(item))
            printf("int\n");
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else if (PyList_Check(item))
            printf("list\n");
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyDict_Check(item))
            printf("dict\n");
        else if (PySet_Check(item))
            printf("set\n");
        else if (PyAnySet_Check(item))
            printf("set\n");
        else if (PyBytes_Check(item))
            printf("bytes\n");
        else if (PyByteArray_Check(item))
            printf("bytearray\n");
        else if (PyIter_Check(item))
            printf("iterator\n");
        else if (PyModule_Check(item))
            printf("module\n");
        else if (PyCFunction_Check(item))
            printf("builtin_function_or_method\n");
        else if (PyFunction_Check(item))
            printf("function\n");
        else if (PyType_Check(item))
            printf("type\n");
        else
            printf("%s\n", item->ob_type->tp_name);
    }
}

