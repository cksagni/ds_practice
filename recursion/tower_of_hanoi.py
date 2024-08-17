

def tower_of_hanoi(n, source, destination, helper):
    if n == 1:
        print(f"Move disk 1 from rod: {source} to rod: {destination}")
        return
    tower_of_hanoi(n-1, source, helper, destination)
    print(f"Move disk {n} from rod: {source} to rod: {destination}")
    tower_of_hanoi(n-1, helper, destination, source)


if __name__ == "__main__":
    tower_of_hanoi(3, 'A', 'C', 'B')
    print("---------------------------------------------------")

