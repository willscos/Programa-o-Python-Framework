# ## **Exercícios extra com Streamlit…**
# **Classe Livro** – crie uma classe com atributos título, autor, ano. Adicione um método `__str__`.
#  Crie uma subclasse `LivroDigital` que adiciona atributo `formato` e sobrescreva `__str__`.
# **Classe Abstrata Veiculo** – defina uma classe abstrata com método `mover`. Implemente `Carro` e `Bicicleta` com comportamentos diferentes. Teste o polimorfismo.
# **Sobrecarga de operador** – crie uma classe `Vetor` com atributos x, y e implemente `__add__`, `__sub__`, `__mul__` (escalar).
# **Classe anônima** – use `type` para criar uma classe dinâmica com um método `saudacao`. Instancie-a.


import streamlit as st
from dataclasses import dataclass
from abc import ABC, abstractmethod

st.set_page_config(page_title="POO em Python + Streamlit", page_icon="📚", layout="centered")


# ============================================================
# 1) Classe Livro + Subclasse LivroDigital
# ============================================================

@dataclass
class Livro:
    titulo: str
    autor: str
    ano: int

    def __str__(self) -> str:
        return f"📚 '{self.titulo}' — {self.autor} ({self.ano})"


@dataclass
class LivroDigital(Livro):
    formato: str  # e.g. PDF, EPUB, MOBI

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | 💾 Formato: {self.formato}"


# ============================================================
# 2) Classe Abstrata Veiculo + Carro/Bicicleta (polimorfismo)
# ============================================================

class Veiculo(ABC):
    @abstractmethod
    def mover(self) -> str:
        """Retorna uma descrição do movimento do veículo."""
        raise NotImplementedError


class Carro(Veiculo):
    def __init__(self, modelo: str):
        self.modelo = modelo

    def mover(self) -> str:
        return f"🚗 O carro {self.modelo} está andando com motor e rodas."


class Bicicleta(Veiculo):
    def __init__(self, tipo: str):
        self.tipo = tipo

    def mover(self) -> str:
        return f"🚲 A bicicleta ({self.tipo}) está se movendo com pedaladas."


def demonstrar_polimorfismo(veiculos: list[Veiculo]) -> list[str]:
    """Chama mover() em todos os veículos (mesmo método, comportamentos diferentes)."""
    return [v.mover() for v in veiculos]


# ============================================================
# 3) Sobrecarga de operador: Classe Vetor (x, y)
# ============================================================

