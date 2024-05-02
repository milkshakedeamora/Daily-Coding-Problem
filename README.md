# Daily-Coding-Problem
Resoluções dos desafios de codificação enviados pelo [Daily Coding Problem](https://www.dailycodingproblem.com/)

| Day  | Problem | Language | 
| :--------------:| :----------:|  :--------------:|
|[#001](./%23001)| Dada uma lista de números e um número k, retorne se quaisquer dois números da lista somam k.Por exemplo, dado [10, 15, 3, 7] e k de 17, retorne verdadeiro desde que 10 + 7 seja 17. | C | 
|[#002](./%23002)| Dada uma matriz de inteiros, retorne uma nova matriz de modo que cada elemento no índice i da nova matriz seja o produto de todos os números na matriz original, exceto aquele em i. Por exemplo, se nossa entrada fosse [1, 2, 3, 4, 5], a saída esperada seria [120, 60, 40, 30, 24]. Se nossa entrada fosse [3, 2, 1], a saída esperada seria [2, 3, 6]. |  Python| 
|[#003](./%23003)| Dada a raiz para uma árvore binária, implemente serialize(root), que serializa a árvore em uma string, e deserialize(s), que desserializa a string de volta na árvore. |  Python| 
|[#004](./%23004)| Dada uma matriz de números inteiros, encontre o primeiro inteiro positivo ausente em tempo linear e espaço constante. Em outras palavras, encontre o menor inteiro positivo que não existe na matriz. A matriz também pode conter duplicatas e números negativos.Por exemplo, a entrada [3, 4, -1, 1] deve fornecer 2. A entrada [1, 2, 0]deve dar 3. |  Python| 
|[#005](./%23005)| cons(a, b) constrói um par e car(pair) retorna o primeiro e cdr(pair) o último elemento desse par. Por exemplo, car(cons(3, 4)) retorna 3 e cdr(cons(3, 4)) retorna 4.  |  Python| 
|#006|  Uma lista encadeada XOR é uma lista encadeada duplamente mais eficiente em termos de memória. Em vez de cada nó conter <b> next </b> e <b>prev</b> campos, ele contém um campo denominado <b>both</b>, que é um <i>XOR</i> do próximo nó e do nó anterior. Implementar uma lista encadeada XOR; tem um add(element) que adiciona o elemento ao final e um get(index) que retorna o nó no índice. Se estiver usando uma linguagem que não possui ponteiros (como Python), você pode assumir que tem acesso <i>get_pointer</i> e <i>dereference_pointer</i> funções que convertem entre nós e endereços de memória. | | 
|#007| Dado o mapeamento a = 1, b = 2, ... z = 26 e uma mensagem codificada, conte o número de maneiras pelas quais ela pode ser decodificada. Por exemplo, a mensagem '111' daria 3, pois poderia ser decodificada como 'aaa', 'ka' e 'ak'.|  | 
|#008| Uma árvore unival (que significa "valor universal") é uma árvore em que todos os nós abaixo dela têm o mesmo valor. Dada a raiz de uma árvore binária, conte o número de subárvores univais. | | 
|#009| Dada uma lista de números inteiros, escreva uma função que retorne a maior soma de números não adjacentes. Os números podem ser 0 ou negativos. Por exemplo, [2, 4, 6, 2, 5] deve retornar 13, já que escolhemos 2, 6 e 5. [5, 1, 1, 5] deve retornar 10, já que escolhemos 5 e 5| | 
|#010| Implemente um agendador de tarefas que receba uma função <b> f </b> e um número inteiro n e chame f após n milissegundos. |  | 
|#011| Implemente um sistema de preenchimento automático. Ou seja, dada uma string de consulta `s` e um conjunto de todas as strings de consulta possíveis, retorne todas as strings do conjunto que tenham s como prefixo. Por exemplo, dada a string de consulta <i> de </i> e o conjunto de strings [ dog, deer, deal], retorne [ deer, deal]. | | 
|#012| Existe uma escada com N degraus e você pode subir 1 ou 2 degraus por vez. Dado N, escreva uma função que retorne o número de maneiras únicas pelas quais você pode subir a escada. A ordem das etapas é importante. Por exemplo, se N é 4, existem 5 maneiras únicas: `1, 1, 1, 1` ,  `2, 1, 1` , `1, 2, 1` , `1, 1, 2` , `2, 2` . E se, em vez de subir 1 ou 2 degraus de cada vez, você pudesse subir qualquer número de um conjunto de inteiros positivos X? Por exemplo, se X = {1, 3, 5}, você pode subir 1, 3 ou 5 degraus por vez.| |
|#013| Dado um inteiro k e uma string s, encontre o comprimento da substring mais longa que contém no máximo k caracteres distintos. Por exemplo, dados s = "abcba" e k = 2, a substring mais longa com k caracteres distintos é "bcb| | 
|#014| A área de um círculo é definida como πr^2. Estime π com 3 casas decimais usando um método de Monte Carlo. Dica: A equação básica de um círculo é x 2 + y 2 = r 2 .|  | 
|#015| Dado um fluxo de elementos muito grande para armazenar na memória, escolha um elemento aleatório do fluxo com probabilidade uniforme. | | 
|#016| Você administra um site de comércio eletrônico e deseja registrar os últimos N IDs order em um log. Implemente uma estrutura de dados para fazer isso, com a seguinte API: `record(order_id)`: adiciona o order_id ao log ; `get_last(i)`: obtém o i-ésimo último elemento do log. i é garantido como menor ou igual a N.| |
|#017| | |
|#018| Dado um array de inteiros e um número k, onde 1 <= k <= comprimento do array, calcule os valores máximos de cada subarray de comprimento k. Por exemplo, dado array = [10, 5, 2, 7, 8, 7] e k = 3, devemos obter: [10, 7, 8, 8], pois: <br> 10 = máx(10, 5, 2) <br> 7 = máx(5, 2, 7) <br> 8 = máx(2, 7, 8) <br> 8 = máx(7, 8, 7) <br> Faça isso em tempo O(n) e espaço O(k). Você pode modificar a matriz de entrada no local e não precisa armazenar os resultados. Você pode simplesmente imprimi-los enquanto os calcula. | | 
|#019| Um construtor pretende construir uma fileira de N casas que podem ser de K cores diferentes. Ele tem o objetivo de minimizar custos e ao mesmo tempo garantir que não haja duas casas vizinhas da mesma cor. Dada uma matriz N por K onde a n -ésima linha e a k -ésima coluna representam o custo para construir a n -ésima casa com k -ésima cor, retorne o custo mínimo que atinge esse objetivo. |  | 
|#020| Dadas duas listas vinculadas individualmente que se cruzam em algum ponto, encontre o nó que se cruza. As listas não são cíclicas. Por exemplo, dado A = 3 -> 7 -> 8 -> 10 e B = 99 -> 1 -> 8 -> 10, retorne o nó com valor 8.Neste exemplo, suponha que nós com o mesmo valor sejam exatamente os mesmos objetos de nó. Faça isso em tempo O(M + N) (onde M e N são os comprimentos das listas) e espaço constante. | | 
|#021|Dada uma série de intervalos de tempo (início, fim) para palestras em sala de aula (possivelmente sobrepostas), encontre o número mínimo de salas necessárias. Por exemplo, dado [(30, 75), (0, 50), (60, 150)], você deve retornar 2. | |
|#022| Dado um dicionário de palavras e uma string composta por essas palavras (sem espaços), retorne a frase original em uma lista. Se houver mais de uma reconstrução possível, devolva qualquer uma delas. Se não houver reconstrução possível, retorne nulo. Por exemplo, dado o conjunto de palavras 'quick', 'brown', 'the', 'fox' e a string "thequickbrownfox", você deve retornar ['the', 'quick', 'brown', 'fox' ]. Dado o conjunto de palavras 'bed', 'bath', 'bedbath', 'and', 'beyond', e a string "bedbathandbeyond", retorne ['bed', 'bath', 'and', 'beyond] ou  ['bedbath', 'and', 'beyond']..  | | 
|#023|Você recebe uma matriz M por N que consiste em booleanos que representa um tabuleiro. Cada booleano True representa uma parede. Cada booleano False representa um bloco no qual você pode andar. Dada esta matriz, uma coordenada inicial e uma coordenada final, retorne o número mínimo de etapas necessárias para alcançar a coordenada final desde o início. Se não houver caminho possível, retorne nulo. Você pode mover para cima, para a esquerda, para baixo e para a direita. Você não pode passar pelas paredes. Você não pode enrolar nas bordas do tabuleiro. Por exemplo, dada a seguinte placa: `[[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f]] ` e início = (3, 0) (canto inferior esquerdo) e fim = (0, 0) (canto superior esquerdo), o número mínimo de passos necessários para chegar ao final é 7, pois precisaríamos passar por (1, 2) porque há uma parede em todos os outros lugares da segunda linha. |  | 
|#024| Implemente o bloqueio em uma árvore binária. Um nó de árvore binária só pode ser bloqueado ou desbloqueado se todos os seus descendentes ou ancestrais não estiverem bloqueados. Projete uma classe de nó de árvore binária com os seguintes métodos:<br> `is_locked` , que retorna se o nó está bloqueado <br> `lock` , que tenta bloquear o nó. <br> Se não puder ser bloqueado, deverá retornar falso. Caso contrário, deverá bloqueá-lo e retornar verdadeiro. <br> `unlock` , que desbloqueia o nó. Se não puder ser desbloqueado, deverá retornar falso. Caso contrário, deverá desbloqueá-lo e retornar verdadeiro. Você pode aumentar o nó para adicionar ponteiros pai ou qualquer outra propriedade que desejar. Você pode assumir que a classe é usada em um programa de thread único, portanto não há necessidade de bloqueios ou mutexes reais. Cada método deve ser executado em O(h), onde h é a altura da árvore | | 
|#025| Implemente a correspondência de expressões regulares com os seguintes caracteres especiais:<br> `. (ponto)` que corresponde a qualquer caractere único <br> `* (asterisco) ` que corresponde a zero ou mais do elemento anterior <br> Ou seja, implemente uma função que receba uma string e uma expressão regular válida e retorne se a string corresponde ou não à expressão regular.Por exemplo,dada a expressão regular “ra”. e a string "ray", sua função deve retornar verdadeiro. A mesma expressão regular na string "raymond" deve retornar falso.| |
|#026 |Dada uma lista vinculada individualmente e um inteiro k, remova o k <sup>último</sup> elemento da lista. É garantido que k seja menor que o comprimento da lista.A lista é muito longa, então fazer mais de uma passagem é proibitivamente caro.Faça isso em um espaço constante e de uma só vez.| | |
|#027 | Dada uma sequência de colchetes redondos, encaracolados e quadrados de abertura e fechamento, retorne se os colchetes estão balanceados (bem formados).Por exemplo, dada a string "([])[]({})", você deve retornar verdadeiro.Dada a string "([)]" ou "((()", você deve retornar falso.| | |
|#028 | Escreva um algoritmo para justificar o texto. Dada uma sequência de palavras e um comprimento de linha inteiro k, retorne uma lista de strings que representa cada linha, totalmente justificada. Mais especificamente, você deve ter tantas palavras quanto possível em cada linha. Deve haver pelo menos um espaço entre cada palavra. Preencha espaços extras quando necessário para que cada linha tenha exatamente comprimento k. Os espaços devem ser distribuídos da forma mais equitativa possível, com os espaços extras, se houver, distribuídos a partir da esquerda. Se você só conseguir encaixar uma palavra em uma linha, preencha o lado direito com espaços.É garantido que cada palavra não seja maior que k.Por exemplo, dada a lista de palavras `["o", "rápido", "marrom", "raposa", "pular", "sobre", "o", "preguiçoso", "cachorro"]` e k = 16, você deve retornar o seguinte:`["the quick brown", # 1 extra space on the left ` `"fox jumps over", # 2 extra spaces distributed evenly ` `"the lazy dog"] # 4 extra spaces distributed evenly` | | |
|#029 |A codificação run-length é um método rápido e simples de codificação de strings. A ideia básica é representar caracteres repetidos e sucessivos como uma única contagem e caractere. Por exemplo, a string "AAAABBBCCDAA" seria codificada como "4A3B2C1D2A". Implemente codificação e decodificação de comprimento de execução. Você pode assumir que a string a ser codificada não possui dígitos e consiste apenas em caracteres alfabéticos. Você pode assumir que a string a ser decodificada é válida. | | |
|#030 |Você recebe uma matriz de números inteiros não negativos que representa um mapa de elevação bidimensional onde cada elemento é uma parede com largura unitária e o número inteiro é a altura. Suponha que chova e todos os pontos entre duas paredes sejam preenchidos.Calcule quantas unidades de água permanecem presas no mapa em O(N) tempo e O(1) espaço. <br> Por exemplo, dada a entrada [2, 1, 2], podemos manter 1 unidade de água no meio.Dada a entrada [3, 0, 1, 3, 0, 5], podemos manter 3 unidades no primeiro índice, 2 no segundo e 3 no quarto índice (não podemos manter 5, pois iria para o esquerda), então podemos reter 8 unidades de água. | | |
|#031 | A distância de edição entre duas strings refere-se ao número mínimo de inserções, exclusões e substituições de caracteres necessárias para alterar uma string para outra. Por exemplo, a distância de edição entre “kitten” e “sitting” é três: substitua “k” por “s”, substitua “e” por “i” e acrescente um “g”.Dadas duas strings, calcule a distância de edição entre elas. | | |
|#032| Suponha que você receba uma tabela de taxas de câmbio, representada como uma matriz 2D. Determine se existe uma possível arbitragem: isto é, se existe alguma sequência de negociações que você pode fazer, começando com algum valor A de qualquer moeda, para que você possa terminar com algum valor maior que A dessa moeda.Não há custos de transação e você pode negociar quantidades fracionárias.| |  |
|#033 |Calcule a mediana contínua de uma sequência de números. Ou seja, dado um fluxo de números, imprima a mediana da lista até o momento em cada novo elemento.Lembre-se de que a mediana de uma lista par é a média dos dois números do meio.Por exemplo, dada a sequência [2, 1, 5, 7, 2, 0, 5], seu algoritmo deve imprimir:` 2 1.5 2 3.5 2 2 2 ` | | |
|#034 | Dada uma string, encontre o palíndromo que pode ser feito inserindo o menor número possível de caracteres em qualquer lugar da palavra. Se houver mais de um palíndromo de comprimento mínimo que possa ser feito, retorne o mais antigo lexicograficamente (o primeiro em ordem alfabética).Por exemplo, dada a string “race”, você deve retornar “ecarace”, pois podemos adicionar três letras a ela (que é a menor quantidade para formar um palíndromo). Existem sete outros palíndromos que podem ser feitos a partir de “race” adicionando três letras, mas “ecarace” vem primeiro em ordem alfabética.Como outro exemplo, dada a string “google”, você deve retornar “elgoogle”. | | |
|#035 | Dada uma matriz estritamente composta pelos caracteres 'R', 'G' e 'B', separe os valores da matriz de modo que todos os Rs venham primeiro, os Gs venham em segundo e os Bs venham por último. Você só pode trocar elementos do array.Faça isso em tempo linear e no local. Por exemplo, dada a matriz ['G', 'B', 'R', 'R', 'B', 'R', 'G'], ela deve se tornar ['R', 'R', 'R ', 'G', 'G', 'B', 'B']. | | |
|#036 | Dada a raiz de uma árvore de pesquisa binária, encontre o segundo maior nó da árvore.| | |
|#037 | O conjunto potência de um conjunto é o conjunto de todos os seus subconjuntos. Escreva uma função que, dado um conjunto, gere seu conjunto potência.Por exemplo, dado o conjunto `{1, 2, 3} ` , ele deve retornar ` {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}` .Você também pode usar uma lista ou array para representar um conjunto.| | |
|#038 |Você tem uma placa N por N. Escreva uma função que, dado N, retorne o número de possíveis arranjos do tabuleiro onde N rainhas podem ser colocadas no tabuleiro sem ameaçar uma à outra, ou seja, não há duas rainhas que compartilhem a mesma linha, coluna ou diagonal. | | |
|#039 |O Jogo da Vida de Conway ocorre em um tabuleiro bidimensional infinito de células quadradas. Cada célula está viva ou morta e, a cada tick, as seguintes regras se aplicam: <br><br> Qualquer célula viva com menos de dois vizinhos vivos morre. <br>  Qualquer célula viva com dois ou três vizinhos vivos permanece viva. <br> Qualquer célula viva com mais de três vizinhos vivos morre.<br>Qualquer célula morta com exatamente três vizinhos vivos torna-se uma célula viva.<br><br>Uma célula é vizinha de outra célula se ela for adjacente horizontalmente, verticalmente ou diagonalmente.Implemente o Jogo da Vida de Conway. Ele deve poder ser inicializado com uma lista inicial de coordenadas de células ativas e o número de etapas que deve ser executado. Uma vez inicializado, ele deverá imprimir o estado da placa em cada etapa. Como é um tabuleiro infinito, imprima apenas as coordenadas relevantes, ou seja, da célula viva mais à esquerda até a célula viva mais à direita.Você pode representar uma célula viva com um asterisco ( * ) e uma célula morta com um ponto ( . ). | | |
|#040 | Dada uma matriz de números inteiros onde cada número inteiro ocorre três vezes, exceto um número inteiro, que ocorre apenas uma vez, encontre e retorne o número inteiro não duplicado. Por exemplo, dado [6, 1, 3, 3, 3, 6, 6], retorne 1. Dado [13, 19, 13, 13], retorne 19.Faça isso em tempo O(N) e espaço O(1). | | |
|#041 |Dada uma lista não ordenada de voos realizados por alguém, cada um representado como pares (origem, destino), e um aeroporto de partida, calcule o itinerário da pessoa. Se tal itinerário não existir, retorne nulo. Se houver vários itinerários possíveis, retorne o menor lexicograficamente. Todos os voos devem ser utilizados no itinerário. <br>Por exemplo, dada a lista de voos [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] e começando no aeroporto 'YUL', você deve retornar a lista ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']. <br>Dada a lista de voos [('SFO', 'COM'), ('COM', 'YYZ')] e o aeroporto de partida 'COM', você deve retornar nulo. <br>Dada a lista de voos [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] e aeroporto de partida ' A', você deve retornar a lista ['A', 'B', 'C', 'A', 'C'] mesmo que ['A', 'C', 'A', 'B', 'C '] também é um itinerário válido. No entanto, o primeiro é lexicograficamente menor. | | |
|#042 | Dada uma lista de inteiros S e um número alvo k, escreva uma função que retorne um subconjunto de S que soma k. Se tal subconjunto não puder ser criado, retorne nulo. Os números inteiros podem aparecer mais de uma vez na lista. Você pode assumir que todos os números da lista são positivos. Por exemplo, dados S = [12, 1, 61, 5, 9, 2] e k = 24, retorne [12, 9, 2, 1], pois soma 24. | | |
|#043 | Implemente uma pilha que possua os seguintes métodos: <br> push(val), que empurra um elemento para a pilha <br> pop(), que aparece e retorna o elemento mais alto da pilha. Se não houver elementos na pilha, deverá gerar um erro ou retornar nulo. <br> max(), que retorna o valor máximo da pilha atualmente. Se não houver elementos na pilha, deverá gerar um erro ou retornar nulo. <br>Cada método deve ser executado em tempo constante. | | |
|#044 | Podemos determinar o quão "fora de ordem" um array A está contando o número de inversões que ele possui. Dois elementos ` A[i] ` e ` A[j]` formam uma inversão se` A[i] > A[j] `mas` i < j` . Ou seja, um elemento menor aparece depois de um elemento maior. Dado um array, conte o número de inversões que ele possui. Faça isso mais rápido que o tempo O(N^2). Você pode assumir que cada elemento da matriz é distinto. Por exemplo, uma lista ordenada tem zero inversões. A matriz [2, 4, 1, 3, 5] possui três inversões: (2, 1), (4, 1) e (4, 3). A matriz [5, 4, 3, 2, 1] possui dez inversões: cada par distinto forma uma inversão. | | |
|#045 | Usando uma função `rand5()` que retorna um número inteiro de 1 a 5 (inclusive) com probabilidade uniforme, implemente uma função `rand7()` que retorna um número inteiro de 1 a 7 (inclusive). | | |
|#046 | Dada uma string, encontre a substring contígua palindrômica mais longa. Se houver mais de um com comprimento máximo, retorne qualquer um.Por exemplo, a substring palindrômica mais longa de "aabcdcb" é "bcdcb". A substring palindrômica mais longa de "bananas" é "anana". | | |
|#047 | Dada uma série de números que representam os preços das ações de uma empresa em ordem cronológica, escreva uma função que calcule o lucro máximo que você poderia ter obtido ao comprar e vender essas ações uma vez. Você deve comprar antes de poder vendê-lo.Por exemplo, dado [9, 11, 8, 5, 7, 10], você deveria retornar 5, já que poderia comprar a ação por 5 dólares e vendê-la por 10 dólares.| | |
|#048 | Dadas as travessias pré-ordenadas e ordenadas de uma árvore binária, escreva uma função para reconstruir a árvore.Por exemplo, dada a seguinte travessia de pré-pedido: [a, b, d, e, c, f, g] E a seguinte travessia em ordem: [d, b, e, a, f, c, g]. Você deve retornar a seguinte árvore:<br>  a <br> / \ <br> b‎ ‎ ‎  c <br> / \‎ ‎ ‎  / \ <br>d e‎ ‎ ‎  f g  | | |
|#049 | Dada uma matriz de números, encontre a soma máxima de qualquer submatriz contígua da matriz.Por exemplo, dada a matriz [34, -50, 42, 14, -5, 86], a soma máxima seria 137, pois pegaríamos os elementos 42, 14, -5 e 86. Dado o array [-5, -1, -8, -9], a soma máxima seria 0, pois não pegaríamos nenhum elemento. Faça isso em tempo O(N). | | |
|#050 | Suponha que uma expressão aritmética seja dada como uma árvore binária. Cada folha é um número inteiro e cada nó interno é um de '+', '−', '∗' ou '/'.Dada a raiz dessa árvore, escreva uma função para avaliá-la. Por exemplo, dada a seguinte árvore: <br>  * <br> / \ <br> +‎ ‎ ‎  + <br> / \‎ ‎ ‎  / \ <br>3 2‎ ‎ ‎  4 5  <br> Você deve retornar 45, pois é (3 + 2) * (4 + 5). | | |
|#051 | Dada uma função que gera números perfeitamente aleatórios entre 1 e k (inclusive), onde k é uma entrada, escreva uma função que embaralhe um baralho de cartas representado como um array usando apenas trocas.Deve ser executado em tempo O(N). <br>Dica: certifique-se de cada um dos 52! permutações do baralho são igualmente prováveis. | | |
|#052 | Implemente um cache LRU (menos usado recentemente). Deve poder ser inicializado com um tamanho de cache n e conter os seguintes métodos: <br> set(key, value) : define key como value . Se já houver n itens no cache e estivermos adicionando um novo item, ele também deverá remover o item usado menos recentemente. <br> get(key) : obtém o valor em key . Se essa chave não existir, retorne nulo. <br>Cada operação deve ser executada em tempo O(1). | | |
|#053 | Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it. | | |
|#054 | Sudoku é um quebra-cabeça onde você recebe uma grade 9 por 9 parcialmente preenchida com dígitos. O objetivo é preencher a grade com a restrição de que cada linha, coluna e caixa (subgrade 3 por 3) deve conter todos os dígitos de 1 a 9. Implemente um solucionador de sudoku eficiente. | | |
|#055 | Implemente um encurtador de URL com os seguintes métodos: `shorten(url) `, que encurta o URL em uma sequência alfanumérica de seis caracteres, como zLg6wl .`restore(short)` , que expande a string encurtada para o URL original. Se não existir tal string abreviada, retorne nulo. <br> Dica: e se inserirmos o mesmo URL duas vezes? | | |
|#056 | Dado um grafo não direcionado representado como uma matriz de adjacência e um inteiro k, escreva uma função para determinar se cada vértice no grafo pode ser colorido de forma que não haja dois vértices adjacentes compartilhando a mesma cor usando no máximo k cores. | |
|#057 |Dada uma string s e um inteiro k, divida a string em várias linhas, de modo que cada linha tenha um comprimento k ou menos. Você deve separá-lo para que as palavras não ultrapassem as linhas. Cada linha deve ter a quantidade máxima possível de palavras. Se não houver como dividir o texto, retorne nulo. Você pode assumir que não há espaços no final da string e que há exatamente um espaço entre cada palavra. Por exemplo, dada a string  "the quick brown fox jumps over the lazy dog" e k = 10, você deve retornar: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. Nenhuma string na lista tem comprimento superior a 10. | | |
|#058 | Uma matriz classificada de inteiros foi girada um número desconhecido de vezes. Dado tal array, encontre o índice do elemento no array em tempo mais rápido que o linear. Se o elemento não existir no array, retorne nulo. Por exemplo, dado o array [13, 18, 25, 2, 8, 10] e o elemento 8, retorne 4 (o índice de 8 no array). Você pode assumir que todos os números inteiros da matriz são únicos. | | |
|#059 | Implemente um algoritmo de sincronização de arquivos para dois computadores em uma rede de baixa largura de banda. E se soubermos que os arquivos nos dois computadores são basicamente iguais? | | |
|#060 | Dado um multiconjunto de inteiros, retorne se ele pode ser particionado em dois subconjuntos cujas somas sejam iguais. Por exemplo, dado o multiconjunto {15, 5, 20, 10, 35, 15, 10} , ele retornaria verdadeiro, pois podemos dividi-lo em {15, 5, 10, 15, 10} e {20, 35}, que somam 55 . Dado o multiconjunto {15, 5, 20, 10, 35} , ele retornaria falso, pois não podemos dividi-lo em dois subconjuntos que somam a mesma soma.| | |
|#061 | | | |
|#062 | | | |
|#063 | | | |
|#064 | | | |
|#065 | | | |
|#066 | | | |
|#067 | | | |
|#068 | | | |
|#069 | | | |
|#070 | | | |
|#071 | | | |
|#072 | | | |
|#073 | | | |
|#074 | | | |
|#075 | | | |
|#076 | | | |
|#077 | | | |
|#078 | | | |
|#079 | | | |
|#080 | | | |
|#081 | | | |
|#082 | | | |
|#083 | | | |
|#084 | | | |
|#085 | | | |
|#086 | | | |
|#087 | | | |
|#088 | | | |
|#089 | | | |
|#090 | | | |
|#091 | | | |
|#092 | | | |
|#093 | | | |
|#094 | | | |
|#095 | | | |
|#096 | | | |
|#097 | | | |
|#098 | | | |
|#099 | | | |
|#100 | | | |
|#101 | | | |
|#102 | | | |
|#103 | | | |
|#104 | | | |
|#105 | | | |
|#106 | | | |
|#107 | | | |
|#108 | | | |
|#109 | | | |
|#110 | | | |
|#111 | | | |
|#112 | | | |
|#113 | | | |
|#114 | | | |
|#115 | | | |
|#116 | | | |
|#117 | | | |
|#118 | | | |
|#119 | | | |
|#120 | | | |
|#121 | | | |
|#122 | | | |
|#123 | | | |
|#124 | | | |
|#125 | | | |
|#126 | | | |
|#127 | | | |
|#128 | | | |
|#129 | | | |
|#130 | | | |
|#131 | | | |
|#132 | | | |
|#133 | | | |
|#134 | | | |
|#135 | | | |
|#136 | | | |
|#137 | | | |
|#138 | | | |
|#139 | | | |
|#140 | | | |
|#141 | | | |
|#142 | | | |
|#143 | | | |
|#144 | | | |
|#145 | | | |
|#146 | | | |
|#147 | | | |
|#148 | | | |
|#149 | | | |
|#150 | | | |
|#151 | | | |
|#152 | | | |
|#153 | | | |
|#154 | | | |
|#155 | | | |
|#156 | | | |
|#157 | | | |
|#158 | | | |
|#159 | | | |
|#160 | | | |
|#161 | | | |
|#162 | | | |
|#163 | | | |
|#164 | | | |
|#165 | | | |
|#166 | | | |
|#167 | | | |
|#168 | | | |
|#169 | | | |
|#170 | | | |
|#171 | | | |
|#172 | | | |
|#173 | | | |
|#174 | | | |
|#175 | | | |
|#176 | | | |
|#177 | | | |
|#178 | | | |
|#179 | | | |
|#180 | | | |
|#181 | | | |
|#182 | | | |
|#183 | | | |
|#184 | | | |
|#185 | | | |
|#186 | | | |
|#187 | | | |
|#188 | | | |
|#189 | | | |
|#190 | | | |
|#191 | | | |
|#192 | | | |
|#193 | | | |
|#194 | | | |
|#195 | | | |
|#196 | | | |
|#197 | | | |
|#198 | | | |
|#199 | | | |
|#200 | | | |
|#201 | | | |
|#202 | | | |
|#203 | | | |
|#204 | | | |
|#205 | | | |
|#206 | | | |
|#207 | | | |
|#208 | | | |
|#209 | | | |
|#210 | | | |
|#211 | | | |
|#212 | | | |
|#213 | | | |
|#214 | | | |
|#215 | | | |
|#216 | | | |
|#217 | | | |
|#218 | | | |
|#219 | | | |
|#220 | | | |
|#221 | | | |
|#222 | | | |
|#223 | | | |
|#224 | | | |
|#225 | | | |
|#226 | | | |
|#227 | | | |
|#228 | | | |
|#229 | | | |
|#230 | | | |
|#231 | | | |
|#232 | | | |
|#233 | | | |
|#234 | | | |
|#235 | | | |
|#236 | | | |
|#237 | | | |
|#238 | | | |
|#239 | | | |
|#240 | | | |
|#241 | | | |
|#242 | | | |
|#243 | | | |
|#244 | | | |
|#245 | | | |
|#246 | | | |
|#247 | | | |
|#248 | | | |
|#249 | | | |
|#250 | | | |
|#251 | | | |
|#252 | | | |
|#253 | | | |
|#254 | | | |
|#255 | | | |
|#256 | | | |
|#257 | | | |
|#258 | | | |
|#259 | | | |
|#260 | | | |
|#261 | | | |
|#262 | | | |
|#263 | | | |
|#264 | | | |
|#265 | | | |
|#266 | | | |
|#267 | | | |
|#268 | | | |
|#269 | | | |
|#270 | | | |
|#271 | | | |
|#272 | | | |
|#273 | | | |
|#274 | | | |
|#275 | | | |
|#276 | | | |
|#277 | | | |
|#278 | | | |
|#279 | | | |
|#280 | | | |
|#281 | | | |
|#282 | | | |
|#283 | | | |
|#284 | | | |
|#285 | | | |
|#286 | | | |
|#287 | | | |
|#288 | | | |
|#289 | | | |
|#290 | | | |
|#291 | | | |
|#292 | | | |
|#293 | | | |
|#294 | | | |
|#295 | | | |
|#296 | | | |
|#297 | | | |
|#298 | | | |
|#299 | | | |
|#300 | | | |
|#301 | | | |
|#302 | | | |
|#303 | | | |
|#304 | | | |
|#305 | | | |
|#306 | | | |
|#307 | | | |
|#308 | | | |
|#309 | | | |
|#310 | | | |
|#311 | | | |
|#312 | | | |
|#313 | | | |
|#314 | | | |
|#315 | | | |
|#316 | | | |
|#317 | | | |
|#318 | | | |







 


