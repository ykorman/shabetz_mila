# coding=utf-8

import ctypes

def run_demo():
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


class Hspell:
	def __init__(self):
		# load hspell dynamic library, compiled from sources of hspell-1.2
		self.hspell_lib = ctypes.cdll.LoadLibrary("hspell/libhspell.so")
		# set location of Hebrew dictionary
		self.dict_location = ctypes.c_char_p("hspell/hebrew.wgz")
		self.hspell_lib.hspell_set_dictionary_path(dict_location)
		# initialize hspell dict
		self.dict_radix = ctypes.POINTER(ctypes.c_int)()
		res = self.hspell_lib.hspell_init(ctypes.byref(dict_radix),0)
		if (res != 0):
			raise Exception('Failed to initialize hspell')
		# allocate integer for the check_word function (later used)
		self.preflen = ctypes.c_int()

	def __del__(self):
		self.hspell_lib.hspell_uninit(self.dict_radix)

	def check_word(self, word):
		encoded_word = ctypes.c_char_p(word.encode("iso8859_8"))
		res = self.hspell_lib.hspell_check_word(self.dict_radix, encoded_word, ctypes.byref(self.preflen))
		if (res == 1):
			return True
		else:
			return False

if __name__ == '__main__':
	run_demo()


		