import mysql.connector
import warnings
import pandas as pd
from tabulate import tabulate
from funcoes import classes as c, s
from datetime import date
import numpy as np


#conexão BD
global Conn
Conn = mysql.connector.connect(host='localhost', database='cf', user='root', password=s.pa())

global Cursor
Cursor = Conn.cursor()

global Cursor2
Cursor2 = Conn.cursor(buffered=True)

def d_pag(data):
    a = data
    b = str(data)
    c = int(b[0:4])
    pagamento = ""
    if a[5:7] == "01":
        pagamento = f"{c}-02-01"
    elif a[5:7] == "02":
        pagamento = f"{c}-03-01"
    elif a[5:7] == "03":
        pagamento = f"{c}-04-01"
    elif a[5:7] == "04":
        pagamento = f"{c}-05-01"
    elif a[5:7] == "05":
        pagamento = f"{c}-06-01"
    elif a[5:7] == "06":
        pagamento = f"{c}-07-01"
    elif a[5:7] == "07":
        pagamento = f"{c}-08-01"
    elif a[5:7] == "08":
        pagamento = f"{c}-09-01"
    elif a[5:7] == "09":
        pagamento = f"{c}-10-01"
    elif a[5:7] == "10":
        pagamento = f"{c}-11-01"
    elif a[5:7] == "11":
        pagamento = f"{c}-12-01"
    elif a[5:7] == "12":
        pagamento = f"{c+1}-01-01"
    return pagamento

def c_pag(data):
    c_pagamento = 0
    if data[5:7] == "11":
        c_pagamento += 11
    elif data[5:7] == "12":
        c_pagamento += 10
    elif data[5:7] == "01":
        c_pagamento += 10
    elif data[5:7] == "02":
        c_pagamento += 9
    elif data[5:7] == "03":
        c_pagamento += 8
    elif data[5:7] == "04":
        c_pagamento += 7
    elif data[5:7] == "05":
        c_pagamento += 6
    elif data[5:7] == "06":
        c_pagamento += 5
    elif data[5:7] == "07":
        c_pagamento += 4
    elif data[5:7] == "08":
        c_pagamento += 3
    elif data[5:7] == "09":
        c_pagamento += 2
    elif data[5:7] == "10":
        c_pagamento += 1
    return c_pagamento

#envia para o BD os dados inputados como despesa fixa
def set_desp_fixa():
    query = f"""INSERT INTO cf.desp_fixa(finalidade, novembro_2022, dezembro_2022, janeiro_2023, 
            fevereiro_2023, marco_2023, abril_2023, maio_2023, junho_2023, julho_2023, agosto_2023, setembro_2023, outubro_2023, novembro_2023)
            VALUES ("{c.desp_fixa.finalidade}", "{c.desp_fixa.novembro_2022}","{c.desp_fixa.dezembro_2022}","{c.desp_fixa.janeiro_2023}", "{c.desp_fixa.fevereiro_2023}", "{c.desp_fixa.marco_2023}",
             "{c.desp_fixa.abril_2023}", "{c.desp_fixa.maio_2023}", "{c.desp_fixa.junho_2023}", "{c.desp_fixa.julho_2023}",
             "{c.desp_fixa.agosto_2023}", "{c.desp_fixa.setembro_2023}", "{c.desp_fixa.outubro_2023}", "{c.desp_fixa.novembro_2023}")"""
    Cursor.execute(query)
    Conn.commit()
    #total_geral()
    return Conn.commit()

#envia para o BD os dados inputados como cartões novos.
def set_cartao():
    query = f"""INSERT INTO cf.cartao(catao, banco_finan, limite)
            VALUES ("{c.cartao.cartao}","{c.cartao.banco_finan}", "{c.cartao.limite}")"""
    Cursor.execute(query)
    Conn.commit()
    return Conn.commit()

