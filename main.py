import tkinter
from tkinter import Tk, messagebox, ttk
from tkinter import *
from funcoes import classes as c
from funcoes import functions
from datetime import date


def cadastrar_cartao():
    janela.destroy()

    global c_cartao
    c_cartao = Tk()
    c_cartao.title("Cadastro de cartão")

    label = Label(c_cartao, text="Nome do cartão")
    label.grid(row=1, column=0)

    global c_nome
    c_nome = Entry(c_cartao, width=25)
    c_nome.grid(row=1, column=1)

    label = Label(c_cartao, text="Banco / Financeira")
    label.grid(row=2, column=0)

    global banco_fin
    banco_fin = Entry(c_cartao, width=25)
    banco_fin.grid(row=2, column=1)

    label = Label(c_cartao, text="Limite")
    label.grid(row=3, column=0)

    global limite_c
    limite_c = Entry(c_cartao, width=25)
    limite_c.grid(row=3, column=1)

    botao_env = Button(c_cartao, text="Cadastrar cartão", command=env_cartao, width=25)
    botao_env.grid(row=4, column=1)

    c_cartao.geometry("500x300")


def d_pag():
    a = str(date.today())
    b = str(date.today())
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


def env_cartao():
    c.cartao.cartao = c_nome.get()
    c.cartao.banco_finan = banco_fin.get()
    c.cartao.limite = limite_c.get()
    functions.set_cartao()
    c_cartao.destroy()
    messagebox.showinfo("Retorno", "Ok, cartão cadastrado com sucesso!!")
    tela_inicial()

def cadastrar_desp_fixa():
    janela.destroy()
    global c_d_f
    c_d_f = Tk()
    c_d_f.title("Cadastro de despesa fixa")

    label = Label(c_d_f, text="Finalidade")
    label.grid(row=1, column=0)

    global fin_fixa
    fin_fixa = Entry(c_d_f, width=25)
    fin_fixa.grid(row=1, column=1)

    label = Label(c_d_f, text="Valor")
    label.grid(row=2, column=0)

    global valor_fixa
    valor_fixa = Entry(c_d_f, width=25)
    valor_fixa.grid(row=2, column=1)

    botao_enviar = Button(c_d_f, text="Cadastrar despesa fixa", command=env_desp_fixa)
    botao_enviar.grid(row=3, column=1)

    c_d_f.geometry("500x300")

def d_pag_t():
    a = str(date.today())
    b = a[0:7]
    pag = f"{b}-01"
    return pag

def env_desp_fixa():
    c.desp_fixa.finalidade = fin_fixa.get()
    c.desp_fixa.novembro_2022 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.dezembro_2022 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.janeiro_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.fevereiro_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.marco_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.abril_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.maio_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.junho_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.julho_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.agosto_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.setembro_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.outubro_2023 = round(float(valor_fixa.get()), 2)
    c.desp_fixa.novembro_2023 = round(float(valor_fixa.get()), 2)
    functions.set_desp_fixa()
    functions.resumo_desp_fixa()
    functions.total_geral()
    c_d_f.destroy()
    messagebox.showinfo("Retorno", "Ok, despesa fixa cadastrada com sucesso!!")
    tela_inicial()


def cadastrar_desp_var():
    janela.destroy()

    global c_d_v
    c_d_v = Tk()
    c_d_v.title("Cadastro de despesa variavel")

    label = Label(c_d_v, text="Finalidade")
    label.grid(row=0, column=0)

    global fin_var
    fin_var = Entry(c_d_v, width=25)
    fin_var.grid(row=0, column=1)

    label = Label(c_d_v, text="Cartão", width=25)
    label.grid(row=1, column=0)

    lista_cart = functions.get_cart()

    global car_var
    car_var = ttk.Combobox(c_d_v, values=lista_cart, width=23)
    car_var.grid(row=1, column=1)

    label = Label(c_d_v, text="Parcelas")
    label.grid(row=2, column=0)

    global parcelas
    parcelas = Entry(c_d_v, width=25)
    parcelas.grid(row=2, column=1)

    parc = c_d_v.register(only_int)
    parcelas.config(validate="key", validatecommand=(parc, '%P'))

    label = Label(c_d_v, text="Valor")
    label.grid(row=3, column=0)

    global valor_var
    valor_var = Entry(c_d_v, width=25)
    valor_var.grid(row=3, column=1)

    vl_v = c_d_v.register(only_float)
    valor_var.config(validate="key", validatecommand=(vl_v, "%P"))

    botao_env = Button(c_d_v, text="Cadastrar despesa variavel", command=env_desp_var)
    botao_env.grid(row=4, column=1)

    c_d_v.geometry("500x300")

