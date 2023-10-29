
def main():
    n, k = map(int, input().split())  # Read n and k from input
    checks = list(map(int, input().split()))  # Read the list of check values

    # Sort the checks in descending order
    checks.sort(reverse=True)

    # Select the top k checks and calculate the maximum total value
    max_total_value = sum(checks[:k])

    # Print the maximum total value
    print(max_total_value)

if __name__ == '__main__':
    main()