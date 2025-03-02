// O que é uma thread e como ela difere de um processo?
// Uma thread é a unidade básica de execução dentro de um processo. Ela representa uma sequência de instruções que podem ser executadas de forma independente, mas que compartilham o mesmo espaço de memória e recursos do processo ao qual pertencem. Uma thread é parte de um processo e, portanto, todos os threads de um mesmo processo têm acesso às mesmas variáveis, arquivos abertos e outros recursos do processo.

// A principal diferença entre processo e thread é que um processo é uma instância de execução de um programa, que possui seu próprio espaço de memória, recursos e contexto de execução. Já uma thread é uma subunidade dentro desse processo, compartilhando o mesmo espaço de memória, mas com seu próprio contador de programa, pilha e registradores.

// Processo: Tem seu próprio espaço de memória, recursos e contexto de execução.
// Thread: Compartilha o espaço de memória do processo, mas tem seu próprio contador de programa, pilha e registradores