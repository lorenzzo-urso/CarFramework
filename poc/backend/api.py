"""
api — a API do Compadre / Terra Comum (P0-2).

Expõe o Agent Hub via HTTP:
- GET  /          -> status do serviço + provedor de LLM + agentes carregados
- GET  /agentes   -> lista os agentes carregados dos manifestos (P1-1b)
- POST /conversa  -> roda o Compadre (SICAR -> ontologia -> LLM); pergunta
                     conceitual é delegada ao Professor
- GET  /analise/demo -> análise própria de déficit de APP (P0-8)

Rodar:  uvicorn api:app --reload
Docs:   http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from agent_hub import AgentHub
from traduzir_llm import escolher_provedor
from analise_app import analisar_geometria_fixture

DESCRICAO = """
**Terra Comum** é a camada semântica aberta do território rural; o **Compadre**
é o primeiro agente que roda sobre ela. Toda resposta é rastreável: cita a regra
concreta vinda da ontologia do Código Florestal (`backend/ontologia/car.ttl`) —
nunca inventada pelo LLM.

O mesmo Hub carrega vários agentes a partir de manifestos YAML. Trocar o
manifesto muda o agente sem tocar no código.

### Como navegar
- **Status** — saúde do serviço e provedor de LLM ativo.
- **Hub** — os agentes registrados na plataforma (alimenta a vitrine).
- **Conversa** — o produtor fala com o Compadre; perguntas conceituais caem no Professor.
- **Análise** — déficit de APP descoberto a partir de dado aberto, antes do envio.
"""

TAGS = [
    {"name": "Status", "description": "Saúde do serviço e configuração ativa."},
    {"name": "Hub", "description": "Agentes registrados a partir dos manifestos YAML."},
    {"name": "Conversa", "description": "Diálogo com o Compadre (com delegação ao Professor)."},
    {"name": "Análise", "description": "Validação antecipada: déficit de APP via geometria × ontologia."},
]

app = FastAPI(
    title="Compadre / Terra Comum — PoC",
    description=DESCRICAO,
    version="0.1.0",
    openapi_tags=TAGS,
    # operationId limpo no /docs: usa o nome da função (ex.: "analise_demo")
    generate_unique_id_function=lambda route: route.name,
)

# PoC: libera CORS para a interface web (poc/web/) chamar a API do navegador.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

hub = AgentHub()


class ConversaIn(BaseModel):
    numero_car: str = Field(
        ...,
        description="Número do CAR do imóvel (ou um identificador de demonstração).",
        examples=["MG-3102308-1F30612FD2F845A7B8852A7B0BF07455"],
    )
    mensagem: str = Field(
        ...,
        description="O que o produtor escreveu. Perguntas conceituais ('o que é APP?') "
        "são delegadas automaticamente ao Professor.",
        examples=["consulta inicial"],
    )


@app.get("/", tags=["Status"], summary="Status do serviço")
def raiz():
    """Saúde do serviço: nome, provedor de LLM ativo e os agentes carregados."""
    return {
        "servico": "Compadre / Terra Comum",
        "provedor_llm": escolher_provedor(),
        "agentes": [a["name"] for a in hub.listar()],
    }


@app.get("/agentes", tags=["Hub"], summary="Lista os agentes do Hub")
def agentes():
    """Lista os agentes registrados no Hub (alimenta a vitrine em `web/hub.html`).

    Cada item traz `name`, `description`, `tools`, `ontology_concepts` e
    `operacional` — este último indica se todas as tools declaradas no manifesto
    estão registradas na plataforma."""
    return hub.listar()


@app.post("/conversa", tags=["Conversa"], summary="Conversa com o Compadre")
def conversa(inp: ConversaIn):
    """O produtor manda o número do CAR + mensagem; o Compadre responde.

    O pipeline é: consulta SICAR → ontologia → LLM, sempre com `regra_aplicada`
    rastreável. Se a mensagem for uma pergunta conceitual, o Compadre delega ao
    **Professor** e a resposta vem marcada com `delegado_por: "compadre"`."""
    return hub.run_agent("compadre", inp.numero_car, inp.mensagem)


@app.get("/analise/demo", tags=["Análise"], summary="Déficit de APP (validação antecipada)")
def analise_demo():
    """Análise própria de déficit de APP (P0-8) — a plataforma *descobre* o
    problema a partir de dado aberto, antes do produtor enviar.

    Lê a geometria do contrato `geometria.fixture.json` (recorte do GeoPackage
    SFB) e cruza com a faixa exigida pela ontologia. Devolve `faixa_exigida_m`,
    `deficit_m2`, `deficit_ha`, `conforme` e o rastro legal (`fonte`,
    `rastro_ontologia`)."""
    return analisar_geometria_fixture()
