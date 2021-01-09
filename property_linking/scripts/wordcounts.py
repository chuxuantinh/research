# coding=utf-8
# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple word frequency counter for 3-column TSV."""
from __future__ import print_function
from collections import Counter  # pylint: disable=g-importing-member
import sys


def count(f):
  word_counter = Counter()

  with open(f, "r") as kb_file:
    for line in kb_file:
      items = line.split("\t")[1].split()
      word_counter.update(items)
  return word_counter


def count_col(f):
  word_counter = Counter()
  with open(f, "r") as kb_file:
    for line in kb_file:
      items = line.split()
      word_counter.update(items)
  return word_counter

first = count_col(sys.argv[1])
second = count_col(sys.argv[2])

counter = Counter()
for word, val in first.items():
  if word in second:
    counter[word] += min(val, second[word])

print (counter.most_common(1000))
