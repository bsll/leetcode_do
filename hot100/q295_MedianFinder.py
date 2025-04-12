'''
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

示例 1：

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
提示:

-105 <= num <= 105
在调用 findMedian 之前，数据结构中至少有一个元素
最多 5 * 104 次调用 addNum 和 findMedian
'''
'''
思路: 
小根堆保存大的那部分元素，这样小根堆堆顶就是大的元素中最小的，同理可得大根堆堆顶就是小的元素中最大的，这2的堆顶的2个元素就是，就是数组之后最中间的2个元素
用两个优先队列maxHeap和minHeap分别记录小于中位数的数和大于等于中位数的数。
小顶堆，存大的那一半（那么堆顶元素就是大半里面最小的那个，即最接近中心的）
大顶堆，存小的那一半（那么堆顶元素就是小半里面最大的那个，即最接近中心的）
当累计添加的数的数量为奇数时，minHeap中的数的数量比maxHeap多一个，此时中位数为minHeap的队头。当累计添加的数的数量为偶数时，两个优先队列中的数的数量相同，此时中位数为它们的队头的平均值。
'''
import headq
class MedianFinder(object):

    def __init__(self):
        #最大堆
        self.queMin = list()
        #最小堆 
        self.queMax = list()

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        queMin_ = self.queMin
        queMax_ = self.queMax
        # 若queMin为空，或当前数字num小于等于queMin的最大值（即-queMin[0]），则将num插入queMin（需取负数存入）。
        if not queMin_ or num <= -queMin_[0]:
            headq.headppush(queMin_, -num)
            # 若queMin的长度超过queMax长度超过1，说明小堆部分过大，需将queMin的最大值（堆顶）弹出，插入queMax。
            if len(queMax_) + 1 < len(queMin_):
                headq.headppush(queMax_, -headq.headppop(queMin_))
        else:
            headq.headppush(queMax_, num)
            # 若queMax的长度超过queMin，说明大堆部分过大，需将queMax的最小值（堆顶）弹出，插入queMin
            if len(queMax_) > len(queMin_):
                headq.heappush(queMin_, -headq.headppop(queMax_))        

    def findMedian(self):
        """
        :rtype: float
        """
        queMin_ = self.queMin
        queMax_ = self.queMax
        # 若总元素数为奇数（len(queMin) > len(queMax)），中位数为queMin的最大值（即-queMin[0]）。
        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        # 若为偶数，中位数是queMin最大值和queMax最小值的平均数。
        return (-queMin_[0] + queMax_[0]) / 2.0


# 最大堆最小堆解法，参考题解:https://www.bilibili.com/video/BV1J5411J7yj/
import heapq
class MedianFinder:
 
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = [] # 最大堆保存的是最小的n/2个数
        self.minHeap = [] # 最小堆保存的是最大的n/2个数
 
    def addNum(self, num: int) -> None:
        # 若两堆的数目相等，就让minHeap的元素个数+1
        # 具体做法分为两步 1.将新元素加入maxHeap 2.将maxHeap的堆顶元素加入minHeap
        if len(self.maxHeap)==len(self.minHeap):
            heapq.heappush(self.minHeap,-heapq.heappushpop(self.maxHeap,-num))
        else:
            heapq.heappush(self.maxHeap,-heapq.heappushpop(self.minHeap,num))
            
    def findMedian(self) -> float:
        if len(self.maxHeap)==len(self.minHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2.0
        else:
            return self.minHeap[0]