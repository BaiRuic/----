class BinarySearch():
    def search(self, list, item):
        '''
        数据需要是从小到大排列
        '''
        low = 0
        high = len(list)-1
        while (low <= high):
            mid = (low + high)//2 
            if(list[mid]>item):
                high = mid-1
            if(list[mid]<item):
                low = mid+1
            if(list[mid] == item):
                return mid   
        return None
        

if __name__ == '__main__':
    list = [53,56]
    item = 56
    S = BinarySearch()
    idx = S.search(list, item)
    print(idx)
