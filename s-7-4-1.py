# 計数ソート
# サンプルを参考に実装はしたが、なぜソートされるのかよくわからない

def counting_sort(input_array, output_array, less_than):
  counter = [0] * less_than

  for i in range(0, len(input_array)):
    counter[input_array[i]] += 1
  
  for i in range(1, len(input_array)):
    counter[i] = counter[i] + counter[i - 1]
    
  for i in reversed(range(0, len(input_array))):
    output_array[counter[input_array[i]] - 1] = input_array[i]
    counter[input_array[i]] -= 1
  print(output_array)

list = [2, 5, 1, 3, 2, 3, 0]
output_array = [0] * len(list)

counting_sort(list, output_array, 7)

