import random

words = [
    {"korean": "안녕하세요", "english": "Hello"},
    {"korean": "감사합니다", "english": "Thank you"},
    {"korean": "사랑", "english": "Love"},
    {"korean": "안녕", "english": "Hi/Bye"},
    {"korean": "좋아요", "english": "Good"},
    {"korean": "네", "english": "Yes"},
    {"korean": "아니요", "english": "No"},
    {"korean": "미안합니다", "english": "I'm sorry"},
    {"korean": "이해합니다", "english": "I understand"},
    {"korean": "도와주세요", "english": "Please help me"},
    {"korean": "잘가", "english": "Goodbye"},
    {"korean": "배고파요", "english": "I'm hungry"},
    {"korean": "아름다워요", "english": "It's beautiful"},
    {"korean": "괜찮아요", "english": "It's okay"},
    {"korean": "이것", "english": "This"},
    {"korean": "저것", "english": "That"},
    {"korean": "어디", "english": "Where"},
    {"korean": "언제", "english": "When"},
    {"korean": "무엇", "english": "What"},
    {"korean": "왜", "english": "Why"},
    {"korean": "어떻게", "english": "How"},
    {"korean": "사람", "english": "Person"},
    {"korean": "친구", "english": "Friend"},
    {"korean": "가족", "english": "Family"},
    {"korean": "학교", "english": "School"},
    {"korean": "직업", "english": "Job"},
    {"korean": "집", "english": "House"},
    {"korean": "차", "english": "Car"},
    {"korean": "책", "english": "Book"},
    {"korean": "영화", "english": "Movie"},
    {"korean": "음악", "english": "Music"},
    {"korean": "사랑해요", "english": "I love you"},
    {"korean": "안녕히 주무세요", "english": "Good night"},
    {"korean": "생일", "english": "Birthday"},
    {"korean": "결혼", "english": "Marriage"},
    {"korean": "오늘", "english": "Today"},
    {"korean": "내일", "english": "Tomorrow"},
    {"korean": "어제", "english": "Yesterday"},
    {"korean": "시간", "english": "Time"},
    {"korean": "이제", "english": "Now"},
    {"korean": "아직", "english": "Still"},
    {"korean": "전", "english": "Before"},
    {"korean": "후", "english": "After"},
    {"korean": "전화", "english": "Phone"},
    {"korean": "메일", "english": "Email"},
    {"korean": "여행", "english": "Travel"},
    {"korean": "일", "english": "Work"},
    {"korean": "공원", "english": "Park"},
    {"korean": "식당", "english": "Restaurant"},
    {"korean": "시장", "english": "Market"},
    {"korean": "가게", "english": "Store"},
    {"korean": "병원", "english": "Hospital"},
    {"korean": "약국", "english": "Pharmacy"},
    {"korean": "신문", "english": "Newspaper"},
    {"korean": "전화기", "english": "Telephone"},
    {"korean": "컴퓨터", "english": "Computer"},
    {"korean": "인터넷", "english": "Internet"},
    {"korean": "사전", "english": "Dictionary"},
    {"korean": "카메라", "english": "Camera"},
    {"korean": "사진", "english": "Photo"},
    {"korean": "문", "english": "Door"},
    {"korean": "창문", "english": "Window"},
    {"korean": "의자", "english": "Chair"},
    {"korean": "테이블", "english": "Table"},
    {"korean": "침대", "english": "Bed"},
    {"korean": "옷", "english": "Clothes"},
    {"korean": "신발", "english": "Shoes"},
    {"korean": "모자", "english": "Hat"},
    {"korean": "가방", "english": "Bag"},
    {"korean": "소리", "english": "Sound"},
    {"korean": "색", "english": "Color"},
    {"korean": "하늘", "english": "Sky"},
    {"korean": "물", "english": "Water"},
    {"korean": "음식", "english": "Food"},
    {"korean": "과일", "english": "Fruit"},
    {"korean": "야채", "english": "Vegetable"},
    {"korean": "고기", "english": "Meat"},
    {"korean": "생선", "english": "Fish"},
    {"korean": "빵", "english": "Bread"},
    {"korean": "컵", "english": "Cup"},
    {"korean": "접시", "english": "Plate"},
    {"korean": "포크", "english": "Fork"},
    {"korean": "나이프", "english": "Knife"},
    {"korean": "숟가락", "english": "Spoon"},
    {"korean": "맛", "english": "Taste"},
    {"korean": "건강", "english": "Health"},
    {"korean": "행복", "english": "Happiness"},
    {"korean": "슬픔", "english": "Sadness"},
    {"korean": "기쁨", "english": "Joy"},
    {"korean": "걱정", "english": "Worry"},
    {"korean": "공감", "english": "Empathy"},
    {"korean": "희망", "english": "Hope"},
    {"korean": "꿈", "english": "Dream"},
    {"korean": "진실", "english": "Truth"},
    {"korean": "거짓", "english": "Lie"},
    {"korean": "생각", "english": "Thought"},
    {"korean": "기억", "english": "Memory"},
    {"korean": "마음", "english": "Heart"},
    {"korean": "마법", "english": "Magic"},
    {"korean": "이유", "english": "Reason"},
    {"korean": "방법", "english": "Method"},
    {"korean": "세상", "english": "World"},
    {"korean": "사건", "english": "Event"},
    {"korean": "사실", "english": "Fact"},
    {"korean": "이해", "english": "Understanding"},
    {"korean": "의미", "english": "Meaning"},
    {"korean": "정보", "english": "Information"},
    {"korean": "지식", "english": "Knowledge"},
    {"korean": "배우다", "english": "Learn"},
    {"korean": "가르치다", "english": "Teach"}
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['korean']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!!\n")
            score += 1
        else:
            print(f"Wrong, The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")


def main():
    print("Welcome to the Korean Language Learning Flashcards App!")
    input("Please Enter to start the quiz....")
    quiz_user(words)

if __name__ == "__main__":
    main()