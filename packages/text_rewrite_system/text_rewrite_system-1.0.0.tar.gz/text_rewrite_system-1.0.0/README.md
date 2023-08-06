# Enunciado 2: Sistema de Reescrita Textual / Regex

## Introdução

Este enunciado descreve a criação de um módulo capaz de converter "pseudo-funções", responsáveis por converter texto para, por exemplo, outra língua, em funções Python que permitam aplicar essa conversão em textos.

Estas "pseudo-funções" deverão seguir um *template* que será lido e transformado pelo módulo.

## Template

O template segue um modelo semelhante ao seguinte:

```py
defrt p2e
    "o gato" => "the cat"
    "chama-se {}" => "is called $1"
    "gritar" => str.upper($0)
endrt
```

Cada linha dentro da função possui um par, com o primeiro elemento correspondente ao valor a procurar no texto e o segundo correspondente ao valor que o deverá substituir.

Aqui, as conversões são lidas e interpretadas por ordem (de cima para baixo). Desta forma, as expressões mais específicas deverão ser colocadas mais acima na função. Para além disso, deverão ser escritas com letra minúscula. Se o texto original contiver letras maiúsculas, o módulo tentará efetuar a conversão e manter a capitalização original.
Por exemplo, se o texto original contiver "The cat" e a função contiver o par `"the cat" => "o gato"`, o texto final irá mostrar a expressão "O gato", visto que o texto original continha a primeira letra maiúscula.

O segundo elemento do par pode ser uma *string*, um *callable*, isto é, uma função de Python, ou um condicional, que usa a sintaxe `[condição] ? [valor_se_verdade] : [valor_se_falso]` ou apenas `[condição] ? [valor_se_verdade]`. Dentro do elemento, poderão existir valores como `$0` ou `$1`. Estes representam grupos de captura do texto original. `$0` diz respeito a toda a *string* capturada, enquanto que `$N`, em que `N > 0`, corresponde ao grupo de captura N, representado na *string* original por `{}`.

No caso do elemento condicional apenas tiver o valor de verdade (i.e.: `[condição] ? [valor_se_verdade]`) e a condição não se verificar, a correspondência é ignorada. Por outras palavras, o programa continua a percorrer a lista de expressões à procura de uma nova correspondência.

Os caracteres `{}` na *string* do lado esquerdo do par, se não tiverem nada dentro dos mesmos, correspondem a uma palavra. Contudo, é possível escrever uma expressão regular dentro das chavetas, que será usada para o grupo de captura.

O ficheiro `reescrita_textual.py` converte um ficheiro `.pyrt`, isto é, um ficheiro Python com pseudo-funções de reescrita textual, como a do exemplo acima, num ficheiro `.py` funcional.

Para tal, é utilizado o módulo Lark para gerar uma Representação Intermédia (RI) a partir das pseudo-funções, que é posteriormente convertida para código Python válido.

## Representação Intermédia

A RI usa um formato semelhante a JSON com a seguinte estrutura:

```json
{
    "name": "[nome da função]",
    "values": [
        {
            "type": "(term / callable)",
            "original": "[texto original]",
            "converted": "[novo valor, pode ser textual ou um callable]"
        },
        {
            "type": "conditional",
            "original": "[texto original]",
            "condition": "[condição para efetuar a reescrita]",
            "if_true": {
                "type": "(term / callable)",
                "converted": "[novo valor, pode ser textual ou um callable]"
            },
            "if_false": {
                "type": "(term / callable)",
                "converted": "[novo valor, pode ser textual ou um callable]"
            },
        }
    ]
}
```

Cada valor pode assumir 1 de 3 tipos, termo, *callable* ou condicional. O tipo condicional, por ser mais complexo do que os outros dois, requer mais valores. O valor "if_false" é opcional.

Cada função de reescrita textual possui a sua própria RI. Por outras palavras, as funções de conversão são sempre independentes uma das outras, sendo que um ficheiro pode conter várias.
