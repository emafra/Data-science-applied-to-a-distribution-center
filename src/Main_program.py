import pandas as pd
import displacement as dp
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

class OPP():
    '''Order picking process'''

    def __init__(self, order, table_order, table_picking):
        self._key = order
        self._table_order = table_order
        self._table_picking = table_picking
        self._picker = self._table_order.iloc[0]['funcionario']
        self._order_type = 0
        [self._meters, self._address_nfound] = self.meters_traveled()
        [self._amount_collected, self._start_time,
         self._final_time] = self.picking_performed()

    def not_picking(self):
        self._order_type += 1

    def meters_traveled(self):
        positions = self._table_order['posicao'].unique()
        distance_list = []
        if len(positions) > 1:
            for i in range(0, len(positions) - 1):
                adr1 = dp.Adress(positions[i])
                adr2 = dp.Adress(positions[i + 1])
                distance_list.append(adr1.travelled_distance(adr2))
                if not adr1.is_picking() or not adr2.is_picking():
                    self.not_picking()
            if None not in distance_list:
                return [sum(distance_list), None]

        if len(positions) == 1:
            adr = dp.Adress(positions[0])
            distance_list.append(0)
            if not adr.is_picking():
                self.not_picking()
            if None not in distance_list:
                return [distance_list[0], None]
        return [-1, 'X']

    def picking_performed(self):
        rows = self._table_picking.shape[0]
        picking_day = self._table_picking.iloc[0]['Data de criação']
        start_time = self._table_picking.iloc[0]['Hora registro']
        start_time = picking_day + ' ' + start_time
        picking_day = self._table_picking.iloc[-1]['Data de criação']
        final_time = self._table_picking.iloc[rows - 1]['Hora registro']
        final_time = picking_day + ' ' + final_time
        return [rows, start_time, final_time]

    @property
    def key(self):
        return self._key

    @property
    def picker(self):
        return self._picker

    @property
    def table_order(self):
        return self._table_order

    @property
    def table_picking(self):
        return self._table_picking

    @property
    def order_type(self):
        return self._order_type

    @property
    def meters(self):
        return self._meters

    @property
    def amount_colleted(self):
        return self._amount_collected

    @property
    def start_time(self):
        return self._start_time

    @property
    def final_time(self):
        return self._final_time

    @property
    def address_nfound(self):
        return self._address_nfound

