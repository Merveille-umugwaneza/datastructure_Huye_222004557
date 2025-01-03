def counting_sort_by_priority(catalog, priority_key):
    
    max_priority = max(item[priority_key] for item in catalog)
    min_priority = min(item[priority_key] for item in catalog)
    
    
    count = [0] * (max_priority - min_priority + 1)
    
    
    for item in catalog:
        count[item[priority_key] - min_priority] += 1
    
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    output = [None] * len(catalog)
    for item in reversed(catalog):  
        priority = item[priority_key]
        position = count[priority - min_priority] - 1
        output[position] = item
        count[priority - min_priority] -= 1
    
    catalog[:] = output

catalog = [
    {"name": "Washing Machine", "priority": 3},
    {"name": "Refrigerator", "priority": 1},
    {"name": "Microwave", "priority": 2},
    {"name": "Air Conditioner", "priority": 2},
    {"name": "Dishwasher", "priority": 3},
]

print("Before Sorting:", catalog)
counting_sort_by_priority(catalog, priority_key="priority")
print("After Sorting:", catalog)

