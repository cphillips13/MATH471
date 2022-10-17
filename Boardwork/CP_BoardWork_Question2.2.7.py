#Last updated on 10/16/2022
#Author: Corey Phillips
#Boardwork for Numerical Methods, problem 2.2.7
#Present on 10/17/2022

#Fill in the data from problem 4 using methods that are O(h^2) at each point
#Hint: See the previous problem number 6.

#First here is the table for problem 4.

#Column 1 of our table: x
tableColumn1 = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
#Column 2 of our table: f(x)
tableColumn2 = [1.0,.9513507699,.9181687424,.8974706963,.8872638175,.8862269255,.8935153493,.9086387329,.9313837710,.9617658319,1.0]

#Our h value, the reason I am doing 1/10, is because this actually lets me approximate the derivatives without knowing the
#original function.
h = 1/10

#This is my big O approximation
#(-3/2hf(x) + (2/h)f(x+h) + (-1/2h)f(x+2h) + bigO(h^2))

#Prints a default for the x = 1, this is because I cannot 

for i in range(9):
    print('x = ', tableColumn1[i], 'f(x) = ', tableColumn2[i], "f'(x) = ",
    ((-3/2)*h)*tableColumn2[i] + (2/h)*tableColumn2[i+1] + ((-1*h)/2)*tableColumn2[i+2])
    #print(((-3/2)*h)*tableColumn2[i+1] + (2/h)*tableColumn2[i+2] + ((-1*h)/2)*tableColumn2[i+3])
    #print("")


#I printed a default derivative of N/A, by using methods that are big O
#I was not sure how to go above these numbers because I needed to use the values
#That were on the table and when I added more to my X, I did not have the values to 
#evaluate at.
i = 9
for j in range(2):
    print('x = ', tableColumn1[i+j], 'f(x) = ', tableColumn2[i+j], "f'(x) = N/A")

#Would like to work with this further, to bring it into a 2D numpy array.