#envia para o BD os dados inputados como despesa variavel.
def set_desp_var():
    query = f"""INSERT INTO cf.desp_var(finalidade, cartao, parcelas, valor, novembro_2022, dezembro_2022, janeiro_2023, fevereiro_2023, marco_2023, abril_2023, maio_2023, junho_2023, julho_2023, agosto_2023, setembro_2023, outubro_2023, novembro_2023)
            VALUES ("{c.desp_var.finalidade}","{c.desp_var.cartao}", {c.desp_var.parcelas},"{c.desp_var.valor}", "{c.desp_var.novembro_2022}", "{c.desp_var.dezembro_2022}", "{c.desp_var.janeiro_2023}", "{c.desp_var.fevereiro_2023}", "{c.desp_var.marco_2023}", "{c.desp_var.abril_2023}","{c.desp_var.maio_2023}", "{c.desp_var.junho_2023}", "{c.desp_var.julho_2023}","{c.desp_var.agosto_2023}", "{c.desp_var.setembro_2023}", "{c.desp_var.outubro_2023}", "{c.desp_var.novembro_2023}")"""
    Cursor.execute(query)
    Conn.commit()
    return Conn.commit()

#trás uma lista com os cartões cadastrados.
def get_cart():
    cartoes = []
    query = ("SELECT * FROM cf.cartao")
    Cursor.execute(query)
    for row in Cursor:
        cartoes.append(row[0])
    return cartoes

#função genérica para usar no treeview.
def get_relat(tabela, treeview):
    query = (f"SELECT * FROM {tabela}")
    Cursor.execute(query)
    for i in Cursor:
        treeview.insert("","end", values=i)

#função especifica para retornar os dados consolidados do cartão de crédito para jogar no treeview.
def get_relat_ger_cartoes(tabela, treeview):
    query = (f"SELECT cartao, round(sum(novembro_2022), 2), round(sum(dezembro_2022), 2), round(sum(janeiro_2023), 2), round(sum(fevereiro_2023), 2), round(sum(marco_2023), 2), round(sum(abril_2023), 2), round(sum(maio_2023),2 ), round(sum(junho_2023), 2), round(sum(julho_2023), 2), round(sum(agosto_2023), 2),round(sum(setembro_2023), 2), round(sum(outubro_2023), 2), round(sum(novembro_2023), 2)  FROM desp_var GROUP BY cartao")
    Cursor.execute(query)
    for i in Cursor:
        treeview.insert("","end", values=i)

def get_relat_ger_cartoes_agg_f(treeview):
    query = (f"SELECT finalidade, round(sum(novembro_2022), 2), round(sum(dezembro_2022), 2), round(sum(janeiro_2023), 2), round(sum(fevereiro_2023), 2), round(sum(marco_2023), 2), round(sum(abril_2023), 2), round(sum(maio_2023),2 ), round(sum(junho_2023), 2), round(sum(julho_2023), 2), round(sum(agosto_2023), 2),round(sum(setembro_2023), 2), round(sum(outubro_2023), 2), round(sum(novembro_2023), 2)  FROM desp_var GROUP BY finalidade")
    Cursor.execute(query)
    for i in Cursor:
        treeview.insert("","end", values=i)

def get_relat_ger_fixa(tabela, treeview):
    query = (f"SELECT cartao, sum(novembro_2022), sum(dezembro_2022), sum(janeiro_2023), sum(fevereiro_2023), sum(marco_2023), sum(abril_2023), sum(maio_2023), sum(junho_2023), sum(julho_2023), sum(agosto_2023), sum(setembro_2023), sum(outubro_2023), sum(novembro_2023) FROM desp_var GROUP BY cartao")
    Cursor.execute(query)
    for i in Cursor:
        treeview.insert("","end", values=i)

#trás um dataframe consolidado de gastos gerais agrupados por cartão.
def get_geral_cartao():
    query = ("SELECT cartao, sum(novembro_2022), sum(dezembro_2022), sum(janeiro_2023), sum(fevereiro_2023), sum(marco_2023), sum(abril_2023), sum(maio_2023), sum(junho_2023), sum(julho_2023), sum(agosto_2023), sum(setembro_2023), sum(outubro_2023), sum(novembro_2023) FROM desp_var GROUP BY cartao")
    Cursor.execute(query)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        df = pd.read_sql(query, Conn)
    table = df
    headers = ["cartao", "parcelas", "valor", "novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"]
    print(tabulate(table, headers, showindex=False , tablefmt="pretty"))
    return df

