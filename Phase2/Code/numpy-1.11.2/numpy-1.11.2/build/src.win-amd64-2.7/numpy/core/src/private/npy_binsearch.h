#line 1 "numpy\\core\\src\\private\\npy_binsearch.h.src"

/*
 *****************************************************************************
 **       This file was autogenerated from a template  DO NOT EDIT!!!!      **
 **       Changes should be made to the original source (.src) file         **
 *****************************************************************************
 */

#line 1
#ifndef __NPY_BINSEARCH_H__
#define __NPY_BINSEARCH_H__

#include "npy_sort.h"
#include <numpy/npy_common.h>
#include <numpy/ndarraytypes.h>

typedef void (PyArray_BinSearchFunc)(const char*, const char*, char*,
                                     npy_intp, npy_intp,
                                     npy_intp, npy_intp, npy_intp,
                                     PyArrayObject*);

typedef int (PyArray_ArgBinSearchFunc)(const char*, const char*,
                                       const char*, char*,
                                       npy_intp, npy_intp, npy_intp,
                                       npy_intp, npy_intp, npy_intp,
                                       PyArrayObject*);

struct binsearch_map {
    enum NPY_TYPES typenum;
    PyArray_BinSearchFunc *binsearch[NPY_NSEARCHSIDES];
};

struct argbinsearch_map {
    enum NPY_TYPES typenum;
    PyArray_ArgBinSearchFunc *argbinsearch[NPY_NSEARCHSIDES];
};

