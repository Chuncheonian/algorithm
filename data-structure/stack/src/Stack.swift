// Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

struct Stack<T> {

    private var array = [T]()

    var count: Int {
        return array.count
    }

    var isEmpty: Bool {
        return array.isEmpty
    }

    // Push Time Complexity: O(1)
    mutating func push(_ elem: T) {
        array.append(elem)
    }

    // Pop Time Complexity: O(1)
    mutating func pop() -> T? {
        return array.popLast()
    }

    var top: T? {
        return array.last
    }
}

// ExpressibleByArrayLiteral
// 배열 리터럴을 통해 초기화 가능하게 해주는 Protocol
// Array Literal: [1, 2, 3], ["a", "b", "c"], ...
extension Stack: ExpressibleByArrayLiteral {
    init(arrayLiteral elements: T...) {
        self.init()
        for element in elements {
            self.array.append(element)
        }
    }
}

// Sequence
// 개개의 원소들을 순서대로 하나씩 순회할 수 있도록 해주는 Protocol
extension Stack: Sequence {
    func makeIterator() -> AnyIterator<T> {
        var curr = self
        return AnyIterator {
            return curr.pop()  // First Out
        }
    }
}

// CustomStringConvertible
// Instance를 String으로 변환할 때, 커스텀할 수 있도록 도와주는 Protocol
extension Stack: CustomStringConvertible, CustomDebugStringConvertible{
    // print()
    var description: String {
        return "Stack Description: " + self.array.description
    }
  
    // debugPrint()
    var debugDescription: String {
        return "Stack DebugDescription " + self.array.debugDescription
    }
}


// Testcase

// ExpressibleByArrayLiteral
var myStack: Stack<Int> = [1, 2, 3]

// push
myStack.push(4)
myStack.push(5)

// top
print(myStack.top!)  // > 5

// pop
print(myStack.pop()!)  // > 5

// count
print(myStack.count)  // > 4

// CustomStringConvertible
print(myStack)// > Stack Description: [1, 2, 3, 4]

// CustomDebugStringConvertible
debugPrint(myStack)  // > Stack DebugDescription [1, 2, 3, 4]

// isEmpty
print(myStack.isEmpty)  // > false

// Sequence
myStack.forEach { print($0, terminator: " ") }  // > 4, 3, 2, 1
