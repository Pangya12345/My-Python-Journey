# Import the data from file called "Data.student"
from Data import data
# Set - up the indicators
count_A = 0
count_B = 0
count_C = 0
sum_A = 0
sum_B = 0
sum_C = 0
A_list = []
B_list = []
C_list = []
count_compare = []
output = {}

# Set - up the output title
for i in data:
    output[i["name"]] = {}
for t in output:
    output[t]["avg"] = None
    output[t]["max"] = None

# Define the function called "calculate average" to find the average result for each name
def calculate_average(info4, out123, count_a, count_b, count_c, sum_a, sum_b, sum_c):
    for y in info4:
        if y["name"] == "A":
            count_a = count_a + 1
            sum_a = sum_a + y["score"]
            average_a = (sum_a / count_a)
            out123[y["name"]]["avg"] = average_a # mean of value "A"
        elif y["name"] == "B":
            count_b = count_b + 1
            sum_b = sum_b + y["score"]
            average_b = (sum_b / count_b)
            out123[y["name"]]["avg"] = average_b # mean of value "B"
        else:
            count_c = count_c + 1
            sum_c = sum_c + y["score"]
            average_c = (sum_c / count_c)
            out123[y["name"]]["avg"] = average_c # mean of value "C"
calculate_average(data, output, count_A, count_B, count_C, sum_A, sum_B, sum_C)

# Find the largest value of each name
for x in data:
    if x["name"] == "A":
        if x["score"] > count_A:
            count_A = x["score"]
            output["A"]["max"] = count_A # largest value of "A"

    elif x["name"] == "B":
        if x["score"] > count_B:
            count_B = x["score"]
            output["B"]["max"] = count_B # largest value of "B"
    else:
        if x["score"] > count_C:
            count_C = x["score"]
            output["C"]["max"] = count_C # largest value of "C"
print(output)
