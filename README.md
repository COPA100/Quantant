# Quantly

Goal:
Quantly is a hybrid Python/C++ tool that analyzes a stock portfolio’s historical performance and risk metrics. Users upload a CSV file of their portfolio, which is parsed and stored in a database with JWT-secured authentication. Historical stock data is fetched via the Yahoo Finance API, and performance metrics are computed efficiently in C++ before being returned to the frontend for visualization.

This is going to take a while to learn/make, but my plan of attack is to create the backend first and then connect it to the frontend with FastAPI. Also, I am using pybind to combine the C++ and python together. C++ makes more sense to utilize for more complex calculations and when scaled to many users.

I’m excited to build this project because the vast amount of stock data opens the door to advanced analytics, algorithmic modeling, and scalable performance insights. I have been investing recently too, so making a tool that can help with that is something I am very passionate about.

Frontend:
React, TypeScript, Tailwind

Backend:
C++, Python, SQL (SQLite for dev, PostgreSQL for prod), pandas, numpy, FastAPI
