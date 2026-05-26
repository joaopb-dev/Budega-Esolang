Budega is an esoteric programming language.

(Read-me in Portuguese)

# Budega

![Logo do Projeto](Logo.png)

Acrônimo para: **B**ando de **U**tilitários **D**uvidosos para **E**mendar **G**ambiarras e **A**pps.

Budega é uma linguagem esotérica feita para a disciplina de Paradigmas de Programação. Ela se baseia na linguagem popular cearense, valendo-se de gírias, bordões e expressões do cotidiano para compor a própria sintaxe.

O objetivo da linguagem é divulgar e homenagear a rica e vasta cultura do interior cearense em forma de linguagem de programação, misturando humor regional, estrutura inspirada em C e uma proposta didática para estudar construção de linguagens.

"Budega" é uma gíria para uma pequena mercearia, mas também pode ser usada como sinônimo de "qualquer coisa", como em "Pega aquela budega pra mim" ou "Aquela budega não funciona!".

## Sintaxe

A sintaxe da Budega segue uma estrutura parecida com C: blocos são delimitados por `{` e `}`, instruções terminam com `;`, operadores aritméticos mantêm a mesma precedência de C e chamadas de função usam parênteses.

A diferença é que as palavras-chave foram trocadas por expressões com cara de conversa de feira, mercearia, interior e gambiarra.

### Tipos primitivos

A Budega conta com uma coleção de tipos primitivos, em sua maior parte derivada da linguagem C.

| Tipo | Palavra-chave |
|---|---|
| Inteiro | `inteirinho` |
| Flutuante | `banda` |
| Dupla precisão | `taiada` |
| Caractere | `garrancho` |
| Booleano | `apois` |
| Vazio / sem retorno | `nadinha` |

#### Valores booleanos

| Valor | Palavra-chave |
|---|---|
| Verdadeiro | `valendo` |
| Falso | `nem` |

Exemplo:

```budega
uma apois de tem_cuscuz = valendo;
uma apois de acabou_o_cafe = nem;
```

### Modificadores

| Modificador | Palavra-chave |
|---|---|
| Prefixo de variável | `um` / `uma` |
| Longo | `bocado` |
| Vetor | `ruma de [tamanho][n]...[n-dimensão]` |
| Sufixo de ponteiro | `acolá` |
| Palavra auxiliar | `de` |
| Constante | `num_mexe` |

O prefixo de variável é uma característica da linguagem que facilita a leitura do código. Ele indica ao compilador que se trata de uma variável. A escolha por `um` ou `uma` é condicionada à concordância gramatical, entretanto ambas as palavras funcionam da mesma forma.

O sufixo de ponteiro permite que a Budega opere em baixo nível, assim como C. Diferente de C, que utiliza prefixos para indicar ponteiros, a Budega utiliza um indicador após o nome da variável, também como forma de manter a concordância.

A palavra auxiliar `de` é opcional na maior parte dos casos e é ignorada pelo compilador. A exceção é a declaração de vetores, onde `de` se torna obrigatória para manter a leitura natural da sentença.

Exemplos de código:

```budega
um inteirinho de milho = 10;
uma ruma de [5] banda de cavalos = {1.1, 2.2, 3.3, 4.4, 5.5};
um inteirinho de silo acolá = milho acolá;
num_mexe uma taiada de pi = 3.1415926535;
```

### Operadores lógicos

| Operador | Palavra-chave |
|---|---|
| Negação | `ai_dentro` |
| Interseção / E lógico | `emenda` |
| Junção / OU lógico | `mói` |
| Implicação | `implica` |
| Bi-implicação / equivalência | `fresca` |

Normalmente, a maior parte das linguagens comerciais não implementa implicação e bi-implicação como operadores lógicos diretos. Na Budega, esses operadores existem para reforçar o caráter acadêmico e esotérico da linguagem.

Exemplo:

```budega
uma apois de tem_dinheiro = valendo;
uma apois de tem_fome = valendo;

se_der (tem_dinheiro emenda tem_fome) {
    berra("Bora comprar um salgado.\n");
}
```

### Operadores relacionais e aritméticos

Os operadores aritméticos e relacionais seguem o comportamento de C.

| Operação | Operador |
|---|---|
| Soma | `+` |
| Subtração | `-` |
| Multiplicação | `*` |
| Divisão | `/` |
| Resto | `%` |
| Igualdade | `==` |
| Diferença | `!=` |
| Maior que | `>` |
| Menor que | `<` |
| Maior ou igual | `>=` |
| Menor ou igual | `<=` |

