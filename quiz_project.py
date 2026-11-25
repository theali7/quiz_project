def choose_topic(questions):
    topics = sorted({question["topic"] for question in questions})
    if not topics:
        print("Тем пока нет")
        return None
    print("\nВыберите тему:")
    for number, topic in enumerate(topics, start=1):
        print(f"{number} - {topic}")
    while True:
        choice = input("Номер темы: ").strip()
        if choice.isdecimal():
            number = int(choice)
            if 1 <= number <= len(topics):
                return topics[number - 1]
        print("Введите номер темы из списка")
def choose_level():
    levels = ["Лёгкий", "Средний", "Сложный"]
    print("\nВыберите сложность:")
    for number, level in enumerate(levels, start=1):
        print(f"{number} - {level}")
    while True:
        choice = input("Номер сложности: ").strip()
        if choice in ("1", "2", "3"):
            return levels[int(choice) - 1]
        print("Введите 1, 2 или 3")
def input_not_empty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Поле не должно быть пустым")
def choose_player(table_of_result):
    while True:
        player = input_not_empty("\nНапишите свой никнейм: ")
        if player not in table_of_result:
            return player
        print("Этот никнейм уже используется")
        print("1 - Я тот же игрок, хочу сыграть ещё раз")
        print("2 - Я другой человек, выберу другой ник")
        while True:
            choice = input("Выберите 1 или 2: ").strip()
            if choice in ("1", "2"):
                break
            print("Введите 1 или 2")
        if choice == "1":
            return player
def play(topic, level, questions):
    correct = []
    incorrect = []
    analysis = []
    selected_questions = []
    for question in questions:
        if question["topic"] == topic and question["difficulty"] == level:
            selected_questions.append(question)
    for number, question in enumerate(selected_questions, start=1):
        print(f'\nВопрос {number} из {len(selected_questions)}')
        print(question["question"])
        for option_number, option in enumerate(question["options"], start=1):
            print(f"{option_number} - {option}")
        while True:
            choice = input("Ваш ответ: ").strip()
            if choice in ("1", "2", "3", "4"):
                choice = int(choice)
                break
            print("Введите только цифры от 1 до 4")
        if choice == question["answer"]:
            correct.append(question["id"])
            print("Ваш ответ верный!")
        else:
            incorrect.append(question["id"])
            correct_text = question["options"][question["answer"] - 1]
            analysis.append({
                "question": question["question"],
                "user_answer": question["options"][choice - 1],
                "correct_answer": correct_text
            })
            print("Ваш ответ неправильный!")
            print(f"Правильный ответ: {correct_text}")
    return correct, incorrect, analysis
def show_analysis(analysis):
    if not analysis:
        print("Ошибок нет!")
        return
    while True:
        choice = input("\nХотите разбор ошибок? (да/нет): ").strip().lower()
        if choice == "да":
            print("\nРазбор ошибок:")
            for mistake in analysis:
                print(f'\nВопрос: {mistake["question"]}')
                print(f'Ваш ответ: {mistake["user_answer"]}')
                print(f'Правильный ответ: {mistake["correct_answer"]}')
            return
        if choice == "нет":
            return
        print("Введите да или нет")
def show_results(table_of_result):
    if not table_of_result:
        print("\nТаблица результатов пока пустая")
        return
    print("\nТаблица результатов:")
    for name, result in table_of_result.items():
        print(f"\n{name}:")
        print(
            f'{result["topic"]} — {result["difficulty"]} — '
            f'{result["score"]}/{result["max_score"]}'
        )
