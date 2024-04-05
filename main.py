### Менеджер задач
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                break

    def show_current_tasks(self):
        for task in self.tasks:
            if not task.is_completed:
                print(f"Task: {task.description}, Due: {task.due_date}")

### Класс Store

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

store_1 = Store("ГлавРыба", "12 пл.Победы")
store_1.add_item("яйца", 0.5)
store_1.add_item("бананы", 0.75)

store_2 = Store("ТехноБаза", "45 Аллея Смелых")
store_2.add_item("кабель юэсби", 5.99)
store_2.add_item("Пауэрбанк", 24.99)

store_3 = Store("Читальня", "777 Переулок грустного философа")
store_3.add_item("Улитка на склоне", 29.99)
store_3.add_item("Желтая стрела", 19.99)
