file_load = open("input1.txt", "r")
file_in = list(map(int, file_load.read().split("\n")))
file_load.close() 

def run():

  def two(input_in):
    for temp_x in input_in:
      for temp_y in input_in:
        if temp_x != temp_y:
          if temp_x + temp_y == 2020:
            return temp_x * temp_y

  def three(input_in):
    for temp_x in input_in:
      for temp_y in input_in:
        for temp_z in input_in:
          if temp_x != temp_y:
            if temp_y != temp_z:
              if temp_z != temp_x:
                if temp_x + temp_y + temp_z == 2020:
                  return temp_x * temp_y * temp_z

  return two(file_in), three(file_in)