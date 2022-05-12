// Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

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