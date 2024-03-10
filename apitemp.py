import requests
import customtkinter as ctk
from tkinter import messagebox
import datetime
from io import BytesIO
from googletrans import Translator

API_KEY = "9353163c3fd06797a54198348c1bcb9d"

class Interface(ctk.CTk):
    # Variaveis Globais
    confirmar_modo = False
    porrasenha=False


# Interfacess
    

    # Função Inicio, Encontrar Cidade
    def Cidade(self):
        self.title("Previsão do Tempo")
        self.geometry("900x600")
    

        # Criar widgets
        self.titulo = ctk.CTkLabel(self, text='Bem Vindo a Plataforma!', font=ctk.CTkFont(size=20, weight="bold"), bg_color="transparent")
        self.titulo.grid(row=0, column=0, padx=10, pady=(20))
        
        self.label_login = ctk.CTkLabel(self, text="Encontre sua cidade", font=ctk.CTkFont(size=20, weight="bold"), text_color="white", bg_color="transparent")
        self.label_login.grid(row=1, column=2, padx=10, pady=20)
        
        self.label_cidade = ctk.CTkLabel(self, text="Cidade: ", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_cidade.grid(row=2, column=1, padx=10, pady=10)
        self.entry_cidade = ctk.CTkEntry(self, width=380)
        self.entry_cidade.grid(row=2, column=2, padx=10, pady=10)
    
        
        self.bt_sair = ctk.CTkButton(self, text="Sair", bg_color="transparent", command=self.Sair)
        self.bt_sair.grid(row=499, column=0, pady=(10, 20))
        
        self.btn_cadastrarL = ctk.CTkButton(self, text="Previsão", width=140, height=40, command=self.exibir_previsao)
        self.btn_cadastrarL.grid(row= 497, column=2, padx=0, pady=30)

        self.appearance_mode_label = ctk.CTkLabel(self, text="""⬇ Aparência ⬇️""", anchor="w", text_color="white", font=("Helvetica", 14))
        self.appearance_mode_label.grid(row=500, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, values=["Dark", "Light"],
                                                                       command=self.aparencia_mode)
        self.appearance_mode_optionemenu.grid(row=502, column=0, padx=20, pady=(10, 10))
        
        if Interface.confirmar_modo == True:
            ctk.set_default_color_theme("green")
            # Alterar a cor do texto para preto no modo "Write"
            self.titulo.configure(text_color="black")
            self.label_login.configure(text_color="black")
            self.label_cidade.configure(text_color="black")
            self.appearance_mode_label.configure(text_color="black")
            # Alterar a cor dos botões para verde no modo "Write"
            self.bt_sair.configure(fg_color="green", hover_color="light green", text_color="black")
            self.btn_cadastrarL.configure(fg_color="green", hover_color="light green", text_color="black")
            self.appearance_mode_optionemenu.configure(fg_color="green",button_color="green",button_hover_color="light green", text_color="black")
            Interface.confirmar_modo = True
        else:
            self.titulo.configure(text_color="white")
            self.label_login.configure(text_color="white")
            self.label_cidade.configure(text_color="white")
            self.appearance_mode_label.configure(text_color="white")
            # Alterar a cor dos botões para verde no modo "white"
            self.bt_sair.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.btn_cadastrarL.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.appearance_mode_optionemenu.configure(fg_color="#1d6ca4",button_color="#1d6ca4",button_hover_color="#144c74", text_color="white")
            Interface.confirmar_modo = False



# Funções
            

    # Modo de Aparencia de Dark e White
    def aparencia_mode(self, new_appearance_mode: str):
        if not new_appearance_mode or new_appearance_mode == "Sistema":
            ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        else:
            ctk.set_appearance_mode(new_appearance_mode)
        if new_appearance_mode == "Dark":
            self.titulo.configure(text_color="white")
            self.label_login.configure(text_color="white")
            self.label_cidade.configure(text_color="white")
            self.appearance_mode_label.configure(text_color="white")
            # Alterar a cor dos botões para verde no modo "white"
            self.bt_sair.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.btn_cadastrarL.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.appearance_mode_optionemenu.configure(fg_color="#1d6ca4",button_color="#1d6ca4",button_hover_color="#144c74", text_color="white")
            Interface.confirmar_modo = False

        else:
            self.titulo.configure(text_color="black")
            self.label_login.configure(text_color="black")
            self.label_cidade.configure(text_color="black")
            self.appearance_mode_label.configure(text_color="black")
            # Alterar a cor dos botões para verde no modo "Write"
            self.bt_sair.configure(fg_color="green", hover_color="light green", text_color="black")
            self.btn_cadastrarL.configure(fg_color="green", hover_color="light green", text_color="black")
            self.appearance_mode_optionemenu.configure(fg_color="green",button_color="green",button_hover_color="light green", text_color="black")
            Interface.confirmar_modo = True
    

    # Função de Confirmação de Cidade
    def exibir_previsao(self):
        cidade = self.entry_cidade.get()
        dados = self.buscar_dados(cidade)
        if 'cod' in dados and dados['cod'] == '404':
            messagebox.showerror("Erro", "Erro ao encontrar a cidade. Por favor, verifique e tente novamente")
        else:
            # Exibir previsão em uma nova janela
            janela_previsao = ctk.CTk()
            janela_previsao.title("Previsão do Tempo")
            janela_previsao.geometry("900x700")

            # Data
            dt_segundos = dados['dt']
            dt = datetime.datetime.utcfromtimestamp(dt_segundos)
            data_formatada = dt.strftime('%d de %B')
            label_data = ctk.CTkLabel(janela_previsao, text=f"Data: {data_formatada}", font=("Arial", 16), text_color="red", anchor='w')
            label_data.grid(row=1, column=0, padx=10, pady=10)

            # Horas
            dt_segundos = dados['dt']
            dt = datetime.datetime.utcfromtimestamp(dt_segundos)
            hora = dt.strftime('%H:%M')
            label_tempo = ctk.CTkLabel(janela_previsao, text=f"{hora} Horas", font=("Arial", 15), text_color="red", anchor='w')
            label_tempo.grid(row=1, column=1, padx=5)

            # Nome Cidade e estado
            nome_cidade = dados['name']
            codigo_pais = dados['sys']['country']
            label_localizacao = ctk.CTkLabel(janela_previsao, text=f"{nome_cidade},{codigo_pais}", font=("Arial", 20, "bold"), anchor='w')
            label_localizacao.grid(row=2, column=0, padx=0, pady=5)

            # Temperatura em ºC
            label_temperatura = ctk.CTkLabel(janela_previsao, text=f" 🌦️{dados['main']['temp']}°C", font=("Arial", 30))
            label_temperatura.grid(row=3, column=0, padx=0 )

            # Criar um label para mostrar a sensação térmica
            sensacao_termica = dados['main']['feels_like']
            label_sensacao_termica = ctk.CTkLabel(janela_previsao, text=f"Sensação Térmica de {sensacao_termica}°C", font=("Arial", 16, "bold"))
            label_sensacao_termica.grid(row=4, column=0, padx=10, pady=10)

            # Criar um label para exibir o weather main
            main_weather = dados['weather'][0]['main']
            descricao_weather = dados['weather'][0]['description']

            # # Traduzindo informações para o portugues
            # translator = Translator()
            # main_weather = translator.translate(main_weather, dest='pt')
            # descricao_weather = translator.translate(descricao_weather, dest='pt')


            label_main_weather = ctk.CTkLabel(janela_previsao, text=f"{main_weather}", font=("Arial", 16))
            label_main_weather.grid(row=4, column=1, padx=10, pady=10)
            label_descricao_weather = ctk.CTkLabel(janela_previsao, text=f"{descricao_weather}", font=("Arial", 16))
            label_descricao_weather.grid(row=4, column=2, padx=10, pady=10)




            # Criar um label para exibir a quantidade de chuva
            # Verificar se os dados de chuva estão presentes no JSON
            if 'rain' in dados:
                # Verificar se a chave específica para a quantidade de chuva está presente
                if '1h' in dados['rain']:
                    quantidade_chuva = dados['rain']['1h']
                    label_quantidade_chuva = ctk.CTkLabel(janela_previsao, text=f" ⛈️ Chuva: {quantidade_chuva} mm", font=("Arial", 16), anchor='w')
                    label_quantidade_chuva.grid(row=5, column=0, padx=10, pady=10)
            else:
                # Se os dados de chuva não estiverem presentes, exibir uma mensagem de que os dados estão indisponíveis
                label_quantidade_chuva = ctk.CTkLabel(janela_previsao, text=" ⛈️ Chuva: indisponíveis", font=("Arial", 14), anchor='w')
                label_quantidade_chuva.grid(row=5, column=0, padx=10, pady=10)


            # Criar um label para exibir a velocidade do vento
            if 'wind' in dados:
                velocidade_vento = dados['wind'].get('speed', 0)  # Se não houver dados de vento, assume 0 m/s
                label_velocidade_vento = ctk.CTkLabel(janela_previsao, text=f" 🍃 Vento: {velocidade_vento} m/s", font=("Arial", 14), anchor='w')
                label_velocidade_vento.grid(row=5, column=1, padx=5)

            # Label para Umidade
            label_umidade = ctk.CTkLabel(janela_previsao, text=f"Umidade: {dados['main']['humidity']}%", font=("Arial", 14), anchor="e", width=12)
            label_umidade.grid(row=8, column=0)

              # Criar um label para exibir o ponto de condensação da água
            if 'dew_point' in dados:
                ponto_condensacao = dados['dew_point']
                # Criar um label para exibir o ponto de condensação da água
                label_ponto_condensacao = ctk.CTkLabel(janela_previsao, text=f"Ponto de Condensação da Água: {ponto_condensacao}°C", font=("Arial", 14), anchor="e", width=12)
                label_ponto_condensacao.grid(row=9, column=0, padx=10, pady=10)
            else:
                # Se o campo 'dew_point' não estiver presente, exibir uma mensagem de que os dados estão indisponíveis
                label_ponto_condensacao = ctk.CTkLabel(janela_previsao, text="Ponto de Condensação da Água: Dados indisponíveis", font=("Arial", 14), anchor="e", width=12)
                label_ponto_condensacao.grid(row=9, column=0, padx=10, pady=10)

            # Label para visibilidade
            # Verificar se o campo 'visibility' está presente nos dados
            if 'visibility' in dados:
                # Converter a visibilidade de metros para quilômetros
                visibilidade_km = dados['visibility'] / 1000
                # Criar um label para exibir a visibilidade em quilômetros
                label_visibilidade = ctk.CTkLabel(janela_previsao, text=f"Visibilidade: {visibilidade_km:.2f} km", font=("Arial", 14), justify='left')
                label_visibilidade.grid(row=10, column=0, padx=10, pady=10)
            else:
                # Se o campo 'visibility' não estiver presente, exibir uma mensagem de que os dados estão indisponíveis
                label_visibilidade = ctk.CTkLabel(janela_previsao, text="Visibilidade: indisponíveis", font=("Arial", 14), justify='left')
                label_visibilidade.grid(row=10, column=0, padx=10, pady=10)


            self .destroy()
            janela_previsao.mainloop()
            

    # Função de Buscar dados na API
            
    def buscar_dados(self, cidade):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric"
        requisicao = requests.get(url)
        return requisicao.json()

    # Função Sair e Fechar
    def Sair(self):
        # Fechar todas as janelas abertas
        self.destroy()


if __name__ == "__main__":
    app = Interface()
    app.Cidade()
    app.mainloop()
