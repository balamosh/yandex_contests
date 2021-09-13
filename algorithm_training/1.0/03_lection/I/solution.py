students = int(input())

everyone_langs = set()
anyone_langs = set()
for i in range(students):
    n_langs = int(input())
    student_langs = set()
    for j in range(n_langs):
        curr_lang = input()
        student_langs.add(curr_lang)
        anyone_langs.add(curr_lang)
    if i == 0:
        everyone_langs = set(anyone_langs)
    to_delete = []
    for lang in everyone_langs:
        if lang not in student_langs:
            to_delete.append(lang)
    for j in range(len(to_delete)):
        everyone_langs.remove(to_delete[j])

print(len(everyone_langs))
for lang in everyone_langs:
    print(lang)
print(len(anyone_langs))
for lang in anyone_langs:
    print(lang)
