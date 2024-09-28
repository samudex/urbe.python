import csv

def app():
    data: list[dict] = read_csv('./data.csv')
    female = 0
    male = 0

    for value in data:
        if value['gender'] == 'female':
            female += 1
        else:
            male += 1

    print(f"Female: {female}\nMale: {male}")

def read_csv(path: str):
        with open(path, 'r') as file:
        #print(file.read())

        reader = csv.reader(file)
        #print(reader)
        return list

        headers = next(reader)

        print(headers)

        a = [1, 2]
        b = [3, 4]

        print(dict(zip(a,b)))



if __name__ == '__main__':
    app()