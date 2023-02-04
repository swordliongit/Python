

lang_file = "German.txt"

question_list = []
answer_list = []

combined_list = []

with open(lang_file) as file:
    combined_list = file.readlines()
    file.seek(0)

for line in combined_list:
    print(line)
    # answer_list = line.split(":")[1]

# print(question_list)
# print(answer_list)
