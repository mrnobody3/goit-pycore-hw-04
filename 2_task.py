def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(",")
                    cats_list.append({"id": cat_id, "name": name, "age": age})
                except Exception as e:
                    print('Error read line', e)
        
        return cats_list
    
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print('Error to open file:', e)
        return []

cats_info = get_cats_info('cats.txt')
print(cats_info)