while True:
    user_input = input("영어 단어를 입력하세요: ")
    if user_input.strip() == "q":
        break
    if len(user_input.strip()) == 0:
        continue
    word = user_input.strip()
    meaning = input("한국어 뜻을 입력하세요: ")
    if meaning.strip() == "q":
        break
    if len(meaning.strip()) == 0:
        continue
    with open('vacabulary.txt', 'a') as f:
        f.write(f'{word}: {meaning}\n')