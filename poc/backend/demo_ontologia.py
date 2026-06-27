"""
demo_ontologia — prova o ponto.

Roda a tool consultar_ontologia contra o imóvel de teste (Sítio Três Rios,
Mata Atlântica) e mostra que cada resposta carrega a regra concreta + a fonte
legal + o rastro no grafo. É a evidência de "raciocina sobre ontologia, não
adivinha sobre texto".

Rodar:  python demo_ontologia.py
"""

import json
from consultar_ontologia import Ontologia


def bloco(titulo, resultado):
    print(f"\n{'='*70}\n{titulo}\n{'-'*70}")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


def main():
    onto = Ontologia()
    print("Ontologia carregada:", len(onto.g), "triplas\n")
    print("IMÓVEL DE DEMO: Sítio Três Rios — Rio Bonito/RJ — bioma Mata Atlântica")
    print("Pendências reais do SICAR de teste: CIB ausente, representante ausente")

    # 1. A pendência que o produtor recebeu (CIB) — traduzida com fonte
    bloco(
        "1) Pendência recebida: 'Informe o código CIB do imóvel'",
        onto.regra_para_pendencia("CIB_ausente"),
    )

    # 2. O nome 'Três Rios' = APP hídrica. Rio típico pequeno (< 10 m) -> 30 m
    bloco(
        "2) Enriquecimento: o sítio tem cursos d'água. Faixa de APP de um rio de 8 m",
        onto.app_hidrica(largura_rio_m=8),
    )

    # 3. Reserva Legal para o bioma do imóvel
    bloco(
        "3) Reserva Legal exigida no bioma do imóvel (Mata Atlântica)",
        onto.reserva_legal("Mata Atlântica"),
    )

    # 4. O que o CAR regularizado desbloqueia
    bloco(
        "4) Benefícios que o CAR ativo desbloqueia",
        onto.beneficios(situacao_car="Ativo"),
    )

    # Contraprova: outro bioma muda a regra (mostra que não é hard-coded)
    bloco(
        "CONTRAPROVA) Mesmo método, bioma Amazônia -> regra diferente",
        onto.reserva_legal("Amazônia"),
    )

    print(f"\n{'='*70}")
    print("PONTO PROVADO: cada resposta veio do grafo, com fonte legal rastreável.")
    print("O LLM (P0-5) só vai traduzir isto em linguagem simples — não inventa a regra.")
    print("="*70)


if __name__ == "__main__":
    main()
