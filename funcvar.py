#!/usr/bin/python3

__all__ = ("FunctionVar",)


class FunctionVar(object):
    
    __slots__ = ("__msg", "__func", "__preserve")
    
    def __init__(self, startmsg="", func=None, preserve=False):
        self.__msg      = str(startmsg)
        self.__func     = func
        self.__preserve = preserve
    
    def __call__(self, *a, **k):
        
        ret = self.__func(*a, **k)
        
        if not self.__preserve:
            self.__msg = str(ret)
        
        return ret;
    
    def __repr__(self):
        return self.__msg