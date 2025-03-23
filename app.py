import pandas as pd

#CRIA a tabela inicial com NOME, IDADE e CIDADE
def create_dataframe():
    data = {
        'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
        'Age': [10, 20, 30, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }

    return pd.DataFrame(data)

#ADICIONA a coluna CUSTO MENSAL
def add_month_cost(df, month_costs):
    df['Month Cost'] = month_costs

#ADICIONA a coluna CUSTO ANUAL EM MILHARES
def add_annual_cost_in_thousands(df):
    df['Annual Cost in Thousands'] = 12 * df['Month Cost'] // 1000

#EXECUTA o código
if __name__ == '__main__':
    df = create_dataframe()
    add_month_cost(df, [50000, 80000, 20000, 50000])
    add_annual_cost_in_thousands(df)
    print(df)