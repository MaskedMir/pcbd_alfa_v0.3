import sqlite3


def mb_db(cpu, price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM motherboard '
                f'WHERE (price <= {price_max})'
                f'AND (price >=  {price_min})'
                f'AND ((SELECT cpu.chipset FROM cpu WHERE cpu.name = "{cpu[0]}") = motherboard.chipset)')
    selection = cur.fetchall()

    return selection


def ps_db(power, price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM ps '
                f'WHERE (price <= {price_max})'
                f'AND (price >=  {price_min})'
                f'AND (power >= {power})')
    selection = cur.fetchall()

    return selection


def db_sel(table, price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()
    selection = None
    if table == "cpu":
        cur.execute(f'SELECT * FROM cpu '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "gpu":
        cur.execute(f'SELECT * FROM gpu '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "psd":
        cur.execute(f'SELECT * FROM psd '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "ram":
        cur.execute(f'SELECT * FROM ram '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    return selection

