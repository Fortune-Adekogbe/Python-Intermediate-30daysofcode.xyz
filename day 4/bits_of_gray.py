def bits_of_gray(n: int)->list:
  """
  This function returns the corresponding gray code for a specified number of bits.
  """
  try:
    assert type(n)==int and n > 0,"Invalid input"
  except AssertionError as e:
    return e
  if n==1:
    return ['0', '1']
  else:
    prev = bits_of_gray(n-1)
    return [f'0{i}' for i in prev] + [f'1{i}' for i in prev[::-1]]
print(bits_of_gray(3))
