from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import os

def baixar_video(url, pasta_saida="videos"):
    """Baixa o vídeo do YouTube e retorna o caminho do arquivo salvo"""
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    caminho_arquivo = stream.download(output_path=pasta_saida)
    print(f"Vídeo baixado em: {caminho_arquivo}")
    return yt, caminho_arquivo


def gerar_descricao(video, video_id, arquivo_saida="descricao.txt"):
    """Gera descrição do vídeo a partir da transcrição (se disponível)"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])
        texto = " ".join([t['text'] for t in transcript])
    except Exception as e:
        texto = "Nenhuma transcrição disponível para este vídeo."
        print("⚠️ Não foi possível obter legenda:", e)

    descricao = f"Título: {video.title}\n"
    descricao += f"Canal: {video.author}\n"
    descricao += f"Duração: {video.length // 60} min {video.length % 60} seg\n\n"
    descricao += "Resumo / Descrição:\n"
    descricao += texto[:2000] + "..."  # Limita a 2000 caracteres para não ficar gigante

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(descricao)

    print(f"Descrição salva em: {arquivo_saida}")


if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")

    yt, caminho_video = baixar_video(url)
    video_id = url.split("v=")[-1]
    gerar_descricao(yt, video_id, "descricao.txt")
