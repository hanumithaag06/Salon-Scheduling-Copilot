from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres.xbksvdahrfwzholglnbs:hanusuha%400910@aws-1-ap-northeast-1.pooler.supabase.com:6543/postgres?sslmode=require"

engine = create_engine(DATABASE_URL)