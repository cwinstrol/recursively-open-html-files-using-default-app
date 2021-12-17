import os
#dn=''
def of(dn):
    for p,ds,fs in os.walk(dn):
        for f in fs:
            if f.endswith('.html'):
                os.startfile(os.path.normpath(p+'\\'+f))
