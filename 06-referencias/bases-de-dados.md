# Bases de dados abertas

> O Desafio 1 exige usar pelo menos uma base aberta. A solução usa várias e é
> construída sobre o RER open-source.

## Bases que a solução usa

| Base | O que fornece | Papel na solução | Acesso |
|---|---|---|---|
| **SICAR / Portal CAR** | Situação do cadastro do imóvel | Status atual do CAR | car.gov.br · consulta.car.gov.br |
| **SIGEF (INCRA)** | Georreferenciamento de imóveis | Pré-preenchimento de limites | sigef.incra.gov.br |
| **MapBiomas** | Cobertura e uso do solo (histórico) | Validar APP/RL vs. autodeclaração | mapbiomas.org |
| **Código Florestal** | Parâmetros legais (APP/RL por bioma) | Base da ontologia | Lei 12.651/2012 |
| **RER (open-source)** | Registro/gestão do CAR (PostGIS, REST API) | Fundação transacional | github.com/Rural-Environmental-Registry/core |
| **SNIF / Painel Regularização** | Status por estado, contexto | Métricas agregadas | snif.florestal.gov.br |

## Referências de ontologia (para reúso / alinhamento)

- **AGROVOC** (FAO) — tesauro agrícola multilíngue
- **Embrapa** — OntoAgroHidro, GTermos/Agrotermos
- **AgroPortal**, **AgroLD** — repositórios/linked data agrícolas internacionais

## Honestidade de acesso

- SICAR: sem API pública por CPF — consulta pelo nº do CAR
- SIGEF: API pública, mas cobre só imóveis certificados
- MapBiomas: via Google Earth Engine (não é chamada simples por CPF)
- RER: REST API numa **instância própria** self-hostável ≠ sistema nacional ao vivo
