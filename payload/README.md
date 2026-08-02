# Payload da validação ECHOLOOM

Os arquivos `chunk-*` são segmentos Base64 consecutivos de `echoloom-source.zip.xz`. O workflow concatena os arquivos em ordem lexical, decodifica Base64, valida o SHA-256 do XZ, descomprime o ZIP e valida o SHA-256 do ZIP antes de executar `npm ci` ou qualquer script do projeto.