@dataclass(frozen=True)
class Vetor:
    x: float
    y: float

    def __add__(self, other: "Vetor") -> "Vetor":
        if not isinstance(other, Vetor):
            return NotImplemented
        return Vetor(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vetor") -> "Vetor":
        if not isinstance(other, Vetor):
            return NotImplemented
        return Vetor(self.x - other.x, self.y - other.y)

    def __mul__(self, escalar: float) -> "Vetor":
        if not isinstance(escalar, (int, float)):
            return NotImplemented
        return Vetor(self.x * escalar, self.y * escalar)

    def __rmul__(self, escalar: float) -> "Vetor":
        # permite: 2 * Vetor(...)
        return self.__mul__(escalar)

    def __str__(self) -> str:
        return f"⟨{self.x}, {self.y}⟩"


# ============================================================
# 4) Classe anônima com type
# ============================================================

def criar_classe_dinamica(nome: str = "PessoaDinamica"):
    def saudacao(self, quem: str = "mundo"):
        return f"👋 Olá, {quem}! Eu sou uma instância de {self.__class__.__name__}."

    # type(nome_da_classe, (classes_base,), dict_de_atributos/metodos)
    ClasseDinamica = type(nome, (), {"saudacao": saudacao})
    return ClasseDinamica


# ============================================================
# UI Streamlit
# ============================================================

st.title("📌 Exercícios Extra: POO em Python + Streamlit")
st.caption("Livro/LivroDigital • Classe Abstrata Veiculo • Sobrecarga de Operadores • Classe Dinâmica com type")

aba1, aba2, aba3, aba4 = st.tabs(["📚 Livro", "🚗 Veículo (ABC)", "🧭 Vetor", "✨ Classe Dinâmica"])


# ----------------------------
# Aba 1: Livro / LivroDigital
# ----------------------------
with aba1:
    st.subheader("1) Classe Livro e Subclasse LivroDigital")

    col1, col2 = st.columns(2)
    with col1:
        titulo = st.text_input("Título", value="Dom Casmurro")
        autor = st.text_input("Autor", value="Machado de Assis")
    with col2:
        ano = st.number_input("Ano", min_value=0, max_value=3000, value=1899, step=1)
        tipo_livro = st.selectbox("Tipo", ["Livro (físico)", "LivroDigital"], index=1)

    formato = None
    if tipo_livro == "LivroDigital":
        formato = st.selectbox("Formato", ["PDF", "EPUB", "MOBI", "AZW", "HTML"], index=0)

    if st.button("Criar objeto e mostrar __str__", key="btn_livro"):
        if tipo_livro == "LivroDigital":
            obj = LivroDigital(titulo=titulo, autor=autor, ano=int(ano), formato=formato)
        else:
            obj = Livro(titulo=titulo, autor=autor, ano=int(ano))

        st.success("Objeto criado!")
        st.code(str(obj), language="text")
        st.write("🔎 Representação do objeto:", obj)


# ----------------------------
# Aba 2: Veículo (ABC)
# ----------------------------
with aba2:
    st.subheader("2) Classe Abstrata Veiculo + Polimorfismo")
    st.write("Aqui a ideia é: **uma interface comum (`mover`)** e implementações diferentes.")

    c1, c2 = st.columns(2)
    with c1:
        modelo_carro = st.text_input("Modelo do carro", value="Civic")
    with c2:
        tipo_bike = st.selectbox("Tipo de bicicleta", ["urbana", "mountain bike", "speed", "dobrável"], index=1)

    if st.button("Testar polimorfismo", key="btn_poly"):
        veiculos: list[Veiculo] = [Carro(modelo_carro), Bicicleta(tipo_bike)]
        saidas = demonstrar_polimorfismo(veiculos)

        st.success("Resultado chamando mover() em objetos diferentes:")
        for s in saidas:
            st.write("-", s)

    st.info("💡 Dica: tente criar novas subclasses de Veiculo, como Moto, Patinete, Ônibus…")


# ----------------------------
# Aba 3: Vetor
# ----------------------------
with aba3:
    st.subheader("3) Sobrecarga de operadores: Vetor (x, y)")
    st.write("Operações: `v1 + v2`, `v1 - v2`, `v1 * escalar` e `escalar * v1`.")

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Vetor 1**")
        x1 = st.number_input("x1", value=1.0, step=0.5)
        y1 = st.number_input("y1", value=2.0, step=0.5)

    with colB:
        st.markdown("**Vetor 2**")
        x2 = st.number_input("x2", value=3.0, step=0.5)
        y2 = st.number_input("y2", value=4.0, step=0.5)

    escalar = st.number_input("Escalar", value=2.0, step=0.5)

    v1 = Vetor(x1, y1)
    v2 = Vetor(x2, y2)

    st.write("v1 =", str(v1))
    st.write("v2 =", str(v2))

    if st.button("Calcular operações", key="btn_vetor"):
        st.write("✅ **v1 + v2** =", str(v1 + v2))
        st.write("✅ **v1 - v2** =", str(v1 - v2))
        st.write("✅ **v1 * escalar** =", str(v1 * escalar))
        st.write("✅ **escalar * v1** =", str(escalar * v1))


# ----------------------------
# Aba 4: Classe dinâmica com type
# ----------------------------
with aba4:
    st.subheader("4) Classe anônima/dinâmica com `type`")
    st.write("Cria uma classe em tempo de execução com um método `saudacao`.")

    nome_classe = st.text_input("Nome da classe dinâmica", value="PessoaDinamica")
    quem = st.text_input("Saudar quem?", value="Streamlit")

    if st.button("Criar classe + instanciar + chamar saudacao()", key="btn_type"):
        ClasseDinamica = criar_classe_dinamica(nome_classe)
        obj = ClasseDinamica()
        st.success("Classe dinâmica criada e instanciada!")
        st.code(obj.saudacao(quem), language="text")

        st.write("🔍 Tipo do objeto:", type(obj))
        st.write("🔍 Métodos disponíveis:", [m for m in dir(obj) if not m.startswith("_")])