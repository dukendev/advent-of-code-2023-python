def concatenate_strings_to_integer(str_list):
    concatenated_str = "".join(str_list)
    result = int(concatenated_str)
    return result


test_path = "./input.txt"

with open(test_path, "r") as file:
    time_content = file.readline()
    distance_content = file.readline()

time_raw = time_content.split(":")[1].strip().split(" ")
time = list(filter(lambda x: x != "", time_raw))
time_of_race = concatenate_strings_to_integer(time)
time_nums = list(map(int, time))


distance_raw = distance_content.split(":")[1].strip().split(" ")
distance = list(filter(lambda x: x != "", distance_raw))
distance_of_race = concatenate_strings_to_integer(distance)
distance_nums = list(map(int, distance))


product = 1
for i, t in enumerate(time_nums):
    count = 0
    for j in range(0, t):
        if distance_nums[i] < (j * (t - j)):
            count += 1
    product *= count


print(product)


c = 0
for j in range(0, time_of_race):
    if distance_of_race < (j * (time_of_race - j)):
        c += 1

print(c)
