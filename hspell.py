# coding=utf-8

import ctypes

# load hspell dynamic library, compiled from sources of hspell-1.2
hspell = ctypes.cdll.LoadLibrary("hspell/libhspell.so")

# set location of Hebrew dictionary
dict_location = ctypes.c_char_p("hspell/hebrew.wgz")
hspell.hspell_set_dictionary_path(dict_location)

# initialize hspell dict
dict_radix = ctypes.POINTER(ctypes.c_int)()
res = hspell.hspell_init(ctypes.byref(dict_radix),0)
print res

# check words
preflen = ctypes.c_int()
test_word = ctypes.c_char_p("hello")
res = hspell.hspell_check_word(dict_radix, test_word, ctypes.byref(preflen))
print res 

unicode_test_word = u"שלום"
test_word = ctypes.c_char_p(unicode_test_word.encode("iso8859_8"))
res = hspell.hspell_check_word(dict_radix, test_word, ctypes.byref(preflen))
print res 

unicode_test_word = u"םולש"
test_word = ctypes.c_char_p(unicode_test_word.encode("iso8859_8"))
res = hspell.hspell_check_word(dict_radix, test_word, ctypes.byref(preflen))
print res 

# free dict
res = hspell.hspell_uninit(dict_radix)
print res

# check dict location
hspell_get_dictionary_path = hspell.hspell_get_dictionary_path
hspell_get_dictionary_path.restype = ctypes.c_char_p
print hspell_get_dictionary_path()
