def bits_of_gray(n):
  if n==1:
    return ['0', '1']
  else:
    prev = bits_of_gray(n-1)
    return [f'0{i}' for i in prev] + [f'1{i}' for i in prev[::-1]]
