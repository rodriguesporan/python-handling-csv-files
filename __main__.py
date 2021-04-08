import csv
import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format #Formatting float column of Dataframe in Pandas

# webmotors = []
# with open('dataset_case_busdev_bi.csv', 'r') as csv_file: #abrir o arquivo convertido pra csv e atribuindo à variavel csv_file
#     csv_rows = csv.reader(csv_file, delimiter=';') #lendo o arquivo
#     for columns in csv_rows:
#         webmotors.append(columns[0].split(';')) #pega a unica coluna do arquivo original e separa em várias colunas

# with open('new.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';',lineterminator='\n')
#     for row in webmotors:#linha da lista webmotors
#         writer.writerow(row)
#         print(row)

# dataframe
df = pd.read_csv(r'new.csv', delimiter=';', encoding='latin1')
dfSomeCols = df.reindex(columns=['Model.Value', 'Price', 'FipePercent', 'YearModel', 'Odometer'])
models = dfSomeCols.groupby(['Model.Value'])
# print(dfSomeCols)
# print(models.count().reset_index('Model.Value', col_level=1))
quantityByModel = models.size()
# # .reset_index(name='counts')
# # # .set_index(['Model.Value', 'counts'])
# # # .sort_values(by='counts', ascending=False)
# # # .nlargest(20, 'counts')
# print(quantityByModel)
# print(models.mean().reset_index('Model.Value', col_level=1))
avgByModel = models.mean()
# .reset_index('Model.Value', col_level=1)
# print(avgByModel)

# result = pd.concat([quantityByModel, avgByModel], axis=1, join="inner")
# # result = quantityByModel.append(models.mean().reset_index('Model.Value', col_level=1))
result = pd.concat([quantityByModel, avgByModel], axis=1, join="inner")
result = result.sort_values(by=0, ascending=False).head(20)
result = result.reset_index('Model.Value', col_level=1)
result = result.rename(columns={"Model.Value": "model", 0: "counts", "Price": "price", "FipePercent": "fipe-percent", "YearModel": "year-model", "Odometer": "odometer"})
print(result)

# aggregations = models.agg(['sum', 'count', 'mean']).reset_index('Model.Value', col_level=1)
# print(aggregations.rename(str.lower, axis='columns'))

# #fazendo o valor total das vendas por modelo para achar o valor médio por modelo
# # faturamentoModelo = df[['Model.Value', 'Price']].groupby('Model.Value').mean()
# faturamentoModelo = df[['Model.Value', 'Price']].groupby('Model.Value').mean()
# faturamentoModelo = faturamentoModelo.sort_values(by='Price', ascending=False)
# print(faturamentoModelo)