#trás um dataframe com os dados consolidados dos cartões, ou seja, contem os gastos gerais do mês com cartão
def get_soma_cartao():
    query = ("SELECT sum(novembro_2022), sum(dezembro_2022), sum(janeiro_2023), sum(fevereiro_2023), sum(marco_2023), sum(abril_2023), sum(maio_2023), sum(junho_2023), sum(julho_2023), sum(agosto_2023), sum(setembro_2023), sum(outubro_2023), sum(novembro_2023) FROM desp_var as total")
    Cursor.execute(query)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        df = pd.read_sql(query, Conn)
    table = df
    headers = ["Total","novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"]
    print(tabulate(table, headers, showindex=False , tablefmt="pretty"))
    return df

#insere os novos gastos na tabela consolidada de gastos gerais de cartões.
def resumo_cartao():
    total = ""
    nov_22 = 0
    dez_22 = 0
    jan_23 = 0
    fev_23 = 0
    mar_23 = 0
    abr_23 = 0
    mai_23 = 0
    jun_23 = 0
    jul_23 = 0
    ago_23 = 0
    set_23 = 0
    out_23 = 0
    nov_23 = 0    
    query = ("SELECT * FROM cf.total_cartao")
    Cursor2.execute(query)
    teste = []
    for f in Cursor2:
        teste.append(f)
    t = "Total Despesas Variaveis"
    if teste == []:
        query1 = f"""INSERT INTO cf.total_cartao(total, novembro_2022, dezembro_2022, janeiro_2023, fevereiro_2023, marco_2023, abril_2023, maio_2023, junho_2023, julho_2023, agosto_2023, setembro_2023, outubro_2023, novembro_2023)
                VALUES ("{t}", "{c.desp_var.novembro_2022}", "{c.desp_var.dezembro_2022}", "{c.desp_var.janeiro_2023}", "{c.desp_var.fevereiro_2023}", "{c.desp_var.marco_2023}", "{c.desp_var.abril_2023}","{c.desp_var.maio_2023}", "{c.desp_var.junho_2023}", "{c.desp_var.julho_2023}","{c.desp_var.agosto_2023}", "{c.desp_var.setembro_2023}", "{c.desp_var.outubro_2023}","{c.desp_var.novembro_2023}")"""
        Cursor2.execute(query1)
        Conn.commit()
    else:
        query2 = ("SELECT * FROM cf.total_cartao")
        Cursor2.execute(query2)
        for i in Cursor2:
            total = i[0]
            nov_22 = i[1]
            dez_22 = i[2]
            jan_23 = i[3]
            fev_23 = i[4]
            mar_23 = i[5]
            abr_23 = i[6]
            mai_23 = i[7]
            jun_23 = i[8]
            jul_23 = i[9]
            ago_23 = i[10]
            set_23 = i[11]
            out_23 = i[12]
            nov_23 = i[13]
        query2 = (f"UPDATE total_cartao SET novembro_2022 = {c.desp_var.novembro_2022 + nov_22}, dezembro_2022 = {c.desp_var.dezembro_2022 + dez_22}, janeiro_2023 = {c.desp_var.janeiro_2023 + jan_23}, fevereiro_2023 = {c.desp_var.fevereiro_2023 + fev_23}, marco_2023 = {c.desp_var.marco_2023 + mar_23}, abril_2023 = {c.desp_var.abril_2023 + abr_23}, maio_2023 = {c.desp_var.maio_2023 + mai_23}, junho_2023 = {c.desp_var.junho_2023 + jun_23}, julho_2023 = {c.desp_var.junho_2023 + jun_23}, agosto_2023 = {c.desp_var.agosto_2023 + ago_23}, setembro_2023 = {c.desp_var.setembro_2023 + set_23}, outubro_2023 = {c.desp_var.outubro_2023 + out_23}, novembro_2023 = {c.desp_var.novembro_2023 + nov_23}")
        Cursor2.execute(query2)
        Conn.commit()

