from main import (average, 
                  med, 
                  standard_deviation, 
                  summary_stats,
                  visualize_data)
import pandas as pd

'''Testing Simple Functionality of Descriptive Statistics Functions'''

dataset = {"Values": [1, 3, 5, 7, 9]}
testing_data = pd.DataFrame(dataset)
def testing_main_avg():
    assert average(testing_data['Values']) == 5

def testing_main_med():
    assert med(testing_data['Values']) == 5

def testing_main_std():
    assert standard_deviation(testing_data['Values']) == 3.16

testing_main_avg()
testing_main_med()
testing_main_std()


'''Testing Usage of Visualization Function'''


df = pd.read_csv("RiskData_SumScores.csv")

# Testing Usage of Visualization function:
visualize_data(
    df,
    "SES",
    "RiskPreferences",
    hue="Gender",
    title="Violin Plot for Age vs Risk Preferences,"
    + "\n"
    + "separated by Gender [1: Male; 2: Female]",
    xlabel="Socioeconomic Status",
    ylabel="Risk Preferences",
)
