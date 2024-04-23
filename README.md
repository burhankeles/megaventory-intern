# Installation
1. Install requirements.
    ``py -m pip install -r requirements.txt``
2. Run the FastAPI webserver.
    ``py -m uvicorn main:app --port 8005``
3. Run the run.py for required steps for interview.
    ``py run.py``

# Project Description

## What did I do?
The needed project about developing a web-application to call MegaventoryAPI's.
I added the required endpoints using Update and Insert separately.
So, I developed an additional API system using FastAPI framework which I have experience on 
(Experience Link: https://gitlab.com/burhankeles/burhankelesweb).

## Why did I choose FastAPI?
Because it is easy to implement even though you don't have any API programming experience.

## What can be added?
Due to limited time (I have exams following week :)), I couldn't add my additional wants.
1. I might have implemented modular json statements in the main.py.
2. I might have used api_key statement on main.py in a secret way via using secrets.
3. The last task (5th) didn't worked well.

## Note
There is limited use of OOP because to use Body on FastAPI requests, you need to inherit a BaseClass and create 
a Template, which you can see examples in ./src/*.py, so it might be insufficient for you. 
Also, I might need to make some exercise to remember OOP best practices.