def add_question(questions):
    print("\n1 - Добавить вопрос на существующую тему")
    print("2 - Добавить новую тему и вопрос")
    print("0 - Назад")
    while True:
        choice = input("Выберите: ").strip()
        if choice in ("0", "1", "2"):
            break
        print("Введите 0, 1 или 2")
    if choice == "0":
        return
    if choice == "1":
        topic = choose_topic(questions)
        if topic is None:
            return
    else:
        existing_topics = {
            question["topic"].casefold()
            for question in questions
        }
        while True:
            topic = input_not_empty("Название новой темы: ")
            if topic.casefold() not in existing_topics:
                break
            print("Такая тема уже существует. Введите другое название")
    level = choose_level()
    text = input_not_empty("Напишите вопрос: ")
    options = []
    for number in range(1, 5):
        variant = input_not_empty(f"{number}-й вариант ответа: ")
        options.append(variant)
    while True:
        answer = input("Номер правильного ответа (1–4): ").strip()
        if answer in ("1", "2", "3", "4"):
            answer = int(answer)
            break
        print("Введите число от 1 до 4")
    max_id = 0
    for question in questions:
        if question["topic"] == topic and question["difficulty"] == level:
            if question["id"] > max_id:
                max_id = question["id"]
    questions.append({
        "id": max_id + 1,
        "topic": topic,
        "difficulty": level,
        "question": text,
        "options": options,
        "answer": answer
    })
    print("\nВопрос добавлен!")
