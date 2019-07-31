import re

sentence = """A, very   very; irregular_sentence"""
desired_output = "A very very irregular sentence"

print(' '.join(re.split("\W+", sentence)))