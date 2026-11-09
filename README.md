# Lembrete de Treino ⏱️💪

Automação em Python que me lembra de fazer pausas para treinar durante os estudos.

A cada 1 hora de estudo, o programa abre um aviso na tela e só libera o próximo ciclo depois que eu confirmo que treinei.

## Como funciona

1. O programa espera o tempo de estudo configurado (padrão: 60 minutos).
2. Exibe um popup avisando que está na hora de treinar.
3. Pergunta "Você já treinou?" e repete até a resposta ser "Sim".
4. Inicia um novo ciclo de estudo.

## Tecnologias

- Python 3
- tkinter (interface dos popups)
- time (temporizador)

Nenhuma instalação extra é necessária, pois as bibliotecas já vêm com o Python.

## Como usar

```bash
python main.py
```

Para testar rapidamente, altere `MINUTOS_DE_ESTUDO` para `0.1` no topo do arquivo.

## Objetivo

Projeto criado para praticar Python e automação, unindo duas metas: estudar com constância e manter a saúde em dia.