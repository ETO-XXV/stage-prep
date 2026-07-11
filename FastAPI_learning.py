from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    gender: str
    age: int

class Competitor(BaseModel):
    company_name : str 
    website_url : str
    target_keywords : list[str]


@app.post("/user")
def create_user(user: User):
    return {
        "status": "success",
        "message": f"{user.name}  is already at the age of {user.age}",
    }



@app.post("/analysis")
def analyse_compititor( payload : Competitor):
    
    name = payload.company_name
    url = payload.website_url
    keywords = payload.target_keywords
    
    return {
        "status": "received",
        "message": f"Starting AI growth analysis for {name} ({url}).",
        "keywords_to_track": keywords
    }

@app.get("/status")
def check_status():
    return {"status": "success", "message": "hello world!"}


@app.get("/greeting/{name}")
def greet_user(name: int):
    return {"status": "success", "message": f"hello {name}!"}


@app.get("/search")
def search(country: str, industry: str = "all"):
    return {
        "message": f"Searching for leads in {country} under the {industry} sector.",
        "filters_applied": {"country": country, "industry": industry},
        "results_found": 12,
    }
