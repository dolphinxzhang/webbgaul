# GenerateWeather.py
# Crystal Zhu, Cindy Zhang, Joyce Yuan
# 11.28.2018

"""
    A module that computes the windchill factor.
    Contains test function that allows users to check whether the computed windchill factor is correct or not. 
"""

import Weather

def WindChill(T,W):
    """Returns the windchill factor as a rounded float value.
    Fahrenheit temperature input will return result in Fahrenheit.
    Celsius temperature input will return result in Celsius.
    
    Precondition:
     T is a string that represents temperature, numbers without a unit specification will be assumed as in units of Fharenheit.
     W is a string that represents windspeed, numbers without a unit specification will be assumed as in units of miles per hour."""
     
    if 'F' in T: #temperature in Fharenheit 
        pt=T.find('F') #finding position of 'F' in user input
        temp= float(T[ :pt]) #extract numerical values of temperature 
       
    elif 'C' in T: #temperature in Celsius
        pt=T.find('C') #finding position of C in user inputs
        num= float(T[ :pt]) #extract numerical values
    
        temp=Weather.to_F(num) #converting Celsius to Fharenheit
    
        
    elif T.find('F') == -1 and T.find('C') == -1: #user input without units 
        temp= float(T)

    if 'mph' in W: #for wind speed in miles per hour
        pw=W.find('mph') #position of 'mph' in user input
        
        wind= float(W[ :pw]) #extract numerical values of windspeed
        
    elif 'kph' in W: #for wind speed in kilometers per hour
        pw=W.find('kph') #position of 'kph' in user input
        
        windink=float(W[ :pw]) #extract numerical values of windspeed in kilometers per hour
        
        wind=Weather.to_M(windink) #convert kilometers to miles 
           
    else: #for windspeed inputs without unit specification, assumes it's in miles
        wind=float(W) #convert string value into float 
   
   
    if 'C' in T: #user inputs temperature in Celsius      
        if temp<=50.0: 
            TrueWCF= float(round(Weather.to_C(Weather.WCF(temp, wind)))) #celsius input will return windchill factor in celsius
        if wind<=3.0: #if wind is smaller than 3mph
           return num #returns temperature in Celsius 
    if 'C' in T and wind <=3.0:
            return TrueWCF
    elif 'C' in T and temp>50.0:
            return num
    elif temp>=50.0 or wind<=3.0: #when temp is greater than 50F or the wind speed is less than 3mph, Fahrenheit windchill temp equals air temp.
        TrueWCF=float(round(temp))
    else:
        TrueWCF= float(round(Weather.WCF(temp,wind))) #otherwise, windchill factor will be calculated and returned as a rounded float value.
   
    return TrueWCF
    
 

def Test(T,W,TrueWC):
    """  Prints T, W, WindChill(T,W) and the True Windchill
    
    Precondition: T is a  valid temperature string, W is a valid wind string, and TrueWC is
    the actual wind chill asociated with T and W.
    """
    
    WC = WindChill(T,W)
    print 'WindChill returns %4.1f     Actual = %5.1f    Input = (%s,%s)    ' % (WindChill(T,W),TrueWC,T,W)


#Application Script 
if __name__ == '__main__':
    """ Confirms the correctness of WindChill in
    ten different representative cases.
    
    T=raw_input('temperature: ') #temperature input
    W=raw_input('windspeed: ') #wind speed 
    print WindChill(T,W)"""

    
    Test('85','100kph',85.0) #greater than 50F
    Test('30F','80mph',8.0) #combination of F and mph
    Test('40', '60',25.0) #both with no units
    Test('30C','60mph', 30.0) #combination of Celsius and mph, greater than 50F
    Test('30F', '2mph',30.0) # less than 3 mph
    Test('100C','0', 100.0) #greater than 50 F AND less than 3mph
    Test('-30F','80mph',-81.0) #combination of negative F and 80
    Test('-30C','40kph',-53.0)#combination of negative C and kph
    Test('-30F','1',-30.0) #combination of negative F and less than 3 mph
    Test('30F','40kph',16.0) # combination of F and kph
     
'''Ms. Duron's test cases:       
    Test('10','20',-9.0)
    Test('-5F','20',-29.0)
    Test('-15C','20',-15.0)
    Test('10','30mph',-12.0)
    Test('-5F','30mph',-33.0)
    Test('-15C','30mph',-19.0)
    Test('10','40kph',-11.0)
    Test('-5F','40kph',-31.0)
    Test('-15C','40kph',-17.0)
    Test('-15C','0',-15.0)
    '''
  
 
 

    

    
   
    






