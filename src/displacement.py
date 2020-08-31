import street_graphs
import main_graph
import dijkstra_algorithm

class Adress:

    def __init__(self, adress):
        '''
        Receives a string of address
        corresponding to the item's position.
        Main graph is same for every object, and corresponds
        to the CD graph.
        Its nodes is the crossings between the streets.
        The subgraph is only the graphic belongs to the street where the address is.
        '''
        self._adress = adress
        self._graph = main_graph.graph()
        [self._street, self._position, self._value] = self._sort()
        self._nodes = self._adress_nodes()
        self._sub_graph = self._get_sub_graph()

    def _sort(self):
        if self.format_is_valid():
            # Through the address returns street and position with suitable format.
            words = ['A','B','C','D','E','F','G']
            self._street = self._adress[:2]
            self._position = self._adress[3:6]

            if self._position[2] == ".":
                self._position = self._position[:2]
                self._value = int(self._position)
                self._position = str(self._value)

            else:
                self._value = int(self._position)
                self._position = str(self._value)

            if self._adress[len(self._adress)-1] in words:
                self._position = self._position + self._adress[len(self._adress)-1]

            return [self._street, self._position, self._value]
        return [None, None, None]

    def _adress_nodes(self):
        '''Returns nodes referring to intersections.'''
        self._nodes = None

        if self._street == '04':
            self._nodes = ["A", "B", "C", "D"]

        elif self._street == '05':
            self._nodes = ["E", "F", "G"]

        elif self._street == '06':
            self._nodes = ["H", "I", "J", "K"]

        elif self._street == '07':
            self._nodes = ["L", "M", "N"]

        elif self._street == '08':
            self._nodes = ["O", "P", "Q"]

        elif self._street == '09':
            self._nodes = ["S", "T"]

        elif self._street == '10':
            self._nodes = ["U", "V"]

        elif self._street == '11':
            self._nodes = ["W", "X"]

        elif self._street == '12':
            self._nodes = ["Y", "Z"]

        elif self._street == '13':
            self._nodes = ["Aa", "Ab"]

        elif self._street == '14':
            self._nodes = ["Ad", "Ae"]

        elif self._street == '15':
            self._nodes = ["Ag", "Ah"]

        elif self._street == '16':
            if self._value % 2 == 0:
                self._nodes = ["Ai", "Aj", "Ak"]
            else:
                self._nodes = ["Ai", "Aj", "Ak", "Al"]

        elif self._street == '17':
            self._nodes = ["Am", "An", "Ao", "Ap"]

        elif self._street == '18':
            self._nodes = ["Aq", "Ar", "As"]

        elif self._street == '19':
            self._nodes = ["At"]

        elif self._street == '20':
            self._nodes = ["Au"]

        elif self._street == '55':
            self._nodes = ["Ab", "Ac"]

        elif self._street == '60':
            self._nodes = ["Ae", "Af"]

        elif self._street == '65':
            self._nodes = ["Ak", "Al"]

        return self._nodes

    def _get_sub_graph(self):
        ''''Returns street subgraph.'''
        self._sub_graph = None
        words = ['A','B','C','D','E','F','G']

        value_positionn = self._position
        if self.format_is_valid():
            if len(self._position) == 3:
                if self._position[2] in words:
                    value_positionn = self._position[:2]
                else:
                    pass
            elif len(self._position) == 2:
                if self._position[1] in words:
                    value_positionn = self._position[:1]
                else:
                    pass

            if self._street == '04':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_4()
                else:
                    self._sub_graph = street_graphs.even_4()

            elif self._street == '05':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_5()
                else:
                    self._sub_graph = street_graphs.even_5()

            elif self._street == '06':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_6()
                else:
                    self._sub_graph = street_graphs.even_6()

            elif self._street == '07':
                if int(value_positionn) % 2 != 0:
                    self._sub_graph = street_graphs.even_7()

            elif self._street == '08':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_8()
                else:
                    self._sub_graph = street_graphs.even_8()

            elif self._street == '09':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_9()
                else:
                    self._sub_graph = street_graphs.even_9()

            elif self._street == '10':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_10()
                else:
                    self._sub_graph = street_graphs.even_10()

            elif self._street == '11':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_11()
                else:
                    self._sub_graph = street_graphs.even_11()

            elif self._street == '12':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_12()
                else:
                    self._sub_graph = street_graphs.even_12()

            elif self._street == '13':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_13()
                else:
                    self._sub_graph = street_graphs.even_13()

            elif self._street == '14':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_14()
                else:
                    self._sub_graph = street_graphs.even_14()

            elif self._street == '15':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_15()
                else:
                    self._sub_graph = street_graphs.even_15()

            elif self._street == '16':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_16()
                else:
                    self._sub_graph = street_graphs.even_16()

            elif self._street == '17':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_17()
                else:
                    self._sub_graph = street_graphs.even_17()

            elif self._street == '18':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_18()
                else:
                    self._sub_graph = street_graphs.even_18()

            elif self._street == '19':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_19()
                else:
                    self._sub_graph = street_graphs.even_19()

            elif self._street == '20':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_20()
                else:
                    self._sub_graph = street_graphs.even_20()

            elif self._street == '55':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_55()
                else:
                    self._sub_graph = street_graphs.even_55()

            elif self._street == '60':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_60()
                else:
                    self._sub_graph = street_graphs.even_60()

            elif self._street == '65':
                if int(value_positionn) % 2 == 0:
                    self._sub_graph = street_graphs.odd_65()

        return self._sub_graph

    def _approximates_position(self):
        '''For positions that are not mapped in the graph, an approximation is necessary.'''
        approximations_floor = ['1A','1B','1C','1D','1E','1F','1G','1H']
        if self._adress[-2:] in approximations_floor:
            self._position = str(self._value)
            if self.is_valid():
                return True
            else:
                return False

    def is_valid(self):
        """Checks whether the address attribute belongs to the CD.
        For the analyzed process, only the first floor will be considered.
        """
        approximations_floor = ['1A','1B','1C','1D','1E','1F','1G','1H']
        if self._sub_graph is None:
            return False
        if self._position not in self._sub_graph:
            return False
        else:
            return self.is_picking()

    def street_distances(self):
        '''Receive list of distances between intersections and the position of interest.'''
        distance_list = []
        for x in self._nodes:
            distance_list.append\
                (dijkstra_algorithm.dijkstra_path(self._sub_graph, self._position, x))
        return distance_list

    def intersections_distance(self, other):
        '''
        Receive list of distances between intersections and the position of interest,
        for both streets.
        Obtains a list of the shortest distances between the nodes of the main graph.
        '''
        distance_list = []
        for x in self._nodes:
            for y in other.nodes:
                distance_list.append\
                    (dijkstra_algorithm.dijkstra_path(self._graph, x, y))
        return distance_list

    def travelled_distance(self, other):
        '''
        Validates if the address exists, else return none.
        Combines the three lists and returns the lowest value.
        Return min value.
        '''
        if self.is_valid() and other.is_valid():
            possible_routes = []
            initial_distances = self.street_distances()
            arrival_distances = other.street_distances()
            central_distances = self.intersections_distance(other)

            for x in range (0,len(initial_distances)):
                for y in range (0,len(arrival_distances)):
                    for z in range (0,len(central_distances)):
                        possible_routes.append(initial_distances[x] + arrival_distances[y] \
                                         + central_distances[z])
            return min(possible_routes)
        if other.is_valid():
            if self._approximates_position():
                return self.travelled_distance(other)
            else:
                pass
        if self.is_valid():
            if other._approximates_position():
                return self.travelled_distance(other)
            else:
                pass
        return None

    def is_picking(self):
        approximations_floor = ['1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H']
        if self._adress[-2:] == '01':
            return True
        if self._adress[-2:] in approximations_floor:
            return True
        return False

    def format_is_valid(self):
        if not None:
            if len(self._adress) > 6:
                if self._adress[2] == '.':
                    return True
        return False

    @property
    def adress(self):
        return self._adress
    @property
    def graph(self):
        return self._graph
    @property
    def street(self):
        return self._street
    @property
    def position(self):
        return self._position
    @property
    def sub_graph(self):
        return self._sub_graph
    @property
    def nodes(self):
        return self._nodes

# adress_initial = '05.02.01A'
# finish_adress = '06.04.01'
# rua = Adress(adress_initial)
# # print(rua.nodes)
# rua2 = Adress(finish_adress)
# # print(rua2.nodes)
# # print(rua2.adress[-1], rua2.adress[-2:])
# #
# print(rua.travelled_distance(rua2))
# print(rua2.street,rua2.position)
# print(rua2.position in rua2.sub_graph)
# # print(rua.street_distances(), rua2.street_distances(), rua.intersections_distance(rua2))
# # print('D' in rua.sub_graph, '47' in rua2.sub_graph)