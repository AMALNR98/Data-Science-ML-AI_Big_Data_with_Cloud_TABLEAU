- s1: earth is the third planet from the sun
- s2: jupiter is the largest planet
---
- Step 1: Tokenization, avoiding duplicates
    - Words
        - earth
        - is 
        - the
        - third
        - planet
        - from sun
        - jupiter 
        - largest
- Step 2: Term frequency of sentence 1
  - TF(S1):
    - earth: 1/8
    - is: 1/8
    - the: 2/8
    - third: 1/8
    - planet: 1/8
    - from: 1/8
    - sun:1/8
    - jupiter: 0
    - largest: 0
  - TF(S2):
    - earth: 0/8
    - is: 1/5
    - the: 1/5
    - third: 0
    - planet: 1/5
    - from: 0
    - sun: 0
    - jupiter: 1/5
    - largest: 1/5
  - IDF: log(TD/AD)
    - Where: 
      - TD: Total documents (S1, S2-> 2)
        - AD: Available documents : in how-many documents available

| Words   | TF(S1) | TF(S2) | IDF : log(TD/AD) | TF - IDF(S1) | TF - IDF(S2)|
|---------|--------|--------|------------------|--------------|--------------
| Earth   | 1/8    | 0      | log(2/1) = 0.30  |
| is      | 1/8    | 1/5    | log(2/2) = 0     |
| the     | 2/8    | 1/5    | log(2/2) = 0              
| third   | 1/8    |
| planet  | 1/8 |
| from    | 1/8 |
| sun     | 1/8 |
| jupiter | 0 |
| largest | 0 |
