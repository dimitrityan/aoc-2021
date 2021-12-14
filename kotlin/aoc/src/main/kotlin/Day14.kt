class Day14 {
    fun main() {
        fun solve(input: List<String>, steps: Long) : Long {
            val replacements = HashMap<String, String>()
            val occ = HashMap<String, Long>()
            val pairToOccurrences = HashMap<String, Long>()
            val template = input[0]
            for (i in 2 until input.size) {
                val lhs = input[i].split(" -> ")[0]
                val rhs = input[i].split(" -> ")[1]
                replacements[lhs] = rhs
            }

            for (c in template) {
                occ[c.toString()] = occ.getOrDefault(c.toString(), 0) + 1
            }
            for (i in 0 until template.length-1) {
                val pair = template.substring(i, i+2)
                pairToOccurrences[pair] = pairToOccurrences.getOrDefault(pair, 0) + 1
            }

            var least = Long.MAX_VALUE
            var most = Long.MIN_VALUE

            for (i in 0 until steps) {
                val toAdd = HashMap<String, Long>()
                val toRemove = HashSet<String>()
                for (pairKey in pairToOccurrences.keys) {
                    val numOccPair = pairToOccurrences[pairKey]!!
                    if (replacements.contains(pairKey)) {
                        val rep = replacements[pairKey].toString()
                        val pair1 = pairKey[0] + rep
                        val pair2 = rep + pairKey[1]
                        toAdd[pair1] = toAdd.getOrDefault(pair1, 0) + numOccPair
                        toAdd[pair2] = toAdd.getOrDefault(pair2, 0) + numOccPair
                        occ[rep] = occ.getOrDefault(rep, 0) + numOccPair
                        toRemove.add(pairKey)
                    }
                }
                for (k in toRemove) {
                    pairToOccurrences.remove(k)
                }
                for (k in toAdd.keys) {
                    pairToOccurrences[k] = pairToOccurrences.getOrDefault(k, 0) + toAdd[k]!!
                }
            }

            for (k in occ.keys) {
                if (occ[k]!! > most) {
                    most = occ[k]!!
                }
                if (occ[k]!! < least) {
                    least = occ[k]!!
                }
            }
            return most - least
        }

        fun part1(input: List<String>): Long {
            val start = System.currentTimeMillis()
            val sol = solve(input, 10)
            val end = System.currentTimeMillis()
            println("Time needed (ms): ${end-start}")
            return sol
        }

        fun part2(input: List<String>): Long {
            val start = System.currentTimeMillis()
            val sol = solve(input, 40)
            val end = System.currentTimeMillis()
            println("Time needed (ms): ${end-start}")
            return sol
        }

        val input = readInput("Day14")
        println("Solution part 1: ${part1(input)}")
        println("Solution part 2: ${part2(input)}")
    }
}

fun main() {
    val day14 = Day14()
    day14.main()
}