# 💇 Salon Scheduling Copilot (PRJ-012)

## 📌 Description

A full-stack salon booking system that allows users to schedule services, manage bookings, and view availability. Built using FastAPI, PostgreSQL (Supabase), and React.

---

## 🚀 Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL (Supabase)
* **Frontend:** React
* **ORM:** SQLAlchemy

---

# ✅ Week 1 Implementation

## 🔹 Features

* Database setup (users, services, bookings tables)
* Sample data insertion
* FastAPI backend with CRUD APIs:

  * GET `/services`
  * POST `/book`
  * GET `/bookings`
  * PUT `/book/{id}`
  * DELETE `/book/{id}`
* Basic React UI:

  * Booking form
  * Services display
  * Booking list

## 🔹 Testing

* API tested using Swagger (`/docs`)
* CRUD operations verified
* Database insert & fetch validated
* Basic form validation implemented

---

# ✅ Week 2 Implementation

## 🔹 Core Logic

* Slot Availability Engine (prevents double booking)
* Date Validation (no past bookings)
* Input Validation (valid user/service)

## 🔹 Filter APIs

* GET `/bookings/date/{date}`
* GET `/bookings/user/{user_id}`
* GET `/bookings/service/{service_id}`

## 🔹 Analytics

* GET `/analytics`

  * Total bookings
  * Most popular service

## 🔹 Recommendation (Copilot Feature)

* GET `/recommend`

  * Suggests most frequently booked service

## 🔹 Testing

* Slot conflict tested
* Validation scenarios verified
* Filter APIs tested
* Analytics & recommendation verified

---

## 📡 API Endpoints

### Core APIs

* GET `/services`
* POST `/book`
* GET `/bookings`
* PUT `/book/{id}`
* DELETE `/book/{id}`

### Advanced APIs (Week 2)

* GET `/bookings/date/{date}`
* GET `/bookings/user/{user_id}`
* GET `/bookings/service/{service_id}`
* GET `/analytics`
* GET `/recommend`

---

## ⚙️ Setup Instructions

### 🔹 Backend

```bash
cd backend
pip install fastapi uvicorn sqlalchemy psycopg2-binary
py -m uvicorn main:app --port 8001 --reload
```

### 🔹 Frontend

```bash
cd frontend
npm install
npm start

---

## 🎯 Project Status

* Week 1: ✅ Completed
* Week 2: ✅ Completed


---

## 👩‍💻 Author

**HANUMITHAA GNANAVELU**
