# Orientação a Objeto (OOP):
    ## Classe é a Forma de bolo;
    ## Instância é a utilização da classe, um exemplar;
    ## Classe é um objeto;
---
>           classe C:
>               a = 1
>           C.a
> 
>           C.__class__ > type
>           type(C) > type
>           isintance(C, type) > True
>           isintance(object, type) > True
---
    ### A própria Classe é um objeto, e o próprio objeto vem de uma classe, sendo uma instância;
---
>        class C:
>           def metodo_bacana(cls): 
>               ...
> 
>        C.__dict__ > mappingproxy({
>               '__module__': '__main__',
>               'metodo_bacana': <function C.metodo_bacana at 0x73f73b5ac540>,
>               '__dict__': <attribute '__dict__' of 'C' objects>,
>               '__weakref__': <attribute '__weakref__' of 'C' objects>,
>               '__doc__': None
>       })
---
    ### self - corresponde a um atributo da instancia.
    ### cls - corresponde a m atributo da própria classe.

*       !> Logo, a Classe já é um objeto, sendo instância de alguém.

    > Uso do decorador @classmethod

        class C:
            @classmethod
            def metodo_bacana(cls): 
                return 'Fui chamado'

        C.metodo_bacana() > 'Fui chamado'
        
*       > O @classmethod já cria a instância, como se fosse:
            a = C()
            a.metodo_bacana > 'Fui chamado'
    
*       > Logo o @classmethod define o metodo_bacana como um metodo e não um atributo da instância, como um função;
        
> Padrões Criacionais:
    
    !> Como os Objetos são criados? objetivo desses padrões.
        Ex.:
*           **Builder**: Criação de instâncias em etapas;
*           **Factory**: Interfaces padrões para criação de objetos distintos, 'Fábrica de Classes';
*           **Prototype**: Criação de um objeto a partir de outro, como cópia;
*           **Singleton**: Garantir que uma classe crie apenas uma instância e forneça um ponto de global de acesso.
        As criações desses padrões é feita por atributos e métodos de classe.

> Singleton:
    
    !> GOF - Gang of Four - Livro de Padrão de Projetos
    |> Garantir que uma classe tenha somente uma instância, e fornecer um ponto global de acesso;

    !> A instância deve ser obtida sem chamar o construtor. Devemos pedir por método.
        > Método construtor do Python - __new__
        > Chamar - C() , onde '()' é o chamar a classe.

        class Singleton:
            instance: Singleton

            @classmethod
            def get_instance(cls) -> Singleton:
                if not hasattr(cls, 'instance'):
                    cls.instance = Singleton()
                return cls.instance
        
        > Quem gerencia a criação de uma nova instância é a própria classe, que também cria as instâncias;
        > O get_instance é o ponto único;
        > Caso o Atributo de classe não esteja instanciado, a própria classe o cria.
                |-> cls.instance = Singleton()

         

