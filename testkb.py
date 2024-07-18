from server.knowledge_base.kb_service.faiss_kb_service import FaissKBService
from server.knowledge_base.migrate import create_tables
from server.knowledge_base.utils import KnowledgeFile


kbService = FaissKBService("samples")
test_kb_name = "samples"
test_file_name = "docs/pkitool.json"
testKnowledgeFile = KnowledgeFile(test_file_name, test_kb_name)
print("kb is load!")

def test_add_doc():
    result = kbService.add_doc(testKnowledgeFile)
    print("add doc result : ", result)

# def search_db(search_content):
#     result = kbService.search_docs(search_content)
#     print("search result : ", result)
    
if __name__ == '__main__':
#     search_content = "什么是密评"
#     search_db(search_content)
#     search_content = "密评都有什么标准"
#     search_db(search_content)
#     search_content = "网络需要如何保护"
#     search_db(search_content)
#     search_content = "应用需要如何保护"
#     search_db(search_content)
#     search_content = "密评都有哪些流程"
#     search_db(search_content)
    test_add_doc()
    
# import requests
# import json
# import sys
# from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent.parent))
# from configs import BING_SUBSCRIPTION_KEY
# from server.utils import api_address

# from pprint import pprint

# api_base_url = api_address()

# headers = {
#     'accept': 'application/json',
#     'Content-Type': 'application/json',
# }

# def dump_input(d, title):
#     print("\n")
#     print("=" * 30 + title + "  input " + "="*30)
#     pprint(d)

# def test_knowledge_chat(api="/chat/knowledge_base_chat"):
#     url = f"{api_base_url}{api}"
#     data = {
#         "query": "商用密码产品认证证书过期的合规性判定是什么",
#         "knowledge_base_name": "samples",
#         "history": [
#             {
#                 "role": "user",
#                 "content": "你好"
#             },
#             {
#                 "role": "assistant",
#                 "content": "你好，我是 ChatGLM"
#             }
#         ],
#         "stream": True
#     }
#     dump_input(data, api)
#     response = requests.post(url, headers=headers, json=data, stream=True)
#     print("\n")
#     print("=" * 30 + api + "  output" + "="*30)
#     for line in response.iter_content(None, decode_unicode=True):
#         data = json.loads(line[6:])
#         if "answer" in data:
#             print(data["answer"], end="", flush=True)
#     pprint(data)
#     assert "docs" in data and len(data["docs"]) > 0
#     assert response.status_code == 200
    
    
# if __name__ == '__main__':
#     test_knowledge_chat()