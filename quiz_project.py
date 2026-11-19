def choose_topic():
    print("\nВыберите тему: \n")
    print("1. Python\n" \
    "2. Java\n" \
    "3. C++")
    while True:
        topic_choice = input("Выберите по номеру: ")
        if topic_choice.isdigit() and topic_choice == "1" and len(topic_choice) == 1:
            return "Python"
        elif topic_choice.isdigit() and topic_choice == "2" and len(topic_choice) == 1:
            return "Java"
        elif topic_choice.isdigit() and topic_choice == "3" and len(topic_choice) == 1:
            return "C++"
        else:
            print("Что-то не так. Выберите тему по номеру")
def choose_level():
    print("Выберите уровень: ")
    print("1. Легкий\n" \
        "2. Средний\n" \
        "3. Сложный")
    while True:
        level_choice = input("Выберите уровень: ")
        if level_choice.isdigit() and level_choice == "1" and len(level_choice) == 1:
            return "Лёгкий"
        elif level_choice.isdigit() and level_choice == "2" and len(level_choice) == 1:
            return "Средний"
        elif level_choice.isdigit() and level_choice == "3" and len(level_choice) == 1:
            return "Сложный"
        else:
            print("Что-то не так. Выберите тему по номеру")
def play(topic, level, questions):
    correct = []
    incorrect = []
    for question in questions:
        if question["topic"] == topic and question["difficulty"] == level:
            print(f'\n{question["id"]}. {question["question"]}')
            for number, option in enumerate(question["options"], start=1):
                print(f"{number}. {option}")
            choice = input("Ваш ответ: ")
            if question["answer"] == int(choice):
                correct.append(question["id"])
            else:
                incorrect.append(question["id"])
    return correct, incorrect
