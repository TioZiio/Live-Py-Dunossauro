
Informações mais relevantes do Singleton:

1. GOF - Gang of Four - Livro de Padrão de Projetos
2. Garantir que uma classe tenha somente uma instância, e fornecer um ponto global de acesso
3. A instância deve ser obtida sem chamar o construtor. Devemos pedir por método
4. Quem gerencia a criação de uma nova instância é a própria classe, que também cria as instâncias

> Estrutura básica do Singleton:  

~~~python  
from __future__ import annotations

class Singleton:  
    instance: Singleton  
     
    @classmethod  
    def get_instance(cls) -> Singleton:  
        if not hasattr(cls, 'instance'):  
            cls.instance = Singleton()  
        return cls.instance
~~~

> Se a linguagem de programação possuir MetaClasses:
> Segundo ALAN KAY:  
> Criador da linguagem de programação SMALLTALK
> Um dos pais da Orientação a Objeto (OOP)
>> SE A LINGUAGEM NÃO TEM METACLASSES, ELA NÃO É ORIENTADA A OBJETOS  

~~~python  
class MetaSingleton(type):  
    _instances = {}  
    def __call__(cls, *args, **kwargs):  
        if cls not in cls._instances:  
            cls._instances[cls] = super().__call__(*args, **kwargs)  
        return cls._instances[cls]  
  
class Singleton(metaclass=MetaSingleton):  
        ...  
~~~

>__call__ é um atributo de instância normalmente, porque é chamado. Entretanto, nesta classe ele é m atributo de classe (Type).
