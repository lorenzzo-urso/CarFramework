"""
analise_app — análise própria de déficit de APP hídrica (P0-8).

O diferencial construível: em vez de raspar a pendência do governo, a Terra Comum
DESCOBRE o problema cruzando geometria + dado aberto + ontologia.

  faixa de APP exigida  ← vem da ONTOLOGIA (consultar_ontologia.app_hidrica)
  buffer do rio por essa faixa  ∩  imóvel        = APP que devia ser mata
  APP que devia ser mata  −  vegetação existente = DÉFICIT de mata ciliar

Não depende de autenticação no SICAR — usa só geometria + a regra do grafo.

No PoC: geometria de amostra em metros (dados_demo/imovel_demo.geojson).
Em produção: imóvel/rio da consulta pública + recorte do GeoPackage SFB (Dev B).
"""

import json
from pathlib import Path
from shapely.geometry import shape
from consultar_ontologia import Ontologia

AMOSTRA = Path(__file__).parent / "dados_demo" / "imovel_demo.geojson"


def analisar_app(geo: dict, onto: Ontologia | None = None) -> dict:
    """Calcula o déficit de APP hídrica para uma geometria de imóvel.
    `geo` precisa ter: largura_rio_m, imovel, curso_dagua, vegetacao_existente."""
    onto = onto or Ontologia()
    largura = float(geo["largura_rio_m"])

    # 1) a regra vem da ontologia (faixa exigida pela largura do rio)
    regra = onto.app_hidrica(largura)
    faixa_m = regra["faixa_protegida_m"]

    # 2) geometrias
    imovel = shape(geo["imovel"])
    rio = shape(geo["curso_dagua"])
    veg = shape(geo["vegetacao_existente"])

    # 3) APP exigida dentro do imóvel = buffer do rio ∩ imóvel
    app_exigida = rio.buffer(faixa_m).intersection(imovel)

    # 4) déficit = APP exigida que NÃO tem vegetação
    deficit_geom = app_exigida.difference(veg)

    area_app = app_exigida.area
    area_deficit = deficit_geom.area
    conforme = area_deficit < 1.0  # tolerância de 1 m²

    return {
        "largura_rio_m": largura,
        "faixa_exigida_m": faixa_m,
        "area_app_exigida_m2": round(area_app, 1),
        "deficit_m2": round(area_deficit, 1),
        "deficit_ha": round(area_deficit / 10_000, 4),
        "conforme": conforme,
        "regra": regra["explicacao"],
        "fonte": regra["fonte"],
        "rastro_ontologia": regra["rastro_ontologia"],
    }


def analisar_amostra() -> dict:
    """Roda a análise sobre a geometria de amostra do PoC."""
    geo = json.loads(AMOSTRA.read_text(encoding="utf-8"))
    geo.pop("_comment", None)
    return analisar_app(geo)


if __name__ == "__main__":
    r = analisar_amostra()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    if not r["conforme"]:
        print(f"\n→ Déficit de {r['deficit_m2']} m² de mata ciliar "
              f"(a lei exige {r['faixa_exigida_m']} m; {r['fonte']}).")
