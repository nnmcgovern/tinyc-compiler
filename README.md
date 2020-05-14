# Tiny-C Compiler (Scanner & Parser Only)

**Sample source.tinyc input file:**
```C
i=1;
while (i<10)
  i=i+1;
```

**Source code file passed to python through terminal:**
```
python tinyc_main.py source.tinyc
```

**Generated tokens.txt output file:**
```
id: "i"
ASGN: "="
num: "1"
SC: ";"
WHILE: "while"
LP: "("
id: "i"
COMPARE: "<"
num: "10"
RP: ")"
id: "i"
ASGN: "="
id: "i"
ADD: "+"
num: "1"
SC: ";"
```

**Generated parse_tree.txt output file:**
```
<program>
<statement_list>
<statement>
id
ASGN
<expr>
<test>
<sum>
<term>
num
<sum_opt>
<test_opt>
SC
<statement_list>
<statement>
WHILE
<paren_expr>
LP
<expr>
<test>
<sum>
<term>
id
<sum_opt>
<test_opt>
COMPARE
<sum>
<term>
num
<sum_opt>
RP
<statement>
id
ASGN
<expr>
<test>
<sum>
<term>
id
<sum_opt>
ADD
<term>
num
<sum_opt>
<test_opt>
SC
<statement_list>
```
