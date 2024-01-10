import os


def build_env():
    print('工作路径', os.getcwd())
    print('当前目录', os.path.abspath(os.curdir))
    os.system("pip install chromadb==0.3.29")
    os.system("pip install pysqlite3")
    os.system(
        "git clone https://gitee.com/yzy0612/nltk_data.git  --branch gh-pages;cd nltk_data;mv packages/*  ./;cd tokenizers;unzip punkt.zip;cd ../taggers;unzip averaged_perceptron_tagger.zip")

    # download model
    if not os.path.exists('/home/xlab-app-center/model/InternLM-chat-7b'):
        from openxlab.model import download
        download(model_repo='OpenLMLab/InternLM-chat-7b', output='/home/xlab-app-center/model/InternLM-chat-7b')
        os.system("python LLM_chain.py")

    if not os.path.exists('/home/xlab-app-center/model/sentence-transformer'):
        # 设置环境变量
        os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
        # 下载模型
        os.system(
            'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir /home/xlab-app-center/model/sentence-transformer')

    os.system("python create_db.py")
    # 导入必要的库
    print(os.getcwd())
