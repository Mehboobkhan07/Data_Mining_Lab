
# Step 1: Input Transactions
transactions = [
    ["apple", "banana", "date", "elderberry"],
    ["banana", "cherry", "elderberry"],
    ["apple", "banana", "cherry", "elderberry"],
    ["banana", "elderberry"],
    ["apple", "banana", "cherry", "elderberry"]
]

# min_support = 3
min_support=int(input("enter the minimum support: "))


# Step 2: Count Frequency of Each Item

freq = {}
for t in transactions:
    for item in t:
        if item not in freq:
            freq[item] = 0
        freq[item] += 1

# Remove items below min_support
for k in list(freq.keys()):
    if freq[k] < min_support:
        del freq[k]

print("Frequent Items with Support >= 3:", freq)

# Step 3: Build FP-Tree (nested dict)

root = ["null", 1, {}]   # [item, count, children]

for t in transactions:
    # Keep only frequent items, order by global frequency
    ordered = [item for item in sorted(freq, key=freq.get, reverse=True) if item in t]
    
    # Insert into tree
    current = root
    for item in ordered:
        if item not in current[2]:
            current[2][item] = [item, 0, {}]
        current[2][item][1] += 1
        current = current[2][item]

# Step 4: Display FP-Tree

def print_tree(node, indent=0):
    if node[0] != "null":
        print("  " * indent + f"{node[0]} : {node[1]}")
    for child in node[2].values():
        print_tree(child, indent + 1)

print("\nFP-Tree:")
print_tree(root)

# Step 5: Mine Frequent Patterns (recursive)

def mine_tree(node, prefix, patterns):
    children = node[2]
    if not children:
        return
    for item, child in children.items():
        new_pattern = prefix + [item]
        patterns.append((new_pattern, child[1]))
        mine_tree(child, new_pattern, patterns)

frequent_patterns = []
mine_tree(root, [], frequent_patterns)

# Step 6: Filter patterns by min_support

final_patterns = [(p, s) for p, s in frequent_patterns if s >= min_support]

print("\nFrequent Patterns (multi-item included):")
for p, s in final_patterns:
    print(p, "Support:", s)


