import libs.examples.example_module


def main():
    input = [1, 2]
    output = libs.examples.example_module.get_sum_of_numbers([1, 2])

    print(input, "->", output)


if __name__ == "__main__":
    main()
