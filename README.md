# Cifra de César

Este projeto tem como objetivo a implementação de um código capaz de codificar e decodificar a Cifra de César em **Python**, além de ter sido produzida uma interface gráfica para o programa utilizando a biblioteca **PySimpleGUI**. Por favor, leia os requisitos para que consiga rodar o código sem problemas.

## 1. Informações Relevantes

### 1.1 Cifra de César

A cifra de César é uma forma simples de criptografia em que as letras são deslocadas para o lado com base em um número pré-definido pelo usuário. Possui esse nome em homenagem ao imperador Júlio César, que o usou para se comunicar com os seus generais.

A cifra acontece com a rotação do alfabeto padrão para a direita ou para a esquerda, onde as duas pessoas que estão conversando definem quanto será rotacionado. Abaixo temos um exemplo de como ficaria o alfabeto para a cifra de César rotacionado 4 posições para a esquerda:

       ALFABETO PADRÃO:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ALFABETO ROTACIONADO:  EFGHIJKLMNOPQRSTUVWXYZABCD

## 2. Requisitos

### 2.1 Python

Para que o código seja executado, é necessário ter o Python 3 instalado em sua máquina. No meu caso, utilizei a versão 3.9.10 do python. O arquivo a ser rodado se chama `tela.py`, mesmo arquivo que possui a tela. A função responsável por codificar e decodificar está presente no arquivo `cifra_de_cesar.py`.

### 2.2 PySimpleGUI

A única biblioteca utilizada no projeto foi o [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/), uma biblioteca capaz de gerar interfaces gráficas de maneira simples utilizando apenas Python. Para instalá-la, basta utilizar o código abaixo em seu terminal:

    pip install PySimpleGUI

A versão que utilizei foi a 4.56.0.

## 3. Considerações Finais

Agradeço por ter chegado até aqui, espero que tenha gostado do projeto. Qualquer dúvida sobre o código, a biblioteca utilizada ou sugestão, meu email é davimatiasaraujo@gmail.com.