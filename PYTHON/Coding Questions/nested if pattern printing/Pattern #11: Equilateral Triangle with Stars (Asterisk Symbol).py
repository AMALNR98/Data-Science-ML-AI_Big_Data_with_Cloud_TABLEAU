#           *
#
#          * *
#
#         * * *

#        * * * *

#       * * * * *

#      * * * * * *

#     * * * * * * *

size = 7
m = (2*size)-1
for i in range(0,size):
    for j in range(0, m):
        print(end=' ')
    m = m-1 # decrementing m after each loop
    for j in range(0, i+1):
        #Printing full triangle pyramid using stars
        print("*", end=' ')
    print(' ')