class tables_OPP():
    def __init__(self, table1, table2, table3, flag=1):
        self._LTAP_table = table1
        self._ZTWM_table = table2
        self._pendency_table = table3
        if flag == 1:
            self._result_table = self.build_resulting_table()
        else:
            self._result_table = self.build_resulting_table_TEST()
        self._picking_table = self.picking_process()
        print('Olha nos aqui:', len(self._picking_table['ordem']))
        self._order_list = self._picking_table['ordem'].unique()

    def table_format(self):
        return pd.DataFrame(columns=['ordem', 'funcionario', 'distancia', 'Qtd_coletada',
                                     'inicial', 'final', 'type', 'Pos nencontrada'])

    def intersection_table(self):
        ''' Eliminates orders that are not exclusively Pa0 and pa1.
        Delete pending orders, and then,
        filters the tables by their intersection '''
        print('**************** FILTROS *****************\n')

        print('Tamanho listas originas para cada ordem:')
        l_test_1 = self._LTAP_table['ordem'].unique()
        l_test_2 = self._ZTWM_table['ordem'].unique()
        print('LTAP_list[ordem]:', len(l_test_1), 'ZTWM_list[ordem]', len(l_test_2))
        print('*********************************\n')

        print('Intersecção por ordem:')
        l_test_3 = [value for value in l_test_1 if
                value in l_test_2]
        #intersection_by_order = self._ZTWM_table[self._ZTWM_table['ordem'].isin(l_test_3)]
        print('Intersecção[ordem]:', len(l_test_3), 'Proporção:', f'{(len(l_test_3)*100/len(l_test_2))}%')
        print('Obs: Este print é só para ver como seria o tamanho da intersecção original.')
        print('*********************************')

        'filter by keys:'
        lst1_key = self._LTAP_table['chave'].unique()
        lst2_key = self._ZTWM_table['chave'].unique()
        lst_not_PA1_keys = [value for value in lst2_key if
                value not in lst1_key]
        not_intersection = self._ZTWM_table[self._ZTWM_table['chave'].isin(lst_not_PA1_keys)]
        contaminated_orders = not_intersection['ordem'].unique()
        intersection = self._ZTWM_table[~self._ZTWM_table['ordem'].isin(contaminated_orders)]
        num_orders = len(intersection['ordem'].unique())
        print('Intersecção por chave:')
        print('Intersecção[ordem]_Filtro_1:', num_orders, 'Proporção:',
              f'{(num_orders*100/len(l_test_2))}%')
        print('*********************************')

        print('Numero de ordens da tabela pendência:\n')
        lst_orders_pending = self._pendency_table['ordem'].unique()
        print('Pendências[ordem]:', len(lst_orders_pending))
        print('*********************************')

        print('Remoção de ordens com pendência:')
        result = intersection[~intersection['ordem'].isin(lst_orders_pending)]
        valid_orders = result['ordem'].unique()
        num_orders = len(valid_orders)
        print('Sengundo filtro, sem pendencias:', num_orders, 'Proporção:',
              f'{(num_orders*100/len(l_test_2))}%')
        return valid_orders

    def build_resulting_table(self):
        order_list = self.intersection_table()
        result_table = self.table_format()

        for x in order_list:
            table1 = self._LTAP_table[(self._LTAP_table['ordem'] == x)]
            table2 = self._ZTWM_table[(self._ZTWM_table['ordem'] == x)]
            order = OPP(x, table1, table2)
            new_row = {'ordem': order.key, 'funcionario': order.picker,
                       'distancia': order.meters, 'Qtd_coletada': order.amount_colleted,
                       'inicial': order.start_time, 'final': order.final_time,
                       'type': order.order_type, 'Pos nencontrada': order.address_nfound}
            result_table = result_table.append(new_row, ignore_index=True)

        result_table['inicial'] = pd.to_datetime(result_table['inicial'])
        result_table['final'] = pd.to_datetime(result_table['final'])
        result_table['seconds'] = result_table['final'] - result_table['inicial']
        result_table['seconds'] = result_table['seconds'].dt.total_seconds()
        result_table[result_table['seconds'] == 0] = -1

        result_table['produtividade'] = ((result_table['distancia']/0.685) +
                                         (result_table['Qtd_coletada']/0.121)) / result_table['seconds']

        result_table[['Qtd_coletada', 'distancia', 'produtividade']] = \
            result_table[['Qtd_coletada', 'distancia', 'produtividade']].astype(np.float64)
        return result_table

    def build_resulting_table_TEST(self):
        test_list = self.intersection_table()
        result_table = self.table_format()

        i = 0
        for x in test_list:
            table1 = self._LTAP_table[(self._LTAP_table['ordem'] == x)]
            table2 = self._ZTWM_table[(self._ZTWM_table['ordem'] == x)]
            order = OPP(x, table1, table2)
            new_row = {'ordem': order.key, 'funcionario': order.picker,
                       'distancia': order.meters, 'Qtd_coletada': order.amount_colleted,
                       'inicial': order.start_time, 'final': order.final_time,
                       'type': order.order_type, 'Pos nencontrada': order.address_nfound}
            result_table = result_table.append(new_row, ignore_index=True)
            i += 1
            if i == 50:
                break

        result_table['inicial'] = pd.to_datetime(result_table['inicial'])
        result_table['final'] = pd.to_datetime(result_table['final'])
        result_table['seconds'] = result_table['final'] - result_table['inicial']
        result_table['seconds'] = result_table['seconds'].dt.total_seconds()
        result_table[result_table['seconds'] == 0] = -1

        result_table['produtividade'] = (result_table['distancia'] +
                                         result_table['Qtd_coletada']) / result_table['seconds']

        result_table[['Qtd_coletada', 'distancia', 'produtividade']] = \
            result_table[['Qtd_coletada', 'distancia', 'produtividade']].astype(np.float64)
        return result_table

    def picking_process(self):
        picking_table = self._result_table[(self._result_table['type'] == 0) &
                                           (self._result_table['Pos nencontrada'] != 'X') & (
                                                   self._result_table['seconds'] != -1)]
        return picking_table

    def with_pendency(self):
        pendency_table = self._result_table[(self._result_table['type'] != 0) |
                                            (self._result_table['Pos nencontrada'] == 'X') | (
                                                    self._result_table['seconds'] == 0)]
        return pendency_table

    def productivity_histogram(self):
        plt.figure()
        self._picking_table['produtividade'].plot.hist(bins=100, alpha=1)
        plt.show()

    def correlation_map(self):
        corrMatrix = self._picking_table.corr()
        sn.heatmap(corrMatrix, annot=True)
        plt.show()

    def variables_histogram(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)
        ax1.hist(self._picking_table['distancia'], bins=100, alpha=1)
        ax1.set_title("Distância Percorrida")
        ax2.hist(self._picking_table['Qtd_coletada'], bins=100, alpha=1)
        ax2.set_title("Qtd Coletada")
        plt.show()

    def productivity_employee_plot(self):
        employee_list = self._picking_table['funcionario'].unique()
        productivity_list = []
        sample_list = []
        for x in employee_list:
            productivity_list.append(
                self._picking_table['produtividade'][(self._picking_table['funcionario'] == x)].mean())
            sample_list.append(
                self._picking_table['produtividade'][(self._picking_table['funcionario'] == x)].count())
        z = pd.DataFrame({'employee': employee_list,
                          'Productivity': productivity_list, 'number of samples': sample_list})
        z.plot.bar(rot=0, subplots=True, x='employee')
        plt.show()

    @property
    def LTAP_table(self):
        return self._LTAP_table

    @property
    def ZTWM_table(self):
        return self._ZTWM_table

    @property
    def result_table(self):
        return self._result_table

    @property
    def picking_table(self):
        return self._picking_table

    @property
    def order_list(self):
        return self._order_list

