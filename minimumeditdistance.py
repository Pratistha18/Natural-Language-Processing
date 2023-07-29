def min_edit_distance(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        dp[i][0]=i
    for j in range(n+1):
        dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(1+dp[i-1][j],1+dp[i][j-1],2+dp[i-1][j-1])
    return dp[m][n]

#prompt user for string input
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

#compute the minimum edit distance
med=min_edit_distance(str1,str2)
print(med)