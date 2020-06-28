'''
Estimate Pi, given to random variables from 0 to 1
'''
import random


def est_pi(n):
  point_circle = 0
  total_point = 0
  for i in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    dis = x ** 2 + y ** 2
    if dis <= 1:
      point_circle += 1
    total_point += 1
  return 4 * point_circle / total_point

print(est_pi(100))