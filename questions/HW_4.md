## Module 4: Time Series|||
### Problem 2: The Mauna Loa CO<sub>2</sub> Concentration
### The final model  
**1.** Plot the periodic signal $P_i$. (Your plot should have 1 data point for each month, so 12 in total.) Clearly state the definition the $P_i$, and make sure your plot is clearly labeled.
>Python tip: For interpolation, you may use interp1d from Scikit-learn. See Documentation on interp1d.|||
**2.** Plot the final fit $F_n(t_i)+P_i$. Your plot should clearly show the final model on top of the entire time series, while indicating the split between the training and testing data.|||
**3.** Report the root mean squared prediction error RMSE and the mean absolute percentage error MAPE with respect to the test set for this final model. Is this an improvement over the previous model $F_n(t_i)$ without the periodic signal? (Maximum 200 words.)|||
**4.** What is the ratio of the range of values of $F$ to the amplitude of $P_i$ and the ratio of the amplitude of $P$ to the range of the residual $R_i$ (from removing both the trend and the periodic signal)? Is this decomposition of the variation of the CO2 concentration meaningful? (Maximum 200 words.)|||

### Problem 3: Autocovariance Functions
**1.** Consider the MA(1) model,
$$X_t = W_t + \theta W_{t-1},$$
where $W_t\sim W\sim\mathcal{N}(0,\sigma^2)$. Find the autocovariance function of $X_t$.
Include all important steps of your computations in your report.|||
**2.** Consider the AR(1) model,
$$X_t=\phi X_{t-1}+W_t,$$
where $W\sim W_t\sim\mathcal{N}(0,\sigma^2)$. Suppose $|\phi|<1$. Find the autocovariance function of ${X_t}$. (You may use, without proving, the fact that ${X_t}$ is stationary if $|\phi|<1$.)  
Include all important steps of your computations in your report.|||

### Problem 5: Converting to Inflation Rates
### Inflation Rate from CPI
Repeat the model fitting and evaluation procedure from the previous page for the monthly inflation rate computed from CPI.

Your response should include:

**1.** 
- (1 point) Description of how you compute the monthly inflation rate from CPI and a plot of the monthly inflation rate.  
- (2 points) Description of how the data has been detrended and a plot of the detrended data. (You may choose to work with log of the CPI for later convenience.)  
- (3 points) Statement of and justification for the chosen AR($p$) model. Include plots and reasoning.  
- (3 points) Description of the final model; computation and plots of the 1 month-ahead forecasts for the validation data. In your plot, overlay predictions on top of the data.|||
**2.** (3 points) Which AR($p$) model gives the best predictions? Include a plot of the RSME against different lags $p$ for the model.|||
**3.** (3 points) Overlay your estimates of monthly inflation rates and plot them on the same graph to compare. (There should be 4 lines, one for each dataset, plus the predictions) over time (months from September 2013 onward).|||

### Problem 6: External Regressors and Model Improvements
### External Regressors
**1.** (4 points) Include as external regressors monthly average PriceStats inflation rate data and monthly BER data. Use cross-correlation plots to find the lag between the following:
- CPI inflation rate and PriceStats inflation rate
- CPI and BER inflation rate.|||
**2.** (3 points) Fit a new AR model to the CPI inflation rate with these external regressors and the most appropriate lag. Report the coefficients.
> Python Tip: You may use use sm.tsa.statespace.SARIMAX.|||
**3.** (3 points) Report the mean squared prediction error for 1 month ahead forecasts.|||
### Improving your model  
(5 points) What other steps can you take to improve your model from part III? What is the smallest prediction error you can obtain? Describe the model that performs best. You might consider including MA terms, adding a seasonal AR term, or adding multiple daily values (or values from different months) of PriceStats and BER data as external regressors.
