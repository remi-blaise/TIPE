#!/usr/bin/env python3
# -*-coding:Utf-8 -*


def inject_arguments(inFunction):
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
            if nb_defaults > 0:
                _self.__dict__.update(zip(
                    _names[-nb_defaults:], inFunction.__defaults__[-nb_defaults:]
                ))
        
        return inFunction(*args,**kwargs)

    return outFunction


if __name__=='__main__':
    class Test:
        @inject_arguments
        def __init__(self, name, surname, default = 'lol'):
            pass
    
    t = Test('mickey', surname='mouse')
    assert(t.name == 'mickey' and t.surname == 'mouse' and t.default == 'lol')
    
    class Test:
        @inject_arguments
        def __init__(self, default='lol'):
            pass
    
    t = Test(2)
    assert(t.default == 2)
    
    class Child(Test):
        @inject_arguments
        def __init__(self, minus = None, malus = None, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
    c = Child(3, 4)
    assert(c.minus == 3 and c.malus == 4 and c.default == 'lol')
    
    c = Child(3, 4, 'hey')
    assert(c.minus == 3 and c.malus == 4 and c.default == 'hey')
    
    class A():
        @inject_arguments
        def __init__(self, a1):
            pass

    class B(A):
        @inject_arguments
        def __init__(self, b1 = None, b2 = None, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
    b = B(0, 1, 2)
    assert(b.b1 == 0 and b.b2 == 1 and b.a1 == 2)
