import math
import matplotlib.pyplot as plt

domain = list(range(1,51))

def collatz_conjecture(x):
    sequence = []
    while x !=1:
        if x % 2 == 0:
            x = x //2
        else:
            x = 3*x + 1
        sequence.append(x) 
    return sequence

answer_list = []
for i in domain:
    collatz_answers = collatz_conjecture(i)
    answer_list.append(collatz_answers)
    print(f"{collatz_answers}")

print(f"{len(answer_list)}")

step_counts = [len(sequence) - 1 for sequence in answer_list] 
plt.plot(domain, step_counts)
plt.xlabel("Starting number")
plt.ylabel("Steps to reach 1")
plt.title("Collatz Conjecture")
plt.show()

plt.figure(figsize=(12, 6))

for seq in answer_list:
    plt.plot(seq, linewidth=0.5, alpha=0.4)

plt.yscale("log")
plt.xlabel("Step")
plt.ylabel("Value")
plt.show()