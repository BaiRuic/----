from typing import List

class SelectionSort():

    def select_max(self, arr:List):
        _max = arr[0]
        for i in arr:
            if i > _max:
                _max = i
        return _max

    def select_sort(self, arr:List):
        new_arr = []
        list_len = len(arr)
        while  len(new_arr) < list_len:
            new_arr.append(self.select_max(arr))
            arr.remove(self.select_max(arr))
        return new_arr

if __name__ == "__main__":
    arr = [i for i in range(10)]
    print(arr)
    S = SelectionSort()
    new_arr = S.select_sort(arr)
    
    print(new_arr)