def get_questions():
    questions = []
    groups = {
        "Python": {
            "Лёгкий": [
                (
                    "Какой тип данных возвращает input()?",
                    ["int", "str", "float", "bool"],
                    2
                ),
                (
                    "Что выведет код?\nprint(2 + 3 * 2)",
                    ["10", "12", "8", "7"],
                    3
                ),
                (
                    "Какая коллекция хранит пары ключ — значение?",
                    ["list", "tuple", "set", "dict"],
                    4
                ),
                (
                    "Что выведет код?\nnumbers = [10, 20, 30]\nprint(numbers[1])",
                    ["10", "20", "30", "1"],
                    2
                ),
                (
                    "Сколько раз выполнится print()?\n"
                    "for i in range(3):\n"
                    "    print(i)",
                    ["3 раза", "2 раза", "4 раза", "1 раз"],
                    1
                )
            ],
            "Средний": [
                (
                    "Что выведет код?\n"
                    "numbers = [1, 2, 3, 4, 5]\n"
                    "print(numbers[1:4])",
                    ["[1, 2, 3, 4]", "[2, 3, 4]", "[2, 3, 4, 5]", "[1, 2, 3]"],
                    2
                ),
                (
                    "Что произойдёт при обращении к отсутствующему ключу "
                    "обычного словаря через data[key]?",
                    ["Вернётся None", "Создастся ключ", "Ошибка KeyError", "Вернётся False"],
                    3
                ),
                (
                    "Что выведет код?\n"
                    "def add_item(items):\n"
                    "    items.append(3)\n"
                    "numbers = [1, 2]\n"
                    "add_item(numbers)\n"
                    "print(numbers)",
                    ["[1, 2]", "[3]", "None", "[1, 2, 3]"],
                    4
                ),
                (
                    "Чем return отличается от print()?",
                    [
                        "return возвращает значение и завершает вызов функции, "
                        "print() выводит данные",
                        "print() завершает функцию",
                        "Они всегда делают одно и то же",
                        "return работает только с числами"
                    ],
                    1
                ),
                (
                    "Что выведет код?\n"
                    "total = 0\n"
                    "for number in range(1, 6):\n"
                    "    if number % 2 == 0:\n"
                    "        continue\n"
                    "    total += number\n"
                    "print(total)",
                    ["15", "6", "9", "5"],
                    3
                )
            ],
            "Сложный": [
                (
                    "Что выведет код?\n"
                    "a = [[1, 2], [3, 4]]\n"
                    "b = a.copy()\n"
                    "b[0].append(5)\n"
                    "print(a[0])",
                    ["[1, 2]", "[1, 2, 5]", "[3, 4, 5]", "Ошибка"],
                    2
                ),
                (
                    "Что выведет код?\n"
                    "def add(value, items=[]):\n"
                    "    items.append(value)\n"
                    "    return items\n"
                    "add(1)\n"
                    "print(add(2))",
                    ["[2]", "[1]", "[1, 2]", "[]"],
                    3
                ),
                (
                    "Почему список нельзя использовать как ключ словаря?",
                    [
                        "Список хранит только числа",
                        "Ключами могут быть только строки",
                        "У списка нет индексов",
                        "Список является нехешируемым типом"
                    ],
                    4
                ),
                (
                    "Что выведет код?\n"
                    "def calculate(n):\n"
                    "    if n <= 1:\n"
                    "        return 1\n"
                    "    return n * calculate(n - 2)\n"
                    "print(calculate(5))",
                    ["15", "120", "10", "5"],
                    1
                ),
                (
                    "Что произойдёт?\n"
                    "x = 10\n"
                    "def change():\n"
                    "    x = x + 1\n"
                    "    return x\n"
                    "print(change())",
                    ["Выведется 11", "Выведется 10", "Ошибка UnboundLocalError", "Выведется None"],
                    3
                )
            ]
        },
        "Java": {
            "Лёгкий": [
                (
                    "Какой примитивный тип хранит true и false?",
                    ["int", "String", "boolean", "char"],
                    3
                ),
                (
                    "Что выведет код?\nSystem.out.println(2 + 3 * 2);",
                    ["10", "8", "12", "7"],
                    2
                ),
                (
                    "С какого индекса начинается массив?",
                    ["0", "1", "-1", "Зависит от длины"],
                    1
                ),
                (
                    "Что выведет код?\n"
                    "int[] numbers = {10, 20, 30};\n"
                    "System.out.println(numbers[2]);",
                    ["10", "20", "2", "30"],
                    4
                ),
                (
                    "Сколько раз выполнится println()?\n"
                    "for (int i = 0; i < 4; i++) {\n"
                    "    System.out.println(i);\n"
                    "}",
                    ["3 раза", "4 раза", "5 раз", "1 раз"],
                    2
                )
            ],
            "Средний": [
                (
                    "Что выведет код?\n"
                    "int a = 7;\n"
                    "int b = 2;\n"
                    "System.out.println(a / b);",
                    ["3.5", "4", "3", "Ошибка"],
                    3
                ),
                (
                    "Как сравнить содержимое двух строк, если они не null?",
                    ["equals()", "Всегда через ==", "Через in", "Сравнить длины"],
                    1
                ),
                (
                    "Что выведет код?\n"
                    "int[] a = {1, 2, 3};\n"
                    "int[] b = a;\n"
                    "b[0] = 9;\n"
                    "System.out.println(a[0]);",
                    ["1", "0", "3", "9"],
                    4
                ),
                (
                    "Что означает перегрузка методов?",
                    [
                        "Повторный вызов метода",
                        "Одинаковое имя, разные списки параметров",
                        "Различие только в возвращаемом типе",
                        "Удаление метода родителя"
                    ],
                    2
                ),
                (
                    "Что выведет код?\n"
                    "int total = 0;\n"
                    "for (int i = 1; i <= 5; i++) {\n"
                    "    if (i % 2 == 0) {\n"
                    "        continue;\n"
                    "    }\n"
                    "    total += i;\n"
                    "}\n"
                    "System.out.println(total);",
                    ["15", "6", "9", "5"],
                    3
                )
            ],
            "Сложный": [
                (
                    "Что выведет код?\n"
                    'String a = new String("Java");\n'
                    'String b = new String("Java");\n'
                    "System.out.println(a == b);\n"
                    "System.out.println(a.equals(b));",
                    ["true, true", "false, true", "false, false", "true, false"],
                    2
                ),
                (
                    "Что выведет программа?\n"
                    "class Main {\n"
                    "    static void change(int[] values) {\n"
                    "        values[0] = 9;\n"
                    "        values = new int[]{7, 8};\n"
                    "    }\n"
                    "    public static void main(String[] args) {\n"
                    "        int[] numbers = {1, 2};\n"
                    "        change(numbers);\n"
                    "        System.out.println(numbers[0]);\n"
                    "    }\n"
                    "}",
                    ["1", "7", "9", "Ошибка"],
                    3
                ),
                (
                    "Что вернёт метод при вызове?\n"
                    "static int calculate() {\n"
                    "    try {\n"
                    "        return 1;\n"
                    "    } finally {\n"
                    "        return 2;\n"
                    "    }\n"
                    "}",
                    ["2", "1", "Сначала 1, затем 2", "Ошибка компиляции"],
                    1
                ),
                (
                    "Что выведет программа?\n"
                    "class Animal {\n"
                    '    String sound() { return "Animal"; }\n'
                    "}\n"
                    "class Dog extends Animal {\n"
                    "    @Override\n"
                    '    String sound() { return "Dog"; }\n'
                    "}\n"
                    "class Main {\n"
                    "    public static void main(String[] args) {\n"
                    "        Animal animal = new Dog();\n"
                    "        System.out.println(animal.sound());\n"
                    "    }\n"
                    "}",
                    ["Animal", "Animal Dog", "Ошибка компиляции", "Dog"],
                    4
                ),
                (
                    "Какое правило связывает equals() и hashCode()?",
                    [
                        "Разные объекты всегда имеют разные хеш-коды",
                        "Равные по equals() объекты имеют одинаковый hashCode()",
                        "Одинаковый hashCode() всегда означает равенство",
                        "equals() возвращает int"
                    ],
                    2
                )
            ]
        },
        "C++": {
            "Лёгкий": [
                (
                    "Какой тип хранит true и false?",
                    ["int", "bool", "char", "double"],
                    2
                ),
                (
                    "Что выведет код?\nstd::cout << 2 + 3 * 2;",
                    ["10", "12", "8", "7"],
                    3
                ),
                (
                    "Какой заголовок нужен для std::cout?",
                    ["<iostream>", "<string>", "<vector>", "<cmath>"],
                    1
                ),
                (
                    "Что выведет код?\n"
                    "int numbers[] = {10, 20, 30};\n"
                    "std::cout << numbers[1];",
                    ["10", "30", "1", "20"],
                    4
                ),
                (
                    "Сколько раз выполнится вывод?\n"
                    "for (int i = 0; i < 3; i++) {\n"
                    "    std::cout << i;\n"
                    "}",
                    ["2 раза", "3 раза", "4 раза", "1 раз"],
                    2
                )
            ],
            "Средний": [
                (
                    "Что выведет код?\n"
                    "int a = 7;\n"
                    "int b = 2;\n"
                    "std::cout << a / b;",
                    ["3.5", "4", "3", "Ошибка компиляции"],
                    3
                ),
                (
                    "Что выведет код?\n"
                    "int x = 5;\n"
                    "int& ref = x;\n"
                    "ref = 12;\n"
                    "std::cout << x;",
                    ["12", "5", "0", "Ошибка компиляции"],
                    1
                ),
                (
                    "Какой метод std::vector добавляет элемент в конец?",
                    ["append()", "add()", "put()", "push_back()"],
                    4
                ),
                (
                    "Что выведет код?\n"
                    "int total = 0;\n"
                    "for (int i = 1; i <= 5; i++) {\n"
                    "    if (i % 2 == 0) {\n"
                    "        continue;\n"
                    "    }\n"
                    "    total += i;\n"
                    "}\n"
                    "std::cout << total;",
                    ["15", "9", "6", "5"],
                    2
                ),
                (
                    "Что означает перегрузка функций?",
                    [
                        "Вызов функции внутри себя",
                        "Различие только в возвращаемом типе",
                        "Одинаковое имя, разные списки параметров",
                        "Несколько вызовов функции в цикле"
                    ],
                    3
                )
            ],
            "Сложный": [
                (
                    "Что выведет программа?\n"
                    "#include <iostream>\n"
                    "void change(int* p) {\n"
                    "    *p = 9;\n"
                    "    p = nullptr;\n"
                    "}\n"
                    "int main() {\n"
                    "    int x = 1;\n"
                    "    int* ptr = &x;\n"
                    "    change(ptr);\n"
                    '    std::cout << x << " " << (ptr == nullptr);\n'
                    "}",
                    ["9 1", "9 0", "1 0", "Ошибка компиляции"],
                    2
                ),
                (
                    "Что выведет программа?\n"
                    "#include <iostream>\n"
                    "class Base {\n"
                    "public:\n"
                    "    virtual int value() const { return 1; }\n"
                    "};\n"
                    "class Derived : public Base {\n"
                    "public:\n"
                    "    int value() const override { return 2; }\n"
                    "};\n"
                    "int main() {\n"
                    "    Derived d;\n"
                    "    Base b = d;\n"
                    "    Base& ref = d;\n"
                    '    std::cout << b.value() << " " << ref.value();\n'
                    "}",
                    ["2 2", "1 1", "1 2", "2 1"],
                    3
                ),
                (
                    "В чём основная идея RAII?",
                    [
                        "Связать ресурс со временем жизни объекта "
                        "и освобождать его в деструкторе",
                        "Освобождать ресурсы только при завершении программы",
                        "Использовать только глобальные переменные",
                        "Заменить указатели числами"
                    ],
                    1
                ),
                (
                    "Что выведет программа?\n"
                    "#include <iostream>\n"
                    "int main() {\n"
                    "    int x = 5;\n"
                    "    auto by_value = [x]() { return x; };\n"
                    "    auto by_reference = [&x]() { return x; };\n"
                    "    x = 10;\n"
                    '    std::cout << by_value() << " " << by_reference();\n'
                    "}",
                    ["10 10", "5 5", "10 5", "5 10"],
                    4
                ),
                (
                    "Что произойдёт в C++11 или новее?\n"
                    "#include <memory>\n"
                    "int main() {\n"
                    "    std::unique_ptr<int> first(new int(5));\n"
                    "    std::unique_ptr<int> second = first;\n"
                    "}",
                    [
                        "Создадутся два независимых объекта int",
                        "Ошибка компиляции: unique_ptr нельзя копировать",
                        "Оба указателя станут nullptr",
                        "Владение автоматически перейдёт к second"
                    ],
                    2
                )
            ]
        }
    }
    for topic, levels in groups.items():
        for difficulty, items in levels.items():
            for number, item in enumerate(items, start=1):
                text, options, answer = item
                questions.append({
                    "id": number,
                    "topic": topic,
                    "difficulty": difficulty,
                    "question": text,
                    "options": options,
                    "answer": answer
                })
    return questions
