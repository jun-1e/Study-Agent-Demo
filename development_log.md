***2026-10-15
    **!发现问题，ref_userfile方法的关键词需要与save_file产生的关键词严格匹配才能检索内容。虽然符合关键词时能正常生效，但通常因无法匹配关键词产生默认返回。
        *可以建立模糊查询字典，让索引keyword生成时同时扩充字典，检索时在精确查询失败后再进行模糊查询。
    
    **后续需要减少history加入prompt的条数，增强性能。
        *需要改变history保存策略，使最后的history扩充到原本history的最后（例如删去最后history的前（开头加入条数）条信息）

***2026-10-12
    **修改savefile方法时加入了异常处理，并且将保存结果设置为json格式，但测试保存结果是null
        *方法中append部分只执行添加操作，返回的是none，所以结果是null
    **设计了读取userfile的方法，但测试时发生了openai.BadRequestError
        *func_lists中定义格式错误导致出现异常
            *出现了索引错误，用字符串索引字符串出现异常，先json.load改变指向内容解决了
                *主程序开始的readfile方法错误的初始化了userfiles文件，导致内容检测错误，返回KeyError: 'keyword_1'，加入判断条件解决了问题
    
***2026-10-8
    **设计了savefile方法，可以保存用户提供的资料到本地

    **!调用计算器工具时会出现'ZeroDivisionError: division by zero'异常，需要进行异常处理。
        *通过在方法中除项加入异常处理返回错误信息解决了问题，对话历史log中也能看到进行工具调用后正确处理了异常
    **!清空history文件会导致读取值为none，出现json.decoder.JSONDecodeError异常
        *尝试重建初始history解决异常，但返回了io.UnsupportedOperation: not readable
        *问题在于没有设置json读状态。。设置后可以正常重设历史记录
            **!如果结构异常也会重置所有history内容
                *通过分别处理两种异常并在数据异常项加入判断条件，保存文件副本，读取异常时直接关闭程序解决了问题
    **!如果直接删除history文件会返回FileNotFoundError异常
        *增加了except项解决了问题
    **!savefile功能只能保存一条消息，并且保存格式是字符串
        *通过改变输入状态现在可以保存多条用户消息，但与预期格式不同，且无法格式化读取
    
    **后续计划开发rag工具，将savefile方法保存的信息用于回答参考
    **修复savefile方法出现的漏洞
    **使promt只包含userFiles精简过的内容，减少token消耗并增强性能

***2026-10-7
    **改变了messages的append位置，现在不会保存exit等退出指令，并且会保存assistant非tool_call情况下的回复
    **增加了分词器，便于后续进行embedding
    **预设了savefile工具，计划功能为使agent选择保存用户输入到本地文档，创建知识库

***2026-10-6
    **通过循环内使用input实现了用户的多轮对话，退出条件设置为输入exit
    **加入了events文件，方便管理方法。创建了read和write files方法，加入了appendmsg便于messages的增加

    **测试能否读取历史对话时发现询问上次调用了什么方法会导致报错
        循环response中即使没有tool_call依然进入了tool_calls部分
            !tool_calls是空的会导致msg_append方法报错NoneType无效
                *解决：问题不在于append方法，在退出循环判断条件后加入continue跳过后续操作只进行没有tool_calls的部分解决了问题
    
    **后续应将没有tools调用的assistant对话也加入history
        []加入RAG文档功能，用来读写本地保存用户输入的资料
        []做一个前端使功能表现更直观
        []加入分词器使文档内容匹配更精确
        []更多tools种类

***2026-10-5
    **遇到了api格式不兼容的问题，原本的tools定义结构使用了response API格式但主程序使用了chat completions格式。统一改为使用较简单的chat completions API格式
    **用while True实现tool_call循环，只有没有工具被调用时才会退出循环

***/此前没有记录/