# Stack (스택)

> *목록의 끝에서만 접근할 수 있는 나열구조*

<br>

## 특징

* 스택은 나중에 넣은 데이터를 가장 먼저 빼는 Last In First Out (LIFO)의 특징을 가지는 자료구조이다.

* 이로 인해, 데이터를 임시 저장할 때 주로 사용된다.

* 꽉 찬 스택에 요소를 삽입하고자 할 때 스택에 요소가 넘쳐서 에러가 발생하는 것을 스택 버퍼 오버플로(Stack Buffer Overflow)라고 부른다.

<br>

## 코드

### Swift
[전체 코드](./src/Stack.swift)
```swift
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
```

---