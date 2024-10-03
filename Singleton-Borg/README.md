
Informações mais relevantes do Singleton:

1. GOF - Gang of Four - Livro de Padrão de Projetos
2. Garantir que uma classe tenha somente uma instância, e fornecer um ponto global de acesso;
3. A instância deve ser obtida sem chamar o construtor. Devemos pedir por método
4. Quem gerencia a criação de uma nova instância é a própria classe, que também cria as instâncias

> class Singleton:
>    instance: Singleton
> 
>    @classmethod
>    def get_instance(cls) -  Singleton:
>        if not hasattr(cls, 'instance'):
>            cls.instance = Singleton()
>        return cls.instance
