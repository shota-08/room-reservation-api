from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 同じディレクトリにDB作成
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# インスタンス
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # 接続設定
Base = declarative_base() # クラスの継承
