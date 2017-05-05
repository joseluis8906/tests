#!/bin/python

import urllib.request
import re

if __name__ == "__main__":
    
    cuentas = []
    for n in [1,2,3,4,5,6,7,8,9]:

        a = urllib.request.urlopen ("http://puc.com.co/cuentas/clase/{}".format(n)).read()
        
        ptr = re.compile ('<li><a href="/*\w*"><span class="code">*\w*</span> *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]*</a></li>')
        l = re.findall (ptr, str(a.decode()))
        for m in l:
            code = re.search ('(?<="code">)\w*', m).group(0)
            name = re.search ('(?<=</span>) *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]* *[\w,\/\-]*', m).group(0)
            cuentas.append ('INSERT INTO "AccountingAccount"("Code", "Name") VALUES(\'{}\', \'{}\')'.format (code.strip(), name.strip()))
        
    f = open ("cuentas.sql", "w")
    f.write (";\n".join(cuentas))
    f.close ()

