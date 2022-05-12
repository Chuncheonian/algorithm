# Deque (데크)

> *Double Ended Queue의 약자로, 양쪽 끝을 모두 추출할 수 있는 Queue*

<br>

## 특징

* 양쪽에서 삭제와 삽입을 모두 처리할 수 있으며, 스택과 큐의 특징을 모두 갖고 있습니다.


<br>

## 코드

### Swift
[전체 코드](./src/Deque.swift)

```swift
struct Deque<T: Equatable> {
    private var enqueueStack: [T]
    private var dequeueStack: [T] = []

    var count: Int {
        return enqueueStack.count + dequeueStack.count
    }

    var isEmpty: Bool {
        return enqueueStack.isEmpty && dequeueStack.isEmpty
    }

    var front: T? {
        return dequeueStack.isEmpty ? enqueueStack.first : dequeueStack.last
    }

    var back: T? {
        return enqueueStack.isEmpty ? dequeueStack.first : enqueueStack.last
    }

    init(_ queue: [T] = []) {
        self.enqueueStack = queue
    }

    mutating func enqueue(_ element: T) {
        enqueueStack.append(element)
    }

    mutating func enqueueFront(_ element: T) {
        dequeueStack.append(element)
    }

    mutating func dequeue() -> T? {
        if dequeueStack.isEmpty {
            dequeueStack = enqueueStack.reversed()
            enqueueStack.removeAll()
        }
        return dequeueStack.popLast()
    }

    mutating func dequeueBack() -> T? {
        var value: T?
        if enqueueStack.isEmpty {
            dequeueStack.reverse()
            value = dequeueStack.popLast()
            dequeueStack.reverse()
        } else {
            value = enqueueStack.popLast()
        }
        return value
    }   

    mutating func removeAll() {
        enqueueStack.removeAll()
        dequeueStack.removeAll()
    }

    mutating func firstIndex(of element: T) -> Int? {
        if dequeueStack.isEmpty {
            return enqueueStack.firstIndex(of: element)
        }
        
        dequeueStack.reverse()

        if let index = dequeueStack.firstIndex(of: element) {
            dequeueStack.reverse()
            return .some(index)
        } else {
            dequeueStack.reverse()
            return .some(dequeueStack.count + enqueueStack.firstIndex(of: element)!)
        }
    }
}
```