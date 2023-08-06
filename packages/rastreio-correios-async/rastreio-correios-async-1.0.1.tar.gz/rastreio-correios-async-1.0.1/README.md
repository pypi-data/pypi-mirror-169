# 🐍 Rastreador de Encomendas

## Esse programa tem como seu intuito fazer o rastreio de encomendas dos correios

- Rastreio de encomendas

## Como utilizar?

```shell
$ pip install rastreio-correios-async
```

```Python
from asyncio import run

from rastreio_correios import Rastreio


async def main():
    rastreio = Rastreio()
    codigo = 'LB526033530HK'
    resultado = await rastreio.rastrear(codigo)
    print(resultado)


run(main())
```

### O que usamos na infraestrutura?

- [Utilizamos a linguagem Python](https://www.python.org/)
