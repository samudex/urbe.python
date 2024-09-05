# request(url='', method='post', data={})


def send_data(**kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(f'{key} -> {value}')


send_data(
    name='Ronald',
    lastname='Abu Saleh',
    age=26,
    position='Developer'
)
