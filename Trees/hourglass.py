if __name__ == '__main__':
    i = 0
    j = 0
    l = []
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    while (i!=len(arr)):
        while(j!=(len(arr[0]) - 2)):
            sm = 0
            i1 = i + 2
            l1 = []
            for k in range(j, j+3):
                sm = sm + arr[i][k]
                l1.append(sm)
                print("1st : ", sm)
                sm = sm + arr[i+1][j+1]
                l1.append(sm)
                print("2nd : ", sm)
                sm = sm + arr[i+1][j+1]
                l1.append(sm)
                print("3rd : ", sm)

            #for k in range(j, j+3):
                #sm = sm + arr[i1][k]
            #sm = sm + arr[i+1][j+1]
            print("print befor append: ", sm)
            l.append(l1)
            l.append(sm)
            print(l)
            j +=1
        i += 1
    print(l) 

