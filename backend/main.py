from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import text
from database import engine
from datetime import datetime

app = FastAPI()

# CORS (for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------- MODEL ---------
class Booking(BaseModel):
    user_id: int
    service_id: int
    date: str
    time_slot: str
    status: str

# --------- ROUTES ---------

# Home
@app.get("/")
def home():
    return {"message": "Backend connected"}

# Get services
@app.get("/services")
def get_services():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM services"))
        return [dict(row._mapping) for row in result]

# Create booking (WITH VALIDATION + SLOT CHECK)
@app.post("/book")
def create_booking(booking: Booking):
    with engine.connect() as conn:

        # 🔹 1. Validate date (no past booking)
        today = datetime.now().date()
        booking_date = datetime.strptime(booking.date, "%Y-%m-%d").date()

        if booking_date < today:
            return {"error": "Cannot book past dates"}

        # 🔹 2. Basic validation
        if not booking.user_id or not booking.service_id:
            return {"error": "Invalid user or service"}

        # 🔹 3. Slot availability check
        check = conn.execute(
            text("""
                SELECT * FROM bookings
                WHERE date = :date AND time_slot = :time_slot
            """),
            {"date": booking.date, "time_slot": booking.time_slot}
        ).fetchone()

        if check:
            return {"error": "Slot already booked"}

        # 🔹 4. Insert booking
        conn.execute(
            text("""
                INSERT INTO bookings (user_id, service_id, date, time_slot, status)
                VALUES (:user_id, :service_id, :date, :time_slot, :status)
            """),
            booking.dict()
        )
        conn.commit()

    return {"message": "Booking confirmed"}

# Get all bookings
@app.get("/bookings")
def get_bookings():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM bookings"))
        return [dict(row._mapping) for row in result]

@app.get("/bookings/date/{date}")
def get_bookings_by_date(date: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM bookings WHERE date = :date"),
            {"date": date}
        )
        return [dict(row._mapping) for row in result]

@app.get("/bookings/user/{user_id}")
def get_bookings_by_user(user_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM bookings WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        return [dict(row._mapping) for row in result]

@app.get("/bookings/service/{service_id}")
def get_bookings_by_service(service_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM bookings WHERE service_id = :service_id"),
            {"service_id": service_id}
        )
        return [dict(row._mapping) for row in result]

# Update booking
@app.put("/book/{id}")
def update_booking(id: int, status: str):
    with engine.connect() as conn:
        conn.execute(
            text("UPDATE bookings SET status = :status WHERE id = :id"),
            {"id": id, "status": status}
        )
        conn.commit()
    return {"message": "Booking updated"}

# Delete booking
@app.delete("/book/{id}")
def delete_booking(id: int):
    with engine.connect() as conn:
        conn.execute(
            text("DELETE FROM bookings WHERE id = :id"),
            {"id": id}
        )
        conn.commit()
    return {"message": "Booking deleted"}

@app.get("/analytics")
def get_analytics():
    with engine.connect() as conn:

        # Total bookings
        total = conn.execute(
            text("SELECT COUNT(*) FROM bookings")
        ).scalar()

        # Most popular service
        popular = conn.execute(
            text("""
                SELECT service_id, COUNT(*) as count
                FROM bookings
                GROUP BY service_id
                ORDER BY count DESC
                LIMIT 1
            """)
        ).fetchone()

    return {
        "total_bookings": total,
        "most_popular_service": dict(popular._mapping) if popular else None
    }

@app.get("/recommend")
def recommend_service():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT service_id, COUNT(*) as count
                FROM bookings
                GROUP BY service_id
                ORDER BY count DESC
                LIMIT 1
            """)
        ).fetchone()

    if result:
        return {
            "recommended_service_id": result.service_id,
            "reason": "Most frequently booked service"
        }

    return {"message": "No data available"}