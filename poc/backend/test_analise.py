"""
Testes da análise de déficit de APP (P0-8). Roda sem pytest:
    python test_analise.py
"""

import copy
import json
from pathlib import Path
from analise_app import analisar_app, analisar_amostra

AMOSTRA = json.loads((Path(__file__).parent / "dados_demo" / "imovel_demo.geojson").read_text(encoding="utf-8"))


def test_deficit_amostra():
    r = analisar_amostra()
    # rio de 8 m -> faixa de 30 m (da ontologia)
    assert r["faixa_exigida_m"] == 30
    # APP exigida = 30 m x 100 m = 3000 m²
    assert abs(r["area_app_exigida_m2"] - 3000) < 1
    # vegetação cobre 12 m -> déficit = (30-12) x 100 = 1800 m²
    assert abs(r["deficit_m2"] - 1800) < 1
    assert r["conforme"] is False


def test_faixa_vem_da_ontologia():
    # mudar a largura do rio muda a faixa exigida — prova que vem do grafo
    geo = copy.deepcopy(AMOSTRA)
    geo["largura_rio_m"] = 30          # 10–50 m -> faixa de 50 m
    r = analisar_app(geo)
    assert r["faixa_exigida_m"] == 50


def test_conforme_quando_mata_suficiente():
    # vegetação cobrindo 35 m (> 30 exigidos) -> sem déficit
    geo = copy.deepcopy(AMOSTRA)
    geo["vegetacao_existente"] = {
        "type": "Polygon",
        "coordinates": [[[0, 0], [35, 0], [35, 100], [0, 100], [0, 0]]],
    }
    r = analisar_app(geo)
    assert r["deficit_m2"] < 1
    assert r["conforme"] is True


def test_p07_tem_fonte_e_rastro():
    r = analisar_amostra()
    assert r["fonte"]
    assert r["rastro_ontologia"].startswith("car:")


if __name__ == "__main__":
    testes = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in testes:
        t()
        print(f"  OK  {t.__name__}")
    print(f"\n{len(testes)}/{len(testes)} testes passaram.")
