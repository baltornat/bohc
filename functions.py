#!/usr/bin/env python3

import hashlib as h
from colored import fg
import itertools

pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"    #Item pool 

def try_md5(inputhash):
    s = ""
    out = h.md5(s.encode()).hexdigest()
    if out == inputhash:
        return ""

    for i in range(1, 8):
        print(fg("green"), "Trying length", fg("white"), i)
        for item in itertools.product(pool, repeat=i):  #Try all the combinations with length=1, then lenght=2... 
            s = "".join(item)
            out = h.md5(s.encode()).hexdigest()
            if out == inputhash:
                return s
            else:
                continue        
        
def try_sha1(inputhash):
    s = ""
    out = h.sha1(s.encode()).hexdigest()
    if out == inputhash:
        return ""

    for i in range(1, 8):
        print(fg("green"), "Trying length", fg("white"), i)
        for item in itertools.product(pool, repeat=i):  #Try all the combinations with length=1, then lenght=2...
            s = "".join(item)
            out = h.sha1(s.encode()).hexdigest()
            if out == inputhash:
                return s
            else:
                continue
            
        
def try_sha224(inputhash):
    s = ""
    out = h.sha224(s.encode()).hexdigest()
    if out == inputhash:
        return ""

    for i in range(1, 8):
        print(fg("green"), "Trying length", fg("white"), i)
        for item in itertools.product(pool, repeat=i):  #Try all the combinations with length=1, then lenght=2...
            s = "".join(item)
            out = h.sha224(s.encode()).hexdigest()
            if out == inputhash:
                return s
            else:
                continue



def try_sha256(inputhash):
    s = ""
    out = h.sha256(s.encode()).hexdigest()
    if out == inputhash:
        return ""
    
    for i in range(1, 8):
        print(fg("green"), "Trying length", fg("white"), i)
        for item in itertools.product(pool, repeat=i):  #Try all the combinations with length=1, then lenght=2...
            s = "".join(item)
            out = h.sha256(s.encode()).hexdigest()
            if out == inputhash:
                return s
            else:
                continue
        

def try_sha384(inputhash):
    s = ""
    out = h.sha384(s.encode()).hexdigest()
    if out == inputhash:
        return ""
    
    for i in range(1, 8):
        print(fg("green"), "Trying length", fg("white"), i)
        for item in itertools.product(pool, repeat=i):  #Try all the combinations with length=1, then lenght=2...
            s = "".join(item)
            out = h.sha384(s.encode()).hexdigest()
            if out == inputhash:
                return s
            else:
                continue 
        
        
def try_sha512(inputhash):
    s = ""
    out = h.sha512(s.encode()).hexdigest()
    if out == inputhash:
        return ""

    for i in range(1, 8):
        print(fg("green"), "Trying length", fg("white"), i)
        for item in itertools.product(pool, repeat=i):  #Try all the combinations with length=1, then lenght=2...
            s = "".join(item)
            out = h.sha512(s.encode()).hexdigest()
            if out == inputhash:
                return s
            else:
                continue