#insere os novos gastos na tabela consolidada de gastos gerais de despesa fixa.
def resumo_desp_fixa():
    total = ""
    nov_22 = 0
    dez_22 = 0
    jan_23 = 0
    fev_23 = 0
    mar_23 = 0
    abr_23 = 0
    mai_23 = 0
    jun_23 = 0
    jul_23 = 0
    ago_23 = 0
    set_23 = 0
    out_23 = 0
    nov_23 = 0
    query = ("SELECT * FROM cf.total_desp_fix")
    Cursor2.execute(query)
    teste = []
    for f in Cursor2:
        teste.append(f)
    t = "Total Despesa Fixa"
    if teste == []:
        query1 = f"""INSERT INTO cf.total_desp_fix(total,novembro_2022, dezembro_2022, janeiro_2023, fevereiro_2023, marco_2023, abril_2023, maio_2023, junho_2023, julho_2023, agosto_2023, setembro_2023, outubro_2023, novembro_2023)
                VALUES ("{t}", "{c.desp_fixa.novembro_2022}", "{c.desp_fixa.dezembro_2022}", "{c.desp_fixa.janeiro_2023}", "{c.desp_fixa.fevereiro_2023}", "{c.desp_fixa.marco_2023}", "{c.desp_fixa.abril_2023}","{c.desp_fixa.maio_2023}", "{c.desp_fixa.junho_2023}", "{c.desp_fixa.julho_2023}","{c.desp_fixa.agosto_2023}", "{c.desp_fixa.setembro_2023}", "{c.desp_fixa.outubro_2023}","{c.desp_fixa.novembro_2023}")"""
        Cursor2.execute(query1)
        Conn.commit()
    else:
        query2 = ("SELECT * FROM cf.total_desp_fix")
        Cursor2.execute(query2)
        for i in Cursor2:
            #total = i[0]
            nov_22 = i[1]
            dez_22 = i[2]
            jan_23 = i[3]
            fev_23 = i[4]
            mar_23 = i[5]
            abr_23 = i[6]
            mai_23 = i[7]
            jun_23 = i[8]
            jul_23 = i[9]
            ago_23 = i[10]
            set_23 = i[11]
            out_23 = i[12]
            nov_23 = i[13]
        query2 = (f"UPDATE total_desp_fix SET novembro_2022 = {c.desp_fixa.novembro_2022 + nov_22}, dezembro_2022 = {c.desp_fixa.dezembro_2022 + dez_22}, janeiro_2023 = {c.desp_fixa.janeiro_2023 + jan_23}, fevereiro_2023 = {c.desp_fixa.fevereiro_2023 + fev_23}, marco_2023 = {c.desp_fixa.marco_2023 + mar_23}, abril_2023 = {c.desp_fixa.abril_2023 + abr_23}, maio_2023 = {c.desp_fixa.maio_2023 + mai_23}, junho_2023 = {c.desp_fixa.junho_2023 + jun_23}, julho_2023 = {c.desp_fixa.junho_2023 + jun_23}, agosto_2023 = {c.desp_fixa.agosto_2023 + ago_23}, setembro_2023 = {c.desp_fixa.setembro_2023 + set_23}, outubro_2023 = {c.desp_fixa.outubro_2023 + out_23}, novembro_2023 = {c.desp_fixa.novembro_2023 + nov_23}")
        Cursor2.execute(query2)
        Conn.commit()

def total_geral():
    resp = 0
    query = ("SELECT * FROM cf.total_desp_fix")
    Cursor2.execute(query)
    for i in Cursor2:
        global tdfnov_22
        tdfnov_22 = i[1]
        global tdfdez_22
        tdfdez_22 = i[2]
        global tdfjan_23
        tdfjan_23 = i[3]
        global tdffev_23
        tdffev_23 = i[4]
        global tdfmar_23
        tdfmar_23 = i[5]
        global tdfabr_23
        tdfabr_23 = i[6]
        global tdfmai_23
        tdfmai_23 = i[7]
        global tdfjun_23
        tdfjun_23 = i[8]
        global tdfjul_23
        tdfjul_23 = i[9]
        global tdfago_23
        tdfago_23 = i[10]
        global tdfset_23
        tdfset_23 = i[11]
        global tdfout_23
        tdfout_23 = i[12]
        global tdfnov_23
        tdfnov_23 = i[13]
    total_2()

