from collections import ChainMap

# ChainMap - это класс из модуля collections,
# который позволяет объединить несколько словарей в один.
# Он принимает несколько словарей в качестве аргументов
# и возвращает объект, который ведет себя
# как единый словарь.
# При обращении к ключу, ChainMap будет
# искать его сначала в первом словаре,
# затем во втором и так далее,
# пока не найдет его или не достигнет
# конца списка словарей.
# Это полезно для создания иерархий
# конфигураций или для объединения нескольких источников данных.


def main():
    tested_dict_one = {"yjewo": 100, "hf": 94, "fr": 76, "byj": 7, "gu": 92}
    tested_dict_two = {"ponkt": 20, "ua": 39, "op": 47, "ib": 26, "bfrhw": 45}
    tested_dict_three = {"op": 11, "la": 44, "zt": 4, "nz": 17, "aokhk": 39}
    s = ChainMap(tested_dict_one, tested_dict_two, tested_dict_three)
    print(s["yjewo"], s["ponkt"], s["op"])  # 100, 20, 11
    assert s["op"] == 47  # 47, так как он находится в tested_dict_two,
    # который идет перед tested_dict_three


if __name__ == "__main__":
    main()
