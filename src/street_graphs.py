def odd_4():
    x = 1.415
    y = 0
    graph = {"A": {"2": 4.063 + 0.5 * x},
             "2": {"A": 4.063 + 0.5 * x, "4": 2 * x},
             "4": {str(4 - 2): 2 * x, str(4 + 2): 2 * x},
             "6": {str(6 - 2): 2 * x, str(6 + 2): 1.5 * x},
             "8": {str(8 - 2): 1.5 * x, str(8 + 2): x}}

    for y in range(10, 28, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 28
    graph.update({str(y): {str(y - 2): x, str(y + 2): x}})  # 28

    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(y + 2): 3.472}})  # 30

    y = y + 2  # 32
    graph.update({str(32): {str(y - 2): 3.472, str(y + 2): x}})  # 32

    for y in range(34, 60, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 60
    graph.update({str(y): {str(y - 2): x, "B": 0.598}})  # 60

    graph.update({"B": {str(60): 0.598, str(62): 0.818}})

    y = y + 2  # 62
    graph.update({str(y): {"B": 0.818, str(64): 3.605}})  # 62

    y = y + 2  # 64
    graph.update({str(y): {str(62): 3.605, str(66): x}})  # 64

    for y in range(66, 88, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 88
    graph.update({str(y): {str(y - 2): x, "C": 3.282}})  # 88

    graph.update({"C": {str(88): 3.282, str(96): 2.392}})

    y = 96
    graph.update({str(y): {"C": 2.392, str(y + 2): x}})  # 96

    for y in range(98, 124, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2
    graph.update({str(124): {str(y - 2): x, "D": 2.229}})

    graph.update({"D": {str(124): 2.229}})

    return graph

def even_4():
    x = 1.347
    y = 0
    graph = {"A": {"1": 4.553},
             "1": {"A": 4.553, "3": x}}

    for y in range(3, 19, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 19
    graph.update({str(y): {str(y - 2): x, str(y + 2): 5 * x}})  # 19

    y = y + 2  # 21
    graph.update({str(y): {str(y - 2): 5 * x, str(y + 2): x}})  # 21

    for y in range(23, 61, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 61
    graph.update({str(y): {str(y - 2): x, "B": 3.084}})  # 61

    graph.update({"B": {str(61): 3.084, str(63): 3.32}})  # 61

    y = y + 2  # 63
    graph.update({str(y): {"B": 3.32, str(y + 2): x}})  # 63

    for y in range(65, 91, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 91
    graph.update({str(y): {str(y - 2): x, "C": 2.521}})  # 91

    graph.update({"C": {str(91): 2.521, str(93): 3.819}})

    y = y + 2  # 93
    graph.update({str(y): {"C": 3.819, str(y + 2): x}})  # 93

    for y in range(95, 119, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 119
    graph.update({str(119): {str(y - 2): x, "D": 3.141}})

    graph.update({"D": {str(119): 3.141}})

    return graph

def odd_5():
    x = 1.347
    y = 0

    graph = {"E": {"2": 4.553},
             "2": {"E": 4.553, "4": x}}

    for y in range(4, 20, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 20
    graph.update({str(y): {str(y - 2): x, str(y + 2): 5 * x}})

    y = y + 2  # 22
    graph.update({str(y): {str(y - 2): 5 * x, str(y + 2): x}})  # 22

    for y in range(24, 62, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 62
    graph.update({str(62): {str(y - 2): x, "F": 3.084}})

    graph.update({"F": {str(62): 3.084, str(64): 3.323}})

    y = y + 2  # 64
    graph.update({str(y): {"F": 3.323, str(y + 2): x}})  # 64

    for y in range(66, 92, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 92
    graph.update({str(y): {str(y - 2): x, "G": 2.472}})

    graph.update({"G": {str(92): 2.472}})

    return graph

def even_5():
    x = 1.347
    y = 0

    graph = {"E": {"1": 4.553},
             "1": {"E": 4.553, "3": 2 * x},
             "3": {"1": 2 * x, "5": x}}

    for y in range(5, 9, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 9
    graph.update({str(y): {str(y - 2): x, str(y + 2): 2 * x}})  # 9

    y = y + 2  # 11
    graph.update({str(y): {str(y - 2): 2 * x, str(y + 2): x}})  # 11

    for y in range(13, 17, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 17
    graph.update({str(y): {str(y - 2): x, str(y + 2): 2 * x}})  # 17

    y = y + 2  # 19
    graph.update({str(y): {str(y - 2): 2 * x, str(25): 4 * x}})

    y = 25
    graph.update({str(y): {str(19): 4 * x, str(y + 2): x}})  # 25

    for y in range(27, 61, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 61
    graph.update({str(y): {str(y - 2): x, "F": 3.084}})  # 61

    graph.update({"F": {str(61): 3.084, str(63): 3.32}})

    y = y + 2  # 63
    graph.update({str(y): {"F": 3.32, str(y + 2): x}})  # 63

    for y in range(65, 91, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 91
    graph.update({str(91): {str(y - 2): x, "G": 2.473}})

    graph.update({"G": {str(91): 2.473}})

    return graph

def odd_6():
    x = 1.347
    y = 0

    graph = {"H": {"2": 4.553},
             "2": {"H": 4.553, "4": x}}

    for y in range(4, 22, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ############################# segmented positions #############################
    y = y + 2  # 22
    graph.update({str(y): {str(y - 2): x, str(24): (4 / 5) * x}})  # 22

    y = y + 2  # 24
    graph.update({str(y): {str(y - 2): (4 / 5) * x, "24A": (4 / 5) * x}})  # 24

    graph.update({"24A": {str(24): (4 / 5) * x, "24B": (4 / 5) * x}})
    graph.update({"24B": {"24A": (4 / 5) * x, "24C": (4 / 5) * x}})
    graph.update({"24C": {"24B": (4 / 5) * x, "26": 3 * (4 / 5) * x}})

    graph.update({"26": {"24C": 3 * (4 / 5) * x, "28": x}})
    #############################################################################

    for y in range(28, 62, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 62
    graph.update({str(y): {str(y - 2): x, "I": 3.084}})  # 62

    graph.update({"I": {str(62): 3.084, str(64): 3.32}})

    y = y + 2  # 64
    graph.update({str(y): {"I": 3.32, str(y + 2): x}})  # 64

    for y in range(66, 92, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 92
    graph.update({str(y): {str(y - 2): x, "J": 2.472}})  # 92

    graph.update({"J": {str(92): 2.472, str(98): 3.819}})

    y = 98
    graph.update({str(y): {"J": 3.819, str(y + 2): x}})  # 98

    for y in range(100, 124, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 124
    graph.update({str(y): {str(y - 2): x, "K": 3.141}})

    graph.update({"K": {str(124): 3.141}})

    return graph


def even_6():
    x = 1.382
    x2 = 1.347
    y = 0
    graph = {"H": {"1": 4.522},
             "1": {"H": 4.522, "3": x}}

    for y in range(3, 23, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ############################# segmented positions #############################
    y = y + 2  # 23
    graph.update({str(y): {str(y - 2): x, "25": 0.5 * x}})  # 23

    y = y + 2  # 25
    graph.update({str(y): {str(y - 2): 0.5 * x, "25A": 0.5 * x}})
    graph.update({"25A": {"25": 0.5 * x, "25B": 0.5 * x}})
    graph.update({"25B": {"25A": 0.5 * x, "27": 0.5 * x}})

    graph.update({"27": {"25B": 0.5 * x, "29": x}})
    #############################################################################

    for y in range(29, 67, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 67
    graph.update({str(y): {str(y - 2): x, "I": 3.29}})  # 67

    graph.update({"I": {str(67): 3.29, str(69): 3.29}})

    y = y + 2  # 69
    graph.update({str(y): {"I": 3.29, str(y + 2): x}})  # 69

    for y in range(71, 97, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 97
    graph.update({str(97): {str(y - 2): x, "J": 2.006}})

    graph.update({"J": {str(97): 2.006, str(99): 3.819}})

    y = y + 2  # 99
    graph.update({str(99): {"J": 3.819, str(y + 2): x2}})  # 99

    for y in range(101, 105, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 105
    graph.update({str(y): {str(y - 2): x2, str(y + 2): 2 * x2}})  # 105

    y = y + 2  # 107
    graph.update({str(y): {str(y - 2): 2 * x2, str(y + 2): x2}})  # 107

    for y in range(109, 123, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 123
    graph.update({str(y): {str(y - 2): x2, "K": 3.141}})  # 123

    graph.update({"K": {str(123): 3.141}})

    return graph

def even_7():
    x1 = 1.226
    x2 = 1.347
    y = 0

    graph = {"L": {"1": 9.397},
             "1": {"L": x1, "3": x1},
             "3": {"1": x1, "5": x1},
             "5": {"3": x1, "7": x1},
             "7": {"5": x1, "9": x1},
             "9": {"7": x1, "11": x1},
             "11": {"9": x1, "13": 1.286},
             "13": {"11": 1.286, "15": x2}}

    y = 15
    graph.update({str(y): {str(y - 2): x2, str(y + 2): 1.517}})  # 15

    y = y + 2  # 17
    graph.update({str(y): {str(y - 2): 1.517, str(y + 2): 3.033}})  # 17

    y = y + 2  # 19
    graph.update({str(y): {str(y - 2): 3.033, str(y + 2): x2}})  # 19

    y = y + 2  # 21
    graph.update({str(y): {str(y - 2): x2, str(y + 2): 1.723}})  # 21

    y = y + 2  # 23
    graph.update({str(y): {str(y - 2): 1.723, str(y + 2): 3.025}})  # 23

    y = y + 2  # 25
    graph.update({str(y): {str(y - 2): 3.025, str(y + 2): x2}})  # 25

    for y in range(27, 55, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 55
    graph.update({str(y): {str(y - 2): x2, "M": 4.418}})  # 55

    graph.update({"M": {str(55): 4.418, str(57): 6.013}})

    y = y + 2  # 57
    graph.update({str(y): {"M": 6.013, str(y + 2): x2}})  # 57

    for y in range(59, 63, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 63
    graph.update({str(y): {str(y - 2): x2, str(y + 2): 2 * x2}})  # 63

    y = y + 2  # 65
    graph.update({str(y): {str(y - 2): 2 * x2, str(y + 2): x2}})  # 65

    for y in range(67, 75, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 75
    graph.update({str(y): {str(y - 2): x2, "N": 5.166}})  # 75

    graph.update({"N": {str(75): 5.166}})

    return graph

def odd_8():
    x1 = 1.226
    x2 = 1.347
    y = 0
    graph = {"O": {"2": 4.489},
             "2": {"O": 4.489, "4": x1}}

    for y in range(4, 20, 2):
        graph.update({str(y): {str(y - 2): x1, str(y + 2): x1}})

    y = y + 2  # 20
    graph.update({str(y): {str(y - 2): x1, str(y + 2): 1.289}})  # 20

    y = y + 2  # 22
    graph.update({str(y): {str(y - 2): 1.289, str(y + 2): x2}})  # 22

    y = y + 2  # 24
    graph.update({str(y): {str(y - 2): x2, str(y + 2): 1.517}})  # 24

    y = y + 2  # 26
    graph.update({str(y): {str(y - 2): 1.517, str(y + 2): 1.517}})  # 26

    ########################## out of sequence ##########################
    y = y + 2  # 28
    graph.update({str(y): {str(y - 2): 1.517, str(34): 4.587}})  # 28

    y = 34
    graph.update({str(y): {str(28): 4.587, str(y + 2): x2}})  # 34
    ###############################################################################

    y = y + 2  # 36
    graph.update({str(y): {str(y - 2): x2, str(y + 2): 1.679}})  # 36

    y = y + 2  # 38
    graph.update({str(y): {str(y - 2): 1.679, str(y + 2): x2}})  # 38

    for y in range(40, 68, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 68
    ########################## out of sequence ##########################
    graph.update({str(y): {str(y - 2): x2, "P": 4.418}})  # 68

    graph.update({"P": {str(68): 4.418, str(74): 4.667}})

    y = 74
    graph.update({str(y): {"P": 4.667, str(y + 2): x2}})  # 74
    ###############################################################################

    for y in range(76, 100, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 100
    graph.update({str(100): {str(y - 2): x2, "Q": 2.472}})

    graph.update({"Q": {str(100): 2.472}})

    return graph

def even_8():
    x = 1.382
    y = 0
    graph = {"O": {"1": 4.522},
             "1": {"O": 4.522, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(37): 4.43}})  # 29

    y = 37
    graph.update({str(y): {str(29): 4.43, str(y + 2): x}})  # 37
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, "P": 1.624}})  # 71

    graph.update({"P": {str(71): 1.624, str(79): 2.805}})

    y = 79
    graph.update({str(y): {"P": 2.805, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "Q": 2.49}})

    graph.update({"Q": {str(107): 2.49}})

    return graph

def odd_9():
    x = 1.382
    y = 0
    graph = {"S": {"2": 4.523},
             "2": {"S": 4.523, "4": x}}

    for y in range(4, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(36): 2.966}})  # 30

    y = 36
    graph.update({str(y): {str(30): 2.966, str(y + 2): 1.459}})  # 36
    ###############################################################################

    y = 38
    graph.update({str(y): {str(36): 1.459, str(y + 2): x}})  # 38

    for y in range(40, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(y + 2): 1.459}})  # 74

    ########################## out of sequence ##########################

    y = y + 2  # 74
    graph.update({str(y): {str(y - 2): 1.459, str(80): 2.971}})  # 74

    y = 80
    graph.update({str(y): {str(74): 2.971, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "T": 2.491}})

    graph.update({"T": {str(108): 2.491}})

    return graph

def even_9():
    x = 1.382
    y = 0
    graph = {"S": {"1": 4.522},
             "1": {"S": 4.522, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(37): 4.43}})  # 29

    y = 37
    graph.update({str(y): {str(29): 4.43, str(y + 2): x}})  # 35
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, str(79): 4.43}})  # 71

    y = 79
    graph.update({str(y): {str(71): 4.43, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "T": 2.49}})

    graph.update({"T": {str(107): 2.49}})

    return graph

def odd_10():
    x = 1.382
    y = 0    
    graph = {"U": {"2": 4.522},
             "2": {"U": 4.522, "4": x}}

    for y in range(4, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(36): 2.971}})  # 30

    y = 36
    graph.update({str(y): {str(30): 2.971, str(y + 2): 1.459}})  # 36

    y = y + 2  # 38
    graph.update({str(y): {str(36): 1.459, str(y + 2): x}})  # 38
    ###############################################################################

    for y in range(40, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(80): 4.43}})  # 72

    y = 80
    graph.update({str(y): {str(72): 4.43, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "V": 2.49}})

    graph.update({"V": {str(108): 2.49}})

    return graph

def even_10():
    x = 1.382
    y = 0
    graph = {"U": {"1": 4.526},
             "1": {"U": 4.526, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(37): 4.43}})  # 29

    y = 37
    graph.update({str(y): {str(29): 4.43, str(y + 2): x}})  # 35
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, str(79): 4.43}})  # 71

    y = 79
    graph.update({str(y): {str(71): 4.43, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "V": 2.49}})

    graph.update({"V": {str(107): 2.49}})

    return graph

def odd_11():
    x = 1.375
    y = 0
    graph = {"W": {"2": 4.522},
             "2": {"W": 4.522, "4": x}}

    for y in range(4, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(36): 2.971}})  # 30

    y = 36
    graph.update({str(y): {str(30): 2.971, str(y + 2): 1.459}})  # 36

    y = 38
    graph.update({str(y): {str(36): 1.459, str(y + 2): x}})  # 38
    ###############################################################################

    for y in range(38, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(74): 1.459}})  # 72

    y = y + 2  # 74
    graph.update({str(y): {str(72): 1.459, str(80): 2.971}})  # 74

    y = 80
    graph.update({str(y): {str(74): 2.971, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "X": 2.485}})

    graph.update({"X": {str(108): 2.485}})

    return graph

def even_11():
    x = 1.382
    y = 0
    graph = {"W": {"1": 4.522},
             "1": {"W": 4.522, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(35): 2.971}})  # 29

    y = 35
    graph.update({str(y): {str(29): 2.971, str(y + 2): 1.459}})  # 35

    y = 37
    graph.update({str(y): {str(35): 1.459, str(y + 2): x}})  # 37
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, str(79): 4.43}})  # 71

    y = 79
    graph.update({str(y): {str(71): 4.43, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "X": 2.49}})

    graph.update({"X": {str(107): 2.49}})

    return graph

