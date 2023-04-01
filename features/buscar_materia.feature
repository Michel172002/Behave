#language: pt
Funcionalidade: Buscar em Estrutura curricular as Materias de ADS
    '''
    Eu como usuario vou entrar no sistema sigaa do ifsc, 
    e buscar o curso de ads e sua estrutura curricular
    '''

    Cenario: Buscar em Estrutura curricular as Materias de ADS
    Dado Acessar o sistema Sigaa do ifsc
    Quando Realizo o login no sistema
    E expando o menu Ensino
    E clico em Consultar Estrutura curricular
    E busco o curso de ADS de canoinhas
    E clico em Relatorio da Estrutura curricular do curso ADS 2021.1
    E salvo as materias em um arquivo txt
    E clico em voltar  
    Então clico em sair