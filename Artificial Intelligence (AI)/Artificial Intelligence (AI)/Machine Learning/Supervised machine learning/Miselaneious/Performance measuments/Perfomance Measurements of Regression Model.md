How to evaluate performance measurements
---
- In Regression model there is no confusion matirx
- Error
  1. MAE(Mean Absolute Error)
  2. MAPE(Mean Absolute Percentage Error)
  3. MSE(Mean Squared Error)
  4. RMSE (Root Mean Squared Error)
  5. R2_score : 


---

1. MAE
--
Actual_value : y
Predicted_value" : y^

    ``MAE = (1/N) sigma |y-y^|``
2. MAPE
3. MSE
    ``MSE = (1/N) sigma(y-y^)^2``
4. RMSE
---
    ``RMSE = sqrt((1/N) sigma|y-y^|)``
5. R2_Score
   - is also known as coefficient of determination
   - ``R2_Score = 1- RSS/TSS``
     - where
       - RSS : sum of square of Errors(bias)
       - TSS : Total sum of squares
  
    
![](./png_files/R2_Score.png)
