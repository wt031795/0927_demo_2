'''获取返回值中的某一个字段,用于接口间的关联
   实际上就是对字典的操作,通过字典的键返回对应的值
   通过jsonpath库取值
'''
# 导入jsonpath
import jsonpath


def get_keyword(data: dict, keyword):
    '''
    通过关键字获取,对应的值,如果关键字对应的值有多个,那么只获取它的第一个
    :param keyword:字典的关键字
    :return:
    '''
    try:
        return jsonpath.jsonpath(data, f"$..{keyword}")[0]
    except Exception as e:
        print("获取关键字失败", e)


def get_keywords(data: dict, keyword):
    '''
    通过关键字获取,对应的所有值
    :param keyword:字典的关键字
    :return:
    '''
    try:
        return jsonpath.jsonpath(data, f"$..{keyword}")
    except Exception as e:
        print("获取关键字失败", e)


if __name__ == '__main__':
    pass
