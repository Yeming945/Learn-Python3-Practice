""" 练习7 更多打印 """

print("Mary had a little lamb.") # 玛丽有一只小羊羔
print("Its fleece was white as {}.".format('snow')) # 它的毛是雪白色的
print("And everywhere that Mary went.") # 玛丽去过很多地方
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what h
# end起不换行作用
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
