# Trabalho Final Parte 1

## Artigo escolhido

O artigo escolhido foi:

**Monte Carlo Simulations as an Alternative for Solving Engineering Problems in Environmental Sciences: Three Case Studies**

O trabalho apresenta tres estudos de caso em que o metodo de Monte Carlo e usado para resolver problemas de engenharia ambiental com variaveis aleatorias. Neste relatorio foi escolhido o **Caso 2**, que trata do dimensionamento de uma camara de homogeneizacao em uma usina de tratamento de residuos solidos.

## Motivo da escolha do Caso 2

O Caso 2 foi escolhido porque apresenta uma aplicacao direta do metodo de Monte Carlo em um problema de engenharia com variaveis aleatorias bem definidas. O objetivo e estimar o volume necessario de uma camara de homogeneizacao, considerando a variabilidade do processo operacional.

Esse caso tambem e adequado para a disciplina porque permite gerar variaveis aleatorias, aplicar um modelo matematico simples baseado em balanco de massa e comparar os resultados simulados com valores apresentados no artigo.

Outro ponto importante e que o artigo foi indicado pelo professor da disciplina e orientador do mestrado, o que reforca sua adequacao ao trabalho final.

## Explicacao do Caso 2

O Caso 2 analisa uma usina de tratamento de residuos solidos que opera das 08:00 as 16:00. Durante esse periodo, caminhoes descarregam residuos na planta. O material passa por uma etapa de triagem manual, onde parte dos reciclaveis e removida. Em seguida, o residuo restante passa por uma peneira, onde parte da materia organica e separada. O volume restante segue para uma camara de homogeneizacao antes do envio final ao aterro.

O problema consiste em estimar o volume necessario dessa camara para que ela opere de forma adequada em 95% dos cenarios simulados.

## Variaveis aleatorias

As variaveis aleatorias consideradas no modelo foram:

- tipo de caminhao: `10 m3`, `7 m3` ou `3 m3`
- probabilidade dos caminhoes: `20%`, `20%` e `60%`
- tempo entre chegadas: distribuicao exponencial
- eficiencia da triagem manual: `U(5,10)%`
- fracao de materia organica: `U(60,70)%`
- eficiencia da peneiracao: `U(90,95)%`

## Modelo matematico

Para cada caminhao, o volume enviado para a camara e calculado por:

\[
V_i = V_{truck}
\left(1-\frac{E_{sorting}}{100}\right)
\left(1-\frac{\%MO}{100}\frac{E_{screening}}{100}\right)
\]

O volume diario e:

\[
V_{day}=V_1+V_2+\cdots+V_n
\]

Como a camara deve armazenar residuos de tres dias e nao ultrapassar 90% da capacidade, o volume de projeto e:

\[
V_{chamber}=\frac{V_{day1}+V_{day2}+V_{day3}}{0.90}
\]

## Metodologia da simulacao

A simulacao foi feita em Python, em notebook Jupyter, seguindo a estrutura do artigo:

- foram simuladas `1000` iteracoes
- foram feitas `10` repeticoes
- cada iteracao simulou `3` dias de operacao
- para cada dia, foram geradas chegadas de caminhoes por distribuicao exponencial
- para cada caminhao, foram sorteados tipo, eficiencia de triagem, fracao organica e eficiencia de peneiracao
- o volume final da camara foi estimado pelo percentil `95%`

A taxa de chegada usada na simulacao foi `1 caminhao/h`, conforme descrito no artigo.

## Resultados obtidos

Os cenarios deterministicos da Tabela 3 foram reproduzidos corretamente:

| Cenario | Artigo (m3) | Simulacao (m3) |
|---|---:|---:|
| Minimo | 24.12 | 24.12 |
| Intermediario | 68.85 | 68.85 |
| Maximo | 116.53 | 116.53 |

Para a simulacao de Monte Carlo, foram obtidos:

| Resultado | Valor |
|---|---:|
| Media dos volumes simulados | 57.52 m3 |
| Media de caminhoes por dia | 8.99 |
| Volume pelo percentil 95 | 78.31 m3 |
| Resultado MC do artigo na Tabela 3 | 94.71 m3 |
| Resultado MC citado no resumo do artigo | 94.84 m3 |

O erro relativo em relacao ao valor da Tabela 3 foi:

\[
erro=\frac{|78.31-94.71|}{94.71}\cdot 100
\]

\[
erro=17.32\%
\]

## Comparacao com o artigo

A simulacao reproduziu corretamente a estrutura do Caso 2: geracao de variaveis aleatorias, aplicacao do balanco de massa e uso do percentil 95 para definir o volume de projeto.

O valor de Monte Carlo obtido nao foi exatamente igual ao valor do artigo. Isso e esperado, pois a reproducao foi feita a partir da descricao textual do artigo e nao a partir do codigo original dos autores. Alem disso, pequenas diferencas na interpretacao do processo de chegada dos caminhoes alteram diretamente o numero medio de caminhoes por dia e, consequentemente, o volume estimado da camara.

Na simulacao implementada, a media foi de aproximadamente `8.99` caminhoes por dia, enquanto o resultado de Monte Carlo do artigo indica uma condicao operacional mais conservadora para o dimensionamento da camara.

## Figura reproduzida

Foi gerado um histograma dos volumes calculados por Monte Carlo, seguindo a ideia da Figura 11 do artigo. A figura mostra a distribuicao dos volumes simulados e destaca o percentil `95%`, que representa o criterio de projeto.

Arquivo gerado:

`simulacao/figura11_reproduzida.png`

## Conclusao

O Caso 2 mostra que o metodo de Monte Carlo e adequado para problemas de dimensionamento quando existem incertezas operacionais. A abordagem deterministica fornece apenas cenarios fixos, enquanto a simulacao permite avaliar muitos cenarios possiveis e escolher um volume de projeto com base em um criterio de confianca.

Mesmo sem reproduzir exatamente o valor numerico do artigo, a simulacao implementada reproduz a metodologia principal: gerar variaveis aleatorias, calcular o volume por balanco de massa e usar o percentil `95%` para estimar a capacidade necessaria da camara de homogeneizacao.
