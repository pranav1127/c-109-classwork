import pandas as pd
import statistics
import csv
df=pd.read_csv("data.csv")
Height_list=df["Height(Inches)"].to_list()
Weight_list=df["Weight(Pounds)"].to_list()
Height_mean=statistics.mean(Height_list)
Weight_mean=statistics.mean(Weight_list)
Height_median=statistics.median(Height_list)
Weight_median=statistics.median(Weight_list)
Height_mode=statistics.mode(Height_list)
Weight_mode=statistics.mode(Weight_list)
Height_std_deviation=statistics.stdev(Height_list)
Weight_std_deviation=statistics.stdev(Weight_list)
print("mean,meadian,mode for Height is{},{},{}".format(Height_mean,Height_median,Height_mode))
print("mean,meadian,mode for Weight is{},{},{}".format(Weight_mean,Weight_median,Weight_mode))
Height_first_std_deviation_start,Height_first_std_deviation_end =Height_mean-Height_std_deviation,Height_mean+Height_std_deviation
Height_second_std_deviation_start,Height_second_std_deviation_end=Height_mean-(2*Height_std_deviation),Height_mean+(2*Height_std_deviation)
Height_third_std_deviation_start,Height_third_std_deviation_end=Height_mean-(3*Height_std_deviation),Height_mean+(3*Height_std_deviation)

Weight_first_std_deviation_start,Weight_first_std_deviation_end =Weight_mean-Weight_std_deviation,Weight_mean+Weight_std_deviation
Weight_second_std_deviation_start,Weight_second_std_deviation_end=Weight_mean-(2*Weight_std_deviation),Weight_mean+(2*Weight_std_deviation)
Weight_third_std_deviation_start,Weight_third_std_deviation_end=Weight_mean-(3*Weight_std_deviation),Weight_mean+(3*Weight_std_deviation)

Height_list_of_data_within_1_std_deviation=[result for result in Height_list if result>Height_first_std_deviation_start and result<Height_first_std_deviation_end]
Height_list_of_data_within_2_std_deviation=[result for result in Height_list if result>Height_second_std_deviation_start and result<Height_second_std_deviation_end]
Height_list_of_data_within_3_std_deviation=[result for result in Height_list if result>Height_third_std_deviation_start and result<Height_third_std_deviation_end]

Weight_list_of_data_within_1_std_deviation=[result for result in Weight_list if result>Weight_first_std_deviation_start and result<Weight_first_std_deviation_end]
Weight_list_of_data_within_2_std_deviation=[result for result in Weight_list if result>Weight_second_std_deviation_start and result<Weight_second_std_deviation_end]
Weight_list_of_data_within_3_std_deviation=[result for result in Weight_list if result>Weight_third_std_deviation_start and result<Weight_third_std_deviation_end]

print("{} % of data for Height lies within one standard deviation".format(len(Height_list_of_data_within_1_std_deviation)*100.0/len(Height_list)))

print("{} % of data for Height lies within two standard deviation".format(len(Height_list_of_data_within_2_std_deviation)*100.0/len(Height_list)))

print("{} % of data for Height lies within three standard deviation".format(len(Height_list_of_data_within_3_std_deviation)*100.0/len(Height_list)))

print("{} % of data for Weight lies within one standard deviation".format(len(Weight_list_of_data_within_1_std_deviation)*100.0/len(Weight_list)))

print("{} % of data for Weight lies within two standard deviation".format(len(Weight_list_of_data_within_2_std_deviation)*100.0/len(Weight_list)))

print("{} % of data for Weight lies within three standard deviation".format(len(Weight_list_of_data_within_3_std_deviation)*100.0/len(Weight_list)))