def env_desp_var():
    c.desp_var.finalidade = fin_var.get()
    c.desp_var.cartao = car_var.get()
    c.desp_var.parcelas = int(parcelas.get())
    c.desp_var.valor = round(float(valor_var.get()), 2)
    valor_parcela = c.desp_var.valor / c.desp_var.parcelas

    c.desp_var.novembro_2022 = round(valor_parcela, 2)
    if c.desp_var.parcelas >= 2:
        c.desp_var.dezembro_2022 = round(valor_parcela, 2)
    else:
        c.desp_var.dezembro_2022 = 0


    if c.desp_var.parcelas >= 3:
        c.desp_var.janeiro_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.janeiro_2023 = 0
    if c.desp_var.parcelas >= 4:
        c.desp_var.fevereiro_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.fevereiro_2023 = 0
    if c.desp_var.parcelas >= 5:
        c.desp_var.marco_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.marco_2023 = 0
    if c.desp_var.parcelas >= 6:
        c.desp_var.abril_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.abril_2023 = 0
    if c.desp_var.parcelas >= 7:
        c.desp_var.maio_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.maio_2023 = 0
    if c.desp_var.parcelas >= 8:
        c.desp_var.junho_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.junho_2023 = 0
    if c.desp_var.parcelas >= 9:
        c.desp_var.julho_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.julho_2023 = 0
    if c.desp_var.parcelas >= 10:
        c.desp_var.agosto_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.agosto_2023 = 0
    if c.desp_var.parcelas >= 11:
        c.desp_var.setembro_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.setembro_2023 = 0
    if c.desp_var.parcelas >= 12:
        c.desp_var.outubro_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.outubro_2023 = 0
    if c.desp_var.parcelas >= 13:
        c.desp_var.novembro_2023 = round(valor_parcela, 2)
    else:
        c.desp_var.novembro_2023 = 0

    functions.set_desp_var()
    functions.resumo_cartao()
    functions.total_geral()
    c_d_v.destroy()
    messagebox.showinfo("Retorno", "Ok, despesa variavel cadastrada com sucesso!!")
    tela_inicial()


def only_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def only_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def b_v_r():
    vis_relat_c.destroy()
    tela_inicial()
    

