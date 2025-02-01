import sqlite3

conn = sqlite3.connect("database/itids.db")
cursor = conn.cursor()

# Создаем таблицу станций
cursor.execute("""
CREATE TABLE IF NOT EXISTS Stations (
    StationID INTEGER PRIMARY KEY AUTOINCREMENT,
    NameEn TEXT NOT NULL,
    NameFr TEXT NOT NULL,
    Zone TEXT NOT NULL,
    Connects TEXT NOT NULL
)
""")

# Создаем таблицу маршрутов
cursor.execute("""
CREATE TABLE IF NOT EXISTS Routes (
    RouteID INTEGER PRIMARY KEY AUTOINCREMENT,
    TrainNumber TEXT NOT NULL,
    FromStationID INTEGER,
    ToStationID INTEGER,
    FOREIGN KEY (FromStationID) REFERENCES Stations(StationID),
    FOREIGN KEY (ToStationID) REFERENCES Stations(StationID)
)
""")

# Создаем таблицу соединений
cursor.execute("""
CREATE TABLE IF NOT EXISTS Connections (
    ConnID INTEGER PRIMARY KEY AUTOINCREMENT,
    LogoLocation TEXT,
    ConnName TEXT
)
""")

# Создаем таблицу связей между станциями и соединениями
cursor.execute("""
CREATE TABLE IF NOT EXISTS StationConnections (
    StationID INTEGER,
    ConnectionID INTEGER,
    PRIMARY KEY (StationID, ConnectionID),
    FOREIGN KEY (StationID) REFERENCES Stations(StationID),
    FOREIGN KEY (ConnectionID) REFERENCES Connections(ConnID)
)
""")

cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Waterfront", "Waterfront", "M", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Burrard", "Burrard", "M", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Granville", "Granville", "M", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Stadium-Chinatown", "Stadium-Chinatown", "M", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Main Street-Science World", "Main Street-Science World", "1", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Commercial-Broadway", "Commercial-Broadway", "1", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Nanaimo", "Nanaimo", "1", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("29th Avenue", "29th Avenue", "1", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Joyce-Collingwood", "Joyce-Collingwood", "1", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Patterson", "Patterson", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Metrotown", "Metrotown", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Royal Oak", "Royal Oak", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Edmonds", "Edmonds", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("22nd Street", "22nd Street", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("New Westminster", "New Westminster", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Columbia", "Columbia", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Scott Road", "Scott Road", "3", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Gateway", "Gateway", "3", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Surrey Central", "Surrey Central", "3", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("King George", "King George", "3", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Sapperton", "Sapperton", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Braid", "Braid", "2", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Lougheed Town Centre", "Lougheed Town Centre", "3", "SkyTrain"))
cursor.execute("INSERT INTO Stations (NameEn, NameFr, Zone, Connects) VALUES (?, ?, ?, ?)", 
            ("Production Way-University", "Production Way-University", "3", "SkyTrain"))

conn.commit()
conn.close()