import pandas as pd
from graph.graphbuilder import app

df=pd.read_csv("data/evaluation.csv")

correct=0
total=len(df)

for _,row in df.iterrows():

    result=app.invoke({
      "query":row["query"],
      "session_id": "eval"
    })

    prediction=result["next_agent"]

    expected=row["expected_agent"]

    if prediction==expected:
        correct+=1
    else:
        print(f"Query: {row['query']}")
        print(f"Expected: {expected}, Got: {prediction}")
        print("------")


accuracy=correct/total
print(f"Accuracy: {accuracy*100:.2f}%")
