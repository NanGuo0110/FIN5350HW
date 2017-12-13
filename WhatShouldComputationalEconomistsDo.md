
###  What Should (Computational) Economists Do?

**In January 1964,  James M Buchanan wrote a book " What should economists do?".In his book he 
 rejected the familiar proposition advanced by Jacob Viner that "economics is what economists do " and 
 suggested that economists should place more attention on "the theory of markets" and not "the theory of
 resource allocation". He advocated that economists should be market economists and they should focus 
 more on the " a particular form of human activity and upon the various arrangements that arise as a 
 result of this form of activity". However, everyone has different opinions on this questions. Andrew 
 Haldane, the chief economist at the bank of England, said that the economists are just like the weather 
 forecaster. But if economists are like forecasters, they should put more effort on the forecasting. 
 Meteorologists' jobs are difficult but  meteorologists do their job really well--thanks in part to 500,000 
 times everydays weather measurements and powerful supercomputers' simulations. Perhaps 
 economists should use this approach to forcast and analyze the economic market.Nowadays, from 
 online banking systems to  algorithmic trading,  most of the financial services are done in computers. The 
 computer technology has great influence on the financial industry over the last 30 years and a new term 
 generated--computational economics**

**What is computational economics? What are computational economists doing ? What should they be 
 doing?  In general, computational economics is the product of the intersection of physics, mathematics, 
 computer science , and economics. Computational economists use computer-based economic modeling 
 to analyze and help the government and industries to solve many complex economic problems. Since for 
 some complex economic problems, theoretical analysis can not do anything, and similar experiments like 
 natural science can not be carried out. The development of economics calls  for the emergence of new 
 scientific research methods. The increased ability of computers to deal with bulky data has provided the 
 possibility for computing as a means of economic research. Nowadays, the computer-based economic 
 analysis is ubiquitous in economic research and practice.**  
 
**In general, there are 3 steps for computational economists to solve the economic problems:**
   - **Mathematical modeling**
   - **Algorithm design - Coding - Show the numerical results**
   - **Combining numerical results with theoretical analysis and practical experiences and  give an answer 
      to the actual problem or proposes the revision of the model**  

**Here is a simple example to let u understand computatioal economists jobs :**  
 
### St=S0exp((r- 1/2 σ^2)T+σ* T^0.5*z)

**This is a formula that helps us to predict the stock price T (St) by using today's price (S0). Let's suppose
   A stock's price is 80 today, and what's the stock price of A after 2 years? Let's use a simple python 

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
[Ait text] (https://www.dropbox.com/s/qnai6lxzytvydku/Screenshot%202017-11-27%2019.57.56.png?dl=0)

**As we can see , the stock price of A satisfies the lognormal distribution.  Therefore, by using simple 
computing skills , we can easily get the final distributions of the stock price and which helps us analyze stock more efficiently.  In addition, the applications of computer technology and algorithms in financial fields goes far beyond this. For example, the "betterment" company, the online investing company that is based on the algorithms. Users will enter their goals (for example, a $ 250,000 deposit when they retire at age 65), age, income, and current financial assets. the computer based on all the programme they wrote will search and match across assets and financial instruments based on user-entered goals. The entire system will make adjustment based on the changes in user goals and changes in real time markets. However, even though the computing powers of computers is growing rapidly every 
year , we should not forget that  the amount of information that we need to process has been growing 
exponentially. Everyone creates a lot of data every day. In the field of financial research, with the 
improvement of research methods, the amount data has reached an unexpected level.  In today's internet 
age, more and more economic problems need to be solved by better algorithms.**  

**In general, the time consumptions of the pragramme can be divided in two ways:**
 
 **1. Frequently call the functions / methods:**

**For example, in a 3D game, video rendering for each frame needs to be calculated for each pixel of the screen. In a 1366 * 768, 24-frame video game, this calculation requires 25.17 million executions per second. If this calculation is not algorithm optimization, a bit of computing waste will accumulate, eventually affecting the performance of the entire game**

**2. Bad algorithms accumulated in various parts of the program. for eample:**
    
```C++
for (int i = 0; i <dimension (a); i ++) 
{...}
```

**In this program, dimension (a) needs to be repeated on each iteration. The corresponding optimization is to calculate size (a) before the for loop, and save it in a variable. This simple optimization saves time that seems minimal, but that optimization makes sense when the volume of data is huge.**

**Here is another example.  Let's assume you want to use your computer to find a nearby bank to deposit money. How the search engine to deal with your request? There are 2 different algorithms to solve this. The easiest way is to find out all the banks in the city, calculate the distance between you and them, sort all the results and return the smallest one. This may be the most intuitive, but definitely not the fastest. If a city has only a small number of banks, then this should be no problem, anyway, the calculation is not large. But if there are many banks in a city and many more require similar searches, the server is under much pressure. In this case, how do we optimize the algorithm? First, we can do a "pretreatment" of the banks in the city. For example, a city is divided into a number of "grid", and then placed him in a grid according to the user's location, sort the distance of banks only inside this grid.  The second algorithm is obviously the better one.  Therefore, better algorithms can help us process information quickly  and save us a lot of time. Especially in the financial and economic field,  the faster information transmission speed, the higher chance you will win .**


**in my opinions, every economist should study some computing skills. Leda  Braga, who is known as "the queen of quantitative tradings" said that the computer- algorithmic trading will become the mainstream trading methods over the next decades.  So for the computational economists, they should even place more attention on " how to become a better algorithm designer', not just on writing some financial programs and get the numerical results.  Nowadays many financial computing problems have the following characteristics: high-dimensional, multi-scale, nonlinear, singularity, complex regions, not only need large-scale computing, but also require high precision. Without a better algorithm design, the computing is not stable, the numerical economic results are not credible and sometimes contains singularity. In addition, you may have runtime error and cause your programmes terminate abnormally. Such problems can not be solved even by the most powerful computers today. Thus, for computational economists, they should do more algorithmic research and try to devise the optimization algorithms to help the industries and government to solve economic problems efficiently and correctly.**


