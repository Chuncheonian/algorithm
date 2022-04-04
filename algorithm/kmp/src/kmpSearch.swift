// Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

func kmpSearch(str s: [Character], pattern p: [Character]) -> [Int] {
    var result = [Int]()
    let failFunc = makeFailFunc(pattern: p)
    var j = 0  // j : 패턴 인덱스
    
    // i : 문자열 인덱스
    for i in 0..<s.count {

        // {문자가 서로 다름} && {j > 0} 이면, {j = F[j-1]}
        while j > 0, s[i] != p[j] {
            j = failFunc[j - 1]
        }
        
        // 문자가 서로 같으면
        if s[i] == p[j] {
            // 패턴 인덱스가 끝까지 갔으면 패턴 발견!
            if j == p.count - 1 {  
                result.append(i - p.count + 1)  // 문자열에서 패턴 시작 인덱스 저장
                j = failFunc[j]
            } else {  // 패턴 끝이 아니면, {i, j 둘 다 증가}
                j += 1
            }
        }

        // {문자가 서로 다름} && {j == 0} 이면, {i++}
    }
    return result
}

func makeFailFunc(pattern p: [Character]) -> [Int] {
    var failFunc = [Int](repeating: 0, count: p.count)  // F(0)은 항상 0이니까 0으로 초기화
    var j = 0  // j: 패턴 인덱스, 0부터 시작

    for i in 1..<p.count {  // i: F()값을 저장하기 위해 활용하는 인덱스, 1부터 끝까지

        // {j > 0} && {j != i} 이면, {j = F[j-1]}
        while j > 0, p[i] != p[j] {
            j = failFunc[j-1]
        }

        // {j == i}이면, {F[i] = j인덱스 + 1} && {i, j 둘 다 1 증가}
        if p[j] == p[i] {
            j += 1
            failFunc[i] = j
        }

        // {j == 0} && {j != i} 이면, {F[i] = 0} & {i += 1}
    }
    return failFunc
}

// Testcase
let text = "ABDABABCAB"
let pattern = "ABCAB"

print(kmpSearch(str: Array(text), pattern: Array(pattern)))  // > [5]