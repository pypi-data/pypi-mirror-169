import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="队列系统",
    contact={
        "name": "Zhao Hao",
        "email": "601095001@qq.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.post(path="/task")
def addTask():
    return

@app.delete(path="/task")
def deleteTask():
    return

@app.get(path="/task")
def showTask():
    return


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)