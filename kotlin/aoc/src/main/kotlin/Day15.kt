import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.HashMap

class Graph {
    class Node(val id: String) {
        var cost: Long = 0

        override fun equals(other: Any?): Boolean {
            return (((other is Node) && (this.id == other.id)))
        }

        override fun hashCode(): Int {
            return id.hashCode()
        }

        override fun toString(): String {
            return id
        }

        constructor(id: String, cost: Long) : this(id) {
            this.cost = cost
        }

    }

    val adjacencyList = HashMap<Node, ArrayList<Node>>()
    val matrix = HashMap<Pair<Node, Node>, Long>()
    val nodes = HashMap<String, Node>()

    fun addEdge(from: Node, to: Node, dist: Long) {
        adjacencyList.putIfAbsent(from, ArrayList())
        if (!adjacencyList[from]?.contains(to)!!) {
            adjacencyList[from]?.add(to)
        }
        matrix.putIfAbsent(Pair(from, to), dist)
    }

    fun addNode(node: Node): Node {
        adjacencyList.putIfAbsent(node, ArrayList())
        return node
    }
}

class Day15 {
    fun main() {
        fun dijkstra(graph: Graph, src: Graph.Node, dest: Graph.Node): Long {
            val dist = HashMap<Graph.Node, Long>()
            val prev = HashMap<Graph.Node, Graph.Node?>()
            for (node in graph.adjacencyList.keys) {
                dist[node] = Long.MAX_VALUE
                prev[node] = null
            }
            dist[src] = 0
            val priorityQueue = PriorityQueue<Pair<Graph.Node, Long>> { a, b ->
                a.second.compareTo(b.second)
            };
            for (node in graph.adjacencyList.keys) {
                priorityQueue.add(Pair(node, dist[node]!!))
            }
            while (!priorityQueue.isEmpty()) {
                val v = priorityQueue.remove()
                if (v.first == dest) {
                    break
                }
                for (neighbor: Graph.Node in graph.adjacencyList[v.first]!!) {
                    if ((dist[v.first]!! + graph.matrix[Pair(v.first, neighbor)]!!) < dist[neighbor]!!) {
                        dist[neighbor] = dist[v.first]!! + graph.matrix[Pair(v.first, neighbor)]!!
                        priorityQueue.add(Pair(Graph.Node(neighbor.id), dist[neighbor]!!))
                        prev[neighbor] = v.first
                    }

                }
            }
            return dist[dest]!!
        }

        fun part1(input: List<String>): Long {
            val g = Graph()
            val startNode = g.addNode(Graph.Node("start"))
            val destNode = "${input.size-1},${input[0].length-1}"
            for (r in input.indices) {
                for (c in input[r].indices) {
                    if (c < input[r].length - 1) {
                        g.addEdge(Graph.Node("$r,$c"), Graph.Node("$r,${c+1}"), input[r][c+1].toString().toLong())
                    }
                    if (r < input.size - 1) {
                        g.addEdge(Graph.Node("$r,$c"), Graph.Node("${r+1},$c"), input[r+1][c].toString().toLong())
                    }
                    if (c > 0) {
                        g.addEdge(Graph.Node("$r,$c"), Graph.Node("$r,${c-1}"), input[r][c-1].toString().toLong())
                    }
                    if (r > 0) {
                        g.addEdge(Graph.Node("$r,$c"), Graph.Node("${r-1},$c"), input[r-1][c].toString().toLong())
                    }
                }
            }
            g.addEdge(startNode, Graph.Node("0,0"), 0)
            return dijkstra(graph = g, startNode, Graph.Node(destNode))
        }

        fun part2(input: List<String>): Long {
            val g = Graph()
            val startNode = g.addNode(Graph.Node("start"))
            val destNode = Graph.Node("${input.size * 5 - 1},${input[0].length * 5 - 1}")
            val offset = input.size
            for (i in 0 until 5) {
                for (r in input.indices) {
                    for (j in 0 until 5) {
                        for (c in input[r].indices) {
                            val y = offset*i + r
                            val x = offset*j + c
                            val distance = (input[r][c].toString().toLong() + i + j - 1) % 9 + 1
                            g.nodes.putIfAbsent("$y,$x", Graph.Node("$y,$x", distance))
                        }

                    }
                }
            }
            for (i in 0 until input.size*5) {
                for (j in 0 until input.size*5) {
                    val id = "${i},${j}"
                    if (g.nodes.containsKey(id)) {
                        val srcNode = g.nodes[id]
                        if (j < input.size * 5) {
                            if (g.nodes.containsKey("$i,${j+1}")) {
                                val dstNode = g.nodes["$i,${j+1}"]
                                if (dstNode != null) {
                                    g.addEdge(srcNode!!, dstNode, dstNode.cost)
                                }
                            }
                        }
                        if (i < input.size * 5) {
                            if (g.nodes.containsKey("${i+1},$j")) {
                                val dstNode = g.nodes["${i+1},$j"]
                                if (dstNode != null) {
                                    g.addEdge(srcNode!!, dstNode, dstNode.cost)
                                }
                            }
                        }
                        if (j > 0) {
                            if (g.nodes.containsKey("$i,${j-1}")) {
                                val dstNode = g.nodes["$i,${j-1}"]
                                if (dstNode != null) {
                                    g.addEdge(srcNode!!, dstNode, dstNode.cost)
                                }
                            }
                        }
                        if (i > 0) {
                            if (g.nodes.containsKey("${i-1},$j")) {
                                val dstNode = g.nodes["${i-1},$j"]
                                if (dstNode != null) {
                                    g.addEdge(srcNode!!, dstNode, dstNode.cost)
                                }
                            }
                        }
                    }
                }
            }
            g.addEdge(startNode, Graph.Node("0,0"), 0)
            return dijkstra(graph = g, startNode, destNode)
        }

        val input = readInput("Day15")
        println(part1(input))
        println(part2(input))
    }
}

fun main() {
    Day15().main()
}