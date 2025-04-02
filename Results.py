import matplotlib.pyplot as plt

# Data for Greedy Search
greedy_labels = [
    "a woman is mixing something", "a man is playing with a large", "a person is doing a wall",
    "a baby is playing up a", "a man is talking", "a person is playing on a",
    "a baby is drinking her baby", "a panda is climbing", "a man is doing a gun",
    "a man is pouring a on a pan"
]
greedy_times = [1.55, 0.81, 0.70, 0.69, 0.69, 0.67, 0.66, 0.67, 0.67, 0.66]

# Data for Beam Search
beam_labels = [
    "a woman is mixing something", "a man is playing with a", "a person is doing a wall",
    "a baby is playing", "a man is talking", "the animal is sitting on the ground",
    "a baby is feeding a baby", "a panda is climbing", "a man is doing a gun",
    "a man is cooking a"
]
beam_times = [23.30, 12.66, 17.15, 10.29, 9.65, 21.16, 17.88, 15.58, 24.55, 22.32]

# X-axis labels (common index for both methods)
indices = list(range(1, len(greedy_times) + 1))

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(indices, greedy_times, marker='o', linestyle='-', label="Greedy Search", color='blue')
plt.plot(indices, beam_times, marker='s', linestyle='--', label="Beam Search", color='red')

# Labels and title
plt.xlabel("Sentence Index")
plt.ylabel("Prediction Time (seconds)")
plt.title("Comparison of Prediction Time: Greedy vs. Beam Search")
plt.legend()
plt.grid(True)
plt.xticks(indices, labels=indices)  # Use indices for readability

# Show the plot
plt.show()
