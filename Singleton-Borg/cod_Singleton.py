from __future__ import annotations

# Código Base:
"""
class Singleton:  
    instance: Singleton
        
    @classmethod  
    def get_instance(cls) -> Singleton:  
        if not hasattr(cls, 'instance'):  
            cls.instance = Singleton()  
        return cls.instance
"""

# Código com 'privação/sobreescrever':
"""
class Singleton:
    instance: Singleton
    
    def __new__(cls) -> Singleton:
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
"""

# Código usando MetaClasses:
"""
class MetaSingleton(type):
    _instances = {}
   
   def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
"""

# Código com Linguagem Dinâmica:
"""
from functools import cache

@cache
class Singleton: ...
"""

# Código evitando o uso de cache (Dunossauro)
"""
class _Singleton: ...

sing = _Singleton()

def Singleton():
    return sing
"""
