# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:28:29 2017

@author: nangu
"""

import numpy as np
from scipy.stats import binom





class VanillaOption(object):

	
    def __init__(self,strike,expiry):
        
        self.strike = strike

        self.expiry = expiry



    def payoff(self, spot):
        pass



class VanillaCallOption(VanillaOption):

	
    def payoff(self, spot):
        return np.maximum(spot - self.strike, 0.0)



class VanillaPutOption(VanillaOption):

	

    def payoff(self, spot):

        return np.maximum(self.strike - spot, 0.0)
    
    
    
    
   
def EuropeanBinomialPricer(option, spot, rate, vol, div, steps):

    expiry = option.expiry

    strike = option.strike

    nodes = steps + 1

    h = expiry / steps 

    u = np.exp(((rate - div) * h) + vol * np.sqrt(h)) 

    d = np.exp(((rate - div) * h) - vol * np.sqrt(h))

    pu = (np.exp((rate - div) * h) - d) / (u - d)

    pd = 1 - pu

    discount = np.exp(-rate * expiry)

    spotT = 0.0

    payoffT = 0.0

    

    for i in range(nodes):

        spotT = spot * (u ** (steps - i)) * (d ** (i))

        payoffT += option.payoff(spotT)  * binom.pmf(steps - i, steps, pu)  

    price = discount * payoffT 

     



    return price

def AmericanBinomialPricer(option, spot, rate, vol, div, steps):
    expiry=option.expiry
    strike=option.strike
    nodes = steps + 1
    h = expiry / steps
    u = np.exp(((rate - div) * h) + vol * np.sqrt(h))
    d = np.exp(((rate - div) * h) - vol * np.sqrt(h))
    pu = (np.exp((rate - div) *h) - d) / (u - d)
    pd = 1 - pu
    discount= np.exp(-rate * h)
    dpu = discount * pu
    dpd = discount * pd

    payoffT= np.empty(nodes)
    SpotT= np.empty(nodes)

    for i in range(nodes):
        SpotT[i] = spot * (u ** (steps - i)) * (d ** i)
        payoffT[i] = option.payoff(SpotT[i])

    for i in range((steps - 1), -1, -1):
        for j in range(i + 1):
            payoffT[j] = dpu * payoffT[j] + dpd * payoffT[j + 1]
            SpotT[j] = SpotT[j] / u
            payoffT[j] = np.maximum(payoffT[j], option.payoff(SpotT[j]))

    return payoffT[0]


def NaiveMonteCarloPricer(option, spot, rate, vol, div, nreps):
    expiry=option.expiry
    strike=option.strike
    Z=np.random.normal(size=nreps)
    disc=np.exp(-rate*expiry)
    
    S_T=spot*np.exp((rate-div-0.5*vol**2)*expiry+vol*np.sqrt(expiry)*Z)
    payoff_T=option.payoff(S_T)
    price=payoff_T.mean()*disc
    return price
   

def main():
    
    theCall=VanillaCallOption(40,1)
    
    thePut=VanillaPutOption(40,1)
   
    EuropeanCallPrice=EuropeanBinomialPricer(theCall,41,0.08,0.3,0.0,3)
    EuropeanPutPrice=EuropeanBinomialPricer(thePut,41,0.08,0.3,0.0,3)
    AmericanCallPrice=AmericanBinomialPricer(theCall,41,0.08,0.3,0.0,3)
    AmericanPutPrice=AmericanBinomialPricer(thePut,41,0.08,0.3,0.0,3)
    
    print("The Three Period European Binomial Call Price is = {0:.4f}".format(EuropeanCallPrice))
    print("The Three Period European Binomial Put Price is = {0:.4f}".format(EuropeanPutPrice))
    print("The Three Period American Binomial Call Price is = {0:.4f}".format(AmericanCallPrice))
    print("The Three Period American Binomial Put Price is = {0:.4f}".format(AmericanPutPrice))

    EuropeanCallMontecarlo=NaiveMonteCarloPricer(theCall,41,0.08,0.3,0.0,100000)
    EuropeanPutMontecarlo=NaiveMonteCarloPricer(thePut,41,0.08,0.3,0.0,100000)
    print("the european call option using monte carlo method is %.6f"%EuropeanCallMontecarlo)
    print("the european put option using monte carlo method is %.6f"%EuropeanPutMontecarlo)
    
main()
