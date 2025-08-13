from fastapi import FastAPI, Body, HTTPException

app = FastAPI()

PROJECT = [
    {
        "id": 1,
        "project": "Hotel at SR",
        "client": "PEC company",
        "price": "Thinking",
        "web": "http://www.pec.com",
        "email": "pec@gmail.com"
    },
    {
        "id": 2,
        "project": "School Management System",
        "client": "Global Education Ltd",
        "price": "25000 USD",
        "web": "http://www.globaledu.com",
        "email": "contact@globaledu.com"
    },
    {
        "id": 3,
        "project": "E-Commerce Website",
        "client": "SmartShop Co.",
        "price": "18000 USD",
        "web": "http://www.smartshop.com",
        "email": "info@smartshop.com"
    },
    {
        "id": 4,
        "project": "Hospital Management App",
        "client": "HealthFirst Group",
        "price": "32000 USD",
        "web": "http://www.healthfirst.com",
        "email": "support@healthfirst.com"
    },
    {
        "id": 5,
        "project": "Restaurant POS System",
        "client": "TastyFood Inc.",
        "price": "15000 USD",
        "web": "http://www.tastyfood.com",
        "email": "sales@tastyfood.com"
    }
]

@app.get('/all-project')
async def get_project():
    return PROJECT

