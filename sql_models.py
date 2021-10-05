
from datetime import date, datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Time, Numeric, Date, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column, intersect
from sqlalchemy.sql.functions import char_length, current_date
from sqlalchemy.sql.sqltypes import CHAR, JSON, TEXT, TIMESTAMP, Float, Text
from app.database.db import Base


class Annexure_B(Base):
    __tablename__ = "annexure_b"

    id = Column(BigInteger, primary_key=True, index=True)
    organisation_id = Column(BigInteger)
    week = Column(BigInteger)
    brand_id = Column(BigInteger)
    datetime = Column(Date)
    detailed_json = Column(JSON)
    created_datetime = Column(TIMESTAMP)
    merchant_id = Column(CHAR)
    service_range = Column(Text)
    outlet_name = Column(CHAR)
    type = Column(CHAR)

class Aggregator_Payment_Details():
    __tablename__ = "aggregator_payment_details"

    created_datetime = Column(TIMESTAMP)
    organisation_id = Column(BigInteger)
    brand_id = Column(BigInteger)
    start_date = Column(Date)
    detailed_json = Column(JSON)
    id = Column(BigInteger, primary_key=True, index=True)
    datetime = Column(Date)
    merchant_id = Column(CHAR)
    outlet_name = Column(CHAR)
    type = Column(CHAR)

class App_Users():
    __tablename__ = "app_users"

    pk_app_users = Column(BigInteger, primary_key=True, index=True)
    fk_organisations = Column(Integer)
    fk_brands = Column(Integer)
    phone = Column(Numeric)
    is_deleted = Column(Boolean)
    pk_app_users_web = Column(Integer)
    session_json = Column(JSON)
    token = Column(CHAR)
    activation_key = Column(CHAR)
    gcm_id = Column(Text)
    session_token = Column(CHAR)
    fcm_id = Column(CHAR)
    address = Column(Text)
    email = Column(CHAR)
    user_type = Column(CHAR)
    username = Column(CHAR)
    password = Column(CHAR)

class Brands():
    __tablename__ = "brands"

    no_of_kiosks = Column(Integer)
    fk_organisations = Column(Integer)
    is_kiosk_enabled = Column(Integer)
    pk_brands = Column(BigInteger, primary_key=True, index=True)
    no_of_outlets = Column(Integer)
    amount = Column(Integer)
    phone = Column(BigInteger)
    fk_countries = Column(Integer)
    fk_states = Column(Integer)
    fk_cities = Column(Integer)
    creation_time = Column(TIMESTAMP)
    is_deleted = Column(Boolean)
    no_manager_app = Column(Integer)
    active_manager_app = Column(Integer)
    no_captain_app = Column(Integer)
    active_captain_app = Column(Integer)
    brand_name = Column(CHAR)
    email = Column(CHAR)

class Organisations():
    __tablename__ = "organisations"

    phone = Column(BigInteger)
    pk_organisations = Column(BigInteger, primary_key=True, index=True)
    creation_time =Column(TIMESTAMP)
    is_deleted = Column(Boolean)
    Organisation_name = Column(CHAR)
    email = Column(CHAR)
    address = Column(Text)

class Payload_Validation():
    __tablename__ = "payload_validation"

    week = Column(BigInteger)
    organisation_id = Column(BigInteger)
    brand_id = Column(BigInteger)
    datetime = Column(Date)
    detailed_json = Column(JSON)
    created_datetime = Column(TIMESTAMP)
    id = Column(BigInteger, primary_key=True, index = True)
    merchant_id = Column(CHAR)
    service_range = Column(TEXT)
    outlet_name = Column(CHAR)
    type = Column(CHAR)

class Remittence_Bank_Statement():
    __tablename__ = "remittence_bank_statement"

    settlement_date = Column(Date)
    organisation_id = Column(Integer)
    brand_id = Column(Integer)
    amount = Column(Float)
    created_datetime = Column(TIMESTAMP)
    datetime = Column(Date)
    detailed_json = Column(JSON)
    bank_amount = Column(Float)
    difference_amount = Column(Float)
    id = Column(BigInteger, primary_key=True,index=True)
    merchant_id = Column(CHAR)
    outlet_name = Column(CHAR)
    reference_number = Column(CHAR)
    service_range = Column(Text)
    account = Column(CHAR)
    type = Column(CHAR)
    week = Column(CHAR)

class Users():
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index= True)
    created_datetime =Column(TIMESTAMP)
    assigned_hub = Column(Integer)
    name = Column(CHAR)
    user_type = Column(CHAR)
