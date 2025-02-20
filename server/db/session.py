from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from decouple import config


engine = create_async_engine(config('DATABASE_URL'), future=True, echo=True)
SessionLocal = async_sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    async with SessionLocal() as session:
        yield session