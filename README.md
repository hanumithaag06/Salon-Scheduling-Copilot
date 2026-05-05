# Salon Scheduling Copilot

## Description
A full-stack booking system for salon services using FastAPI, PostgreSQL (Supabase), and React.

## Features (Week 1)
- View services
- Create booking
- View bookings
- Update & delete booking
- React UI to display services

## Tech Stack
- FastAPI (Backend)
- PostgreSQL / Supabase (Database)
- React (Frontend)

## How to Run

### Backend
cd backend  
py -m uvicorn main:app --port 8001  

### Frontend
cd frontend  
npm start  

## API Endpoints
- GET /services  
- POST /book  
- GET /bookings  
- PUT /book/{id}  
- DELETE /book/{id}