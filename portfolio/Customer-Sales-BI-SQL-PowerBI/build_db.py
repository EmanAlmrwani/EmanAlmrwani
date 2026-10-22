"""Build a local SQLite database from a synthetic CSV sample."""
from pathlib import Path
import csv,sqlite3
root=Path(__file__).resolve().parent
with (root/'data'/'synthetic_orders.csv').open(newline='') as f: rows=list(csv.DictReader(f))
with sqlite3.connect(root/'sales_demo.sqlite') as con:
    con.execute('CREATE TABLE IF NOT EXISTS orders(order_id TEXT PRIMARY KEY,order_date TEXT,customer_id TEXT,product TEXT,category TEXT,region TEXT,quantity INTEGER,unit_price_sar REAL,discount_rate REAL,order_status TEXT)')
    con.executemany('INSERT OR REPLACE INTO orders VALUES (?,?,?,?,?,?,?,?,?,?)',[(x['order_id'],x['order_date'],x['customer_id'],x['product'],x['category'],x['region'],int(x['quantity']),float(x['unit_price_sar']),float(x['discount_rate']),x['order_status']) for x in rows])
print(f'Loaded {len(rows)} synthetic orders')