def total_2():
    query = ("SELECT * FROM cf.total_cartao")
    Cursor2.execute(query)
    var_resp = []
    for f in Cursor2:
        var_resp.append(f[1])
    if var_resp == []:
        tdvnov_22 = 0
        tdvdez_22 = 0
        tdvjan_23 = 0
        tdvfev_23 = 0
        tdvmar_23 = 0
        tdvabr_23 = 0
        tdvmai_23 = 0
        tdvjun_23 = 0
        tdvjul_23 = 0
        tdvago_23 = 0
        tdvset_23 = 0
        tdvout_23 = 0
        tdvnov_23 = 0    
    else:
        tdvnov_22 = f[1]
        tdvdez_22 = f[2]
        tdvjan_23 = f[3]
        tdvfev_23 = f[4]
        tdvmar_23 = f[5]
        tdvabr_23 = f[6]
        tdvmai_23 = f[7]
        tdvjun_23 = f[8]
        tdvjul_23 = f[9]
        tdvago_23 = f[10]
        tdvset_23 = f[11]
        tdvout_23 = f[12]
        tdvnov_23 = f[13]

    totnov_22 = tdfnov_22 + tdvnov_22
    totdez_22 = tdfdez_22 + tdvdez_22
    totjan_23 = tdfjan_23 + tdvjan_23
    totfev_23 = tdffev_23 + tdvfev_23
    totmar_23 = tdfmar_23 + tdvmar_23
    totabr_23 = tdfabr_23 + tdvabr_23
    totmai_23 = tdfmai_23 + tdvmai_23
    totjun_23 = tdfjun_23 + tdvjun_23
    totjul_23 = tdfjul_23 + tdvjul_23
    totago_23 = tdfago_23 + tdvago_23
    totset_23 = tdfset_23 + tdvset_23
    totout_23 = tdfout_23 + tdvout_23
    totnov_23 = tdfnov_23 + tdvnov_23

    t = "Total Geral DF + DV"
    result = []
    query4 = ("SELECT * FROM cf.total_geral")
    Cursor2.execute(query4)
    for r in Cursor2:
        result.append(r[0])
    if result == []:
        query5 = f"""INSERT INTO cf.total_geral(total, novembro_2022, dezembro_2022, janeiro_2023, fevereiro_2023, marco_2023, abril_2023, maio_2023, junho_2023, julho_2023, agosto_2023, setembro_2023, outubro_2023, novembro_2023)
                VALUES ("{t}","{totnov_22}", "{totdez_22}", "{totjan_23}", "{totfev_23}", "{totmar_23}", "{totabr_23}","{totmai_23}", "{totjun_23}", "{totjul_23}","{totago_23}", "{totset_23}", "{totout_23}", "{totnov_23}")"""
        Cursor2.execute(query5)
        Conn.commit()
    else:
        query3 = (f"UPDATE cf.total_geral SET total = '{t}', novembro_2022 = {totnov_22}, dezembro_2022 = {totdez_22}, janeiro_2023 = {totjan_23}, fevereiro_2023 = {totfev_23}, marco_2023 = {totmar_23}, abril_2023 = {totabr_23}, maio_2023 = {totmai_23}, junho_2023 = {totjun_23}, julho_2023 = {totjul_23}, agosto_2023 = {totago_23}, setembro_2023 = {totset_23}, outubro_2023 = {totout_23}, novembro_2023 = {totnov_23}")
        Cursor2.execute(query3)
        Conn.commit()

def num_linhas(tabela):
    num = 0
    query = (f"select count(*) from {tabela}")
    Cursor2.execute(query)
    for i in Cursor2:
        num += i[0]
    return num
    
#rodou