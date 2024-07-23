import control as ctl
import matplotlib.pyplot as plt
import numpy as np

def funcao_transferencia(num, den):
    return ctl.TransferFunction(num, den)


def malha_aberta_degrau(funcao_transferencia):
    t, y = ctl.step_response(funcao_transferencia)
    
    plt.plot(t, y)
    plt.title('Resposta ao Degrau')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    #plt.show()
   
    

def parametros_sistema(funcao_transferencia):
    
    # Selecionar as chaves desejadas
    chaves_desejadas = ['SettlingTime', 'Overshoot', 'PeakTime', 'SteadyStateValue']
    
    par = ctl.step_info(funcao_transferencia, T=None, T_num=None, yfinal=None, params=None, SettlingTimeThreshold=0.05, RiseTimeLimits=(0.1, 0.9))

    # Criar um novo dicionário com apenas os valores desejados
    valores_extraidos = {chave: par[chave] for chave in chaves_desejadas if chave in par}
    
    return valores_extraidos

    

def overshoot(funcao_transferencia):
    t, y = ctl.step_response(funcao_transferencia)

    # valor final resposta
    valor_final = y[-1]

    # sobressinal
    valor_pico = np.max(y)
    overshoot = ((valor_pico - valor_final)/valor_final)*100
    return overshoot
