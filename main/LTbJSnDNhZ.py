import os
import json
import random
import string
class Utility:
 def generate_random_string(self, length):
  return ''.join(random.choice(string.ascii_letters) for _ in range(length))
 def write_to_file(self, filename, data):
  with open(filename, 'w') as f:
   f.write(data)
 def read_from_file(self, filename):
  with open(filename, 'r') as f:
   return f.read()
 def get_file_size(self, filename):
  return os.path.getsize(filename)
 def list_directory(self, path):
  return os.listdir(path)
 def create_json_file(self, filename, data):
  with open(filename, 'w') as f:
   json.dump(data, f)
 def read_json_file(self, filename):
  with open(filename, 'r') as f:
   return json.load(f)
 def random_number(self, start, end):
  return random.randint(start, end)
 def factorial(self, n):
  if n == 0:
   return 1
  return n * self.factorial(n - 1)
 def fibonacci(self, n):
  if n <= 0:
   return 0
  elif n == 1:
   return 1
  return self.fibonacci(n - 1) + self.fibonacci(n - 2)
 def is_prime(self, num):
  if num <= 1:
   return False
  for i in range(2, int(num**0.5) + 1):
   if num % i == 0:
    return False
  return True
 def get_primes_up_to(self, n):
  return [num for num in range(2, n + 1) if self.is_prime(num)]
 def count_words(self, text):
  return len(text.split())
 def reverse_string(self, s):
  return s[::-1]
 def sort_list(self, lst):
  return sorted(lst)
 def remove_duplicates(self, lst):
  return list(set(lst))
 def merge_sorted_lists(self, lst1, lst2):
  return sorted(lst1 + lst2)
 def find_max(lst):
  return max(lst)
 def find_min(lst):
  return min(lst)
