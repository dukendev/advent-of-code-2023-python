test_path = "./input.txt"

with open(test_path, "r") as file:
    time_content = file.readline()
    distance_content = file.readline()

time_raw = time_content.split(":")[1].strip().split(" ")
time = list(filter(lambda x: x != "", time_raw))
time_nums = list(map(int, time))
print(time_nums)


distance_raw = distance_content.split(":")[1].strip().split(" ")
distance = list(filter(lambda x: x != "", distance_raw))
distance_nums = list(map(int, distance))
print(distance_nums)


product = 1
for i, t in enumerate(time_nums):
    count = 0
    for j in range(0, t):
        if distance_nums[i] < (j * (t - j)):
            count += 1
    product *= count


print(product)
