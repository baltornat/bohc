#!/usr/bin/env python3

import time
import datetime
from colored import fg
from functions import try_md5, try_sha1, try_sha224, try_sha256, try_sha384, try_sha512

def convert(n):
    return str(datetime.timedelta(seconds = n))

inputhash = input("Insert an hash value (max output length = 8): ")
hashlength = len(inputhash)   

if hashlength == 32:
    print(fg("yellow"), "Inserted hash is MD5")
    time.sleep(1)
    print(fg("cyan"), "Start cracking...")
    time.sleep(1)
    starttime = time.time()
    print(fg("red"), "Password found: ", fg("yellow"), try_md5(inputhash))
    print(fg("white"), "Time elapsed: ", fg('cyan'), convert(round((time.time() - starttime), 2)), fg('white'), "seconds")
elif hashlength == 40:
    print(fg("yellow"), "Inserted hash is SHA1")
    time.sleep(1)
    print(fg("cyan"), "Start cracking...")
    time.sleep(1)
    starttime = time.time()
    print(fg("red"), "Password found: ", fg("yellow"), try_sha1(inputhash))
    print(fg("white"), "Time elapsed: ", fg('cyan'), convert(round((time.time() - starttime), 2)), fg('white'), "seconds")
elif hashlength == 56:
    print(fg("yellow"), "Inserted hash is SHA224")
    time.sleep(1)
    print(fg("cyan"), "Start cracking...")
    time.sleep(1)
    starttime = time.time()
    print(fg("red"), "Password found: ", fg("yellow"), try_sha224(inputhash))
    print(fg("white"), "Time elapsed: ", fg('cyan'), convert(round((time.time() - starttime), 2)), fg('white'), "seconds")
elif hashlength == 64:
    print(fg("yellow"), "Inserted hash is SHA256")
    time.sleep(1)
    print(fg("cyan"), "Start cracking...")
    time.sleep(1)
    starttime = time.time()
    print(fg("red"), "Password found: ", fg("yellow"), try_sha256(inputhash))
    print(fg("white"), "Time elapsed: ", fg('cyan'), convert(round((time.time() - starttime), 2)), fg('white'), "seconds")
elif hashlength == 96:
    print(fg("yellow"), "Inserted hash is SHA384")
    time.sleep(1)
    print(fg("cyan"), "Start cracking...")
    time.sleep(1)
    starttime = time.time()
    print(fg("red"), "Password found: ", fg("yellow"), try_sha384(inputhash))
    print(fg("white"), "Time elapsed: ", fg('cyan'), convert(round((time.time() - starttime), 2)), fg('white'), "seconds")
elif hashlength == 128:
    print(fg("yellow"), "Inserted hash is SHA512")
    time.sleep(1)
    print(fg("cyan"), "Start cracking...")
    time.sleep(1)
    starttime = time.time()
    print(fg("red"), "Password found: ", fg("yellow"), try_sha512(inputhash))
    print(fg("white"), "Time elapsed: ", fg('cyan'), convert(round((time.time() - starttime), 2)), fg('white'), "seconds")
    


        