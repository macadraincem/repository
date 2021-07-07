# Michael Angelo C. Adraincem
# MCA655 11208422


import a2q1
import a2q2
import a2q3
import a2q4
import a2q5
import time
import a2q6_rmse


# test_file
# Parameter: filename, test/question number, restart no., step no.
# Return: None
# Post: Prints results
def test_file(filename, test, restart, steps, num):
    start_time = time.time()
    testfile = open(filename, "r")
    nErr = []
    x = 0;
    for line in testfile:
        x += 1
        values = line.split()
        list = []
        print(x)
        for i in range(1, num+1):
            list.append(int(values[i]))
        if test == "a2q1":
            result = a2q1.test(1, float(values[0]), list, 1000)
            nErr.append(result)
        elif test == "a2q2":
            result = a2q2.test(2, float(values[0]), list, 1000)
            nErr.append(result)
        elif test == "a2q3":
            result = a2q3.test(3, float(values[0]), list, 1000)
            nErr.append(result)
        elif test == "a2q4":
            result = a2q4.test(4, float(values[0]), list, 1000, restart, steps)
            nErr.append(result)
        elif test == "a2q5":
            result = a2q5.test(5, float(values[0]), list, 500)
            nErr.append(result)
    print(x)
    print("--- %s seconds ---" % ((time.time() - start_time)/x))
    print(a2q6_rmse.rmse(nErr, x))


def main():
    # test_file("filename.txt", "a2qx", restart number, step number, L number)

    # A2Q6_DATA1.TXT
    test_file("a2q6_data1.txt", "a2q1", 0, 0, 20)         #Random Guessing
    #  test_file("a2q6_data1.txt","a2q2", 0, 0, 20)       #Random Search
    # test_file("a2q6_data1.txt", "a2q3", 0, 0, 20)       #Hill Climbing
    # test_file("a2q6_data1.txt", "a2q5", 0, 0, 20)       #Stochastic Hill Climbing
    # test_file("a2q6_data1.txt", "a2q4", 50, 20, 20)     #Random Restart Hill (50x20)
    # test_file("a2q6_data1.txt", "a2q4", 10, 100, 20)    #Random Restart Hill (10x100)

    # A2Q6_DATA2.TXT
    # test_file("a2q6_data2.txt", "a2q1", 0, 0, 100)       #Random Guessing
    # test_file("a2q6_data2.txt","a2q2", 0, 0, 100)        #Random Search
    # test_file("a2q6_data2.txt", "a2q3", 0, 0, 100)       #Hill Climbing
    # test_file("a2q6_data2.txt", "a2q5", 0, 0, 100)       #Stochastic Hill Climbing
    # test_file("a2q6_data2.txt", "a2q4", 50, 20)          #Random Restart Hill (50x20)
    # test_file("a2q6_data2.txt", "a2q4", 10, 100)         #Random Restart Hill (10x100)



main()
