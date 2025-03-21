def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salaries.append(int(salary))
                except Exception as e:
                    print('Error read line', e)

        if not salaries:
            return (0, 0)
        
        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)
    
    except FileNotFoundError:
        print("File not found")
        return (0, 0)
    except Exception as e:
        print('Error to open file:', e)
        return (0, 0)

total, average = total_salary('workers.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")