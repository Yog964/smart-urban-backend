import psycopg2
import urllib.parse
password = urllib.parse.quote_plus("Sushant@2026")
conn = psycopg2.connect(f"postgresql://postgres.vzvyjryvryggevkuumhm:{password}@aws-1-ap-northeast-2.pooler.supabase.com:6543/postgres")
cur = conn.cursor()
cur.execute("SELECT id, title, length(image_url), substring(image_url from 1 for 100) FROM complaints ORDER BY id DESC LIMIT 5;")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
