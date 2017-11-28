
###  What Should (Computational) Economists Do?

**In January 1964,  James M Buchanan wrote an book " What should economists do?".In his book he 
 rejected the familiar proposition advanced by Jacob Viner that "economics is what economists do " and 
 suggested that economists should place more attention on "the theory of markets" and not "the theory of
 resource allocation". He advocated that economists should be market economists and they should focus 
 more on the " a particular form of human activity and upon the various arrangement that arise as a 
 results of this form of activity". However, everyone has different opinions on this questions. Andrew 
 Haldane, the chief economist at the bank of england, said that the economists are just like the weather 
 forcaster. But if economists are like forecasters, they should put more effort on the forcasting. 
 Meteorologists' jobs are difficult but  meteorologists do their job really well--thanks in part to 500,000 
 times everydays' weather measurements and powerful supercomputers' simulations. Perhaps 
 economists should use this approach to forcast and analyze the economic market.Nowadays, from 
 online banking systems to  algorithmic trading,  most of financial services are done in computers. The 
 computer technology has great influence on the financial industry over the last 30 years and a new term 
 generated--computational economics**

**What is computational economics? What are computational economists doing ? What should they be 
 doing?  In general, computaional economics is the product of the intersection of physics, mathematics, 
 computer science , and economics. Computational economists uses computer-based economic modeling 
 to analyze and help the government and industries to solve many complex economic probelms. Since for 
 some complex economic problems, theoretical analysis can not do anything, and similar experiments like 
 natural science can not be carried out. The development of economics calls  for the emergence of new 
 scientific research methods. The increased ability of computers to deal with bulky data has provided the 
 possibility for computing as a means of economic research. Nowadays, computer-based economic 
 analysis is ubiquitous in economic research and practice.**  
 
**In genenral, there are 3 steps for computational economists to solve the economic problems:**
   - **Mathmatical modeling**
   - **Algorithm design - Coding - Show the numerical results**
   - **Combining numerical results with theoretical analysis and practical experiences and  give an answer 
      to the actual problem or proposes the revision of the model**  

**Here is a simple example to let u understand computatioal economists jobs :**  
 
**St=S0exp((r- 1/2 σ^2)T+σ* T^0.5*z)**

**This is a formula that help us to predict the stock price T (St) by using today's price (S0). Let's suppose
   A stock's price is 80 today, and what's the stock pice of A after 2 years? Let's use a simple python 
   program to solve this questions:**

```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
S0=80
r=0.08
sigma=0.3
T=3
I=5000
St=S0*np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*np.random.standard_normal(I))
plt.hist(St,bins=50)
plt.xlabel('stock price')
plt.ylabel('frequency')
```

## Output:
![Screenshot%202017-11-27%2019.57.56.png](attachment:Screenshot%202017-11-27%2019.57.56.png)  


**As we can see , the stock price of A satisfies the lognormal distribution.  Therefore, by using simple 
computing skills , we can easily get the final distributions of the stock price and which helps us analyze stock more efficiently.  However, eventhough the computing powers of computers is growing rapidly every 
year , we should not forget that  the amount of information that we need to process has been growing 
exponentially. Everyone creates a lot of data every day. In the field of financial research, with the 
improvement of research methods, the amount data has reached an unexpected level.  In today's internet 
age, more and more economic problems need to be solved by better algorithms.**  


**Here is another example.  Let's assume you want to use your computer to find a nearby bank to deposit money. How the search engine to deal with your request? There are 2 different algorithems to solve this. The easiest way is to find out all the banks in the city, calculate the distance between you and them, sort all the results and return the smallest one. This may be the most intuitive, but definitely not the fastest. If a city has only a small number of banks, then this should be no problem, anyway, the calculation is not large. But if there are many banks in a city and many more require similar searches, the server is under much pressure. In this case, how do we optimize the algorithm? First, we can do a "pretreatment" of the banks in the city. For example, a city is divided into a number of "grid", and then placed him in a grid according to the user's location, sort the distance of banks only inside this grid.  The second algorithm is obviously the better one.  Therefore, better algorithms can help us process information quickly  and save us a lot of time. Especially in the financial and economic field,  the faster information transmission speed, the higher chance you will win .**


**in my opinions, every economists should study some computing skills. Leda  Braga, who is known as "the queen of    qutitative tradings" said that the computer- algorithmic trading will become the mainstream trading methods over the next decades.  So for the computational economists, they should even place more attention on " how to become a better algorithm designer', not just on writting some financial programs and get the numerical results.  Nowadays many financial computing problems have the following characteristics: high-dimensional, multi-scale, nonlinear, singularity, complex regions, not only need large-scale computing, but also require high precision. Without a better algorithm design, the computing is not stable, the numerical economic results are not credible and sometimes contains singularity. In addition, you may have runtime error and cause your programes terminate abnormally. Such problems can not be solved even by the most powerful computers today. Thus, for computational economists, they should do more algorithmic research and try to devise the optimization algorithms to help the industries and government to solve economic problems efficiently and correctly.**


