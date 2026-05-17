Budega is a Esoteric programming language.

(Read-me in Portuguese)

# Budega

![Logo do Projeto](Logo.png)

Acrônimo para: **B**ando de **U**tilitários **D**uvidosos para **E**mendar **G**ambiarras e **A**pps.

É uma linguagem esotérica feita para a disciplina de Paradigmas de Programação que se baseia na linguagem popular cearence, se valendo de gírias e bordões conhecidos para compor a própria sintaxe.

O objetivo desta é divulgar e homenagear a rica e vasta cultura do interior cearense como forma de linguagem de programação

Budega é uma gíria para uma pequena mercearia, entretanto pode ser usado como sinônimo para "qualquer coisa", como em "Pega aquela budega pra mim" ou "Aquela budega não funciona!".

## Sintaxe

### Tipos primitivos

A budega conta com uma rica coleção de tipos primitivos, em sua maior parte derivada da linguagem C.

<table>
  <tr>
    <th colspan="2" align="center">Tipos Primitivos</th>
  </tr>
  <tr>
    <td>Inteiro</td>
    <td>inteirinho</td>
  </tr>
  <tr>
    <td>Flutuante</td>
    <td>banda</td>
  </tr>
    <tr>
    <td>Dupla Precisão</td>
    <td>taiada</td>
  </tr>
    <tr>
    <td>Caractere</td>
    <td>garrancho</td>
  </tr>
  <tr>
    <td>Booleano</td>
    <td></td>
  </tr>
</table>

Também temos modificadores para os tipos primitivos:

<table>
  <tr>
    <th colspan="2" align="center">Modificadores</th>
  </tr>
  <tr>
    <td>Prefixo de Variável</td>
    <td>um / uma</td>
  </tr>
  <tr>
    <td>Longo</td>
    <td>bocado</td>
  </tr>
  <tr>
    <td>Vetor</td>
    <td>ruma de [tamanho][n]...[n-dimensão]</td>
  </tr>
  <tr>
    <td>Sufixo de ponteiro</td>
    <td>acolá</td>
  </tr>
  <tr>
    <td>Palavra Auxiliar</td>
    <td>de</td>
  </tr>
    <tr>
    <td>Constante</td>
    <td></td>
  </tr>
</table>

O prefixo de variável é uma característica da linguagem que facilita a leitura do código, ela indica ao compilador que se trata de uma variável, a escolha por `um` ou `uma` é condicionada à concordância gramatical, entretanto ambas palavras irão funcionar da mesma forma.

O sufixo de ponteiro é uma segunda característica da budega que a permite operar em baixo nível assim como C, diferentemente de C que utiliza prefixos para isso o indicador de ponteiro vem após o nome da variável, também como forma de manter concordância.

A palavra auxiliar `de` é totalmente opcional e é uma palavra reservada ignorada pelo compilador, exceto no vetor que se torna de uso obrigatório.

Exemplos de código:
```
um inteirin de milho = 10;
uma ruma de [5] banda de cavalos = {1.1, 2.2, 3.3, 4.4, 5.5};
um interin de silo acolá = milho acolá;
```

### Operadores Lógicos

<table>
  <tr>
    <th colspan="2" align="center">Operadores Lógicos</th>
  </tr>
  <tr>
    <td>Negação</td>
    <td>ai_dentro</td>
  </tr>
  <tr>
    <td>Interseção</td>
    <td>emenda</td>
  </tr>
  <tr>
    <td>Junção</td>
    <td>mói</td>
  </tr>
    <tr>
    <td>Inclusão</td>
    <td>implica</td>
  </tr>
    <tr>
    <td>Igualdade</td>
    <td>fresca</td>
  </tr>
</table>

Normalmente a maior parte das linguagens comerciais não implementa a Implicação e a Biimplicação, não é o caso da budega em que temos esses operadores lógicos.

### Estrutura Condicional

<table>
  <tr>
    <th colspan="2" align="center">Estrutura Condicional</th>
  </tr>
  <tr>
    <td>Se</td>
    <td></td>
  </tr>
  <tr>
    <td>Se não</td>
    <td></td>
  </tr>
      <td>Escolha</td>
    <td></td>
  </tr>
</table>

### Estruturas de Repetição

<table>
  <tr>
    <th colspan="2" align="center">Estruturas de Repetição</th>
  </tr>
  <tr>
    <td>Enquanto</td>
    <td>Arrudeia</td>
  </tr>
  <tr>
    <td>Faça</td>
    <td></td>
  </tr>
    <tr>
    <td>Para</td>
    <td></td>
  </tr>
  <tr>
    <td>Para Cada</td>
    <td></td>
  </tr>
</table>

<table>
  <tr>
    <th colspan="2" align="center">Controle de Fluxo de Dados</th>
  </tr>
  <tr>
    <td>Continuar</td>
    <td></td>
  </tr>
  <tr>
    <td>Quebrar</td>
    <td></td>
  </tr>

</table>

### Funções

### Entrada e Saída

<table>
  <tr>
    <th colspan="2" align="center">Funções de E/S</th>
  </tr>
  <tr>
    <td>Imprimir</td>
    <td></td>
  </tr>
  <tr>
    <td>Escanear</td>
    <td></td>
  </tr>

</table>

## Outros

Operadores aritiméticos, ordem de precedência e funções menores são as mesmas encontradas em C.