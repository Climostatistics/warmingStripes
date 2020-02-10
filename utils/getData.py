# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:38:31 2020

@author: akb

Pull data outlined in 
http://www.climate-lab-book.ac.uk/2018/warming-stripes/


"""


"""
Annual global temperatures from 1850-2017
https://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/download.html


Format https://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/series_format.html

These 'best estimate' series are computed as the medians of regional time series computed for each of the 100 ensemble member realisations. Time series are presented as temperature anomalies (deg C) relative to 1961-1990.

Quoted uncertainties are computed by integrating across the distribution described by the 100 ensemble members, together with additional measurement and sampling error and coverage uncertainty information.

The data files contain 12 columns:

Column 1 is the date.
Column 2 is the median of the 100 ensemble member time series.
Columns 3 and 4 are the lower and upper bounds of the 95% confidence interval of bias uncertainty computed from the 100 member ensemble.
Columns 5 and 6 are the lower and upper bounds of the 95% confidence interval of measurement and sampling uncertainties around the ensemble median. These are the combination of fully uncorrelated measurement and sampling uncertainties and partially correlated uncertainties described by the HadCRUT4 error covariance matrices.
Columns 7 and 8 are the lower and upper bounds of the 95% confidence interval of coverage uncertainties around the ensemble median.
Columns 9 and 10 are the lower and upper bounds of the 95% confidence interval of the combination of measurement and sampling and bias uncertainties.
Columns 11 and 12 are the lower and upper bounds of the 95% confidence interval of the combined effects of all the uncertainties described in the HadCRUT4 error model (measurement and sampling, bias and coverage uncertainties).
"""
annualGlobal="https://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/time_series/HadCRUT.4.6.0.0.annual_ns_avg.txt" 


url="https://www.ncdc.noaa.gov/cag/national/time-series/110-tmin-12-12-1895-2018.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000"

cetMinUrl="https://www.metoffice.gov.uk/hadobs/hadcet/cetmindly1878on_urbadj4.dat"
cetMaxUrl="https://www.metoffice.gov.uk/hadobs/hadcet/cetmaxdly1878on_urbadj4.dat"

