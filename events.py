import json
import sys
import os

class events:

    def write_files(data,name):
        with open("files/"+str(name)+".json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


    def read_files(name):
        file_path = "files/"+str(name)+".json"
        if name == "history":
            default_msg = ([{
                            "role": "system",
                            "content": "You are a helpful assistant."
                        }])
        else:
            default_msg = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
            
        except FileNotFoundError:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(default_msg, f, ensure_ascii=False, indent=2)
            with open(file_path,"r",encoding="utf-8") as f : 
                return json.load(f)
            pass
        except json.decoder.JSONDecodeError:
            if os.path.getsize(file_path) == 0:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(default_msg, f, ensure_ascii=False, indent=2)
                return default_msg
            sys.exit("Error happened when opening " + str(name))     
                


    def append_msg(dict,msg):
        temp = {
        "role": msg.role,
        "content": msg.content
    }
        if msg.tool_calls:
            temp["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "type": tool_call.type,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                }
                for tool_call in msg.tool_calls
            ]
        dict.append(temp)


    def split_text(text, max_length):
        """分词器"""
        chunks = []
        for sentence in text:
            words = sentence.split()
            current_chunk = []
            for word in words:
                test_chunk = ' '.join(current_chunk + [word])
                if len(test_chunk) <= max_length:
                    current_chunk.append(word)
                else:
                    if current_chunk:
                        chunks.append(' '.join(current_chunk))
                    current_chunk = [word]
            if current_chunk:
                chunks.append(' '.join(current_chunk))
        return chunks