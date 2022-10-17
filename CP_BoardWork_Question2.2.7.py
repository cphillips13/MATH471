#Last updated on 10/16/2022
#Author: Corey Phillips
#Boardwork for Numerical Methods, problem 2.2.7

#Fill in the data from problem 4 using methods that are O(h^2) at each point
#Hint: See the previous problem number 6.

#First here is the table for problem 4.

tableColumn1 = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
tableColumn2 = [1.0,.9513507699,.9181687424,.8974706963,.8872638175,.8862269255,.8935153493,.9086387329,.9313837710,.9617658319,1.0]
h = 1/10

#(-3/2hf(x) + (2/h)f(x+h) + (-1/2h)f(x+2h) + bigO(h^2))
i = 0
print('x = ', tableColumn1[i], 'f(x) = ', tableColumn2[i], "f'(x) = N/A")
for i in range(8):
    print('x = ', tableColumn1[i+1], 'f(x) = ', tableColumn2[i+1], "f'(x) = ",
    ((-3/2)*h)*tableColumn2[i+1] + (2/h)*tableColumn2[i+2] + ((-1*h)/2)*tableColumn2[i+3])
    #print(((-3/2)*h)*tableColumn2[i+1] + (2/h)*tableColumn2[i+2] + ((-1*h)/2)*tableColumn2[i+3])
    #print("")

i = 9
for j in range(2):
    print('x = ', tableColumn1[i+j], 'f(x) = ', tableColumn2[i+j], "f'(x) = N/A")