def odd_12():
    x = 1.382
    y = 0
    graph = {"Y": {"2": 4.522},
             "2": {"Y": 4.522, "4": x}}

    for y in range(4, 8, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 8
    graph.update({str(y): {str(y - 2): x, str(12): 2 * x}})

    y = 12
    graph.update({str(y): {str(8): 2 * x, str(y + 2): x}})

    for y in range(14, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(38): 4.43}})  # 30

    y = 38
    graph.update({str(y): {str(30): 4.43, str(y + 2): x}})  # 38
    ###############################################################################

    for y in range(40, 44, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 44
    graph.update({str(y): {str(y - 2): x, str(48): 2 * x}})  # 44

    y = 48
    graph.update({str(y): {str(44): 2 * x, str(y + 2): x}})  # 48

    for y in range(50, 62, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 62
    graph.update({str(y): {str(y - 2): x, str(66): 2 * x}})  # 62

    y = 66
    graph.update({str(y): {str(62): 2 * x, str(y + 2): x}})  # 62

    for y in range(68, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(80): 4.43}})  # 72

    y = 80
    graph.update({str(y): {str(72): 4.43, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "Z": 2.49}})

    graph.update({"Z": {str(108): 2.49}})

    return graph

def even_12():
    x = 1.382
    y = 0
    graph = {"Y": {"1": 4.522},
             "1": {"Y": 4.522, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(37): 4.43}})  # 29

    y = 37
    graph.update({str(y): {str(29): 4.43, str(y + 2): x}})  # 37
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, str(79): 4.43}})  # 71

    y = 79
    graph.update({str(y): {str(71): 4.43, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "Z": 2.49}})

    graph.update({"Z": {str(107): 2.49}})

    return graph

