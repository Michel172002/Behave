#language: pt
Funcionalidade: Buscar o professor da Materia Teste de Software

    '''
    Eu como usuario vou entrar no sistema do sigaa e buscar a
    materia de Teste de Software e seu professor
    '''

    Cenario: Buscar o professor da Materia Teste de Software
    Dado Acessar novamento o sigaa
    Quando Realizar o login novamente
    E abro o menu Ensino
    E clico em consultar turma
    E em "ofertadas ao curso" seleciono ADS
    E busco as turmas disponiveis
    E clico em visualizar menu da Turma de Teste de software
    E clico em vizualizar turma
    E salvo o nome do professor da turma em um arquivo txt
    E clico em voltar novamente
    Então clico em sair novamente