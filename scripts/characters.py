# -*- coding: utf-8 -*-
# 三國演義主要人物表:正名 -> 別名(字、稱號、常見叫法)
# 別名只收正文中會單獨出現、且不易誤判的寫法(至少兩字)
CHARACTERS = {
    "劉備": ["劉玄德", "玄德", "劉皇叔", "劉豫州", "先主"],
    "關羽": ["關雲長", "雲長", "關公", "美髯公", "關某", "漢壽侯"],
    "張飛": ["張翼德", "翼德", "張益德"],
    "諸葛亮": ["諸葛孔明", "孔明", "臥龍", "武侯", "諸葛丞相"],
    "曹操": ["曹孟德", "孟德", "曹阿瞞", "阿瞞", "曹丞相"],
    "孫權": ["孫仲謀", "仲謀", "碧眼兒"],
    "孫策": ["孫伯符", "伯符", "小霸王"],
    "孫堅": ["孫文臺", "文臺"],
    "周瑜": ["周公瑾", "公瑾", "周郎", "周都督"],
    "魯肅": ["魯子敬", "子敬"],
    "呂布": ["呂奉先", "奉先", "呂温侯"],
    "趙雲": ["趙子龍", "子龍"],
    "馬超": ["馬孟起", "孟起"],
    "黃忠": ["黃漢升", "漢升"],
    "魏延": ["魏文長", "文長"],
    "姜維": ["姜伯約", "伯約"],
    "龐統": ["龐士元", "士元", "鳳雛"],
    "徐庶": ["徐元直", "元直", "單福"],
    "司馬懿": ["司馬仲達", "仲達"],
    "司馬師": ["司馬子元"],
    "司馬昭": ["司馬子上"],
    "司馬炎": [],
    "董卓": ["董仲穎", "董太師"],
    "袁紹": ["袁本初", "本初"],
    "袁術": ["袁公路", "公路"],
    "呂蒙": ["呂子明", "子明"],
    "陸遜": ["陸伯言", "伯言"],
    "甘寧": ["甘興霸", "興霸"],
    "太史慈": ["太史子義"],
    "張遼": ["張文遠", "文遠"],
    "徐晃": ["徐公明", "公明"],
    "張郃": ["張儁乂", "儁乂"],
    "夏侯惇": ["夏侯元讓", "元讓"],
    "夏侯淵": ["夏侯妙才", "妙才"],
    "曹仁": ["曹子孝", "子孝"],
    "曹洪": ["曹子廉"],
    "許褚": ["許仲康", "仲康", "虎痴"],
    "典韋": [],
    "郭嘉": ["郭奉孝", "奉孝"],
    "荀彧": ["荀文若", "文若"],
    "荀攸": ["荀公達", "公達"],
    "賈詡": ["賈文和", "文和"],
    "程昱": ["程仲德", "仲德"],
    "楊修": ["楊德祖", "德祖"],
    "禰衡": ["禰正平", "正平"],
    "華佗": [],
    "貂蟬": [],
    "王允": ["王司徒"],
    "陳宮": ["陳公臺", "公臺"],
    "高順": [],
    "顏良": [],
    "文醜": [],
    "華雄": [],
    "公孫瓚": ["公孫伯珪", "伯珪"],
    "劉表": ["劉景升", "景升"],
    "劉璋": ["劉季玉", "季玉"],
    "劉禪": ["後主", "阿斗"],
    "關平": [],
    "關興": [],
    "張苞": [],
    "周倉": [],
    "廖化": [],
    "馬岱": [],
    "王平": [],
    "馬謖": ["馬幼常", "幼常"],
    "法正": ["法孝直", "孝直"],
    "李嚴": [],
    "孟獲": [],
    "黃蓋": ["黃公覆", "公覆"],
    "韓當": [],
    "程普": [],
    "周泰": [],
    "蔣欽": [],
    "凌統": [],
    "丁奉": [],
    "徐盛": [],
    "闞澤": ["闞德潤"],
    "諸葛瑾": ["諸葛子瑜", "子瑜"],
    "張昭": ["張子布", "子布"],
    "顧雍": [],
    "于禁": ["于文則"],
    "樂進": ["樂文謙"],
    "李典": [],
    "龐德": ["龐令明", "令明"],
    "鍾會": ["鍾士季", "士季"],
    "鄧艾": ["鄧士載", "士載"],
    "郝昭": [],
    "曹丕": ["曹子桓", "子桓"],
    "曹植": ["曹子建", "子建"],
    "曹叡": [],
    "曹爽": [],
    "曹髦": [],
    "曹奐": [],
    "華歆": [],
    "王朗": [],
    "孫夫人": [],
    "吳國太": [],
    "大喬": [],
    "小喬": [],
    "蔡瑁": [],
    "張允": [],
    "蔣幹": ["蔣子翼"],
    "黃祖": [],
    "嚴顏": [],
    "張魯": [],
    "韓遂": [],
    "陶謙": ["陶恭祖", "恭祖"],
    "孔融": ["孔文舉", "文舉"],
    "漢獻帝": ["獻帝", "劉協"],
    "何進": ["何國舅"],
    "董承": ["董國舅"],
    "吉平": ["吉太醫"],
    "袁譚": [],
    "袁尚": [],
    "李傕": [],
    "郭汜": [],
    "張繡": [],
    "蔡邕": [],
    "左慈": [],
    "于吉": [],
    "管輅": [],
    "馬騰": [],
    "許攸": ["許子遠", "子遠"],
    "田豐": [],
    "沮授": [],
    "審配": [],
    "郭圖": [],
    "淳于瓊": [],
    "譙周": [],
    "黃皓": [],
    "夏侯霸": [],
    "諸葛誕": [],
    "諸葛恪": [],
    "孫皓": [],
    "羊祜": [],
    "杜預": [],
    "王濬": [],
}

