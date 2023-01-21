import pandas as pd


df = pd.read_csv(
    "????.csv",#nome do arquivo
    encoding='utf-8', 
    usecols=['transactionId', 'tenant', 'partner', 'type',"detailType", #lista das colunas do arquivo que precisei
                "userId", "name", "document","amount","amountDecimal",
                "balanceAfter", "balanceAfterDecimal",	"timestamp",
                "date", "clientType", "boletoId", "fromAtarId",
                "fromName", "fromDocument", "fromAgency", "fromBank",
                "fromAccountNumber", "fromAccountType", "toAtarId",
                "toName", "toDocument", "toBank", "toAgency", "toAccountNumber",
                "toAccountType", "operator", "notes", "rawType", "status", "nuOp"]
)
df.to_csv('info_precisas.csv') #salvando um novo arquivo csv com a lista
print(df)