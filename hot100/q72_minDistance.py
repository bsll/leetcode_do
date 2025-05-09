'''
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
'''
'''
思路：动态规划 
f[i][j] = f[i-1][j-1] if word1[i] == word2[j]
f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1 if word1[i] != word2[j]
'''
class Solution(object):
    def minDistance(self, s1, s2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m ,n = len(s1),len(s2)
        if m == 0:
            return n
        if n == 0:
            return m

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = i
        for j in range(n + 1):
            dp[j][0] = j

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[i][j]
if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse","ros"))
    print(s.minDistance("intention","execution"))