# 第二批:自動發現(原文出現 >=30 次,LLM 分類為人物)
CHARACTERS["張翼"] = []
CHARACTERS["孫乾"] = []
CHARACTERS["曹眞"] = []
CHARACTERS["孟達"] = []
CHARACTERS["郭淮"] = []
CHARACTERS["張任"] = []
CHARACTERS["劉封"] = []
CHARACTERS["楊儀"] = []
CHARACTERS["糜竺"] = []
CHARACTERS["張嶷"] = []
CHARACTERS["馬忠"] = []
CHARACTERS["鄧芝"] = []
CHARACTERS["曹休"] = []
CHARACTERS["楊奉"] = []
CHARACTERS["夏侯楙"] = []
CHARACTERS["劉琦"] = []
CHARACTERS["糜芳"] = []
CHARACTERS["吳懿"] = []
CHARACTERS["冷苞"] = []
CHARACTERS["陳泰"] = []
CHARACTERS["潘璋"] = []
CHARACTERS["紀靈"] = []
CHARACTERS["簡雍"] = []
CHARACTERS["李儒"] = []
CHARACTERS["吳班"] = []
CHARACTERS["孫禮"] = []
CHARACTERS["陳登"] = []
CHARACTERS["張松"] = []
CHARACTERS["雍闓"] = []
CHARACTERS["滿寵"] = []
CHARACTERS["孫綝"] = []

# 第三批:第一回登場人物補完
CHARACTERS["桓帝"] = []
CHARACTERS["靈帝"] = []
CHARACTERS["竇武"] = []
CHARACTERS["陳蕃"] = []
CHARACTERS["曹節"] = []
CHARACTERS["張讓"] = []
CHARACTERS["趙忠"] = []
CHARACTERS["封諝"] = []
CHARACTERS["段珪"] = []
CHARACTERS["侯覽"] = []
CHARACTERS["蹇碩"] = []
CHARACTERS["程曠"] = []
CHARACTERS["夏惲"] = []
CHARACTERS["郭勝"] = []
CHARACTERS["張角"] = []
CHARACTERS["張寶"] = []
CHARACTERS["張梁"] = []
CHARACTERS["南華老仙"] = []
CHARACTERS["馬元義"] = []
CHARACTERS["唐周"] = []
CHARACTERS["盧植"] = []
CHARACTERS["皇甫嵩"] = []
CHARACTERS["朱儁"] = []
CHARACTERS["劉焉"] = []
CHARACTERS["鄒靖"] = []
CHARACTERS["劉貞"] = []
CHARACTERS["劉雄"] = []
CHARACTERS["劉弘"] = []
CHARACTERS["鄭玄"] = []
CHARACTERS["張世平"] = []
CHARACTERS["蘇雙"] = []
CHARACTERS["程遠志"] = []
CHARACTERS["鄧茂"] = []
CHARACTERS["龔景"] = []
CHARACTERS["曹嵩"] = []
CHARACTERS["曹騰"] = []
CHARACTERS["橋玄"] = []
CHARACTERS["何顒"] = []
CHARACTERS["許劭"] = []
CHARACTERS["左豐"] = []

