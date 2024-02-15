---
classoption:
- twocolumn
geometry:
 - "left=1.2cm,right=1.2cm,top=1.2cm,bottom=1.4cm"
 - landscape
papersize: a4
pagestyle: empty
---

## `impose_fine`

Policista potřebuje pomoct s udělováním pokut. Zašel do baru a zjistil věk (`age`) občana a to, zda pije pivo (`beer`). Napište funkci `impose_fine(age, beer)`, která vrátí `True` v případě, že občan je nezletilý a pije pivo.

```python
def impose_fine(age, beer):
    if age < 18 and beer == True:
        impose_fine = True
    else:
        impose_fine = False
    return impose_fine
```

## `count_a`

Napište funkci `count_a(text)`, která v řetězci text spočítá počet výskytů písmene `'a'` (malé i velké písmeno).

```python
def count_a(text):
    a=0
    for i in range(len(text)):
        if text[i]=="a" or text[i]=="A":
            a=a+1
    return a
```

## `join`

Napište funkci `join(text1, text2)`, která vrátí spojení těchto dvou řetězců, přičemž ten kratší z nich bude první.

```python
def join(text1, text2):
    if len(text1) <= len(text2):
        sum_text = text1+text2
    else:
        sum_text = text2 + text1
    result =""
    for i in range (len(sum_text)):
        result += sum_text[i]
    return result
```
\newpage

## `count_zeros`

Vstupem v této úloze je table, což je seznam seznamů čísel reprezentujících tabulku čísel. Napište funkci `count_zeros(table)`, která vrátí počet nul v tabulce.

```python
def count_zeros(table):
    x = 0
    for i in range(len(table)):
        if 0 in table[i]:
            for j in range(len(table[i])):
                if ((table[i])[j]) == 0:
                    x += 1
                else:
                    continue
        else:
            continue
        return(x)
```

## `greatest_common_divisor`

Napište funkci `greatest_common_divisor(a, b)`, která pro zadaná čísla `a`, `b` vrátí jejich největšího společného dělitele.

```python
def greatest_common_divisor(a, b):
    a_dividor = 0
    b_dividor = 0
    common_dividor = 0
    Range_num = 0
    if a > b:
        Range_num = a
    else:
        Range_num = b
    for i in range(1, Range_num + 1):
        if a % i == 0:
            if i > a_dividor:
                a_dividor = i
                #print('a', a_dividor)
        if b % i == 0:
            if i > b_dividor:
                b_dividor = i
                #print('b', b_dividor)
        if a_dividor == b_dividor:
            common_dividor = a_dividor
            #print('c', common_dividor)
    return common_dividor
```