def odd_13():
    x = 1.382
    y = 0
    graph = {"Aa": {"2": 4.522},
             "2": {"Aa": 4.522, "4": x}}

    for y in range(4, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(36): 2.971}})  # 30

    y = 36
    graph.update({str(y): {str(30): 2.971, str(y + 2): 1.459}})  # 36

    y = y + 2
    graph.update({str(y): {str(36): 1.459, str(y + 2): x}})  # 38

    ###############################################################################
    for y in range(40, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(y + 2): 1.459}})  # 72
    
    ########################## out of sequence ##########################
    y = y + 2  # 74
    graph.update({str(y): {str(y - 2): 1.459, str(80): 2.971}})  # 74

    y = 80
    graph.update({str(y): {str(74): 2.971, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "Ab": 2.489}})

    graph.update({"Ab": {str(108): 2.489}})

    return graph

def even_13():
    x = 1.382
    y = 0
    graph = {"Aa": {"1": 4.522},
             "1": {"Aa": 4.522, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(35): 2.971}})  # 29

    y = 35
    graph.update({str(y): {str(29): 2.971, str(y + 2): 1.459}})  # 35

    y = 37
    graph.update({str(y): {str(35): 1.459, str(y + 2): x}})  # 37
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, str(73): 1.459}})  # 71

    y = y + 2  # 73
    graph.update({str(y): {str(y - 2): 1.459, str(79): 2.971}})  # 73

    ########################## out of sequence ##########################
    y = 79
    graph.update({str(y): {str(73): 2.971, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "Ab": 2.49}})

    graph.update({"Ab": {str(107): 2.49}})

    return graph

