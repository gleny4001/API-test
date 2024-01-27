from fastapi import FastAPI


app = FastAPI()

result = {"Positive" : 30, "Negative" :  70}


@app.get("/")
def sentiment():
  return result