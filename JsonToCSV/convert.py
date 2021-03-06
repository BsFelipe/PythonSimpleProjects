import json

if __name__ == '__main__':
    try:
        with open('test.json', 'r') as f:
            data = json.loads(f.read())

        # TODO convert dynamic fields
        output = ';'.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]};{obj["age"]};{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)

    except Exception as ex:
        print(f'Error: {str(ex)}')
