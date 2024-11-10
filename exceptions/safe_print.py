def sum_all(*args):
  """
  This function sums all the numeric arguments passed to it.

  Args:
    *args: A variable number of numeric arguments.

  Returns:
    The sum of all the arguments.
  """
  total = 0
  for num in args:
    try:
      total += num
    except TypeError:
      print("Error: All arguments must be numeric.")
  return total

def safe_print_list(my_list=[], x=0):
  """
  Prints x elements of a list.

  Args:
    my_list: The list to print from.
    x: The number of elements to print.

  Returns:
    The actual number of elements printed.
  """
  i = 0
  while i < x and i < len(my_list):
    print(my_list[i], end=" ")
    i += 1
  print()
  return i
