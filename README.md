<h1 align="center">Matboj</h1>

<div align="center">
    <img alt="GitHub last commit (branch)" src="https://img.shields.io/github/last-commit/Kiyotoko/anonymous-communication-systems/master">
    <img alt="Program" src="https://img.shields.io/badge/written_in-Python-blue">
    <img alt="Language" src="https://img.shields.io/badge/language-Deutsch-crimson">
</div>

## Aufgaben

#### Aufgabe 3

Der französische Mathematiker De Bouvelle bewies im Jahre 1509 fälschlicherweise, dass für alle $n\in\mathbb{N}$ eine der Zahlen $6n − 1$ oder $6n + 1$ eine Primzahl sei.<br>
a) Gib ein Beispiel an, das zeigt, dass er sich geirrt hat.<br>
b) Zeige, dass es unendlich viele n ∈ N gibt, die diese Aussage widerlegen.

```python
[20, 24, 31, 34, 36, 41, 48, 50, 54,
57, 69, 71, 79, 86, 88, 89, 92, 97]
Keine Primzahl: 120 ± 1
```

#### Aufgabe 8

Sei $q(n)$ die Quersumme einer natürlichen Zahl $n$.<br>
Finde die dreistellige natürliche Zahl $m$, für die der Quotient $\frac{m}{q(m)}$ minimal ist.

```python
199 10.473684210526315
```

#### Aufgabe 12

Jedes Quadrat eines $33\times33$ quadratischen Gitters ist mit einer der drei Farben gefärbt: rot, gelb oder blau - und zwar so, dass die Anzahl der Quadrate jeder Farbe gleich ist. Wenn zwei Quadrate mit einer gemeinsamen Kante unterschiedliche Farben haben, nennt man diese gemeinsame Kante eine Trennkante. Finde die minimale Anzahl von Trennkanten im Gitter.

```txt
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 011 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
000 000 000 000 000 001 111 111 111 111 111
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222
222 222 222 222 222 222 222 222 222 222 222

56 Trennkanten
```