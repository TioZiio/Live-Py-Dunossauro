
Arquitetura limpa:

Ordem de produção de software (padrão):

1. Entities 
> Este primeira etapa consiste na definição das regras do negócio ou as funcionalidades;
> Para cada regra de negócio pode-se criar um arquivo de documentação;
2. Use Cases 
> A Lógica para cada regra/funcionalidade, como validações ou verificações de type;
3. Controller 
> Mediador de dados, entre o Use Cases e a View. Recebe uma interação do usuário e conecta com a lógica (sinal);
4. Presenters
> Froamta a saída do Use Cases oara o Usuário;
5. Gateways (Repositórios)
> Fornecem dados externos, como APIs, ou BDs;
6. Web/Device/DB/GUI
> Tela final, onde o usuário toma decisões, como mandar relatórios, ou simplesmente apertar um botãozinho;
