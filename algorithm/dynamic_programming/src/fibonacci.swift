// Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

// 1. fibonacci - bruteforce
func fibonacciBruteforce(_ n: Int) -> Int {
  n < 2 ? n : fibonacciBruteforce(n - 1) + fibonacciBruteforce(n - 2)
}

// 2. fibonacci - tabulation : Bottom-Up
func fibonacciTabulation(_ n: Int) -> Int {
  var dp: [Int] = [0, 1]

  guard n > 1 else {
    return n
  }

  for i in 2...n {
    dp.append(dp[i - 1] + dp[i - 2])
  }

  return dp[n]
}


// 3. fibonacci - memoization : Top-Down
var dp = [Int: Int]()

func fibonacciMemoization(_ n: Int) -> Int {
  if let v = dp[n] {
    return v
  }

  let newValue = n < 2 ? n : fibonacciMemoization(n - 1) + fibonacciMemoization(n - 2)
  dp[n] = newValue
  return newValue
}


// Testcase
print(fibonacciBruteforce(10))
print(fibonacciTabulation(10))
print(fibonacciMemoization(10))