class reference:
    def __init__(self, valid_orders, position_table, base_table):
        self._base_table, self._position_table = self.build_base(valid_orders, position_table, base_table)
        self._pick_table, self._travel_table = self._get_table_references()

    def build_base(self, valid_orders, position_table, base_table):
        base_table = base_table[['ordem', 'item', 'chave',
                                 'Data de criação', 'Hora registro', 'Nome do usuário.1']][
            (base_table['ordem'].isin(valid_orders))].copy()
        position_table = position_table[['chave', 'posicao']][
            (position_table['ordem'].isin(valid_orders))].copy()
        return base_table, position_table

    def _get_rate_values(self, process_table):
        order = process_table.iloc[0]['ordem']
        key = process_table.iloc[0]['chave']
        employee = process_table.iloc[0]['Nome do usuário.1']
        rows = process_table.shape[0]
        picking_day = process_table.iloc[0]['Data de criação']
        start_time = process_table.iloc[0]['Hora registro']
        start_time = picking_day + ' ' + start_time
        picking_day = process_table.iloc[-1]['Data de criação']
        final_time = process_table.iloc[rows - 1]['Hora registro']
        final_time = picking_day + ' ' + final_time
        return [order, key, employee, rows, start_time, final_time]

    def _get_travel_values(self, process_table, buffer_table):
        key_1 = buffer_table.iloc[0]['chave']
        key_2 = process_table.iloc[0]['chave']
        rows1 = buffer_table.shape[0]
        rows2 = process_table.shape[0]
        position_1 = self._position_table[(self._position_table['chave'] == key_1)].iloc[0]['posicao']
        position_2 = self._position_table[(self._position_table['chave'] == key_2)].iloc[0]['posicao']
        employee = buffer_table.iloc[0]['Nome do usuário.1']
        picking_day = buffer_table.iloc[-1]['Data de criação']
        start_time = buffer_table.iloc[-1]['Hora registro']
        start_time = picking_day + ' ' + start_time

        picking_day = process_table.iloc[0]['Data de criação']
        final_time = process_table.iloc[0]['Hora registro']
        final_time = picking_day + ' ' + final_time

        adr1 = dp.Adress(position_1)
        adr2 = dp.Adress(position_2)
        distance = adr1.travelled_distance(adr2)
        return [key_1, key_2, rows1, rows2, employee,
                distance, start_time, final_time]

    def _table_format(self, flag=True):
        if flag == True:
            return pd.DataFrame(columns=['ordem', 'chave', 'Qtd_coletada',
                                         'funcionario', 'inicial', 'final'])
        else:
            return pd.DataFrame(columns=['ordem', 'chave1', 'chave2', 'Qtd1', 'Qtd2',
                 'funcionario', 'inicial', 'final', 'distancia'])

    def _new_pick_line(self, process_table, pick_table):
        if len(process_table) > 1:
            [order, key, employee, rows, start_time, final_time] = self._get_rate_values(process_table)
            if start_time != final_time:
                new_row = {'ordem': order, 'chave': key, 'Qtd_coletada': rows,
                           'funcionario': employee, 'inicial': start_time, 'final': final_time}
                pick_table = pick_table.append(new_row, ignore_index=True)
        return pick_table

    def _new_travel_line(self, process_table, buffer_table, travel_table):
        if len(buffer_table) > 1 and len(process_table) > 1:
            order1 = buffer_table.iloc[0]['ordem']
            order2 = process_table.iloc[0]['ordem']
            if order1 == order2:
                [key_1, key_2, rows1, rows2, employee,
                 distance, start_time, final_time] = self._get_travel_values(process_table, buffer_table)
                if start_time != final_time:
                    new_row = {'ordem': order1, 'chave1': key_1, 'chave2': key_2, 'Qtd1': rows1,
                               'Qtd2': rows2, 'funcionario': employee, 'inicial': start_time,
                               'final': final_time, 'distancia': distance}
                    travel_table = travel_table.append(new_row, ignore_index=True)
        return travel_table

    def _pick_rate(self, pick_table):
        pick_table['inicial'] = pd.to_datetime(pick_table['inicial'])
        pick_table['final'] = pd.to_datetime(pick_table['final'])
        pick_table['seconds'] = pick_table['final'] - pick_table['inicial']
        # pick_table['seconds'] = pick_table['seconds'].dt.total_seconds()
        pick_table['seconds'] = pick_table['Qtd_coletada'] * \
                                ((pick_table['seconds'].dt.total_seconds()) / (pick_table['Qtd_coletada'] - 1))
        pick_table['rate'] = pick_table['Qtd_coletada'] / pick_table['seconds']

        pick_table = pick_table[pick_table['rate'].between(
            pick_table['rate'].quantile(.15), pick_table['rate'].quantile(.85))]
        return pick_table

    def _travel_speed(self, travel_table):
        travel_table['inicial'] = pd.to_datetime(travel_table['inicial'])
        travel_table['final'] = pd.to_datetime(travel_table['final'])
        travel_table['seconds'] = travel_table['final'] - travel_table['inicial']
        travel_table['seconds'] = travel_table['seconds'].dt.total_seconds()
        # travel_table['seconds'] = travel_table['Qtd_coletada'] * \
        #                         ((travel_table['seconds'].dt.total_seconds()) / (travel_table['Qtd_coletada'] - 1))
        travel_table['speed'] = travel_table['distancia'] / travel_table['seconds']

        travel_table = travel_table[travel_table['speed'].between(
            travel_table['speed'].quantile(.15), travel_table['speed'].quantile(.85))]
        return travel_table

    def _get_table_references(self):
        lst = self._base_table['chave'].unique()
        pick_table = self._table_format()
        travel_table = self._table_format(False)
        buffer_table = []
        for x in lst:
            process_table = self._base_table[(self._base_table['chave'] == x)]
            pick_table = self._new_pick_line(process_table, pick_table)
            travel_table = self._new_travel_line(process_table, buffer_table, travel_table)
            buffer_table = process_table
        return self._pick_rate(pick_table), self._travel_speed(travel_table)

    def pick_histogram(self):
        plt.figure()
        self._pick_table['rate'].plot.hist(bins=100, alpha=1)
        plt.show()

    def pick_box_plot(self):
        self._pick_table['rate'].plot.box()
        plt.show()

    def travel_histogram(self):
        plt.figure()
        self._travel_table['speed'].plot.hist(bins=100, alpha=1)
        plt.show()

    def travel_box_plot(self):
        self._travel_table['speed'].plot.box()
        plt.show()

    @property
    def pick_table(self):
        return self._pick_table
    @property
    def travel_table(self):
        return self._travel_table

