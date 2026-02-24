from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CarrierProfile(Base):
    __tablename__ = 'carrier_profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    rating = Column(Float)

    def __repr__(self):
        return f'<CarrierProfile(name={self.name}, contact_info={self.contact_info}, rating={self.rating})>'

class Load(Base):
    __tablename__ = 'loads'

    id = Column(Integer, primary_key=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    weight = Column(Float)
    volume = Column(Float)
    cargo_value = Column(Float)

    def __repr__(self):
        return f'<Load(origin={self.origin}, destination={self.destination}, weight={self.weight}, volume={self.volume}, cargo_value={self.cargo_value})>'

class ProfitabilityCalculation(Base):
    __tablename__ = 'profitability_calculations'

    id = Column(Integer, primary_key=True)
    load_id = Column(Integer, nullable=False)
    carrier_id = Column(Integer, nullable=False)
    cost = Column(Float)
    revenue = Column(Float)
    profit = Column(Float)

    def __repr__(self):
        return f'<ProfitabilityCalculation(load_id={self.load_id}, carrier_id={self.carrier_id}, cost={self.cost}, revenue={self.revenue}, profit={self.profit})>'

# Create engine
# engine = create_engine('sqlite:///load_optimization.db')
# Base.metadata.create_all(engine)

# Session setup
# Session = sessionmaker(bind=engine)
# session = Session()