#line 33

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_bool(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_bool(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_byte(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_byte(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_ubyte(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_ubyte(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_short(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_short(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_ushort(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_ushort(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_int(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_int(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_uint(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_uint(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_long(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_long(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_ulong(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_ulong(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_longlong(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_longlong(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_ulonglong(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_ulonglong(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_half(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_half(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_float(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_float(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_double(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_double(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_longdouble(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_longdouble(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_cfloat(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_cfloat(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_cdouble(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_cdouble(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_clongdouble(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_clongdouble(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_datetime(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_datetime(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_left_timedelta(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_left_timedelta(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);


NPY_VISIBILITY_HIDDEN void
npy_binsearch_left(const char *arr, const char *key, char *ret,
                     npy_intp arr_len, npy_intp key_len,
                     npy_intp arr_str, npy_intp key_str,
                     npy_intp ret_str, PyArrayObject *cmp);
NPY_VISIBILITY_HIDDEN int
npy_argbinsearch_left(const char *arr, const char *key,
                        const char *sort, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str,
                        npy_intp sort_str, npy_intp ret_str,
                        PyArrayObject *cmp);

#line 33

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_bool(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_bool(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_byte(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_byte(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_ubyte(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_ubyte(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_short(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_short(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_ushort(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_ushort(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_int(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_int(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_uint(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_uint(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_long(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_long(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_ulong(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_ulong(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_longlong(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_longlong(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_ulonglong(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_ulonglong(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_half(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_half(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_float(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_float(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_double(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_double(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_longdouble(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_longdouble(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_cfloat(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_cfloat(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_cdouble(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_cdouble(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_clongdouble(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_clongdouble(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_datetime(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_datetime(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);

#line 40

NPY_VISIBILITY_HIDDEN void
binsearch_right_timedelta(const char *arr, const char *key, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str, npy_intp ret_str,
                        PyArrayObject *unused);
NPY_VISIBILITY_HIDDEN int
argbinsearch_right_timedelta(const char *arr, const char *key,
                           const char *sort, char *ret,
                           npy_intp arr_len, npy_intp key_len,
                           npy_intp arr_str, npy_intp key_str,
                           npy_intp sort_str, npy_intp ret_str,
                           PyArrayObject *unused);


NPY_VISIBILITY_HIDDEN void
npy_binsearch_right(const char *arr, const char *key, char *ret,
                     npy_intp arr_len, npy_intp key_len,
                     npy_intp arr_str, npy_intp key_str,
                     npy_intp ret_str, PyArrayObject *cmp);
NPY_VISIBILITY_HIDDEN int
npy_argbinsearch_right(const char *arr, const char *key,
                        const char *sort, char *ret,
                        npy_intp arr_len, npy_intp key_len,
                        npy_intp arr_str, npy_intp key_str,
                        npy_intp sort_str, npy_intp ret_str,
                        PyArrayObject *cmp);


#line 74

static struct binsearch_map _binsearch_map[] = {
    /* If adding new types, make sure to keep them ordered by type num */
    #line 86
    {NPY_BOOL,
        {
            &binsearch_left_bool,
            &binsearch_right_bool,
        },
    },
    
#line 86
    {NPY_BYTE,
        {
            &binsearch_left_byte,
            &binsearch_right_byte,
        },
    },
    
#line 86
    {NPY_UBYTE,
        {
            &binsearch_left_ubyte,
            &binsearch_right_ubyte,
        },
    },
    
#line 86
    {NPY_SHORT,
        {
            &binsearch_left_short,
            &binsearch_right_short,
        },
    },
    
#line 86
    {NPY_USHORT,
        {
            &binsearch_left_ushort,
            &binsearch_right_ushort,
        },
    },
    
#line 86
    {NPY_INT,
        {
            &binsearch_left_int,
            &binsearch_right_int,
        },
    },
    
#line 86
    {NPY_UINT,
        {
            &binsearch_left_uint,
            &binsearch_right_uint,
        },
    },
    
#line 86
    {NPY_LONG,
        {
            &binsearch_left_long,
            &binsearch_right_long,
        },
    },
    
#line 86
    {NPY_ULONG,
        {
            &binsearch_left_ulong,
            &binsearch_right_ulong,
        },
    },
    
#line 86
    {NPY_LONGLONG,
        {
            &binsearch_left_longlong,
            &binsearch_right_longlong,
        },
    },
    
#line 86
    {NPY_ULONGLONG,
        {
            &binsearch_left_ulonglong,
            &binsearch_right_ulonglong,
        },
    },
    
#line 86
    {NPY_FLOAT,
        {
            &binsearch_left_float,
            &binsearch_right_float,
        },
    },
    
#line 86
    {NPY_DOUBLE,
        {
            &binsearch_left_double,
            &binsearch_right_double,
        },
    },
    
#line 86
    {NPY_LONGDOUBLE,
        {
            &binsearch_left_longdouble,
            &binsearch_right_longdouble,
        },
    },
    
#line 86
    {NPY_CFLOAT,
        {
            &binsearch_left_cfloat,
            &binsearch_right_cfloat,
        },
    },
    
#line 86
    {NPY_CDOUBLE,
        {
            &binsearch_left_cdouble,
            &binsearch_right_cdouble,
        },
    },
    
#line 86
    {NPY_CLONGDOUBLE,
        {
            &binsearch_left_clongdouble,
            &binsearch_right_clongdouble,
        },
    },
    
#line 86
    {NPY_DATETIME,
        {
            &binsearch_left_datetime,
            &binsearch_right_datetime,
        },
    },
    
#line 86
    {NPY_TIMEDELTA,
        {
            &binsearch_left_timedelta,
            &binsearch_right_timedelta,
        },
    },
    
#line 86
    {NPY_HALF,
        {
            &binsearch_left_half,
            &binsearch_right_half,
        },
    },
    
};

static PyArray_BinSearchFunc *genbinsearch_map[] = {
    &npy_binsearch_left,
    &npy_binsearch_right,
};

static NPY_INLINE PyArray_BinSearchFunc*
get_binsearch_func(PyArray_Descr *dtype, NPY_SEARCHSIDE side)
{
    static npy_intp num_funcs = sizeof(_binsearch_map) /
                                sizeof(_binsearch_map[0]);
    npy_intp min_idx = 0;
    npy_intp max_idx = num_funcs;
    int type = dtype->type_num;

    if (side >= NPY_NSEARCHSIDES) {
        return NULL;
    }

    /*
     * It seems only fair that a binary search function be searched for
     * using a binary search...
     */
    while (min_idx < max_idx) {
        npy_intp mid_idx = min_idx + ((max_idx - min_idx) >> 1);

        if (_binsearch_map[mid_idx].typenum < type) {
            min_idx = mid_idx + 1;
        }
        else {
            max_idx = mid_idx;
        }
    }

    if (min_idx < num_funcs && _binsearch_map[min_idx].typenum == type) {
        return _binsearch_map[min_idx].binsearch[side];
    }

    if (dtype->f->compare) {
        return genbinsearch_map[side];
    }

    return NULL;
}

#line 74

static struct argbinsearch_map _argbinsearch_map[] = {
    /* If adding new types, make sure to keep them ordered by type num */
    #line 86
    {NPY_BOOL,
        {
            &argbinsearch_left_bool,
            &argbinsearch_right_bool,
        },
    },
    
#line 86
    {NPY_BYTE,
        {
            &argbinsearch_left_byte,
            &argbinsearch_right_byte,
        },
    },
    
#line 86
    {NPY_UBYTE,
        {
            &argbinsearch_left_ubyte,
            &argbinsearch_right_ubyte,
        },
    },
    
#line 86
    {NPY_SHORT,
        {
            &argbinsearch_left_short,
            &argbinsearch_right_short,
        },
    },
    
#line 86
    {NPY_USHORT,
        {
            &argbinsearch_left_ushort,
            &argbinsearch_right_ushort,
        },
    },
    
#line 86
    {NPY_INT,
        {
            &argbinsearch_left_int,
            &argbinsearch_right_int,
        },
    },
    
#line 86
    {NPY_UINT,
        {
            &argbinsearch_left_uint,
            &argbinsearch_right_uint,
        },
    },
    
#line 86
    {NPY_LONG,
        {
            &argbinsearch_left_long,
            &argbinsearch_right_long,
        },
    },
    
#line 86
    {NPY_ULONG,
        {
            &argbinsearch_left_ulong,
            &argbinsearch_right_ulong,
        },
    },
    
#line 86
    {NPY_LONGLONG,
        {
            &argbinsearch_left_longlong,
            &argbinsearch_right_longlong,
        },
    },
    
#line 86
    {NPY_ULONGLONG,
        {
            &argbinsearch_left_ulonglong,
            &argbinsearch_right_ulonglong,
        },
    },
    
#line 86
    {NPY_FLOAT,
        {
            &argbinsearch_left_float,
            &argbinsearch_right_float,
        },
    },
    
#line 86
    {NPY_DOUBLE,
        {
            &argbinsearch_left_double,
            &argbinsearch_right_double,
        },
    },
    
#line 86
    {NPY_LONGDOUBLE,
        {
            &argbinsearch_left_longdouble,
            &argbinsearch_right_longdouble,
        },
    },
    
#line 86
    {NPY_CFLOAT,
        {
            &argbinsearch_left_cfloat,
            &argbinsearch_right_cfloat,
        },
    },
    
#line 86
    {NPY_CDOUBLE,
        {
            &argbinsearch_left_cdouble,
            &argbinsearch_right_cdouble,
        },
    },
    
#line 86
    {NPY_CLONGDOUBLE,
        {
            &argbinsearch_left_clongdouble,
            &argbinsearch_right_clongdouble,
        },
    },
    
#line 86
    {NPY_DATETIME,
        {
            &argbinsearch_left_datetime,
            &argbinsearch_right_datetime,
        },
    },
    
#line 86
    {NPY_TIMEDELTA,
        {
            &argbinsearch_left_timedelta,
            &argbinsearch_right_timedelta,
        },
    },
    
#line 86
    {NPY_HALF,
        {
            &argbinsearch_left_half,
            &argbinsearch_right_half,
        },
    },
    
};

static PyArray_ArgBinSearchFunc *genargbinsearch_map[] = {
    &npy_argbinsearch_left,
    &npy_argbinsearch_right,
};

static NPY_INLINE PyArray_ArgBinSearchFunc*
get_argbinsearch_func(PyArray_Descr *dtype, NPY_SEARCHSIDE side)
{
    static npy_intp num_funcs = sizeof(_argbinsearch_map) /
                                sizeof(_argbinsearch_map[0]);
    npy_intp min_idx = 0;
    npy_intp max_idx = num_funcs;
    int type = dtype->type_num;

    if (side >= NPY_NSEARCHSIDES) {
        return NULL;
    }

    /*
     * It seems only fair that a binary search function be searched for
     * using a binary search...
     */
    while (min_idx < max_idx) {
        npy_intp mid_idx = min_idx + ((max_idx - min_idx) >> 1);

        if (_argbinsearch_map[mid_idx].typenum < type) {
            min_idx = mid_idx + 1;
        }
        else {
            max_idx = mid_idx;
        }
    }

    if (min_idx < num_funcs && _argbinsearch_map[min_idx].typenum == type) {
        return _argbinsearch_map[min_idx].argbinsearch[side];
    }

    if (dtype->f->compare) {
        return genargbinsearch_map[side];
    }

    return NULL;
}


#endif

