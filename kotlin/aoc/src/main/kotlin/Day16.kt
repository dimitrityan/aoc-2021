fun computeSum(packet: Packet): Long {
    var res = 0L
    if (packet.getPackets().isEmpty()) {
        return packet.getLiteralValue()
    } else {
        for (subPacket in packet.getPackets()) {
            res += subPacket.evaluate()
        }
    }
    return res
}

fun computeProduct(packet: Packet): Long {
    var res = 1L
    if (packet.getPackets().isEmpty()) {
        return res
    } else {
        for (subPacket in packet.getPackets()) {
            res *= subPacket.evaluate()
        }
    }
    return res
}

fun computeMin(packet: Packet): Long {
    var res = Long.MAX_VALUE
    for (subPacket in packet.getPackets()) {
        val subpacketValue = subPacket.evaluate()
        if (subpacketValue < res) {
            res = subpacketValue
        }
    }
    return res
}

fun computeMax(packet: Packet): Long {
    var res = Long.MIN_VALUE
    for (subPacket in packet.getPackets()) {
        val subpacketValue = subPacket.evaluate()
        if (subpacketValue > res) {
            res = subpacketValue
        }
    }
    return res
}

fun greaterThan(packet: Packet): Long {
    val firstPacket = packet.getPackets()[0].evaluate()
    val secondPacket = packet.getPackets()[1].evaluate()
    return if (firstPacket > secondPacket) 1
    else 0
}

fun lessThan(packet: Packet): Long {
    val firstPacket = packet.getPackets()[0].evaluate()
    val secondPacket = packet.getPackets()[1].evaluate()
    return if (firstPacket < secondPacket) 1
    else 0
}

fun equal(packet: Packet): Long {
    val firstPacket = packet.getPackets()[0].evaluate()
    val secondPacket = packet.getPackets()[1].evaluate()
    return if (firstPacket == secondPacket) 1
    else 0
}

class Packet(val version: Long, val type: Int) {
    val subpackets = ArrayList<Packet>()
    private var length = 0
    private var literalValue = 0L

    fun setLiteralValue(literalValue: Long) {
        this.literalValue = literalValue
    }

    fun getLiteralValue(): Long {
        return this.literalValue
    }

    fun setPacketLength(length: Long) {
        this.length = length.toInt()
    }

    fun getPacketLength(): Int {
        return this.length
    }

    fun addPacketToSubpackets(packet: Packet) {
        this.subpackets.add(packet)
    }

    fun getPackets(): ArrayList<Packet> {
        return this.subpackets
    }

    fun evaluate(): Long {
        when (type) {
            0 -> return computeSum(this)
            1 -> return computeProduct(this)
            2 -> return computeMin(this)
            3 -> return computeMax(this)
            4 -> return this.literalValue
            5 -> return greaterThan(this)
            6 -> return lessThan(this)
            7 -> return equal(this)
            else -> {
                print("No valid type found")
            }
        }
        return 0
    }
}

class Day16 {
    fun main() {
        fun parsePacket(binaryStr: String): Packet {
            val version = binaryStr.substring(0, 3).toLong(2)
            val type = binaryStr.substring(3, 6).toInt(2)
            // Maintain counter of current packet
            var parseCounter = 6
            val packet = Packet(version, type)

            if (type == 4) {
                // Parse literal value
                var prefix = binaryStr.substring(parseCounter, parseCounter + 1)
                parseCounter++
                var literalValueBinaryStr = ""
                while (true) {
                    val literalValueBinary = binaryStr.substring(parseCounter, parseCounter + 4)
                    parseCounter += 4
                    literalValueBinaryStr += literalValueBinary
                    if (prefix == "0") break
                    prefix = binaryStr.substring(parseCounter, parseCounter + 1)
                    parseCounter++
                }
                val literalVal = literalValueBinaryStr.toLong(2)
                packet.setLiteralValue(literalVal)
                packet.setPacketLength(parseCounter.toLong())
            } else {
                // Parse subpacket(s)
                val lengthTypeId = binaryStr.substring(parseCounter, parseCounter + 1)
                parseCounter++
                if (lengthTypeId == "0") {
                    // 15 bits total length of packet
                    val subpacketLength = binaryStr.substring(parseCounter, parseCounter + 15).toInt(2)
                    parseCounter += 15
                    packet.setPacketLength((parseCounter + subpacketLength).toLong())
                    var parsed = 0
                    while (parsed < subpacketLength) {
                        val subPacket = parsePacket(binaryStr.substring(parseCounter))
                        packet.addPacketToSubpackets(subPacket)
                        parsed += subPacket.getPacketLength()
                        parseCounter += subPacket.getPacketLength()
                    }
                } else if (lengthTypeId == "1") {
                    // 11 bits represent number of subpackets
                    val numSubpackets = binaryStr.substring(parseCounter, parseCounter + 11).toInt(2)
                    parseCounter += 11
                    var counter = 0
                    while (counter < numSubpackets) {
                        // Parse numSubPackets time
                        val subPacket = parsePacket(binaryStr.substring(parseCounter))
                        packet.addPacketToSubpackets(subPacket)
                        counter++
                        parseCounter += subPacket.getPacketLength()
                    }
                    packet.setPacketLength(parseCounter.toLong())
                }
            }
            return packet
        }

        fun computeVersionSum(rootPacket: Packet): Long {
            var sum = rootPacket.version
            if (rootPacket.getPackets().isNotEmpty()) {
                for (packet in rootPacket.getPackets()) {
                    sum += computeVersionSum(packet)
                }
            }
            return sum
        }

        var rootPacket: Packet? = null
        fun part1(input: List<String>): Long {
            var binaryStr = ""
            val inputStr = input[0]
            for (i in inputStr.indices) {
                binaryStr += inputStr[i].toString().toLong(radix = 16).toString(2).padStart(4, '0')
            }
            val packet = parsePacket(binaryStr)
            rootPacket = packet
            return computeVersionSum(packet)
        }

        fun part2(input: List<String>): Long {
            var binaryStr = ""
            val inputStr = input[0]
            for (i in inputStr.indices) {
                binaryStr += inputStr[i].toString().toLong(radix = 16).toString(2).padStart(4, '0')
            }
            val packet = parsePacket(binaryStr)
            return packet.evaluate()
        }

        val input = readInput("Day16")
        println(part1(input))
        println(part2(input))
    }
}

fun main() {
    Day16().main()
}