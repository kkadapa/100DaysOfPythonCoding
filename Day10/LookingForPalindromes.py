MOD = 10**9 + 7

def count_palindromios(n):
    # Initialize a 2D array to store the counts
    dp = [[0] * 10 for _ in range(n + 1)]

    # There is 1 way to form palindromio of length 1 for each digit
    for digit in range(10):
        dp[1][digit] = 1

    # Calculate counts for palindromios of length 2 and above
    for length in range(2, n + 1):
        for first_digit in range(10):
            for second_digit in range(10):
                if abs(first_digit - second_digit) == 1:
                    dp[length][first_digit] = (dp[length][first_digit] + dp[length - 1][second_digit]) % MOD

    # Sum all the counts for palindromios of length n
    total_count = sum(dp[n]) % MOD

    return total_count

def main():
    t = int(input())  # Number of questions

    for _ in range(t):
        n = int(input())  # Length of the "palindromio"
        result = count_palindromios(n)
        print(result)

if __name__ == '__main__':
    main()
