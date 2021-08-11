## 251.py
数组中的第K个最大元素

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5

示例 2:

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4

分析： 先排序，在输出第K个

十大经典排序算法复习（参考链接：https://www.cnblogs.com/onepixel/p/7674659.html）
![](https://img2018.cnblogs.com/blog/849589/201903/849589-20190306165258970-1789860540.png)
![](https://images2018.cnblogs.com/blog/849589/201804/849589-20180402133438219-1946132192.png)

#### 相关概念
    稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
    不稳定：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
    时间复杂度：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
    空间复杂度：是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。

1.冒泡排序（Bubble Sort）

    冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
    如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
    也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

1.1 算法描述

    比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    针对所有的元素重复以上的步骤，除了最后一个；
    重复步骤1~3，直到排序完成。

1.2 python 代码实现

    def bubbleSort(arr):
        for i in range(1, len(arr)):
            for j in range(0, len(arr)-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

2.选择排序

    选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。
    所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

2.1 算法步骤

    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。

2.2 python代码实现

    def selectionSort(arr):
        for i in range(len(arr) - 1):
            minIndex = i  # 记录最小数的索引
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j  # i 不是最小数时，将 i 和最小数进行交换
            if i != minIndex:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

3.插入排序

    插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，
    但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。
    插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，
    对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。

3.1 算法步骤

    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

3.2 python代码实现

    def insertionSort(arr):
        for i in range(len(arr)):
            preIndex = i-1
            current = arr[i]
            while preIndex >= 0 and arr[preIndex] > current:
                arr[preIndex+1] = arr[preIndex]
                preIndex -= 1
                arr[preIndex+1] = current
        return arr

4.希尔排序

    1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。
    它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。

4.1 算法步骤

    先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
    选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
    按增量序列个数k，对序列进行k 趟排序；
    每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

4.2 python代码实现

    def shell_sort(nums):
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i - gap >= 0 and nums[i - gap] > nums[i]:
                    nums[i - gap], nums[i] = nums[i], nums[i - gap]
                    i -= gap
            gap //= 2
        return nums

4.3 算法分析

    希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。
    动态定义间隔序列的算法是《算法（第4版）》的合著者Robert Sedgewick提出的。

5.归并排序

    归并排序是建立在归并操作上的一种有效的排序算法。
    该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
    将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
    若将两个有序表合并成一个有序表，称为2-路归并。

5.1 算法步骤

    把长度为n的输入序列分成两个长度为n/2的子序列；
    对这两个子序列分别采用归并排序；
    将两个排序好的子序列合并成一个最终的排序序列。

5.2 python代码实现

    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        # 分
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        # 合并
        return merge(left, right)


    def merge(left, right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res

5.3 算法分析

    归并排序是一种稳定的排序方法。
    和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，
    因为始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。

6.快速排序

    快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，
    其中一部分记录的关键字均比另一部分的关键字小，
    则可分别对这两部分记录继续进行排序，以达到整个序列有序。

6.1 算法步骤

    步骤1：从数列中挑出一个元素，称为 “基准”（pivot ）；
    步骤2：重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    步骤3：递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

6.2 python代码实现

    def quick_sort(list):
        less = []
        pivotList = []
        more = []
        # 递归出口
        if len(list) <= 1:
            return list
        else:
            # 将第一个值做为基准
            pivot = list[0]
            for i in list:
                # 将比急转小的值放到less数列
                if i < pivot:
                    less.append(i)
                # 将比基准打的值放到more数列
                elif i > pivot:
                    more.append(i)
                # 将和基准相同的值保存在基准数列
                else:
                    pivotList.append(i)
            # 对less数列和more数列继续进行排序
            less = quick_sort(less)
            more = quick_sort(more)
            return less + pivotList + more

6.3 算法分析

    不稳定排序，内排序，时间复杂度度O(nlogn)

7.堆排序

    堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
    堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

7.1 算法步骤

    创建最大堆:将堆所有数据重新排序，使其成为最大堆
    最大堆调整:作用是保持最大堆的性质，是创建最大堆的核心子程序
    堆排序:移除位在第一个数据的根节点，并做最大堆调整的递归运算

7.2 python代码实现

    def heap_sort(list):
        # 创建最大堆
        for start in range((len(list) - 2) // 2, -1, -1):
            sift_down(list, start, len(list) - 1)

        # 堆排序
        for end in range(len(list) - 1, 0, -1):
            list[0], list[end] = list[end], list[0]
            sift_down(list, 0, end - 1)
        return list

    # 最大堆调整
    def sift_down(lst, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

7.3 算法分析

    不稳定排序，内排序，时间复杂度为O(nlogn)

8.计数排序

    计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
    作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

8.1 算法步骤

    找出待排序的数组中最大和最小的元素；
    统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
    对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
    反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

8.2 python代码实现

    def CountingSort(arr):
        if arr.size < 2:
            return arr
        minValue, maxValue = getMinAndMax(arr)
        countArr = [0]*(maxValue-minValue+1)
        resultArr = [0]*len(arr)
        for i in range(len(arr)):
            countArr[arr[i]-minValue] += 1
        for i in range(1, len(countArr)):
            countArr[i] += countArr[i-1]
        for i in range(len(arr)-1, -1, -1):
            idx = countArr[arr[i]-minValue]-1
            resultArr[idx] = arr[i]
            countArr[arr[i]-minValue] -= 1
        return resultArr


    def getMinAndMax(arr):
        maxValue = arr[0]
        minValue = arr[0]
        for i in range(len(arr)):
            if arr[i] > maxValue:
                maxValue = arr[i]
            elif arr[i] < minValue:
                minValue = arr[i]
        return minValue, maxValue

8.3 算法分析

    稳定排序，外排序，时间复杂度O(n + k)O(n+k)，
    但是对于数据范围很大的数组，需要大量时间和内存。

9.桶排序

    桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
    为了使桶排序更加高效，我们需要做到这两点：
        在额外空间充足的情况下，尽量增大桶的数量
        使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
    桶排序的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，
    每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行。

9.1 算法步骤

    设置一个BucketSize，作为每个桶所能放置多少个不同数值；
    遍历输入数据，并且把数据依次映射到对应的桶里去；
    对每个非空的桶进行排序，可以使用其它排序方法，也可以递归使用桶排序；
    从非空桶里把排好序的数据拼接起来。

9.2 python代码实现

    def BucketSort(arr, bucket_size):
        if len(arr) < 2 or bucket_size == 0:
            return arr
        minValue, maxValue = getMinAndMax(arr)
        bucket_cnt = (maxValue-minValue)//bucket_size+1
        bucket = [[] for i in range(bucket_cnt)]
        for i in range(len(arr)):
            idx = (arr[i]-minValue) // bucket_size
            bucket[idx].append(arr[i])
        for i in range(len(bucket)):
            if len(bucket[i]) > 1:
                # 递归使用桶排序，也可使用其它排序算法
                bucket[i] = BucketSort(bucket[i], bucket_size//2)
        result = []
        for i in range(len(bucket)):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
        return result


    def getMinAndMax(arr):
        maxValue = arr[0]
        minValue = arr[0]
        for i in range(len(arr)):
            if arr[i] > maxValue:
                maxValue = arr[i]
            elif arr[i] < minValue:
                minValue = arr[i]
        return minValue, maxValue

9.3 算法分析

    稳定排序，外排序，时间复杂度O(n + k)，k为桶的个数。

10.基数排序

    基数排序是对数字每一位进行排序，从最低位开始排序

10.1 算法步骤

    找到数组最大值，得最大位数；
    从最低位开始取每个位组成radix数组；
    对radix进行计数排序（计数排序适用于小范围的特点）。

10.2 python代码实现

    def Radix_sort(nums):
        if not nums: return []
        _max = max(nums)
        # 最大位数
        maxDigit = len(str(_max))
        bucketList = [[] for _ in range(10)]
        # 从低位开始排序
        div, mod = 1, 10
        for i in range(maxDigit):
            for num in nums:
                bucketList[num % mod // div].append(num)
            div *= 10
            mod *= 10
            idx = 0
            for j in range(10):
                for item in bucketList[j]:
                    nums[idx] = item
                    idx += 1
                bucketList[j] = []
        return nums

251.py 解题思路：用快速排序对列表进行排序，再按索引取出第K个最大值