def odd_14():
    x = 1.382
    y = 0
    graph = {"Ad": {"2": 4.522},
             "2": {"Ad": 4.522, "4": x}}

    for y in range(4, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(36): 2.971}})  # 30

    y = 36
    graph.update({str(y): {str(30): 2.971, str(38): 1.459}})  # 36

    y = 38
    graph.update({str(y): {str(36): 1.459, str(y + 2): x}})  # 38
    ###############################################################################

    for y in range(40, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(80): 4.43}})  # 72

    y = 80
    graph.update({str(y): {str(72): 4.43, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "Ae": 2.49}})

    graph.update({"Ae": {str(108): 2.49}})

    return graph

def even_14():
    x = 1.382
    y = 0
    graph = {"Ad": {"1": 4.522},
             "1": {"Ad": 4.522, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(35): 2.971}})  # 29

    y = 35
    graph.update({str(y): {str(29): 2.971, str(y + 2): 1.459}})  # 35

    y = 37
    graph.update({str(y): {str(35): 1.459, str(y + 2): x}})  # 37
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, str(79): 4.43}})  # 71
    
    y = 79
    graph.update({str(y): {str(71): 4.43, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "Ae": 2.49}})

    graph.update({"Ae": {str(107): 2.49}})

    return graph

def odd_15():
    x = 1.382
    y = 0
    graph = {"Ag": {"2": 4.522},
             "2": {"Ag": 4.522, "4": x}}

    for y in range(4, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(38): 4.43}})  # 30

    y = 38
    graph.update({str(y): {str(30): 4.43, str(y + 2): x}})  # 38
    ###############################################################################

    for y in range(40, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(74): 1.459}})  # 72

    y = y + 2  # 74
    graph.update({str(y): {str(72): 1.459, str(80): 2.971}})  # 80

    ########################## out of sequence ##########################
    y = 80
    graph.update({str(y): {str(74): 2.971, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "Ah": 2.49}})

    graph.update({"Ah": {str(108): 2.49}})

    return graph

