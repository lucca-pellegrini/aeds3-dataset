#!/usr/bin/env python

# SPDX-License-Identifier: ISC

import os
import stat
import shutil

import kagglehub

DATASET_HANDLE = "olegfostenko/almost-a-million-spotify-tracks"
DATASET_FNAME = "tracks.csv"
DATASET_PLAIN = "dataset-raw.csv"
DATASET_CLEAN = "dataset-clean.csv"

def download():
    path = kagglehub.dataset_download(DATASET_HANDLE) # Baixa o arquivo
    path = path + os.sep + DATASET_FNAME # Apende nome do arquivo à pasta
    shutil.copy(path, DATASET_PLAIN) # Copia o arquivo para DATASET_PLAIN
    os.chmod(DATASET_PLAIN, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH) # Torna-o não modificável

# Se o arquivo não já existe, o baixamos
if not os.path.exists(DATASET_PLAIN):
    download()

# Se o arquivo limpo for mais novo que o orignal, não é necessário continuar
if os.path.exists(DATASET_CLEAN) and os.path.getmtime(DATASET_CLEAN) > os.path.getmtime(DATASET_PLAIN):
    print(DATASET_CLEAN + " é mais novo que " + DATASET_PLAIN)
    print("Não é nexessário continuar")
    exit()

print("Iniciando processo de limpeza")

import pandas as pd

# Usamos tipos explícitos para as colunas que contêm dados ambíguos. Registros
# inválidos são ignorados.
df = pd.read_csv(DATASET_PLAIN,
                 dtype={'explicit': str, 'added_at': str},
                 on_bad_lines='skip'
 )

# Função auxiliar para converter valores inválidos da coluna 7 para `false`
def convert_to_bool(value):
    if pd.isna(value):
        return None
    if isinstance(value, str):
        if value.lower() in ['true', '1']:
            return True
        elif value.lower() in ['false', '0']:
            return False
    return None
df['explicit'] = df['explicit'].apply(convert_to_bool).astype('bool')

# Remove colunas em que a maioria dos dados é inválida
df = df.drop(columns=['streams', 'chart', 'track_track_number', 'rank',
                      'region', 'trend', 'duration_ms'])

# Remove colunas desnecessárias
df = df.drop(columns=['available_markets'])

# Remove registros com campos nulos
for col in ('added_at', 'album_name', 'track_artists'):
    df = df.dropna(subset=[col])

# Remove registros com valores inteiros nulos
for col in ('artist_followers', 'artist_popularity', 'album_total_tracks', 'key'):
    df = df.dropna(subset=[col])
    df[col] = df[col].astype(int)


# Função auxiliar para converter campos para listas
def parse_list(value):
    if isinstance(value, str):
        value = value.strip("[]") # Remove colchetes
        items = value.split(",")  # Divide entre vírgulas
        return [item.strip().strip("'").strip('"') for item in items] # Remove aspas e espaço branco
    else:
        return value

for col in ('track_artists', 'genres'):
    df[col] = df[col].apply(parse_list)

df.info()
df.to_csv(DATASET_CLEAN, index=False)