def vis_relat_c():
    janela.destroy()

    global vis_relat_c
    vis_relat_c = Tk()
    vis_relat_c.title("Extrato despesas variáveis")

    head = Label(vis_relat_c, text="Extrato detalhado agrupado por Finalidade", font=("Arial, 15"))
    head.pack()

    global rdv #relatório despesa variável
    rdv = ttk.Treeview(vis_relat_c, height=functions.num_linhas("relat_cartao"), columns=("finalidade", "novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"), show="headings")
    rdv.column("finalidade", width=160)
    rdv.column("novembro_2022", width=80)
    rdv.column("dezembro_2022", width=80)
    rdv.column("janeiro_2023", width=80)
    rdv.column("fevereiro_2023", width=80)
    rdv.column("marco_2023", width=80)
    rdv.column("abril_2023", width=80)
    rdv.column("maio_2023", width=80)
    rdv.column("junho_2023", width=80)
    rdv.column("julho_2023", width=80)
    rdv.column("agosto_2023", width=80)
    rdv.column("setembro_2023", width=80)
    rdv.column("outubro_2023", width=80)
    rdv.column("novembro_2023", width=80)
    rdv.heading("finalidade", text="Finalidade")
    rdv.heading("novembro_2022", text="nov/2022")
    rdv.heading("dezembro_2022", text="dez/2022")
    rdv.heading("janeiro_2023", text="jan/2023")
    rdv.heading("fevereiro_2023", text="fev/2023")
    rdv.heading("marco_2023", text="mar/2023")
    rdv.heading("abril_2023", text="abr/2023")
    rdv.heading("maio_2023", text="mai/2023")
    rdv.heading("junho_2023", text="jun/2023")
    rdv.heading("julho_2023", text="jul/2023")
    rdv.heading("agosto_2023", text="ago/2023")
    rdv.heading("setembro_2023", text="set/2023")
    rdv.heading("outubro_2023", text="out/2023")
    rdv.heading("novembro_2023", text="nov/2023")
    rdv.pack()
    functions.get_relat_ger_cartoes_agg_f(rdv)

    head2 = Label(vis_relat_c, text="Extrato detalhado sem agrupamento", font=("Arial, 15"))
    head2.pack()

    global rdv2 #relatório despesa variável
    rdv2 = ttk.Treeview(vis_relat_c, height=functions.num_linhas("desp_var"), columns=("finalidade", "novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"), show="headings")
    rdv2.column("finalidade", width=160)
    rdv2.column("novembro_2022", width=80)
    rdv2.column("dezembro_2022", width=80)
    rdv2.column("janeiro_2023", width=80)
    rdv2.column("fevereiro_2023", width=80)
    rdv2.column("marco_2023", width=80)
    rdv2.column("abril_2023", width=80)
    rdv2.column("maio_2023", width=80)
    rdv2.column("junho_2023", width=80)
    rdv2.column("julho_2023", width=80)
    rdv2.column("agosto_2023", width=80)
    rdv2.column("setembro_2023", width=80)
    rdv2.column("outubro_2023", width=80)
    rdv2.column("novembro_2023", width=80)
    rdv2.heading("finalidade", text="Finalidade")
    rdv2.heading("novembro_2022", text="nov/2022")
    rdv2.heading("dezembro_2022", text="dez/2022")
    rdv2.heading("janeiro_2023", text="jan/2023")
    rdv2.heading("fevereiro_2023", text="fev/2023")
    rdv2.heading("marco_2023", text="mar/2023")
    rdv2.heading("abril_2023", text="abr/2023")
    rdv2.heading("maio_2023", text="mai/2023")
    rdv2.heading("junho_2023", text="jun/2023")
    rdv2.heading("julho_2023", text="jul/2023")
    rdv2.heading("agosto_2023", text="ago/2023")
    rdv2.heading("setembro_2023", text="set/2023")
    rdv2.heading("outubro_2023", text="out/2023")
    rdv2.heading("novembro_2023", text="nov/2023")
    rdv2.pack()
    functions.get_relat("desp_var", rdv2)

    botao_voltar = Button(vis_relat_c, text="Voltar", command=b_v_r)
    botao_voltar.pack()

    vis_relat_c.geometry("1500x1500")

