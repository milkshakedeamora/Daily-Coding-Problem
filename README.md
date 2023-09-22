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
|#025| Implemente a correspondência de expressões regulares com os seguintes caracteres especiais:<br> `. (ponto)` que corresponde a qualquer caractere único <br> `* (asterisco) ` que corresponde a zero ou mais do elemento anterior <br> Ou seja, implemente uma função que receba uma string e uma expressão regular válida e retorne se a string corresponde ou não à expressão regular.Por exemplo, dada a expressão regular “ra”. e a string "ray", sua função deve retornar verdadeiro. A mesma expressão regular na string "raymond" deve retornar falso.
Dada a expressão regular ".*at" e a string "chat", sua função deve retornar verdadeiro. A mesma expressão regular na string "chats" deve retornar falso| |



 


