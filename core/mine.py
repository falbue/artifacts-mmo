from . import client, api


def mining():
    result = api.sync(name="oleg", client=client)
    print(result)

    if result is None:
        print("Непредвиденный пустой ответ")
    else:
        print(result)
