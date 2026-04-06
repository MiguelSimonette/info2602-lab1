from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

### New Function
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:
                filtered_students.append(student)
        return filtered_students
    return data

### End of new function
@app.get('/students/{id}')
async def get_student(id: str):
    for student in data:
        if student['id'] == id:
            return student
        
#Exercise 1 
@app.get('/stats')
async def get_stats():
    stats = {}

    for student in data:
        pref = student['pref']
        programme = student['programme']

        if pref in stats:
            stats[pref] += 1
        else:
            stats[pref] = 1

        if programme in stats:
            stats[programme] += 1
        else:
            stats[programme] = 1

    return stats

#Exercise 2
@app.get('/add/{a}/{b}')
async def add(a: float, b: float):
    return a + b

@app.get('/subtract/{a}/{b}')
async def subtract(a: float, b: float):
    return a - b

@app.get('/multiply/{a}/{b}')
async def multiply(a: float, b: float):
    return a * b

@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float):
    return a / b