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

# Código PolySingleton
"""
from functools import cache

@cache
class Singleton:
    def __init__(self, context=None, **kwargs):
        self.context = context

db0 = Singleton('sqlite')
db1 = Singleton('mariadb')
db2 = Singleton('sql', comida='arroz')
"""

# Borg
"""
class Borg:
    _share_state = {}
    def __init__(self):
        self.__dict__ = self.share_state
"""

# MetaBorg do Dunossauro
"""
class MetaBorg(type):
    _state = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._state:
            cls._state[cls] = cls.__new__(cls)
        return cls._state[cls]
"""

# RegisBorg
"""
class RegisBorg:
    _instance = {}
    def __init__(self, context=None):
        if not context in self._instance:
            self._instance[context] = self.__dict__
        else:
            self.__dict__ = self._instance[context]
"""
