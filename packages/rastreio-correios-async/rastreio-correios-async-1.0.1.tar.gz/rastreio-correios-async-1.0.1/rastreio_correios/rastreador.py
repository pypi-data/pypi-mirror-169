"""Rastreador."""
from asyncio import gather
from json import loads
from re import IGNORECASE, MULTILINE
from re import compile as compile_re
from typing import Pattern

from aiohttp import ClientSession


class Rastreio:
    """Rastreio

    Na classe rastreio tu irá encontrar métodos para fazer o rastreio de
    encomendas na base de dados dos correios.
    """

    @classmethod
    def __compile_re(cls) -> None:
        """Compilador dos regex.

        Neste método nós fazemos a compilação dos regex que são utilizados
        no código todo.
        """
        regex: str = r'[a-z]{2}[0-9]{9}[a-z]{2}'
        cls.__regex_codigo = compile_re(regex, MULTILINE | IGNORECASE)
        regex: str = r'\{\"codigo\"\:.*?(?:(?:png\"\})' r'|(?:png\"\}\,)){1}'
        cls.__regex_eventos = compile_re(regex, MULTILINE | IGNORECASE)
        regex: str = (
            r'(?P<Ano>[0-9]{4})(?:\-)'
            r'(?P<Mes>[0-9]{2})(?:\-)'
            r'(?P<Dia>[0-9]{2})(?:t)'
            r'(?P<Hora>[0-9]{1,2})(?:\:)'
            r'(?P<Minutos>[0-9]{1,2})(?:.*)'
        )
        cls.__regex_data = compile_re(regex, MULTILINE | IGNORECASE)

    def __new__(cls):
        """__new__

        Efetuamos a verificação se tem outra instância do
        rastreador criada e retornos ela ou criamos uma.

        Returns:
            class : Classe Rastreio.
        """
        if not hasattr(cls, '_isAlive'):
            cls.__compile_re()
            cls._isAlive = super().__new__(cls)
        return cls._isAlive

    async def rastrear(self, codigo: str = '') -> str:
        """Rastrear

        Neste método fazemos o rastreio da encomenda nos correios.

        Args:
            codigo (str): Deve ser passado o código dos correios.

        Returns:
            str: Retornamos o resultado do rastreio de forma limpa.
        """
        retorno_codigo: list[str] = self.__regex_codigo.findall(codigo)
        retorno: str = None

        if retorno_codigo != []:
            codigo: str = retorno_codigo[0]
            url: str = (
                f'https://proxyapp.correios.com.br/' f'v1/sro-rastro/{codigo}'
            )

            async with ClientSession() as session:
                async with session.get(url) as response:
                    retorno_get = await response.text()

            informacoes: list[str] = self.__regex_eventos.findall(retorno_get)

            tasks: list = (self.__limpaMensagem(info) for info in informacoes)

            a = await gather(*tasks)
            retorno = ''.join(a)
            if retorno == '':
                retorno = 'Objeto não encontrado na base de dados.'
        return retorno

    async def __limpaMensagem(self, evento: str = '') -> str:
        """Limpar Mensagem.

        Aqui nós limparemos a mensagem e deixaremos do formato
        que fica muito mais legível.

        Args:
            evento (str): Dado de um evento que contém no rastreio.

        Returns:
            str: Retornamos o evento de forma mais legível.
        """
        data: str = ''
        local: str = ''
        destino: str = ''
        detalhe: str = ''
        descricao: str = ''
        retorno: str = ''
        evento_json: dict = loads(evento)

        if 'descricao' in evento_json:
            descricao = evento_json['descricao']
        if 'detalhe' in evento_json:
            temp: str = evento_json['detalhe']
            detalhe = f'\n{temp}'
        if 'dtHrCriado' in evento_json:
            temp: str = evento_json['dtHrCriado']
            data = await self.__limpaData(data=temp, regex=self.__regex_data)
        if 'unidade' in evento_json:
            temp: dict = evento_json['unidade']
            if 'nome' in temp:
                pais: str = temp['nome']
                local = f'[{pais}]'
            else:
                temp = temp['endereco']
                cidade: str = temp['cidade']
                uf: str = temp['uf']
                local = f'[{cidade}/{uf}]'
        if 'unidadeDestino' in evento_json:
            temp: dict = evento_json['unidadeDestino']
            temp = temp['endereco']
            if ('cidade' in temp) and ('uf' in temp):
                cidade: str = temp['cidade']
                uf: str = temp['uf']
                destino = f' para [{cidade}/{uf}]'
        retorno = f'[{data}] - {descricao} {local}{destino}' f'{detalhe}\n\n\n'
        return retorno

    @staticmethod
    async def __limpaData(data: str = '', regex: Pattern = None) -> str:
        """Limpar Data.

        Aqui nós limparemos a data e deixaremos do formato
        que fica muito mais legível.

        Args:
            data (str): Data pega nos dados da encomenda.
            regex (Pattern): O regex já compilado.

        Returns:
            str: Data em um formato mais legível.
        """
        data = regex.findall(data)
        if data != []:
            data = data[0]
            if len(data) == 5:
                ano = data[0]
                mes = data[1]
                dia = data[2]
                hora = data[3]
                minuto = data[4]
                mensagem = f'{dia}/{mes}/{ano} - {hora}:{minuto}'
                return mensagem
        return ''