def main():
    questions = [
    {
        "id": 1,
        "topic": "Python",
        "difficulty": "Лёгкий",
        "question": "Какой тип данных возвращает input()?",
        "options": ["int", "str", "float", "bool"],
        "answer": 2
    },
    {
        "id": 2,
        "topic": "Python",
        "difficulty": "Лёгкий",
        "question": "Что выведет код?\nprint(2 + 3 * 2)",
        "options": ["10", "12", "8", "7"],
        "answer": 3
    },
    {
        "id": 3,
        "topic": "Python",
        "difficulty": "Лёгкий",
        "question": "Какая коллекция хранит пары «ключ — значение»?",
        "options": ["list", "tuple", "set", "dict"],
        "answer": 4
    },
    {
        "id": 4,
        "topic": "Python",
        "difficulty": "Лёгкий",
        "question": "Что выведет код?\nnumbers = [10, 20, 30]\nprint(numbers[1])",
        "options": ["10", "20", "30", "1"],
        "answer": 2
    },
    {
        "id": 5,
        "topic": "Python",
        "difficulty": "Лёгкий",
        "question": "Сколько раз выполнится print()?\nfor i in range(3):\n    print(i)",
        "options": ["3 раза", "2 раза", "4 раза", "1 раз"],
        "answer": 1
    },
    {
        "id": 1,
        "topic": "Python",
        "difficulty": "Средний",
        "question": "Что выведет код?\nnumbers = [1, 2, 3, 4, 5]\nprint(numbers[1:4])",
        "options": [
            "[1, 2, 3, 4]",
            "[2, 3, 4]",
            "[2, 3, 4, 5]",
            "[1, 2, 3]"
        ],
        "answer": 2
    },
    {
        "id": 2,
        "topic": "Python",
        "difficulty": "Средний",
        "question": "Что произойдёт при обращении к отсутствующему ключу обычного словаря через data[key]?",
        "options": [
            "Вернётся None",
            "Создастся новый ключ",
            "Возникнет ошибка KeyError",
            "Вернётся False"
        ],
        "answer": 3
    },
    {
        "id": 3,
        "topic": "Python",
        "difficulty": "Средний",
        "question": "Что выведет код?\ndef add_item(items):\n    items.append(3)\nnumbers = [1, 2]\nadd_item(numbers)\nprint(numbers)",
        "options": ["[1, 2]", "[3]", "None", "[1, 2, 3]"],
        "answer": 4
    },
    {
        "id": 4,
        "topic": "Python",
        "difficulty": "Средний",
        "question": "Чем return отличается от print() внутри функции?",
        "options": [
            "return возвращает значение и завершает текущий вызов функции, а print() выводит данные",
            "print() завершает функцию, а return только выводит данные",
            "Они всегда выполняют одно и то же действие",
            "return можно использовать только для чисел"
        ],
        "answer": 1
    },
    {
        "id": 5,
        "topic": "Python",
        "difficulty": "Средний",
        "question": "Что выведет код?\ntotal = 0\nfor number in range(1, 6):\n    if number % 2 == 0:\n        continue\n    total += number\nprint(total)",
        "options": ["15", "6", "9", "5"],
        "answer": 3
    },
    {
        "id": 1,
        "topic": "Python",
        "difficulty": "Сложный",
        "question": "Что выведет код?\na = [[1, 2], [3, 4]]\nb = a.copy()\nb[0].append(5)\nprint(a[0])",
        "options": [
            "[1, 2]",
            "[1, 2, 5]",
            "[3, 4, 5]",
            "Возникнет ошибка"
        ],
        "answer": 2
    },
    {
        "id": 2,
        "topic": "Python",
        "difficulty": "Сложный",
        "question": "Что выведет код?\ndef add(value, items=[]):\n    items.append(value)\n    return items\nadd(1)\nprint(add(2))",
        "options": ["[2]", "[1]", "[1, 2]", "[]"],
        "answer": 3
    },
    {
        "id": 3,
        "topic": "Python",
        "difficulty": "Сложный",
        "question": "Почему список нельзя использовать как ключ словаря?",
        "options": [
            "Список может хранить только числа",
            "Ключами могут быть только строки",
            "Список не поддерживает индексы",
            "Список является нехешируемым типом"
        ],
        "answer": 4
    },
    {
        "id": 4,
        "topic": "Python",
        "difficulty": "Сложный",
        "question": "Что выведет код?\ndef calculate(n):\n    if n <= 1:\n        return 1\n    return n * calculate(n - 2)\nprint(calculate(5))",
        "options": ["15", "120", "10", "5"],
        "answer": 1
    },
    {
        "id": 5,
        "topic": "Python",
        "difficulty": "Сложный",
        "question": "Что произойдёт при вызове функции?\nx = 10\ndef change():\n    x = x + 1\n    return x\nprint(change())",
        "options": [
            "Выведется 11",
            "Выведется 10",
            "Возникнет ошибка UnboundLocalError",
            "Выведется None"
        ],
        "answer": 3
    },
    {
        "id": 1,
        "topic": "Java",
        "difficulty": "Лёгкий",
        "question": "Какой примитивный тип используется для значений true и false?",
        "options": ["int", "String", "boolean", "char"],
        "answer": 3
    },
    {
        "id": 2,
        "topic": "Java",
        "difficulty": "Лёгкий",
        "question": "Что выведет код?\nSystem.out.println(2 + 3 * 2);",
        "options": ["10", "8", "12", "7"],
        "answer": 2
    },
    {
        "id": 3,
        "topic": "Java",
        "difficulty": "Лёгкий",
        "question": "С какого индекса начинается нумерация элементов массива?",
        "options": ["0", "1", "-1", "Зависит от длины массива"],
        "answer": 1
    },
    {
        "id": 4,
        "topic": "Java",
        "difficulty": "Лёгкий",
        "question": "Что выведет код?\nint[] numbers = {10, 20, 30};\nSystem.out.println(numbers[2]);",
        "options": ["10", "20", "2", "30"],
        "answer": 4
    },
    {
        "id": 5,
        "topic": "Java",
        "difficulty": "Лёгкий",
        "question": "Сколько раз выполнится println()?\nfor (int i = 0; i < 4; i++) {\n    System.out.println(i);\n}",
        "options": ["3 раза", "4 раза", "5 раз", "1 раз"],
        "answer": 2
    },
    {
        "id": 1,
        "topic": "Java",
        "difficulty": "Средний",
        "question": "Что выведет код?\nint a = 7;\nint b = 2;\nSystem.out.println(a / b);",
        "options": ["3.5", "4", "3", "Возникнет ошибка"],
        "answer": 3
    },
    {
        "id": 2,
        "topic": "Java",
        "difficulty": "Средний",
        "question": "Как сравнить содержимое двух строк String, если обе ссылки не равны null?",
        "options": [
            "Использовать метод equals()",
            "Всегда использовать ==",
            "Использовать оператор in",
            "Сравнить только длины строк"
        ],
        "answer": 1
    },
    {
        "id": 3,
        "topic": "Java",
        "difficulty": "Средний",
        "question": "Что выведет код?\nint[] a = {1, 2, 3};\nint[] b = a;\nb[0] = 9;\nSystem.out.println(a[0]);",
        "options": ["1", "0", "3", "9"],
        "answer": 4
    },
    {
        "id": 4,
        "topic": "Java",
        "difficulty": "Средний",
        "question": "Что означает перегрузка методов (method overloading)?",
        "options": [
            "Повторный вызов одного метода",
            "Методы с одинаковым именем, но разными списками параметров",
            "Методы, отличающиеся только возвращаемым типом",
            "Удаление метода родительского класса"
        ],
        "answer": 2
    },
    {
        "id": 5,
        "topic": "Java",
        "difficulty": "Средний",
        "question": "Что выведет код?\nint total = 0;\nfor (int i = 1; i <= 5; i++) {\n    if (i % 2 == 0) {\n        continue;\n    }\n    total += i;\n}\nSystem.out.println(total);",
        "options": ["15", "6", "9", "5"],
        "answer": 3
    },
    {
        "id": 1,
        "topic": "Java",
        "difficulty": "Сложный",
        "question": "Что выведет код?\nString a = new String(\"Java\");\nString b = new String(\"Java\");\nSystem.out.println(a == b);\nSystem.out.println(a.equals(b));",
        "options": [
            "true, затем true",
            "false, затем true",
            "false, затем false",
            "true, затем false"
        ],
        "answer": 2
    },
    {
        "id": 2,
        "topic": "Java",
        "difficulty": "Сложный",
        "question": "Что выведет программа?\nclass Main {\n    static void change(int[] values) {\n        values[0] = 9;\n        values = new int[]{7, 8};\n    }\n    public static void main(String[] args) {\n        int[] numbers = {1, 2};\n        change(numbers);\n        System.out.println(numbers[0]);\n    }\n}",
        "options": ["1", "7", "9", "Возникнет ошибка"],
        "answer": 3
    },
    {
        "id": 3,
        "topic": "Java",
        "difficulty": "Сложный",
        "question": "Что выведет программа?\nclass Main {\n    static int calculate() {\n        try {\n            return 1;\n        } finally {\n            return 2;\n        }\n    }\n    public static void main(String[] args) {\n        System.out.println(calculate());\n    }\n}",
        "options": [
            "2",
            "1",
            "Сначала 1, затем 2",
            "Возникнет ошибка компиляции"
        ],
        "answer": 1
    },
    {
        "id": 4,
        "topic": "Java",
        "difficulty": "Сложный",
        "question": "Что выведет программа?\nclass Animal {\n    String sound() {\n        return \"Animal\";\n    }\n}\nclass Dog extends Animal {\n    @Override\n    String sound() {\n        return \"Dog\";\n    }\n}\nclass Main {\n    public static void main(String[] args) {\n        Animal animal = new Dog();\n        System.out.println(animal.sound());\n    }\n}",
        "options": [
            "Animal",
            "Animal Dog",
            "Возникнет ошибка компиляции",
            "Dog"
        ],
        "answer": 4
    },
    {
        "id": 5,
        "topic": "Java",
        "difficulty": "Сложный",
        "question": "Какое правило обязательно соблюдать при переопределении equals() и hashCode()?",
        "options": [
            "Разные объекты всегда должны иметь разные хеш-коды",
            "Если объекты равны по equals(), их hashCode() должен совпадать",
            "Одинаковый hashCode() всегда означает равенство по equals()",
            "Метод equals() должен возвращать int"
        ],
        "answer": 2
    },
    {
        "id": 1,
        "topic": "C++",
        "difficulty": "Лёгкий",
        "question": "Какой тип используется для значений true и false?",
        "options": ["int", "bool", "char", "double"],
        "answer": 2
    },
    {
        "id": 2,
        "topic": "C++",
        "difficulty": "Лёгкий",
        "question": "Что выведет код?\nstd::cout << 2 + 3 * 2;",
        "options": ["10", "12", "8", "7"],
        "answer": 3
    },
    {
        "id": 3,
        "topic": "C++",
        "difficulty": "Лёгкий",
        "question": "Какой заголовок нужно подключить для использования std::cout?",
        "options": ["<iostream>", "<string>", "<vector>", "<cmath>"],
        "answer": 1
    },
    {
        "id": 4,
        "topic": "C++",
        "difficulty": "Лёгкий",
        "question": "Что выведет код?\nint numbers[] = {10, 20, 30};\nstd::cout << numbers[1];",
        "options": ["10", "30", "1", "20"],
        "answer": 4
    },
    {
        "id": 5,
        "topic": "C++",
        "difficulty": "Лёгкий",
        "question": "Сколько раз выполнится вывод?\nfor (int i = 0; i < 3; i++) {\n    std::cout << i;\n}",
        "options": ["2 раза", "3 раза", "4 раза", "1 раз"],
        "answer": 2
    },
    {
        "id": 1,
        "topic": "C++",
        "difficulty": "Средний",
        "question": "Что выведет код?\nint a = 7;\nint b = 2;\nstd::cout << a / b;",
        "options": ["3.5", "4", "3", "Возникнет ошибка компиляции"],
        "answer": 3
    },
    {
        "id": 2,
        "topic": "C++",
        "difficulty": "Средний",
        "question": "Что выведет код?\nint x = 5;\nint& ref = x;\nref = 12;\nstd::cout << x;",
        "options": ["12", "5", "0", "Возникнет ошибка компиляции"],
        "answer": 1
    },
    {
        "id": 3,
        "topic": "C++",
        "difficulty": "Средний",
        "question": "Какой метод std::vector добавляет элемент в конец?",
        "options": ["append()", "add()", "put()", "push_back()"],
        "answer": 4
    },
    {
        "id": 4,
        "topic": "C++",
        "difficulty": "Средний",
        "question": "Что выведет код?\nint total = 0;\nfor (int i = 1; i <= 5; i++) {\n    if (i % 2 == 0) {\n        continue;\n    }\n    total += i;\n}\nstd::cout << total;",
        "options": ["15", "9", "6", "5"],
        "answer": 2
    },
    {
        "id": 5,
        "topic": "C++",
        "difficulty": "Средний",
        "question": "Что означает перегрузка функций в C++?",
        "options": [
            "Вызов функции внутри самой себя",
            "Функции с одинаковым именем, отличающиеся только возвращаемым типом",
            "Функции с одинаковым именем, но разными списками параметров",
            "Вызов функции несколько раз в цикле"
        ],
        "answer": 3
    },
    {
        "id": 1,
        "topic": "C++",
        "difficulty": "Сложный",
        "question": "Что выведет программа?\n#include <iostream>\nvoid change(int* p) {\n    *p = 9;\n    p = nullptr;\n}\nint main() {\n    int x = 1;\n    int* ptr = &x;\n    change(ptr);\n    std::cout << x << \" \" << (ptr == nullptr);\n}",
        "options": ["9 1", "9 0", "1 0", "Возникнет ошибка компиляции"],
        "answer": 2
    },
    {
        "id": 2,
        "topic": "C++",
        "difficulty": "Сложный",
        "question": "Что выведет программа?\n#include <iostream>\nclass Base {\npublic:\n    virtual int value() const { return 1; }\n};\nclass Derived : public Base {\npublic:\n    int value() const override { return 2; }\n};\nint main() {\n    Derived d;\n    Base b = d;\n    Base& ref = d;\n    std::cout << b.value() << \" \" << ref.value();\n}",
        "options": ["2 2", "1 1", "1 2", "2 1"],
        "answer": 3
    },
    {
        "id": 3,
        "topic": "C++",
        "difficulty": "Сложный",
        "question": "В чём основная идея RAII в C++?",
        "options": [
            "Связать управление ресурсом со временем жизни объекта: получать ресурс при инициализации и освобождать в деструкторе",
            "Освобождать все ресурсы только при завершении программы",
            "Использовать только глобальные переменные",
            "Заменить все указатели целыми числами"
        ],
        "answer": 1
    },
    {
        "id": 4,
        "topic": "C++",
        "difficulty": "Сложный",
        "question": "Что выведет программа?\n#include <iostream>\nint main() {\n    int x = 5;\n    auto by_value = [x]() { return x; };\n    auto by_reference = [&x]() { return x; };\n    x = 10;\n    std::cout << by_value() << \" \" << by_reference();\n}",
        "options": ["10 10", "5 5", "10 5", "5 10"],
        "answer": 4
    },
    {
        "id": 5,
        "topic": "C++",
        "difficulty": "Сложный",
        "question": "Что произойдёт при компиляции кода C++11 или новее?\n#include <memory>\nint main() {\n    std::unique_ptr<int> first(new int(5));\n    std::unique_ptr<int> second = first;\n}",
        "options": [
            "Создадутся два независимых объекта int",
            "Возникнет ошибка компиляции: std::unique_ptr нельзя копировать",
            "Оба указателя автоматически станут nullptr",
            "Владение автоматически перейдёт к second"
        ],
        "answer": 2
    }
]
    table_of_result = {}
    while True:
        print("1 - Начать игру\n" \
        "2 - Посмотреть таблицу результатов\n" \
        "3 - Добавить вопрос\n" \
        "4 - Выйти из программы")
        mode = input("Выберите: ")
        if mode.isdigit() and len(mode) == 1 and 1 <= int(mode) <= 4 and mode == "1":
            player = input("Напишите свое имя: ")
            player_choice_topic = choose_topic()
            player_choice_level = choose_level()
            correct_answers, incorrect_answers = play(player_choice_topic, player_choice_level, questions)
            print("\nПравильные ответы:", len(correct_answers))
            print("Номера вопросов:", ", ".join(str(n) for n in correct_answers))
            print("Неправильные ответы:", len(incorrect_answers))
            print("Номера вопросов:", ", ".join(str(n) for n in incorrect_answers),"\n")
            table_of_result[player] = f"{len(correct_answers)}/5"
        elif mode.isdigit() and len(mode) == 1 and 1 <= int(mode) <= 4 and mode == "2":
            if not table_of_result:
                print("Упс таблица еще пусто")
            else:
                for name, result in table_of_result.items():
                    print(f"{name} - {result}\n")
        elif mode.isdigit() and len(mode) == 1 and 1 <= int(mode) <= 4 and mode == "3":
            print("1 - Добавить вопрос на существующую тему\n" \
            "2 - Добавить новую тему")
            add_question_topic = input("Выберите: ")
        elif mode.isdigit() and len(mode) == 1 and 1 <= int(mode) <= 4 and mode == "4":
            print("До скорой встречи")
            break
        else:
            print("Упс что-то не то. Попробуйте заново и будте внимательно")
main()
