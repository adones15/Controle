from dataclasses import dataclass

@dataclass
class desp_fixa:
    finalidade: str
    novembro_2022: str
    dezembro_2022: str
    janeiro_2023: str
    fevereiro_2023: str
    marco_2023: str
    abril_2023: str
    maio_2023: str
    junho_2023: str
    julho_2023: str
    agosto_2023: str
    setembro_2023: str
    outubro_2023: str
    novembro_2023: str

@dataclass
class cartao:
    cartao: str
    banco_finan: str
    limite: str

@dataclass
class desp_var:
    finalidade: str
    cartao: str
    parcelas: int
    valor: str
    novembro_2022: str
    dezembro_2022: str
    janeiro_2023: str
    fevereiro_2023: str
    marco_2023: str
    abril_2023: str
    maio_2023: str
    junho_2023: str
    julho_2023: str
    agosto_2023: str
    setembro_2023: str
    outubro_2023: str
    novembro_2023: str

@dataclass
class total_cartao:
    total: str
    novembro_2022: str
    dezembro_2022: str
    janeiro_2023: str
    fevereiro_2023: str
    marco_2023: str
    abril_2023: str
    maio_2023: str
    junho_2023: str
    julho_2023: str
    agosto_2023: str
    setembro_2023: str
    outubro_2023: str
    novembro_2023: str

@dataclass
class total_geral:
    total: str
    novembro_2022: str
    dezembro_2022: str
    janeiro_2023: str
    fevereiro_2023: str
    marco_2023: str
    abril_2023: str
    maio_2023: str
    junho_2023: str
    julho_2023: str
    agosto_2023: str
    setembro_2023: str
    outubro_2023: str
    novembro_2023: str

@dataclass
class cad_desp_var:
    finalidade: str
    valor: str
    cartao: str
    vezes: str
    data_pagamento: str

@dataclass
class cad_desp_fixa:
    finalidade: str
    valor: str
    data_pagamento: str