A palavra-chave `fresca` não substitui necessariamente `==`; ela é usada como equivalência lógica entre expressões booleanas.

### Estrutura condicional

| Estrutura | Palavra-chave |
|---|---|
| Se | `se_der` |
| Se não | `se_num_der` |
| Escolha | `escolhe_ai` |
| Caso | `causo` |
| Caso padrão | `se_num_tiver` |

Exemplo:

```budega
um inteirinho de saldo = 15;

se_der (saldo > 20) {
    berra("Hoje tem rapadura.\n");
} se_num_der {
    berra("Hoje é só olhar mesmo.\n");
}
```

Exemplo com escolha:

```budega
um inteirinho de opcao = 2;

escolhe_ai (opcao) {
    causo 1:
        berra("Pegar farinha.\n");
        arreda;
    causo 2:
        berra("Pegar café.\n");
        arreda;
    se_num_tiver:
        berra("Essa budega não tem não.\n");
}
```

### Estruturas de repetição

| Estrutura | Palavra-chave |
|---|---|
| Enquanto | `arrudeia` |
| Faça | `faz_ai` |
| Para | `pra` |
| Para cada | `pra_cada` |

Exemplo com `arrudeia`:

```budega
um inteirinho de contador = 0;

arrudeia (contador < 5) {
    berra("Rodando a budega...\n");
    contador = contador + 1;
}
```

Exemplo com `faz_ai`:

```budega
um inteirinho de tentativa = 0;

faz_ai {
    berra("Tentando de novo.\n");
    tentativa = tentativa + 1;
} arrudeia (tentativa < 3);
```

Exemplo com `pra`:

```budega
pra (um inteirinho de i = 0; i < 10; i = i + 1) {
    berra("Passou mais um.\n");
}
```

Exemplo com `pra_cada`:

```budega
uma ruma de [3] inteirinho de notas = {7, 8, 10};

pra_cada (um inteirinho de nota em notas) {
    berra("%d\n", nota);
}
```

### Controle de fluxo

| Controle | Palavra-chave |
|---|---|
| Continuar | `passa_reto` |
| Quebrar | `arreda` |
| Retornar | `devolve` |

Exemplo:

```budega
pra (um inteirinho de i = 0; i < 10; i = i + 1) {
    se_der (i == 3) {
        passa_reto;
    }

    se_der (i == 8) {
        arreda;
    }

    berra("%d\n", i);
}
```

### Funções

Funções são declaradas com a palavra-chave `peleja`, indicando uma tarefa que a Budega precisa resolver.

| Conceito | Palavra-chave |
|---|---|
| Declarar função | `peleja` |
| Retornar valor | `devolve` |
| Função principal | `budega_principal` |
| Sem retorno | `nadinha` |

Exemplo:

```budega
peleja inteirinho soma(um inteirinho de a, um inteirinho de b) {
    devolve a + b;
}

peleja nadinha mostra_resultado(um inteirinho de valor) {
    berra("Resultado: %d\n", valor);
}
```

A função principal do programa deve se chamar `budega_principal`.

```budega
peleja inteirinho budega_principal() {
    um inteirinho de resultado = soma(2, 3);
    mostra_resultado(resultado);

    devolve 0;
}
```

### Entrada e saída

| Função | Palavra-chave |
|---|---|
| Imprimir | `berra` |
| Escanear / ler entrada | `escuta` |

As funções de entrada e saída seguem uma lógica parecida com `printf` e `scanf`.

Exemplo:

```budega
peleja inteirinho budega_principal() {
    um inteirinho de idade;

    berra("Diga tua idade: ");
    escuta("%d", idade acolá);

    berra("Tu tem %d anos.\n", idade);

    devolve 0;
}
```

### Comentários

Comentários seguem o mesmo padrão de C.

```budega
// Comentário de uma linha

/*
   Comentário de várias linhas.
   Serve pra explicar a gambiarra antes que ela vire mistério.
*/
```

### Exemplo completo

