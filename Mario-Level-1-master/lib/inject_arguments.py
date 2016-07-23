#!/usr/bin/env python3
# -*-coding:Utf-8 -*


def injectArguments(inFunction):
    """
    Decorator injecting arguments of a method as attributes
    
    Found here: http://code.activestate.com/recipes/577382-keyword-argument-injection-with-python-decorators/
    
    """
    
    def outFunction(*args, **kwargs):
        _self = args[0]
        _self.__dict__.update(kwargs)
        
        # Get all of argument's names of the inFunction
        _total_names = inFunction.__code__.co_varnames[1:inFunction.__code__.co_argcount]
        # Get all of the values
        _values = args[1:]
        # Get only the names that don't belong to kwargs
        _names = [n for n in _total_names if not n in kwargs]

        # Match argument names with values and update __dict__
        _self.__dict__.update(zip(_names,_values))
        
        # Add default value for non-specified arguments
        if inFunction.__defaults__:
            nb_defaults = len(_names) - len(_values)
            _self.__dict__.update(zip(_names[-nb_defaults:], inFunction.__defaults__[-nb_defaults:]))
        
        return inFunction(*args,**kwargs)

    return outFunction


if __name__=='__main__':
    class Test:
        @injectArguments
        def __init__(self, name, surname, default='lol'):
            pass
    
    t = Test('mickey', surname='mouse')
    assert(t.name == 'mickey' and t.surname == 'mouse' and t.default == 'lol')
