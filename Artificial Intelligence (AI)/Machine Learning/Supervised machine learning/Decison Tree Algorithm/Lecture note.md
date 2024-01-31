Basic components
1. Leaf 
2. Root node
3. Intermediate node

- ***Divide and conquer Method***
Involves breaking a complex problem into smaller, more manageable subproblems, solving those subproblems independently, and then combining their solutions to solve the original problem. This approach is often used to solve problems that can be divided into similar or identical subproblems.
    - Example
      - | Height | Weight | Gender |
        |--------|--------|--------|
        | 170    | 75     | F      |
        | 170    | 90     | M      |
        | 185    | 85     | M      |
        | 155    | 50     | F      |
        | 175    | 78     | F      |
- ![](png_file/1.png)
- Decision Tree
  - Height > 180 is root node 
  - Weight > 80 is an intermediate node
    - ![](png_file/2.png)

- ***How to select root node and intermediate node properly***
- It is based on entropy and information gain
  - Entropy
    - Measurement of impurity
    - Measurement of randomness
    - Ranger 0 - 1
    - 50:50 Proportion's entropy is 1
    - ![](png_file/3.png)
    - Equation
    - ![](png_file/4.png)
  - Information Gain
    -  Information Gain(IG) = E(S1)—E(S2)
      - Where :
        - Entropy(S1): Entropy before split data
        - Entropy(S2): Entropy after split data

- ***Problem***
----
  - ![](png_file/5.jpeg)
  - ![](png_file/6.jpeg)


- For blue:
    - Probability of Entropy before split
      - E(S1) = ((-16/30) * log2(16/30)) -  ((14/30) * log2(14/30) = 0.996791632
      - E(Balance < 50k) = 0.39
      - E(Balance >= 50k) = 0.79
      - Weighted average of entropy of balance < 50k and balance >= 50
      - E(S2) = (13/30) * 0.39 + (17/30) * 0.7 = 0.61
    - IG = E(S1) - E(S2)
      - 0.99 - 0.61 = 0.38
- Information gain of Residence
  - E(S1) = 0.99
  - E(Residence = OWN) = (-7/8) * log2(7/8) - (1/8) * log(1/8) = 0.54
  - E(Residence = Rent) = (4/10) * log2(4/10) - 10 * log2(6/10) = 0.97
  - E(Residence = Other) = (-5/12) * log2(5/12) - (7/12) * log2(7/12) = 0.98
  - E(S2) = (8/30) * 0.54 + (10/30) * 0.97 + (12/30) * 0.98 = 0.86
    - IG(Residence) = 0.99 - 0.86 = 0.13
  
  - ![](png_file/7.png)