```budega
peleja inteirinho maior_valor(um inteirinho de a, um inteirinho de b) {
    se_der (a > b) {
        devolve a;
    } se_num_der {
        devolve b;
    }
}

peleja inteirinho budega_principal() {
    um inteirinho de x;
    um inteirinho de y;

    berra("Digite dois números: ");
    escuta("%d %d", x acolá, y acolá);

    um inteirinho de maior = maior_valor(x, y);

    escolhe_ai (maior) {
        causo 0:
            berra("Oxente, deu zero.\n");
            arreda;
        se_num_tiver:
            berra("O maior valor foi %d.\n", maior);
    }

    devolve 0;
}
```

## Tabela rápida de palavras-chave

| C / Conceito | Budega |
|---|---|
| `int` | `inteirinho` |
| `float` | `banda` |
| `double` | `taiada` |
| `char` | `garrancho` |
| `bool` | `apois` |
| `true` | `valendo` |
| `false` | `nem` |
| `const` | `num_mexe` |
| `long` | `bocado` |
| ponteiro | `acolá` |
| vetor | `ruma de` |
| `if` | `se_der` |
| `else` | `se_num_der` |
| `switch` | `escolhe_ai` |
| `case` | `causo` |
| `default` | `se_num_tiver` |
| `while` | `arrudeia` |
| `do` | `faz_ai` |
| `for` | `pra` |
| `foreach` | `pra_cada` |
| `continue` | `passa_reto` |
| `break` | `arreda` |
| `return` | `devolve` |
| função | `peleja` |
| `void` | `nadinha` |
| `printf` | `berra` |
| `scanf` | `escuta` |


## Como usar o interpretador

O interpretador da Budega funciona como um tradutor: ele lê um arquivo-fonte escrito em Budega, analisa o código, gera um arquivo em C equivalente e, em seguida, esse arquivo C pode ser compilado normalmente com `gcc`.

### Requisitos

Para usar o interpretador, é necessário ter instalado:

- Python 3;
- um compilador C, como `gcc`, caso você queira compilar e executar o código gerado;
- um arquivo-fonte Budega, normalmente salvo com a extensão `.bdg`.

### Executando a tradução

Com o arquivo `interpreter.py` e um programa Budega no mesmo diretório, execute:

```bash
python interpreter.py arquivo.bdg
```

Exemplo:

```bash
python interpreter.py teste.bdg
```

O interpretador irá analisar o arquivo, traduzir o código para C e gerar um arquivo de saída com extensão `.c`.

### Escolhendo o arquivo de saída

Também é possível informar manualmente o nome do arquivo C que será gerado:

```bash
python interpreter.py arquivo.bdg saida.c
```

Exemplo:

```bash
python interpreter.py teste.bdg teste.c
```

### Compilando o código gerado

Depois que o arquivo `.c` for criado, compile com `gcc`:

```bash
gcc teste.c -o programa
```

Em seguida, execute o programa:

```bash
./programa
```

No Windows, a execução pode ser feita assim:

```bash
programa.exe
```

### Exemplo completo de uso

Considere um arquivo chamado `teste.bdg`:

```budega
peleja inteirinho budega_principal() {
    um inteirinho de idade;

    berra("Diga tua idade: ");
    escuta("%d", idade acolá);

    berra("Tu tem %d anos.\n", idade);

    devolve 0;
}
```

Traduza o programa:

```bash
python interpreter.py teste.bdg teste.c
```

Compile o código C gerado:

```bash
gcc teste.c -o programa
```

Execute:

```bash
./programa
```

### Mensagens de erro

Quando o interpretador encontra um problema no código Budega, ele mostra uma mensagem indicando a linha e a coluna aproximada do erro. Por exemplo:

```text
Erro de sintaxe: Erro na linha 4, coluna 5: Expressão esperada
```

Nesses casos, confira principalmente:

- se a instrução termina com `;`;
- se os blocos `{` e `}` foram fechados corretamente;
- se chamadas de função usam parênteses;
- se strings foram fechadas com aspas;
- se a palavra-chave usada existe na linguagem.

### Observação

O interpretador não executa diretamente a linguagem Budega como uma máquina virtual. Ele primeiro traduz Budega para C. Por isso, para rodar o programa final, é necessário compilar o arquivo C gerado.

## Outros

Operadores aritméticos, ordem de precedência, comentários, blocos, chamadas de função e funções auxiliares seguem uma estrutura inspirada em C.

Por ser uma linguagem esotérica, a Budega não tem o objetivo de substituir linguagens comerciais. A proposta é servir como experimento acadêmico, exercício de criatividade e homenagem bem-humorada à cultura cearense.