def even_15():
    x = 1.382
    y = 0
    graph = {"Ag": {"1": 4.522},
             "1": {"Ag": 4.522, "3": x}}

    for y in range(3, 29, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 29
    graph.update({str(y): {str(y - 2): x, str(37): 4.43}})  # 29

    y = 37
    graph.update({str(y): {str(29): 4.43, str(y + 2): x}})  # 37
    ###############################################################################

    for y in range(39, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 71
    graph.update({str(y): {str(y - 2): x, str(79): 4.43}})

    y = 79
    graph.update({str(y): {str(71): 4.43, str(y + 2): x}})  # 79
    ###############################################################################

    for y in range(81, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 107
    graph.update({str(107): {str(y - 2): x, "Ah": 2.49}})

    graph.update({"Ah": {str(107): 2.49}})

    return graph

def odd_16():
    x = 1.382
    y = 0 

    graph = {"Ai": {"2": 4.522},
             "2": {"Ai": 4.522, "4": x}}

    for y in range(4, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

   ########################## out of sequence ##########################
    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(36): 2.971}})  # 30

    y = 36
    graph.update({str(y): {str(30): 2.971, str(y + 2): 1.459}})  # 36

    y = 38
    graph.update({str(y): {str(y - 2): 1.459, str(y + 2): x}})  # 38
    ###############################################################################

    for y in range(40, 72, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2  # 72
    graph.update({str(y): {str(y - 2): x, str(80): 4.43}})  # 72

    y = 80
    graph.update({str(y): {str(72): 4.43, str(y + 2): x}})  # 80
    ###############################################################################

    for y in range(82, 108, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 108
    graph.update({str(108): {str(y - 2): x, "Aj": 1.546}})

    graph.update({"Aj": {str(108): 1.546, "Ak": 0.944}})

    graph.update({"Ak": {"Aj": 0.944}})

    return graph

def even_16():
    x = 1.382
    x2 = 1.668
    x3 = 1.226
    x4 = 1.347
    y = 0
    graph = {"Ai": {"35": 25.538},
             "35": {"Ai": 25.538, "37": x}}

    for y in range(37, 43, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2
    graph.update({str(y): {str(y - 2): x, str(47): 2 * x}})  # 43

    y = 47
    graph.update({str(y): {str(43): 2 * x, str(y + 2): x}})  # 47

    y = y + 2
    graph.update({str(y): {str(y - 2): x, str(53): 2 * x}})  # 49

    y = 53
    graph.update({str(y): {str(49): 2 * x, str(y + 2): x}})  # 53

    y = y + 2
    graph.update({str(y): {str(y - 2): x, str(59): 2 * x}})  # 55

    y = 59
    graph.update({str(y): {str(55): 2 * x, str(y + 2): x}})  # 59
    ###############################################################################

    for y in range(61, 71, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2
    graph.update({str(y): {str(y - 2): x, str(81): 7.194}})  # 71

    y = 81
    graph.update({str(y): {str(71): 7.194, str(y + 2): x}})  # 81
    ###############################################################################

    for y in range(83, 107, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    ########################## out of sequence ##########################
    y = y + 2
    graph.update({str(y): {str(y - 2): x, "Aj": 1.547}})  # 107

    graph.update({"Aj": {str(y): 1.547, "Ak": 0.944}})  # Aj

    graph.update({"Ak": {"Aj": 0.944, str(111): 0.746}})  # Aj

    y = 111
    graph.update({str(y): {"Ak": 0.746, str(y + 2): 0.85 * x2}})  # 111
    ###############################################################################

    y = y + 2  # 113
    graph.update({str(y): {str(y - 2): 0.85 * x2, str(y + 2): 0.83 * x2}})  # 113

    for y in range(115, 123, 2):
        graph.update({str(y): {str(y - 2): 0.83 * x2, str(y + 2): 0.83 * x2}})

    y = y + 2  # 123
    graph.update({str(y): {str(y - 2): 0.83 * x2, str(y + 2): 1.607}})  # 123

    y = y + 2  # 125
    graph.update({str(y): {str(y - 2): 1.607, str(y + 2): x3}})  # 125

    for y in range(127, 135, 2):
        graph.update({str(y): {str(y - 2): x3, str(y + 2): x3}})

    y = y + 2
    graph.update({str(y): {str(y - 2): x3, str(y + 2): 1.366}})  # 135

    y = y + 2  # 137
    graph.update({str(y): {str(y - 2): 1.366, str(y + 2): 0.8 * x4}})  # 137

    y = y + 2  # 139
    graph.update({str(y): {str(y - 2): 0.8 * x4, str(y + 2): 0.8 * x4}})  # 139

    for y in range(141, 147, 2):
        graph.update({str(y): {str(y - 2): 0.8 * x4, str(y + 2): 0.8 * x4}})

    y = y + 2  # 147
    graph.update({str(y): {str(y - 2): 0.8 * x4, "Al": 0.9}})  # 147

    y = y + 2  # 149
    graph.update({"Al": {str(147): 0.9, str(149): 0.446}})

    graph.update({str(y): {"Al": 0.466}})  # 149

    return graph

def odd_17():
    x = 1.347
    y = 0
    graph = {"2": {"Am": 0.279},
             "Am": {"2": 0.279, "4": 1.067},
             "4": {"Am": 1.067, "6": x}}

    for y in range(6, 14, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 14
    graph.update({str(y): {str(y - 2): x, "An": 0.92}})  # 14

    y = y + 2  # 16
    graph.update({"An": {str(y - 2): 0.92, str(y): 0.426}})

    graph.update({str(y): {"An": 0.426, str(y + 2): x}})  # 16

    for y in range(18, 30, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x, str(y + 2): 3 * x}})  # 30

    y = y + 2  # 32
    graph.update({str(y): {str(y - 2): 3 * x, str(y + 2): x}})  # 32

    for y in range(34, 66, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 66
    graph.update({str(y): {str(y - 2): x, "Ao": 2.505}})  # 66

    y = y + 2  # 68
    graph.update({"Ao": {str(y - 2): 2.505, str(y): 3.527}})

    graph.update({str(y): {"Ao": 3.527, str(y + 2): x}})  # 68

    for y in range(70, 96, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 96
    graph.update({str(y): {str(y - 2): x, "Ap": 4.669}})  # 96

    y = y + 2  # 98
    graph.update({"Ap": {str(y - 2): 4.669, str(y): 3.411}})

    graph.update({str(y): {"Ap": 3.411, str(y + 2): x}})  # 98

    y = y + 2  # 100
    graph.update({str(y): {str(y - 2): x}})  # 100

    return graph

def even_17():
    x = 1.347
    y = 0
    ############################# segmented positions #############################
    # Distância intervalos =(d/(n-1)) * x
    graph = {"Am": {"An": 8.721},
             "An": {"Am": 8.721, "1E": 1.773},
             "1E": {"An": 1.773, "1D": (4 / 6) * x},
             "1D": {"1E": (4 / 6) * x, "1C": (4 / 6) * x},
             "1C": {"1D": (4 / 6) * x, "1B": (4 / 6) * x},
             "1B": {"1C": (4 / 6) * x, "1A": (4 / 6) * x},
             "1A": {"1B": (4 / 6) * x, "1": (4 / 6) * x},
             "1": {"1A": (4 / 6) * x, "3": (4 / 6) * x},
             str(3): {str(1): (4 / 6) * x, str(5): x}}
    #############################################################################

    for y in range(5, 47, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 47
    graph.update({str(y): {str(y - 2): x, "Ao": 2.505}})  # 47

    graph.update({"Ao": {str(47): 2.505, str(53): 2.18}})  # Ao

    y = 53  # 53
    graph.update({str(y): {"Ao": 2.18, str(y + 2): x}})  # 53

    for y in range(55, 83, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 83
    graph.update({str(y): {str(y - 2): x, "Ap": 0.629}})

    graph.update({"Ap": {str(83): 0.629, str(85): 0.718}})

    y = y + 2  # 85
    graph.update({str(y): {"Ap": 0.718, str(y + 2): x}})  # 85

    y = y + 2  # 87
    graph.update({str(y): {str(y - 2): x}})  # 87

    return graph

def odd_18():
    x = 1.347
    y = 0
    graph = {"Aq": {"Ar": 8.721},
             "Ar": {"Aq": 8.721, "2E": 1.773},
             "2E": {"Ar": 1.773, "2D": (4 / 6) * x},
             "2D": {"2E": (4 / 6) * x, "2C": (4 / 6) * x},
             "2C": {"2D": (4 / 6) * x, "2B": (4 / 6) * x},
             "2B": {"2C": (4 / 6) * x, "2A": (4 / 6) * x},
             "2A": {"2B": (4 / 6) * x, "2": (4 / 6) * x},
             "2": {"2A": (4 / 6) * x, "4": (4 / 6) * x},
             str(4): {str(2): (4 / 6) * x, str(6): x}}

    for y in range(6, 48, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 48
    graph.update({str(y): {str(y - 2): x, "As": 2.505}})  # 48

    graph.update({"As": {str(48): 2.505, str(54): 2.18}})  # As

    y = 54  # 54
    graph.update({str(y): {"As": 2.18, str(y + 2): x}})  # 54

    for y in range(56, 88, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 88
    graph.update({str(y): {str(y - 2): x}})  # 100

    return graph

def even_18():
    x1 = 1.347
    x2 = 1.382
    y = 0
    graph = {"Aq": {"1F": 2.908},

             # Fórmula segmented positions
             # Distância intervalos =(d/(n-1)) * x
             "1F": {"Aq": 2.908, "1E": x1},
             "1E": {"1F": x1, "1D": x1},
             "1D": {"1E": x1, "1C": x1},
             "1C": {"1D": x1, "Ar": 1.773},

             "Ar": {"1C": 1.773, "1B": 2.42},

             "1B": {"Ar": 2.42, "1A": (2 / 3) * x2},
             "1A": {"1B": (2 / 3) * x2, "1": (2 / 3) * x2},
             "1": {"1A": (2 / 3) * x2, "3": (2 / 3) * x2},

             str(3): {str(1): (2 / 3) * x2, str(5): x2}}

    for y in range(5, 49, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 49
    graph.update({str(y): {str(y - 2): x2, "As": 2.317}})  # 49

    graph.update({"As": {str(49): 2.317, str(55): 2.18}})

    y = 55
    graph.update({str(y): {"As": 2.18, str(y + 2): x2}})  # 55

    for y in range(57, 91, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 91
    graph.update({str(y): {str(y - 2): x2}})  # 100

    return graph

def odd_19():
    x = 1.382
    y = 0
    graph = {"At": {"2F": 2.42},
             "2F": {"At": 2.42, "2E": (2 / 7) * x},
             "2E": {"2F": (2 / 7) * x, "2D": (2 / 7) * x},
             "2D": {"2E": (2 / 7) * x, "2C": (2 / 7) * x},
             "2C": {"2D": (2 / 7) * x, "2B": (2 / 7) * x},
             "2B": {"2C": (2 / 7) * x, "2A": (2 / 7) * x},
             "2A": {"2B": (2 / 7) * x, "2": (2 / 7) * x},
             "2": {"2A": (2 / 7) * x, "4": (2 / 7) * x},
             "4": {"2": (2 / 7) * x, "6": x}}

    for y in range(6, 50, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 50
    graph.update({str(y): {str(y - 2): x, str(56): 4.43}})  # 48

    y = 56
    graph.update({str(y): {str(50): 4.43, str(y + 2): (18 / 19) * x}})  # 56

    for y in range(58, 94, 2):
        graph.update({str(y): {str(y - 2): (18 / 19) * x, str(y + 2): (18 / 19) * x}})

    y = y + 2  # 94
    graph.update({str(y): {str(y - 2): (18 / 19) * x}})  # 100

    return graph

def even_19():
    x = 1.381
    y = 0
    graph = {"At": {"1F": 2.42},
             "1F": {"At": 2.42, "1E": (2 / 7) * x},
             "1E": {"1F": (2 / 7) * x, "1D": (2 / 7) * x},
             "1D": {"1E": (2 / 7) * x, "1C": (2 / 7) * x},
             "1C": {"1D": (2 / 7) * x, "1B": (2 / 7) * x},
             "1B": {"1C": (2 / 7) * x, "1A": (2 / 7) * x},
             "1A": {"1B": (2 / 7) * x, "1": (2 / 7) * x},
             "1": {"1A": (2 / 7) * x, "3": (2 / 7) * x},
             "3": {"1": (2 / 7) * x, "5": x}}

    for y in range(5, 49, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 49
    graph.update({str(y): {str(y - 2): x, str(55): 4.43}})  # 49

    y = 55
    graph.update({str(y): {str(49): 4.43, str(y + 2): x}})  # 55

    for y in range(57, 91, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 91
    graph.update({str(y): {str(y - 2): x}})  # 91

    return graph

def odd_20():
    x = 1.382
    y = 0
    graph = {"Au": {"2F": 2.42},
             "2F": {"Au": 2.42, "2E": (2 / 7) * x},
             "2E": {"2F": (2 / 7) * x, "2D": (2 / 7) * x},
             "2D": {"2E": (2 / 7) * x, "2C": (2 / 7) * x},
             "2C": {"2D": (2 / 7) * x, "2B": (2 / 7) * x},
             "2B": {"2C": (2 / 7) * x, "2A": (2 / 7) * x},
             "2A": {"2B": (2 / 7) * x, "2": (2 / 7) * x},
             "2": {"2A": (2 / 7) * x, "4": (2 / 7) * x},
             str(4): {str(2): (2 / 7) * x, str(6): x}}

    for y in range(6, 50, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 50
    graph.update({str(y): {str(y - 2): x, str(56): 4.43}})

    y = 56
    graph.update({str(y): {str(50): 4.43, str(y + 2): x}})  # 56

    for y in range(58, 92, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 92
    graph.update({str(y): {str(y - 2): x}})  # 92

    return graph

def even_20():
    x = 1.382
    y = 0
    graph = {"Au": {"1": 2.703},
             "1": {"Au": 2.703, "3": x}}

    for y in range(3, 91, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2
    graph.update({str(y): {str(y - 2): x}})  # 91

    return graph

def odd_55():
    x = 1.347
    y = 0
    graph = {"Ab": {"4": 4.156},
             "4": {"Ab": 4.156, "6": 1.683},
             "6": {"4": 1.683, "8": 1.683},
             "8": {"6": 1.683, "10": 1.683},
             "10": {"8": 1.683, "12": x}}

    for y in range(12, 28, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 28
    graph.update({str(y): {str(y - 2): x, str(30): 1.178}})  # 28

    y = y + 2  # 30
    graph.update({str(y): {str(28): 1.178, "Ac": 1.965}})  # 30

    graph.update({"Ac": {str(30): 1.965}})

    return graph

def even_55():
    x1 = 1.347
    x2 = 1.226
    y = 0
    graph = {"Ab": {"1": 5.166},
             "1": {"Ab": 5.166, "3": x1}}

    for y in range(3, 9, 2):
        graph.update({str(y): {str(y - 2): x1, str(y + 2): x1}})

    y = y + 2  # 9
    graph.update({str(y): {str(y - 2): x1, str(11): 1.352}})  # 9

    y = y + 2  # 11
    graph.update({str(y): {str(9): 1.352, str(y + 2): x2}})  # 11

    for y in range(13, 23, 2):
        graph.update({str(y): {str(y - 2): x2, str(y + 2): x2}})

    y = y + 2  # 23
    graph.update({str(y): {str(y - 2): x2, "Ac": 5.207}})  # 23

    graph.update({"Ac": {str(23): 5.207}})

    return graph

def odd_60():
    x1 = 1.347
    x2 = 1.226
    y = 0
    graph = {"Ae": {"2": 5.166},
             "2": {"Ae": 5.166, "4": x1}}

    for y in range(4, 10, 2):
        graph.update({str(y): {str(y - 2): x1, str(y + 2): x1}})

    y = y + 2  # 10
    graph.update({str(y): {str(y - 2): x1, str(12): 1.352}})

    y = y + 2  # 12
    graph.update({str(y): {str(10): 1.352, str(y + 2): x2}})  # 12

    for y in range(14, 30, 2):
        graph.update({str(y): {str(y - 2): x1, str(y + 2): x1}})

    y = y + 2  # 30
    graph.update({str(y): {str(y - 2): x2, "Af": 1.53}})  # 30

    graph.update({"Af": {str(30): 1.53}})

    return graph

def even_60():
    x = 1.345
    y = 0
    graph = {"Ae": {"3": 3.757},
             "3": {"Ae": 3.757, "5": x}}

    for y in range(5, 31, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 31
    graph.update({str(y): {str(y - 2): x, "Af": 1.876}})  # 31

    graph.update({"Af": {str(31): 1.876}})

    return graph

def odd_65():
    x = 1.345
    y = 0
    graph = {"Ak": {"4": 2.412},
             "4": {"Ak": 2.412, "6": x}}

    for y in range(6, 34, 2):
        graph.update({str(y): {str(y - 2): x, str(y + 2): x}})

    y = y + 2  # 34
    graph.update({str(y): {str(y - 2): x, "Al": 3.22}})  # 34

    graph.update({"Al": {str(34): 3.22}})

    return graph
