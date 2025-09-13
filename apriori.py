# Step 1: Read 5 text files
files = [
    r"C:\Users\IOTLAB_5\Documents\python program\apriori_algorithm\text1.txt",
    r"C:\Users\IOTLAB_5\Documents\python program\apriori_algorithm\text2.txt",
    r"C:\Users\IOTLAB_5\Documents\python program\apriori_algorithm\text3.txt",
    r"C:\Users\IOTLAB_5\Documents\python program\apriori_algorithm\text4.txt",
    r"C:\Users\IOTLAB_5\Documents\python program\apriori_algorithm\text5.txt"
]

transactions = []

for fname in files:
    with open(fname, "r") as f:
        line = f.readline().strip().split()
        transactions.append(line)

print("All Transactions:")
for i, t in enumerate(transactions, 1):
    print(f"Transaction {i}: {t}")


# Step 2: Collect all unique items
all_items = []
for t in transactions:
    for item in t:
        if item not in all_items:
            all_items.append(item)

print("\nUnique Items:", all_items)


# Step 3: Ask user for min support and min confidence
min_support = int(input("\nEnter minimum support (number of transactions): "))
min_confidence = float(input("Enter minimum confidence (0 to 1): "))


# Step 4: Calculate Support Count
support_count = {}

for item in all_items:
    count = 0
    for t in transactions:
        if item in t:
            count += 1
    support_count[item] = count

print("\nSupport Count:")
for item, count in support_count.items():
    if count >= min_support:
        print(f"{item}: {count} (frequent)")


# Step 5: Calculate Confidence (for pairs)
print("\nConfidence of Rules:")
for item1 in all_items:
    for item2 in all_items:
        if item1 != item2:
            # Support(X)
            item1_count = 0
            for t in transactions:
                if item1 in t:
                    item1_count += 1

            # Support(X∪Y)
            both_count = 0
            for t in transactions:
                if item1 in t and item2 in t:
                    both_count += 1

            if item1_count > 0:
                confidence = both_count / item1_count
                if confidence >= min_confidence:
                    print(f"{item1} -> {item2}, confidence = {confidence:.2f}")
