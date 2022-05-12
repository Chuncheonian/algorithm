// Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

import Foundation

struct PriorityQueue<T: Comparable> {
    var heap: Heap<T>

    init(elements: [T] = [], priorityFunction: @escaping (T, T) -> Bool) {
        self.heap = Heap<T>(elements: elements, priorityFunction: priorityFunction)
    }

    var count: Int {
        return heap.count
    }

    var isEmpty: Bool {
        return heap.isEmpty
    }

    var peek: T? {
        return heap.peek
    }

    mutating func enqueue(_ element: T) {
        heap.insert(element)
    }

    mutating func dequeue() -> T? {
        return heap.remove()
    }

    mutating func clear() {
        while heap.isEmpty == false {
            _ = heap.remove()
        }
    }
}

struct Heap<T: Comparable> {
    
    private var elements: [T] = []

    /// > : Max Heap
    /// < : Min Heap
    private let priorityFunction: (T, T) -> Bool
    
    var isEmpty: Bool {
        return elements.isEmpty
    }

    var count: Int {
        return elements.count
    }

    var peek: T? {
        return elements.first
    }
    
    init(elements: [T] = [], priorityFunction: @escaping (T, T) -> Bool) {
        self.elements = elements
        self.priorityFunction = priorityFunction
        
        if isEmpty == false {
            buildHeap()
        }
    }
    
    func leftChildIndex(of index: Int) -> Int {
        return 2 * index + 1
    }

    func rightChildIndex(of index: Int) -> Int {
        return 2 * index + 2
    }

    func parentIndex(of index: Int) -> Int {
        return (index - 1) / 2
    }

    /// 새로운 데이터를 Heap의 마지막 데이터에 삽입후, 부모 데이터들과 교환
    mutating func insert(_ node: T) {
        elements.append(node)               // O(1)
        swimUp(from: elements.endIndex - 1) // O(logN)
    }

    mutating func swimUp(from index: Int) {
        var index = index

        while index > 0, priorityFunction(elements[index], elements[parentIndex(of: index)]) {
            elements.swapAt(index, parentIndex(of: index))
            index = parentIndex(of: index)
        }
    }

    mutating func remove() -> T? {
        if elements.isEmpty { return nil }
        
        elements.swapAt(0, elements.endIndex - 1)  // 루트노드와 마지막노드와 Swap
        let deleted = elements.removeLast()
        diveDown(from: 0)
        
        return deleted
    }

    mutating func diveDown(from index: Int) {
        var higherPriority: Int = index
        let leftChildIndex: Int = leftChildIndex(of: index)
        let rightChildIndex: Int = rightChildIndex(of: index)
        
        // 왼쪽 자식 노드가 더 우선순위가 높을 때
        if leftChildIndex < elements.endIndex, priorityFunction(elements[leftChildIndex], elements[higherPriority]) {
            higherPriority = leftChildIndex
        }

        // 오른쪽 자식 노드가 더 우선순위가 높을 때
        if rightChildIndex < elements.endIndex, priorityFunction(elements[rightChildIndex], elements[higherPriority]) {
            higherPriority = rightChildIndex
        }
        
        // 교환이 필요 없는 경우
        if higherPriority == index { return }
        
        // 교환 후 서브트리로 이동
        elements.swapAt(higherPriority, index)
        diveDown(from: higherPriority)
    }
    
    mutating func buildHeap() {
        for index in stride(from: count / 2, through: 0, by: -1) {
            diveDown(from: index)
        }
    }
}

//  Testcase
var priorityQueue: PriorityQueue<Int> = .init(priorityFunction: >)

priorityQueue.enqueue(5)
priorityQueue.enqueue(6)
print(priorityQueue)
priorityQueue.enqueue(2)
print(priorityQueue)
print(priorityQueue.peek!)
print(priorityQueue.dequeue()!)
print(priorityQueue.dequeue()!)
print(priorityQueue.dequeue()!)