# 第四批:候選池全收(出現次數 N>=10,已 LLM 過濾非人名),143 人
CHARACTERS["馬良"] = []  # 29
CHARACTERS["黃權"] = []  # 28
CHARACTERS["賈充"] = []  # 28
CHARACTERS["劉璝"] = []  # 28
CHARACTERS["劉繇"] = []  # 27
CHARACTERS["董荼那"] = []  # 26
CHARACTERS["劉琮"] = []  # 26
CHARACTERS["辛毗"] = []  # 25
CHARACTERS["夏侯尚"] = []  # 25
CHARACTERS["劉曄"] = []  # 25
CHARACTERS["雷銅"] = []  # 24
CHARACTERS["袁熙"] = []  # 24
CHARACTERS["蔣琬"] = []  # 24
CHARACTERS["王雙"] = []  # 24
CHARACTERS["張濟"] = []  # 24
CHARACTERS["張南"] = []  # 24
CHARACTERS["傅士仁"] = []  # 24
CHARACTERS["孫桓"] = []  # 23
CHARACTERS["孟優"] = []  # 23
CHARACTERS["伊籍"] = []  # 23
CHARACTERS["鄧賢"] = []  # 22
CHARACTERS["樊稠"] = []  # 22
CHARACTERS["楊阜"] = []  # 22
CHARACTERS["呂範"] = []  # 22
CHARACTERS["兀突骨"] = []  # 22
CHARACTERS["侯成"] = []  # 22
CHARACTERS["高翔"] = []  # 21
CHARACTERS["陳式"] = []  # 21
CHARACTERS["鄧忠"] = []  # 21
CHARACTERS["朱然"] = []  # 21
CHARACTERS["高覽"] = []  # 20
CHARACTERS["董襲"] = []  # 20
CHARACTERS["公孫淵"] = []  # 20
CHARACTERS["馮習"] = []  # 19
CHARACTERS["韓暹"] = []  # 19
CHARACTERS["逢紀"] = []  # 19
CHARACTERS["甘夫人"] = []  # 19
CHARACTERS["王經"] = []  # 19
CHARACTERS["楊松"] = []  # 19
CHARACTERS["李肅"] = []  # 19
CHARACTERS["李樂"] = []  # 19
CHARACTERS["曹芳"] = []  # 19
CHARACTERS["魏續"] = []  # 18
CHARACTERS["馬遵"] = []  # 18
CHARACTERS["陳武"] = []  # 18
CHARACTERS["蔡夫人"] = []  # 18
CHARACTERS["張虎"] = []  # 18
CHARACTERS["崔諒"] = []  # 18
CHARACTERS["吳蘭"] = []  # 18
CHARACTERS["陳應"] = []  # 17
CHARACTERS["鍾繇"] = []  # 17
CHARACTERS["車胄"] = []  # 17
CHARACTERS["毋丘儉"] = []  # 17
CHARACTERS["樂綝"] = []  # 17
CHARACTERS["楊彪"] = []  # 17
CHARACTERS["文欽"] = []  # 17
CHARACTERS["宋憲"] = []  # 17
CHARACTERS["周魴"] = []  # 17
CHARACTERS["呂曠"] = []  # 17
CHARACTERS["劉辟"] = []  # 17
CHARACTERS["韓玄"] = []  # 16
CHARACTERS["陳珪"] = []  # 16
CHARACTERS["蔡和"] = []  # 16
CHARACTERS["蔡中"] = []  # 16
CHARACTERS["胡遵"] = []  # 16
CHARACTERS["牛金"] = []  # 16
CHARACTERS["楊任"] = []  # 16
CHARACTERS["戴陵"] = []  # 16
CHARACTERS["傅僉"] = []  # 16
CHARACTERS["丁原"] = []  # 16
CHARACTERS["高幹"] = []  # 15
CHARACTERS["韓浩"] = []  # 15
CHARACTERS["王基"] = []  # 15
CHARACTERS["朱桓"] = []  # 15
CHARACTERS["孫峻"] = []  # 15
CHARACTERS["呂翔"] = []  # 15
CHARACTERS["伏后"] = []  # 15
CHARACTERS["趙範"] = []  # 14
CHARACTERS["糜夫人"] = []  # 14
CHARACTERS["申耽"] = []  # 14
CHARACTERS["王瓘"] = []  # 14
CHARACTERS["楊昂"] = []  # 14
CHARACTERS["文鴦"] = []  # 14
CHARACTERS["徐質"] = []  # 14
CHARACTERS["張紘"] = []  # 14
CHARACTERS["張楊"] = []  # 14
CHARACTERS["周善"] = []  # 14
CHARACTERS["司馬望"] = []  # 14
CHARACTERS["龔都"] = []  # 13
CHARACTERS["韓胤"] = []  # 13
CHARACTERS["賈逵"] = []  # 13
CHARACTERS["臧霸"] = []  # 13
CHARACTERS["耿紀"] = []  # 13
CHARACTERS["楊秋"] = []  # 13
CHARACTERS["楊懷"] = []  # 13
CHARACTERS["師纂"] = []  # 13
CHARACTERS["孫亮"] = []  # 13
CHARACTERS["喬國老"] = []  # 13
CHARACTERS["呂凱"] = []  # 13
CHARACTERS["伏完"] = []  # 13
CHARACTERS["高沛"] = []  # 12
CHARACTERS["韋晃"] = []  # 12
CHARACTERS["雅丹"] = []  # 12
CHARACTERS["許靖"] = []  # 12
CHARACTERS["虞翻"] = []  # 12
CHARACTERS["申儀"] = []  # 12
CHARACTERS["毛玠"] = []  # 12
CHARACTERS["楊陵"] = []  # 12
CHARACTERS["李豐"] = []  # 12
CHARACTERS["姜敍"] = []  # 12
CHARACTERS["嚴氏"] = []  # 12
CHARACTERS["傅彤"] = []  # 12
CHARACTERS["郤正"] = []  # 11
CHARACTERS["費禕"] = []  # 11
CHARACTERS["諸葛瞻"] = []  # 11
CHARACTERS["蔡氏"] = []  # 11
CHARACTERS["蒯良"] = []  # 11
CHARACTERS["管亥"] = []  # 11
CHARACTERS["王甫"] = []  # 11
CHARACTERS["王子服"] = []  # 11
CHARACTERS["焦觸"] = []  # 11
CHARACTERS["朱靈"] = []  # 11
CHARACTERS["朱異"] = []  # 11
CHARACTERS["張英"] = []  # 11
CHARACTERS["孫休"] = []  # 11
CHARACTERS["公孫康"] = []  # 11
CHARACTERS["何晏"] = []  # 11
CHARACTERS["黃奎"] = []  # 10
CHARACTERS["鄂煥"] = []  # 10
CHARACTERS["諸葛緒"] = []  # 10
CHARACTERS["蔣舒"] = []  # 10
CHARACTERS["蒯越"] = []  # 10
CHARACTERS["王方"] = []  # 10
CHARACTERS["牛輔"] = []  # 10
CHARACTERS["楊柏"] = []  # 10
CHARACTERS["桓範"] = []  # 10
CHARACTERS["李蒙"] = []  # 10
CHARACTERS["李歆"] = []  # 10
CHARACTERS["李勝"] = []  # 10
CHARACTERS["曹彰"] = []  # 10
CHARACTERS["張邈"] = []  # 10
CHARACTERS["張衞"] = []  # 10
CHARACTERS["孫韶"] = []  # 10