def tela_inicial():
    global janela
    janela = Tk()
    janela.title("Controle financeiro")

    head = Label(janela, text="Controle Financeiro", font=("Arial", 15))
    head.pack()

    cad_desp_fix = Button(janela, text="Cadastrar despesa fixa", width=40, command=cadastrar_desp_fixa)
    cad_desp_fix.pack()

    cad_desp_var = Button(janela, text="Cadastrar despesa variavel", width=40, command=cadastrar_desp_var)
    cad_desp_var.pack()

    cad_cart = Button(janela, text="Cadastrar cartão", width=40, command=cadastrar_cartao)
    cad_cart.pack()

    vis_cart_r = Button(janela, text="Extrato despesa variável", width=40, command=vis_relat_c)
    vis_cart_r.pack()

    global tvdf
    tvdf = ttk.Treeview(janela, height=functions.num_linhas("desp_fixa"), columns=("finalidade", "novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"), show="headings")
    tvdf.column("finalidade", width=160)
    tvdf.column("novembro_2022", width=80)
    tvdf.column("dezembro_2022", width=80)
    tvdf.column("janeiro_2023", width=80)
    tvdf.column("fevereiro_2023", width=80)
    tvdf.column("marco_2023", width=80)
    tvdf.column("abril_2023", width=80)
    tvdf.column("maio_2023", width=80)
    tvdf.column("junho_2023", width=80)
    tvdf.column("julho_2023", width=80)
    tvdf.column("agosto_2023", width=80)
    tvdf.column("setembro_2023", width=80)
    tvdf.column("outubro_2023", width=80)
    tvdf.column("novembro_2023", width=80)
    tvdf.heading("finalidade", text="Finalidade")
    tvdf.heading("novembro_2022", text="nov/2022")
    tvdf.heading("dezembro_2022", text="dez/2022")
    tvdf.heading("janeiro_2023", text="jan/2023")
    tvdf.heading("fevereiro_2023", text="fev/2023")
    tvdf.heading("marco_2023", text="mar/2023")
    tvdf.heading("abril_2023", text="abr/2023")
    tvdf.heading("maio_2023", text="mai/2023")
    tvdf.heading("junho_2023", text="jun/2023")
    tvdf.heading("julho_2023", text="jul/2023")
    tvdf.heading("agosto_2023", text="ago/2023")
    tvdf.heading("setembro_2023", text="set/2023")
    tvdf.heading("outubro_2023", text="out/2023")
    tvdf.heading("novembro_2023", text="nov/2023")
    tvdf.pack()
    functions.get_relat("desp_fixa", tvdf)

    global tvdv
    tvdv = ttk.Treeview(janela, height=1, columns=("total","novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"), show="headings")
    tvdv.column("total", width=160)
    tvdv.column("novembro_2022", width=80)
    tvdv.column("dezembro_2022", width=80)
    tvdv.column("janeiro_2023", width=80)
    tvdv.column("fevereiro_2023", width=80)
    tvdv.column("marco_2023", width=80)
    tvdv.column("abril_2023", width=80)
    tvdv.column("maio_2023", width=80)
    tvdv.column("junho_2023", width=80)
    tvdv.column("julho_2023", width=80)
    tvdv.column("agosto_2023", width=80)
    tvdv.column("setembro_2023", width=80)
    tvdv.column("outubro_2023", width=80)
    tvdv.column("novembro_2023", width=80)
    tvdv.heading("total", text="-")
    tvdv.heading("novembro_2022", text="-")
    tvdv.heading("dezembro_2022", text="-")
    tvdv.heading("janeiro_2023", text="-")
    tvdv.heading("fevereiro_2023", text="-")
    tvdv.heading("marco_2023", text="-")
    tvdv.heading("abril_2023", text="-")
    tvdv.heading("maio_2023", text="-")
    tvdv.heading("junho_2023", text="-")
    tvdv.heading("julho_2023", text="-")
    tvdv.heading("agosto_2023", text="-")
    tvdv.heading("setembro_2023", text="-")
    tvdv.heading("outubro_2023", text="-")
    tvdv.heading("novembro_2023", text="-")
    tvdv.pack()
    functions.get_relat("total_desp_fix", tvdv)

    global dvg #despesa variável geral
    dvg = ttk.Treeview(janela, height=functions.num_linhas("cartoes_agrupados"), columns=("cartao", "novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"), show="headings")
    dvg.column("cartao", width=160)
    dvg.column("novembro_2022", width=80)
    dvg.column("dezembro_2022", width=80)
    dvg.column("janeiro_2023", width=80)
    dvg.column("fevereiro_2023", width=80)
    dvg.column("marco_2023", width=80)
    dvg.column("abril_2023", width=80)
    dvg.column("maio_2023", width=80)
    dvg.column("junho_2023", width=80)
    dvg.column("julho_2023", width=80)
    dvg.column("agosto_2023", width=80)
    dvg.column("setembro_2023", width=80)
    dvg.column("outubro_2023", width=80)
    dvg.column("novembro_2023", width=80)
    dvg.heading("cartao", text="")
    dvg.heading("novembro_2022", text="-")
    dvg.heading("dezembro_2022", text="-")
    dvg.heading("janeiro_2023", text="-")
    dvg.heading("fevereiro_2023", text="-")
    dvg.heading("marco_2023", text="-")
    dvg.heading("abril_2023", text="-")
    dvg.heading("maio_2023", text="-")
    dvg.heading("junho_2023", text="-")
    dvg.heading("julho_2023", text="-")
    dvg.heading("agosto_2023", text="-")
    dvg.heading("setembro_2023", text="-")
    dvg.heading("outubro_2023", text="-")
    dvg.heading("novembro_2023", text="-")
    dvg.pack()
    functions.get_relat_ger_cartoes("desp_var", dvg)

    global tdv #total de despesa variavel
    tdv = ttk.Treeview(janela, height=1 ,columns=("total", "novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"), show="headings")
    tdv.column("total", width=160)
    tdv.column("novembro_2022", width=80)
    tdv.column("dezembro_2022", width=80)
    tdv.column("janeiro_2023", width=80)
    tdv.column("fevereiro_2023", width=80)
    tdv.column("marco_2023", width=80)
    tdv.column("abril_2023", width=80)
    tdv.column("maio_2023", width=80)
    tdv.column("junho_2023", width=80)
    tdv.column("julho_2023", width=80)
    tdv.column("agosto_2023", width=80)
    tdv.column("setembro_2023", width=80)
    tdv.column("outubro_2023", width=80)
    tdv.column("novembro_2023", width=80)
    tdv.heading("total", text="-")
    tdv.heading("novembro_2022", text="-")
    tdv.heading("dezembro_2022", text="-")
    tdv.heading("janeiro_2023", text="-")
    tdv.heading("fevereiro_2023", text="-")
    tdv.heading("marco_2023", text="-")
    tdv.heading("abril_2023", text="-")
    tdv.heading("maio_2023", text="-")
    tdv.heading("junho_2023", text="-")
    tdv.heading("julho_2023", text="-")
    tdv.heading("agosto_2023", text="-")
    tdv.heading("setembro_2023", text="-")
    tdv.heading("outubro_2023", text="-")
    tdv.heading("novembro_2023", text="-")
    tdv.pack()
    functions.get_relat("total_cartao", tdv)

    global tdg #total geral de despesas
    tdg = ttk.Treeview(janela, height=1 ,columns=("total", "novembro_2022", "dezembro_2022", "janeiro_2023","fevereiro_2023", "marco_2023", "abril_2023", "maio_2023", "junho_2023", "julho_2023", "agosto_2023", "setembro_2023", "outubro_2023", "novembro_2023"), show="headings")
    tdg.column("total", width=160)
    tdg.column("novembro_2022", width=80)
    tdg.column("dezembro_2022", width=80)
    tdg.column("janeiro_2023", width=80)
    tdg.column("fevereiro_2023", width=80)
    tdg.column("marco_2023", width=80)
    tdg.column("abril_2023", width=80)
    tdg.column("maio_2023", width=80)
    tdg.column("junho_2023", width=80)
    tdg.column("julho_2023", width=80)
    tdg.column("agosto_2023", width=80)
    tdg.column("setembro_2023", width=80)
    tdg.column("outubro_2023", width=80)
    tdg.column("novembro_2023", width=80)
    tdg.heading("total", text="-")
    tdg.heading("novembro_2022", text="")
    tdg.heading("dezembro_2022", text="-")
    tdg.heading("janeiro_2023", text="-")
    tdg.heading("fevereiro_2023", text="-")
    tdg.heading("marco_2023", text="-")
    tdg.heading("abril_2023", text="-")
    tdg.heading("maio_2023", text="-")
    tdg.heading("junho_2023", text="-")
    tdg.heading("julho_2023", text="-")
    tdg.heading("agosto_2023", text="-")
    tdg.heading("setembro_2023", text="-")
    tdg.heading("outubro_2023", text="-")
    tdg.heading("novembro_2023", text="-")
    tdg.pack()
    functions.get_relat("total_geral", tdg)

    janela.geometry("1500x1500")

    janela.mainloop()

tela_inicial()

#rodou