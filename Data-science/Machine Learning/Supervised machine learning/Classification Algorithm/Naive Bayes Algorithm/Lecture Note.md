***2. Naive Bayes Algorith***
-

1. Supervised Machine Learning Algorithm
2. Used for classification
3. To predict a categorical data
4. Based on probability

The classifier based on Bayes theorem, and Bayes Theorem based on conditional probability.

- Probability
  - Chances of occurrence
- Conditional Probability
  - Already an event is occurred, and based on that event, another event will happen.
  - Probability of an even occurring, given that another event has already occurred.
  - ```P(A/B) = P(A inter B)/P(B)```
    - Where :
      - A: first event
      - B: second event
  

**Example: Conditional Probability with Playing Cards**
-
Suppose you have a standard deck of 52 playing cards. You draw one card from the deck and want to find the probability of drawing a red card (hearts or diamonds) given that you have already drawn an ace.

Here's how you can calculate this using conditional probability:

1. **Initial Probabilities**:
   - There are 26 red cards (13 hearts and 13 diamonds) in the deck.
   - There are 4 aces in the deck (one ace in each suit: hearts, diamonds, clubs, and spades).

2. **Step 1: Calculate the Probability of Drawing an Ace**:
   - The probability of drawing an ace (\(P(\text{Ace})\)) is the number of aces divided by the total number of cards:
     \[P(\text{Ace}) = \frac{4}{52} = \frac{1}{13}\]

3. **Step 2: Calculate the Probability of Drawing a Red Card Given an Ace**:
   - Now, we want to find the conditional probability \(P(\text{Red}|\text{Ace})\), which is the probability of drawing a red card given that we have already drawn an ace.
   - Since there are two red aces (the ace of hearts and the ace of diamonds), the probability of drawing a red card given an ace is:
     \[P(\text{Red}|\text{Ace}) = \frac{2}{4} = \frac{1}{2}\]

So, the conditional probability of drawing a red card from the deck given that you have already drawn an ace is \(\frac{1}{2}\), or 50%.

This example demonstrates how conditional probability allows you to update probabilities based on additional information or events that have already occurred. In this case, the probability of drawing a red card is different when you know that you have an ace in your hand compared to when you have no information about the card drawn.

**Bayes Theorem**
- Equation:
  - ``P(A/B) = P(B/A) * P(A)/P(B)``    
    - Where:
      - P(A/B): Posterior probability, it is the conditional probability of event A occurring given that event B has occurred.
      - P(B/A): Likelihood Probability, it is the conditional probability of event B occurring given that event A has occurred
      - P(A): Prior Probability, it is the prior probability of event A, which is your initial belief about the probability of A before considering evidence.
      - P(B): Marginal probability, it  is the total probability of event B, which can be computed as the sum of the joint probabilities of A and B and not-A and B occurring:

**Bayes Theorem Example**
- ![](./png_files/Play%20Tennis%20example%20for%20Bayes%20therorem.jpeg)
     - x = outlook = sunny, Temperature = cool, Humidity:High, wind = Strong
- Ans) 
  - P(yes) = 9 / 14
  - P(No) = 5/14

    - | Outlook     | yes | no  |
      |-------------|-----|-----|
      | Sunny       | 2/9 | 3/5 |
      | Overcast    | 4/9 | 0   |
      | Rain        | 3/9 | 2/5 |
    
    - | Temperature | yes | no  |
      |-------------|-----|-----|
      | Hot         | 2/9 | 2/5 |
      | mild        | 4/9 | 2/5 |
      | cool        | 3/9 | 1/5 |
    
    - | Humidity | yes | no  |
      |----------|-----|-----|
      | high     | 3/9 | 4/5 |
      | normal   | 6/9 | 1/5 |
    
    - | Wind | yes | no  |
      |------|-----|-----|
      | weak | 6/9 | 2/5 |
      | mild | 3/9 | 3/5 |
      
 - x = outlook = sunny, Temperature = cool, Humidity:High, wind = Strong

  - P(yes/x) = P(x/yes)*P(yes)/P(x)
      - = P(outlook = sunny)/yes * P(Temperature = cool)/yes*P(Humidity = high)/yes*p(wind = strong/yes)*p(yes)
      - 2/9 * 3/9 * 3/9 * 3/9 * 9/14 = 0.005

    - P(no/x) = P(x)/no*P(no)/P(x)
      - 3/5*1/5*4/5*3/5*5/14 = 0.0205 

    - P(yes) = 0.0005
    - P(no) = 0.0205
  - So here P(no) is higher value, so in this condition we can't play