class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_end = {}
        end_start = {}
        existed = {}
        for num in nums:
            if num not in existed:
                existed[num] = True

                hadchainbefore = False
                if num - 1 in end_start:
                    # add eleement to rear
                    hadchainbefore = True
                    startofchain = end_start[num-1]
                    start_end[startofchain] = num
                    del end_start[num-1]
                    end_start[num] = startofchain
                    

                hadchainafter = False
                if num + 1 in start_end:
                    # add element to front
                    hadchainafter = True
                    endofchain = start_end[num+1]
                    end_start[endofchain] = num
                    del start_end[num+1]
                    start_end[num] = endofchain
                    

                
                # if they both were present form a connecting chain
                if hadchainbefore and hadchainafter:
                    if num == 3:
                        print(start_end)
                        print(end_start)
                    absoluteleft = end_start[num]
                    absoluteright = start_end[num]
                    del start_end[absoluteleft]
                    del start_end[num]
                    del end_start[num]
                    del end_start[absoluteright]
                    start_end[absoluteleft] = absoluteright
                    end_start[absoluteright] = absoluteleft

                
                if not hadchainbefore and not hadchainafter:
                    start_end[num] = num
                    end_start[num] = num

                
                
        # loop through the start_end and find best
        maxlen = 0
        for chains in start_end:
            maxlen = max(maxlen, (start_end[chains] - chains) + 1)

        return maxlen