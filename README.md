# Hackathon Challenge

Given a starting sequence of 8bp and and ending sequence of 8bp find the minimal path of mutations to get from the start to the end.  The constraint is that you must **only** pass through sequences which exist in a bank of known mutations.

The solution here:

```
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA","TACCGGTT"]

python .\find_paths.py
['AACCGGTT', 'AACCGGTA', 'AAACGGTA']
3

```

For one which doesn't work:

```
start = "GACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA","TACCGGTT"]

python .\find_paths.py
[]
-1
```

