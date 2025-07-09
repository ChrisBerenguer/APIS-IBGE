import json
import yfinance as yf

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

# :::: Ele só está retornando as Bolsas Internacionais ::::

def retorna_cotacao_hist(
        ticker,
        periodo='1mo',              # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max '''   


):
    print('retorna_cotacao_hist',ticker)
    ticker_obj = yf.Ticker(f'{ticker}')
    hist = ticker_obj.history(period=periodo)['Close']
    hist.index = hist.index.strftime('%Y-%m-%d')
    hist = round(hist, 2)
    return hist.to_json()
    if len(hist) > 30:
        slice_hist = int(len(hist) / 30)
        hist = hist.iloc[::slice_hist]
    return hist.to_json()
    





tools = [

    {
        'type': 'function',
        'function':{
            'name': 'retorna_cotacao_hist',
            'description': 'Retorna a cotação histórica de um ativo',
            'parameters': {
                'type': 'object',
                'properties': {
                    'ticker': {
                        'type': 'string',
                        'description': 'o ticker do ativo, por exemplo: "ABEV3" para Ambev, "ITUB4" para Itaú ',

                    },
                    'periodo': {
                        'type': 'string',
                        'description': 'o periodo da cotação histórica',
                        'enum': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'],
                         
                    }
                }
            }
        }
    }
]

funcoes_disponiveis = {'retorna_cotacao_hist': retorna_cotacao_hist}

def geracao_texto(mensagens):
    
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=mensagens,
        tools=tools,
        tool_choice="auto",
        )


    tool_calls = resposta.choices[0].message.tool_calls

    if tool_calls:
        mensagens.append(resposta.choices[0].message)
        for tool_call in tool_calls:
            func_name = tool_call.function.name
            function_to_call = funcoes_disponiveis[func_name]
            func_args = json.loads(tool_call.function.arguments)
            print("Tool call arguments:", func_args)

            func_return = function_to_call(**func_args)
            mensagens.append({
                'tool_call_id': tool_call.id,
                'role':'tool',
                'name':func_name,
                'content': func_return,

            })
        segunda_resposta = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=mensagens,
            tools=tools,
            tool_choice="auto",
            )
        mensagens.append(segunda_resposta.choices[0].message)
        
        




    print(f'Assistant {mensagens[-1].content}')
    return mensagens



if __name__=='__main__':
    print("""
/******************************************************\\
*                                                    *
*            ██████╗██╗  ██╗ █████╗ ████████╗         *
*           ██╔════╝██║  ██║██╔══██╗╚══██╔══╝         *
*           ██║     ███████║███████║   ██║            *
*           ██║     ██╔══██║██╔══██║   ██║            *
*           ╚██████╗██║  ██║██║  ██║   ██║            *
*            ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝            *
*                                                    *
*                C H A T B O T   F I N A N C E I R O   *
*                                                    *
\\******************************************************/
""")
    while True:
        input_usuario = input('User: ')
        mensagens = [
            {"role": "user", 
            "content": input_usuario}
            ]
        mensagens = geracao_texto(mensagens)

