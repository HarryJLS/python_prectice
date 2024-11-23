

import copy



if __name__ == "__main__":
    # name = "abcdef"
    # print(name[0:3])
    # print(name[:3])
    # print(name[3:])
    # print(name[0:-2])
    # print(name[1:5:2])
    # print(name[::-1])
    #
    # my_str = "welcome to www.tulingxueyuan.com"
    # print(my_str.find("to"))
    # print(my_str.index("to"))
    # print(my_str.rfind("to"))
    # print(my_str.rindex("to"))
    # print(my_str.count("to"))
    # print(my_str.replace("to", "TO", 1))
    # split = my_str.split(" ")
    # print(split)

    # nums1 = [11, 22, 33]  # 定义列表
    # nums2 = (44, 55, 66)  # 定义元组
    # nums3 = {77, 88, 99}  # 定义集合
    #
    # # 列表转换为元组、集合
    # print("-----------")
    # nums1_tuple = tuple(nums1)
    # print(type(nums1_tuple))
    # nums1_set = set(nums1)
    # print(type(nums1_set))
    #
    # # 元组转换为列表、集合
    # print("-----------")
    # nums2_list = list(nums2)
    # print(type(nums2_list))
    # nums2_set = set(nums2)
    # print(type(nums2_set))
    #
    # # 集合转换为列表、元组
    # print("-----------")
    # nums3_list = list(nums3)
    # print(type(nums3_list))
    # nums3_tuple = tuple(nums3)
    # print(type(nums3_tuple))
    #
    # test={
    #     "name":"zhangsan",
    #     "age":18
    # }
    # print(test["name"])
    # print(test.get("absduasbdjb", "问题报备"))
    # test["tall"] = 76
    # print(test)
    # del test["tall"]
    # print(test)

    # test1 = [1, 3, 4, 5]
    # t1, t2, t3, t4 = test1
    # print(t1)
    # print(t2)
    # print(t3)
    # print(t4)


    list1 = [["张三", "李四"], "王五", "赵六", "钱七"]
    list2 = copy.deepcopy(list1)   # 进行深拷贝

    # 打印 list1 和 list2 两个列表的内存地址 => 结果不一样
    print(id(list1))    # 3132367069640
    print(id(list2))    # 3132368415752

    # 打印 list1 和 list2 两个列表中的子列表的内存地址 => 结果不一样
    print(id(list1[0]))     # 3132368414728
    print(id(list2[0]))     # 3132368415688


    list2[0][0] = "安娜"

    # 结果 list2 列表修改了，但是不影响list1列表数据
    print(list2)    # [['安娜', '李四'], '王五', '赵六', '钱七']
    print(list1)    # [['张三', '李四'], '王五', '赵六', '钱七']

