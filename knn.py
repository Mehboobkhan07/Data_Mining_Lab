import csv
import matplotlib.pyplot as plt
import seaborn as sns

data = []
filename = r"C:\Users\IOTLAB_5\Documents\python program\KNN\final_dataset.csv"

with open(filename, newline='') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        size = float(row[2])       # column 'size'
        price = float(row[4])      # column 'price'
        category = row[5]          # column 'Category'
        data.append([size, price, category])


sizes = [row[0] for row in data]
prices = [row[1] for row in data]
min_size, max_size = min(sizes), max(sizes)
min_price, max_price = min(prices), max(prices)

normalized_data = []
for row in data:
    norm_size = (row[0] - min_size) / (max_size - min_size)
    norm_price = (row[1] - min_price) / (max_price - min_price)
    normalized_data.append([norm_size, norm_price, row[2]])

size_input = float(input("Enter house size (sqft): "))
price_input = float(input("Enter house price (): "))
k = int(input("Enter k value for KNN: "))

# Normalize input
norm_input = [
    (size_input - min_size) / (max_size - min_size),
    (price_input - min_price) / (max_price - min_price)
]


distances = []
for row in normalized_data:
    dx = row[0] - norm_input[0] ## difference in size between dataset house and input house
    dy = row[1] - norm_input[1]##difference in price between dataset house and input house.
    distance = (dx**2 + dy**2) ** 0.5  ## pythagorus formula 
    distances.append([distance, row[2], row[0], row[1]])  # include coordinates for plotting


distances.sort(key=lambda x: x[0])
top_k = distances[:k]


votes = {}
for d in top_k:
    label = d[1]
    votes[label] = votes.get(label, 0) + 1

predicted = max(votes, key=votes.get)
print(f"\n The house is classified as: {predicted}")


x = [row[0] for row in normalized_data]
y = [row[1] for row in normalized_data]
labels = [row[2] for row in normalized_data]

plt.figure(figsize=(8,6))
sns.scatterplot(x=x, y=y, hue=labels, s=100, edgecolor='k')
plt.scatter(norm_input[0], norm_input[1], c='black', s=200, marker='X', label='Input House')

# Connect input to k neighbors
for neighbor in top_k:
    plt.plot([norm_input[0], neighbor[2]], [norm_input[1], neighbor[3]], 'k--', linewidth=1)

plt.title("Predicted Category: " + predicted)
plt.xlabel("Normalized Size")
plt.ylabel("Normalized Price")
plt.legend()
plt.grid(True)
plt.show()
