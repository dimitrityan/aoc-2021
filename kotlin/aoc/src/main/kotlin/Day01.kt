class Day01 {
    fun main() {
        fun part1(input: List<String>): Int {
            var prev = input[0].toInt()
            var depth: Int?
            var counter = 0
            for (i in 1 until input.size) {
                depth = input[i].toInt()
                if (depth > prev) {
                    counter++
                }
                prev = depth
            }
            return counter
        }

        fun part2(input: List<String>): Int {
            var prevSum = 0
            var counter = 0
            var currentSum = 0
            for (i in input.indices) {
                if (i + 3 > input.size) break
                currentSum = input[i].toInt() + input[i+1].toInt() + input[i+2].toInt()
                if (i == 0) {
                    prevSum = currentSum
                    continue
                }
                if (currentSum > prevSum) {
                    counter++
                }
                prevSum = currentSum
            }
            return counter
        }

        val input = readInput("Day01")
        println(part1(input))
        println(part2(input))
    }
}

fun main() {
    val day01 = Day01()
    day01.main()
}