def main():
    questions = get_questions()
    table_of_result = {}
    points_by_level = {
        "Лёгкий": 1,
        "Средний": 2,
        "Сложный": 3
    }
    while True:
        print("\n1 - Начать игру")
        print("2 - Посмотреть таблицу результатов")
        print("3 - Добавить вопрос")
        print("0 - Выйти")
        mode = input("Выберите: ").strip()
        if mode == "1":
            player = choose_player(table_of_result)
            topic = choose_topic(questions)
            if topic is None:
                continue
            level = choose_level()
            has_questions = False
            for question in questions:
                if question["topic"] == topic and question["difficulty"] == level:
                    has_questions = True
                    break
            if not has_questions:
                print("Для этой темы и сложности вопросов пока нет")
                continue
            correct, incorrect, analysis = play(topic, level, questions)
            points = points_by_level[level]
            score = len(correct) * points
            max_score = (len(correct) + len(incorrect)) * points
            print("\nИтоги игры:")
            print("Правильных ответов:", len(correct))
            print("Неправильных ответов:", len(incorrect))
            print(f"Баллы: {score}/{max_score}")
            show_analysis(analysis)
            table_of_result[player] = {
                "topic": topic,
                "difficulty": level,
                "score": score,
                "max_score": max_score
            }
        elif mode == "2":
            show_results(table_of_result)
        elif mode == "3":
            add_question(questions)
        elif mode == "0":
            print("До скорой встречи!")
            break
        else:
            print("Выберите пункт из меню")
if __name__ == "__main__":
    main()