from fastapi import FastAPI

app=FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}



def main():
    print("Hello from employee-management!")


if __name__ == "__main__":
    main()
