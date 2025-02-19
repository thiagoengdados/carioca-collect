def extractJsonResultadoCarioca(score_carioca, datas_carioca, score_carioca_final):
    # Inicializando a lista para armazenar os resultados com datas_carioca

    # Itera pela lista score_carioca 
    for i in range(len(score_carioca )):
        # Verifica se há elementos suficientes para acessar o índice i + 2 e i + 4
        if i + 2 < len(score_carioca ) and i + 4 < len(score_carioca ):
            # Cria um array com os times e placar (evita valores vazios)
            time1 = score_carioca [i].replace('-', ' ').strip() if score_carioca [i] else None
            placar = score_carioca [i + 2].replace('-', 'x').strip() if score_carioca [i + 2] else None
            score_carioca_str = score_carioca [i + 4].replace('-', ' ').strip() if score_carioca [i + 4] else None

            # Verifica se existe uma data para esse jogo
            data = datas_carioca[i // 5] if i // 5 < len(datas_carioca) else None

            # Adiciona o time, placar e data na lista resultados_json
            if time1 and placar and score_carioca_str and data:
                # Formata a data para o formato desejado ("sáb, 15 fev")
                data_formatada = data.split(',')[0] + ',' + ' ' + data.split(',')[1].strip().replace('.', '')
                
                # Cria o objeto JSON para o jogo
                jogo = {
                    "time1": time1,
                    "placar": placar.replace(" ", " "),  # Substitui espaços por "x" no placar
                    "score_carioca ": score_carioca_str,
                    "data": data_formatada
                }
                score_carioca_final.append(jogo)  # Adiciona o jogo ao array de resultados

