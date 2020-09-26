def combo_string(a, b):
  if len(a) < len(b):
    str = a+b+a
  else:
    str = b+a+b
  return str