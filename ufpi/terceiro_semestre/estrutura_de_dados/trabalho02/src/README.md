##### UNIVERSIDADE FEDERAL DO PIAUÍ 
##### CENTRO DE EDUCAÇÃO ABERTA E A DISTÂNCIA
##### CURSO DE LICENCIATURA EM COMPUTAÇÃO
##### DISCIPLINA: ESTRUTURA DE DADOS
##### PROFª Dr. Francisco Airton Silva
##### Aluno: David Sousa da Silva

### TRABALHO 02

Você deve implementar um sistema que representa um banco. Abaixo serão descritos os requisitos deste sistema. Para atingir a nota máxima neste trabalho, deverá atender a todos os tais requisitos.

Você deverá criar as seguintes classes (no mínimo):

- `Cliente`, que possui os atributos: `String nome` e `String cpf`.
- `Atendente`, que possui o atributo: `String nome`.
- `FilaClientes`, que possui o atributo `Clientes[] clientes` e toda a implementação dos métodos de fila mostrado na vídeo-aula.
- `Banco`, que possui os atributos: `Atendente[] atendentes` e `FilaClientes filaClientes`.
- `Atendimento`, que possui os atributos: `Cliente cliente` e `Atendente atendente`.
- `BancoEmFuncionamento`, onde, contendo um método `main`, irá fazer o banco funcionar, criando atendentes, clientes e uma fila de clientes. Vai adicionar os clientes na fila e depois retirá-los da fila para criar atendimentos.

Não se deve usar a classe List (ou derivadas) nativa do Java para este trabalho. Caso use, receberá zero na nota.

Esta especificação de sistema acima é só uma base, sinta-se livre para incrementar a ideia e tornar seu trabalho mais rico de detalhes.

Postar no SIGAA um arquivo `.zip` contendo todas as classes do seu sistema.

### Algumas considerações

- Adicionei um menu para deixar o prompt mais visual.
- Incluí a opção 6 no menu para agilizar o processo de avaliação.
- Na classe `Banco`, modifiquei o atributo `Atendente[] atendentes` para ser implementado por uma classe de `fila`, assim como a classe `Cliente`.
- Implementei a classe `FilaAtendentes` com a funcionalidade de reinserir (reenfileirar) os atendentes na fila após atenderem os clientes. Isso é comum nos atendimentos bancários, onde os atendentes retornam à `fila` após cada atendimento para ficarem disponíveis novamente.

### Configurações da minha máquina

- **Sistema Operacional:** `Linux Ubuntu 22.04.4 LTS`
- **Versão JAVA:** `javac 17.0.6`
- **IDE:** `Visual Studio Code`

