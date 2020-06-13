import random


def full_graph_generator(output_file_path, n):
    with open(output_file_path, "w") as file:
        file.write(     
            str(n) + "\n"
        )
        for i in range(n):
            for j in range(n):
                if i < j:
                    file.write(
                        str(i+1) + " " +
                        str(j+1) + " " +
                        str(random.random()) + "\n"
                    )


def main():
    output_file_path = input("file_path:")
    n = int(input("n:"))
    full_graph_generator(output_file_path, n)


if __name__ == '__main__':
    main()
    