df = pd.read_csv('Tabela_LTAP.csv', encoding='ISO-8859-1', sep=';'). \
    sort_values(by=['ordem', 'data', 'hora'])
df2 = pd.read_csv('Tabela_ZTWM.csv', encoding='ISO-8859-1', sep=';'). \
    sort_values(by=['ordem', 'Data de criação', 'Hora registro'])
df3 = pd.read_csv('Tabela_Pendencias.csv', encoding='ISO-8859-1', sep=';'). \
    sort_values(by=['ordem', 'data_criacao', 'hora_criacao'])

picking_order = tables_OPP(df, df2, df3)
picking_order.variables_histogram()
picking_order.productivity_employee_plot()
# print(picking_order.picking_table['produtividade'].mean())
# print(len(df['ordem']), df2['ordem'], len(picking_order.LTAP_table['ordem']), len(picking_order.result_table['ordem']),
#       len(picking_order.picking_table))

referencias = reference(picking_order.order_list, df, df2)
#
# # print(referencias.travel_table.columns)
# # print(referencias.travel_table[['chave1', 'chave2', 'inicial', 'final']][(referencias.travel_table['seconds'] < 0)])
# #
# a = referencias.travel_table['speed'].mean()
# b = referencias.pick_table['rate'].mean()
# #
# # print(a, b)
referencias.travel_histogram()
referencias.travel_box_plot()
referencias.pick_histogram()
