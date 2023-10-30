1. KNN Algorithm (K-Neighbors Algorithm)
    - Supervised Learning
    - Used both classification and regression

    - in KNN we should give odd number to K.
- **Example 1**
- 
- ![](../../../Miselaneious/Performance%20measuments/png_files/example 1.png)
  - in this example consider fire point, we give k = 5 then for first point it takes 5 nearest points
    - then we get two circles and three squares, so the shape is predicted as square
  - in the second point we take k = 7 
    - so takes seven nearest shapes so here four circles and three squares
    - so the point is predicted as circle

- **Example 2**
- ![](../../../Miselaneious/Performance%20measuments/png_files/example 2 question.png)
   - in this table if x1 = 3 and x2 = 7 what will be the target??


Distance formula
--------
- p(X1,Y1) --------- p(X2,Y2)
``sqrt((X2-X1)^2 + (y2-y1)^2)``
----

from equation

- p1(7, 7) ------- p5(3, 7)
  - (3 - 7)^2 + (7-7) = root(16) = 4
- p2(7, 4) ------- p5(3, 7)
  - (3 - 7)^2 + (7 - 4)^2 = roo(25) = 5
- p3(3, 4) ------- p5(3,7)
  - (3 - 3)^2 + (7 - 4)^2 = root(9) = 3
- p4(1, 4) ------- p5(3, 7)
  - (3-1)^2 + (7-4)^2 = root(13) = 3.6
- ![](../../../Miselaneious/Performance%20measuments/png_files/final result.png)

- here we take k = 3 
- so take 3 nearest points of p5
- p3, p4, p1 are nearest to p5
- p3 = Good, p4 = Good, p1= Bad
- so majority values are good 
- so the result is good