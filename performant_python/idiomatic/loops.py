def for_loop():
    input = range(100_000)
    output = []

    for i in input:
        if i % 2 == 0:
            output.append(i)

    return output


def list_comp():
    return [i for i in range(100_000) if i % 2 == 0]
